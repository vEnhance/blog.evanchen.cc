#!/usr/bin/env python3
"""Usage: new.py <slug> <YYYY-MM-DD>"""

import argparse
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
CONTENT_DIR = REPO_ROOT / "content"
NON_CATEGORY_DIRS = {"pages", "images", "media", "_DRAFTS"}


def get_categories() -> list[str]:
    return [
        d.name
        for d in CONTENT_DIR.iterdir()
        if d.is_dir() and d.name not in NON_CATEGORY_DIRS
    ]


def main() -> None:
    parser = argparse.ArgumentParser(description="Scaffold a new draft post.")
    parser.add_argument("slug", help="URL slug (e.g. my-post-title)")
    parser.add_argument("category", help="Category name or alias (e.g. math, af)")
    parser.add_argument("date", help="Publication date in YYYY-MM-DD format")
    args = parser.parse_args()

    filepath = CONTENT_DIR / "Drafts" / f"{args.date}-{args.slug}.md"
    filepath.parent.mkdir(parents=True, exist_ok=True)

    filepath.write_text(
        f"---\n"
        f"title: \n"
        f"date: {args.date} 13:37\n"
        f"slug: {args.slug}\n"
        f"tags: \n"
        f"status: draft\n"
        f"---\n"
    )
    print(f"Created: {filepath}")


if __name__ == "__main__":
    main()
