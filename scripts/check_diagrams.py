"""Check repository-owned SVG diagrams and their Markdown embeds offline."""

from pathlib import Path
import math
import re
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

from check_links import without_examples


def inspect_svg(path):
    errors = []
    try:
        root = ET.parse(path).getroot()
    except (ET.ParseError, OSError) as error:
        return [f"invalid SVG: {error}"]
    if root.tag.rsplit("}", 1)[-1] != "svg":
        errors.append("root must be svg")
    try:
        box = [float(value) for value in root.attrib.get("viewBox", "").split()]
        if len(box) != 4 or not all(math.isfinite(value) for value in box) or box[2] <= 0 or box[3] <= 0:
            raise ValueError
    except ValueError:
        errors.append("viewBox must have four numbers and positive dimensions")
    for name in ("title", "desc"):
        nodes = [node for node in root if node.tag.rsplit("}", 1)[-1] == name]
        if not nodes or not "".join(nodes[0].itertext()).strip():
            errors.append(f"missing accessible {name}")
    for node in root.iter():
        name = node.tag.rsplit("}", 1)[-1]
        if name in {"script", "foreignObject", "iframe", "image"}:
            errors.append(f"unsupported active or embedded element: {name}")
        for key, value in node.attrib.items():
            local = key.rsplit("}", 1)[-1]
            if local.lower().startswith("on"):
                errors.append(f"event handler: {local}")
            if local == "href" and not value.startswith("#"):
                errors.append("external resource reference")
            if re.search(r"url\(\s*['\"]?(?!#)[^\s'\"]", value, re.IGNORECASE):
                errors.append("nonlocal CSS resource reference")
        if name == "style" and re.search(r"@import|https?://|url\(\s*['\"]?(?!#)[^\s'\"]", node.text or "", re.IGNORECASE):
            errors.append("external CSS resource")
    return errors


def inspect_embeds(root):
    errors = []
    embeds = 0
    pattern = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
    for path in root.rglob("*.md"):
        for match in pattern.finditer(without_examples(path.read_text(encoding="utf-8"))):
            alt, destination = match.groups()
            url = urlsplit(destination)
            if url.scheme or url.netloc or not url.path.lower().endswith(".svg"):
                continue
            target = (path.parent / unquote(url.path)).resolve()
            try:
                target.relative_to((root / "assets/diagrams").resolve())
            except ValueError:
                continue
            embeds += 1
            if not alt.strip():
                errors.append(f"{path.relative_to(root)}: SVG image needs descriptive alt text")
            if not target.is_file():
                errors.append(f"{path.relative_to(root)}: missing diagram {destination}")
    return embeds, errors


def main(root):
    files = sorted((root / "assets/diagrams").glob("*.svg"))
    errors = []
    for path in files:
        errors.extend(f"{path.relative_to(root)}: {error}" for error in inspect_svg(path))
    embeds, embed_errors = inspect_embeds(root)
    errors.extend(embed_errors)
    for error in errors:
        print(error)
    print(f"Checked {len(files)} original SVGs / {embeds} Markdown embeds / {len(errors)} errors")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(Path(__file__).resolve().parents[1]))
