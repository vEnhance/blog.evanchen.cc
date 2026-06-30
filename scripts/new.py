#!/usr/bin/env python3

import argparse
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
CONTENT_DIR = REPO_ROOT / "content"
NON_CATEGORY_DIRS = {"pages", "images", "media"}
DATE = "2099-12-31"

categories = [
    d.name
    for d in CONTENT_DIR.iterdir()
    if d.is_dir() and d.name not in NON_CATEGORY_DIRS
]


def main() -> None:
    parser = argparse.ArgumentParser(description="Scaffold a new draft post.")
    parser.add_argument(
        "category",
        choices=categories,
        help="Category for the new draft",
    )
    parser.add_argument("slug", help="URL slug (e.g. my-post-title)")
    parser.add_argument("--title", "-t", help="Title for the post")
    args = parser.parse_args()

    filepath = CONTENT_DIR / args.category / f"2099-12-31-{args.slug}.md"
    assert filepath.parent.is_dir(), "WTF? {filepath.parent} doesn't exist"

    filepath.write_text(
        f"---\n"
        f"title: {args.title or args.slug}\n"
        f"date: 2099-12-31 13:37\n"
        f"slug: {args.slug}\n"
        f"tags:\n"
        f"status: draft\n"
        f"---\n"
    )
    print(filepath)


if __name__ == "__main__":
    main()
