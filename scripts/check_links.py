#!/usr/bin/env python3

import re
import sys
from pathlib import Path

CONTENT_DIR = Path(__file__).parent.parent / "content"

LINK_RE = re.compile(r"\(/([\w-]+)/?[)#]")
ARTICLE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}-(.+)\.md$")

# Pelican-generated index pages that have no source article slug.
BUILTIN_SLUGS = {"categories", "archives"}


def get_all_slugs() -> set[str]:
    """
    Articles follow YYYY-MM-DD-{slug}.md (enforced by check-post-metadata).
    Pages live in content/pages/ and use {slug}.md directly.
    """
    slugs: set[str] = set()
    for md_file in CONTENT_DIR.rglob("*.md"):
        m = ARTICLE_RE.match(md_file.name)
        slugs.add(m.group(1) if m else md_file.stem)
    return slugs


def check_file(path: Path, valid_slugs: set[str]):
    with open(path) as f:
        for line in f:
            for m in LINK_RE.finditer(line):
                slug = m.group(1)
                assert slug in valid_slugs, f"{path} references nonexistent /{slug}"


if __name__ == "__main__":
    files = [Path(f) for f in sys.argv[1:] if f.endswith(".md")]
    valid_slugs = get_all_slugs() | BUILTIN_SLUGS
    for path in files:
        check_file(path, valid_slugs)
    print(f"{len(files)} file(s) checked, all internal links OK")
