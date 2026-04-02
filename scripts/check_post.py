#!/usr/bin/env python3

import re
import sys
from pathlib import Path

CONTENT_DIR = Path(__file__).parent.parent / "content"
PAGES_DIR = CONTENT_DIR / "pages"

ARTICLE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-(.+)\.md$")
LINK_RE = re.compile(r"\(/([\w-]+)/?[)#]")

# Pelican-generated index pages with no source article slug.
BUILTIN_SLUGS = {"categories", "archives"}


def get_all_slugs() -> set[str]:
    slugs: set[str] = set()
    for md_file in CONTENT_DIR.rglob("*.md"):
        m = ARTICLE_RE.match(md_file.name)
        slugs.add(m.group(2) if m else md_file.stem)
    return slugs


def check_file(path: Path, valid_slugs: set[str]) -> None:
    lines = path.read_text().splitlines()

    if path.parent != PAGES_DIR and (m := ARTICLE_RE.match(path.name)):
        date_from_name, slug_from_name = m.group(1), m.group(2)
        assert len(lines) >= 5 and lines[0].strip() == "---", (
            f"{path}: missing frontmatter"
        )
        assert lines[1].startswith("title:"), f"{path}: line 2 must be title"
        assert lines[2].startswith("date:"), f"{path}: line 3 must be date"
        assert lines[3].startswith("slug:"), f"{path}: line 4 must be slug"
        assert lines[4].strip().startswith("tags:"), f"{path}: line 5 must be tags"
        date_val = lines[2][5:].strip()[:10]
        slug_val = lines[3][5:].strip()
        assert date_val == date_from_name, (
            f"{path}: filename date {date_from_name} != frontmatter {date_val}"
        )
        assert slug_val == slug_from_name, (
            f"{path}: filename slug {slug_from_name} != frontmatter {slug_val}"
        )

    for line in lines:
        for m in LINK_RE.finditer(line):
            slug = m.group(1)
            assert slug in valid_slugs, f"{path}: broken internal link '/{slug}'"


if __name__ == "__main__":
    files = [Path(f) for f in sys.argv[1:] if f.endswith(".md")]
    if not files:
        sys.exit(0)
    valid_slugs = get_all_slugs() | BUILTIN_SLUGS
    for path in files:
        check_file(path, valid_slugs)
    print(f"{len(files)} file(s) checked and all passed")
