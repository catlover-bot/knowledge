"""Check navigation links offline using a deliberately small Markdown subset."""

import argparse
from dataclasses import dataclass
import html
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
import unicodedata
from urllib.parse import unquote, urlsplit


DEFAULT_FILES = (
    "README.md", "CONTRIBUTING.md", "articles/README.md",
    "papers/README.md", "journals/README.md",
)
LINK_START = re.compile(r"!?\[(?:\\.|[^\[\]\\\n])*\]\(\s*")
REFERENCE = re.compile(r"^ {0,3}\[[^\]\n]+\]:[ \t]*(?:<([^>\n]*)>|(\S+))", re.MULTILINE)


@dataclass
class Issue:
    path: Path
    line: int
    message: str


@dataclass
class Result:
    sources: int
    links: int
    issues: list


def _blank(match):
    return re.sub(r"[^\n]", " ", match.group(0))


def without_examples(text):
    """Mask fenced blocks and comments without changing positions or line numbers."""
    lines = []
    fence = None
    for line in text.splitlines(keepends=True):
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})", line)
        if fence is None and marker:
            fence = marker.group(1)
            lines.append(re.sub(r"[^\n]", " ", line))
        elif fence is not None:
            if re.match(r"^ {0,3}" + re.escape(fence[0]) + r"{" + str(len(fence)) + r",}[ \t]*(?:\n|$)", line):
                fence = None
            lines.append(re.sub(r"[^\n]", " ", line))
        else:
            lines.append(line)
    return re.sub(r"<!--.*?-->", _blank, "".join(lines), flags=re.DOTALL)


def without_inline_code(text):
    # Same-length backtick delimiters; this is not a complete CommonMark parser.
    return re.sub(r"(?<!`)(`+)(?!`)(.*?)(?<!`)\1(?!`)", _blank, text, flags=re.DOTALL)


def destinations(text):
    """Yield (line, URL) for inline links and single-line reference definitions."""
    for match in LINK_START.finditer(text):
        bracket = match.start() + (1 if text[match.start()] == "!" else 0)
        before = bracket - 1
        while before >= 0 and text[before] == "\\":
            before -= 1
        if (bracket - before - 1) % 2:
            continue
        pos = match.end()
        if pos >= len(text):
            continue
        start = pos
        if text[pos] == "<":
            end = text.find(">", pos + 1)
            if end < 0 or "\n" in text[pos:end]:
                continue
            destination = text[pos + 1:end]
            pos = end + 1
        else:
            depth = 0
            while pos < len(text):
                char = text[pos]
                if char == "\\" and pos + 1 < len(text):
                    pos += 2
                    continue
                if char == "(":
                    depth += 1
                elif char == ")":
                    if depth == 0:
                        break
                    depth -= 1
                elif char.isspace() and depth == 0:
                    break
                pos += 1
            destination = text[start:pos]
        # Permit a single quoted/parenthesized title after the destination.
        tail = re.match(r'''[ \t]*(?:(?:"[^"\n]*"|'[^'\n]*'|\([^\n]*?\))[ \t]*)?\)''', text[pos:])
        if tail:
            yield text.count("\n", 0, match.start()) + 1, destination
    for match in REFERENCE.finditer(text):
        yield text.count("\n", 0, match.start()) + 1, match.group(1) or match.group(2) or ""


