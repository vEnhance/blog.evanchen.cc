#!/usr/bin/env python3

import argparse
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
CONTENT_DIR = REPO_ROOT / "content"
DRAFTS_DIR = CONTENT_DIR / "Drafts"
NON_CATEGORY_DIRS = {"pages", "images", "media", "_DRAFTS"}
DATE = "2099-12-31"


def get_categories() -> list[str]:
    return [
        d.name
        for d in CONTENT_DIR.iterdir()
        if d.is_dir() and d.name not in NON_CATEGORY_DIRS
    ]


def main() -> None:
    parser = argparse.ArgumentParser(description="Scaffold a new draft post.")
    parser.add_argument("slug", help="URL slug (e.g. my-post-title)")
    parser.add_argument("title", nargs="?", help="Title for the post")
    args = parser.parse_args()

    assert DRAFTS_DIR.exists(), f"{DRAFTS_DIR} missing"
    filepath = DRAFTS_DIR / f"2099-12-31-{args.slug}.md"
    filepath.parent.mkdir(parents=True, exist_ok=True)

    filepath.write_text(
        f"---\n"
        f"title: {args.title or args.slug}\n"
        f"date: 2099-12-31 13:37\n"
        f"slug: {args.slug}\n"
        f"tags: draft\n"
        f"status: draft\n"
        f"---\n"
    )
    print(f"Created: {filepath}")


if __name__ == "__main__":
    main()
