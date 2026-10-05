"""Find link-only details entries without fetching external sources."""

from pathlib import Path
import re
import sys


DETAILS = re.compile(
    r"<details\b[^>]*>\s*<summary\b[^>]*>(.*?)</summary>(.*?)</details>",
    re.DOTALL | re.IGNORECASE,
)
LINK = re.compile(r"!?\[[^\]]*\]\([^\n]*?\)")


def without_fences(text):
    """Mask fenced markup; retain nonempty code as content and line counts."""
    lines = []
    fence = None
    for line in text.splitlines(keepends=True):
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if fence is None and marker:
            fence = marker.group(1)
            lines.append("\n" if line.endswith("\n") else "")
        elif fence is not None:
            if re.match(r"^\s*" + re.escape(fence[0]) + r"{" + str(len(fence)) + r",}\s*$", line):
                fence = None
                lines.append("\n" if line.endswith("\n") else "")
            else:
                lines.append(("CODE" if line.strip() else "") + ("\n" if line.endswith("\n") else ""))
        else:
            lines.append(line)
    return "".join(lines)


def prose(body):
    text = re.sub(r"<!--.*?-->", "", body, flags=re.DOTALL)
    text = LINK.sub("", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"https?://[^\s<>]+", "", text)
    text = re.sub(r"^\s*\[[^\]]+\]:\s*.*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"!?\[[^\]]*\]\[[^\]]*\]", "", text)
    text = re.sub(r"[\s>*#`_\-:：|]", "", text)
    return re.sub(r"参考|出典|関連|公式|JSTAGE|README", "", text)


def inspect(text):
    findings = []
    pending = 0
    entries = 0
    clean = without_fences(text)
    for match in DETAILS.finditer(clean):
        entries += 1
        title, body = match.groups()
        if not prose(body):
            line = clean.count("\n", 0, match.start()) + 1
            findings.append((line, title))
        if "本文未確認" in title + body:
            pending += 1
    return findings, pending, entries


def main(root):
    errors = 0
    pending = 0
    entries = 0
    files = 0
    for category in ("articles", "papers", "journals"):
        for path in sorted((root / category).rglob("*.md")):
            files += 1
            findings, waiting, count = inspect(path.read_text(encoding="utf-8"))
            pending += waiting
            entries += count
            for line, title in findings:
                errors += 1
                print(f"{path.relative_to(root)}:{line}: リンクのみ: {title}")
    print(f"{files}ファイル / {entries}項目 / リンクのみ {errors}件 / 本文未確認 {pending}件")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(Path(__file__).resolve().parents[1]))