class ExplicitAnchors(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.duplicates = []

    def handle_starttag(self, tag, attrs):
        if tag != "a":
            return
        for name, value in attrs:
            if name == "id" and value is not None:
                if value in self.ids:
                    self.duplicates.append((self.getpos()[0], value))
                self.ids.add(value)


def heading_slug(heading):
    """Approximate common GitHub heading IDs, retaining Japanese and other letters."""
    heading = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", heading)
    heading = re.sub(r"<[^>]*>", "", heading)
    heading = re.sub(r"(?<!\w)_{1,3}(.+?)_{1,3}(?!\w)", r"\1", heading)
    heading = html.unescape(heading).replace("`", "").lower()
    return "".join(
        "-" if char == " " else char
        for char in heading
        if char in " -_" or unicodedata.category(char)[0] in "LNM"
    )


def anchors(text):
    clean = without_examples(text)
    explicit = ExplicitAnchors()
    explicit.feed(without_inline_code(clean))
    ids = set(explicit.ids)
    headings = set()
    previous = ""
    for line in clean.splitlines():
        atx = re.match(r"^ {0,3}#{1,6}(?:[ \t]+(.*)|[ \t]*)$", line)
        heading = None
        if atx:
            heading = re.sub(r"[ \t]+#+[ \t]*$", "", atx.group(1) or "").strip()
        elif previous.strip() and re.match(r"^ {0,3}(?:=+|-+)[ \t]*$", line):
            heading = previous.strip()
        if heading is not None:
            base = heading_slug(heading)
            slug = base
            suffix = 0
            while slug in headings:
                suffix += 1
                slug = f"{base}-{suffix}"
            headings.add(slug)
            ids.add(slug)
        previous = "" if heading is not None else line
    return ids, explicit.duplicates


def default_sources(root):
    """Navigation and paper notes; historical journal outbound links stay opt-in."""
    sources = [root / name for name in DEFAULT_FILES]
    sources += sorted((root / "topics").rglob("*.md"))
    sources += sorted((root / "papers").rglob("*.md"))
    if (root / "assets/diagrams/README.md").is_file():
        sources.append(root / "assets/diagrams/README.md")
    return list(dict.fromkeys(sources))


def expand_paths(paths):
    expanded = []
    for path in paths:
        path = Path(path).resolve()
        expanded.extend(sorted(path.rglob("*.md")) if path.is_dir() else [path])
    return list(dict.fromkeys(expanded))


def check_paths(paths):
    """Check selected sources and anchors in their targets, without fetching URLs."""
    paths = expand_paths(paths)
    issues = []
    documents = {}
    links = 0

    def read(path):
        if path not in documents:
            try:
                text = path.read_text(encoding="utf-8")
            except (OSError, UnicodeError) as error:
                issues.append(Issue(path, 1, f"cannot read Markdown file: {error}"))
                documents[path] = None
            else:
                ids, duplicates = anchors(text)
                for line, value in duplicates:
                    issues.append(Issue(path, line, f"duplicate explicit anchor: {value!r}"))
                documents[path] = (text, ids)
        return documents[path]

    for source in paths:
        document = read(source)
        if document is None:
            continue
        clean = without_inline_code(without_examples(document[0]))
        for line, destination in destinations(clean):
            destination = html.unescape(re.sub(r"\\([!\"#$%&'()*+,\-./:;<=>?@\[\]\\^_`{|}~])", r"\1", destination))
            try:
                url = urlsplit(destination)
            except ValueError:
                issues.append(Issue(source, line, f"unsupported link destination: {destination!r}"))
                continue
            if url.scheme or url.netloc or "?" in destination.split("#", 1)[0]:
                continue
            path = unquote(url.path)
            fragment = unquote(url.fragment)
            if not path and not fragment:
                continue
            if path and Path(path).suffix.lower() != ".md":
                continue
            if path.startswith("/"):
                issues.append(Issue(source, line, f"unsupported root-relative Markdown link: {destination!r}; use a relative path"))
                continue
            links += 1
            target = (source.parent / path).resolve() if path else source
            if not target.is_file():
                issues.append(Issue(source, line, f"missing Markdown target: {destination!r}"))
                continue
            target_document = read(target)
            if target_document is not None and fragment and fragment not in target_document[1]:
                issues.append(Issue(source, line, f"missing anchor {fragment!r} in {str(target)!r}"))
    return Result(len(paths), links, issues)


def main(argv=None):
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(
        description="Check local Markdown file and anchor links offline (standard library only).",
        epilog=(
            "Default source scope: README.md, CONTRIBUTING.md, topics/**/*.md, papers/**/*.md, "
            "assets/diagrams/README.md when present, articles/README.md and journals/README.md. Target anchors are "
            "checked, but their outgoing links are not followed unless selected as sources. "
            "Pass . from the repository root for a broader scan, including historical journals. "
            "Supported: inline links, single-line reference-definition destinations, explicit "
            "<a id=...> anchors, and common ATX/Setext GitHub heading slugs with duplicate suffixes. "
            "Heading slugs are approximate; prefer explicit ASCII anchors for stable links. "
            "External/scheme/query URLs and non-.md assets are ignored. Raw HTML hrefs, "
            "indented code blocks, and complex/multiline Markdown are not supported. "
            "A clean default scan does not validate every link in the repository."
        ),
    )
    parser.add_argument("paths", nargs="*", type=Path,
                        help="source files or directories, relative to the current directory; directories include all *.md recursively")
    args = parser.parse_args(argv)
    result = check_paths(args.paths if args.paths else default_sources(root))
    for issue in result.issues:
        try:
            display = issue.path.relative_to(root)
        except ValueError:
            display = issue.path
        print(f"{display}:{issue.line}: {issue.message}")
    print(f"Checked {result.sources} source files / {result.links} local Markdown links / {len(result.issues)} errors")
    return 1 if result.issues else 0


if __name__ == "__main__":
    sys.exit(main())
