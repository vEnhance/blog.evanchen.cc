#!/usr/bin/env python3

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
CONTENT_DIR = REPO_ROOT / "content"
NON_CATEGORY_DIRS = {"pages", "images", "media"}
DATE = "2099-12-31"

SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
ARTICLE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}-(.+)\.md$")

categories = sorted(
    d.name
    for d in CONTENT_DIR.iterdir()
    if d.is_dir() and d.name not in NON_CATEGORY_DIRS
)


def ask(prompt: str) -> str:
    """Read a line, treating Ctrl-C/Ctrl-D as "never mind"."""
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        print()
        sys.exit(1)


def ask_category() -> str:
    width = len(str(len(categories)))
    for i, name in enumerate(categories, start=1):
        print(f"  {i:>{width}}. {name}")
    while True:
        answer = ask(f"Category [1-{len(categories)}]: ")
        if answer.isdigit() and 1 <= int(answer) <= len(categories):
            return categories[int(answer) - 1]
        print(f"  ! Enter a number from 1 to {len(categories)}.")


def existing_slugs() -> set[str]:
    slugs: set[str] = set()
    for md in CONTENT_DIR.rglob("*.md"):
        m = ARTICLE_RE.match(md.name)
        slugs.add(m.group(1) if m else md.stem)
    return slugs


def ask_slug() -> str:
    taken = existing_slugs()
    while True:
        slug = ask("Slug: ")
        if not SLUG_RE.match(slug):
            print("  ! Slug must be lowercase words joined by single hyphens.")
        elif slug in taken:
            print(f"  ! Slug '{slug}' is already used.")
        else:
            return slug


def ask_title() -> str:
    while True:
        title = ask("Title: ")
        if title:
            return title
        print("  ! Title is required.")


def main() -> None:
    category = ask_category()
    slug = ask_slug()
    title = ask_title()

    filepath = CONTENT_DIR / category / f"{DATE}-{slug}.md"
    assert filepath.parent.is_dir(), f"WTF? {filepath.parent} doesn't exist"

    filepath.write_text(
        f"---\n"
        f"title: {title}\n"
        f"date: {DATE} 13:37\n"
        f"slug: {slug}\n"
        f"tags:\n"
        f"status: draft\n"
        f"---\n"
    )
    print(filepath)


if __name__ == "__main__":
    main()
