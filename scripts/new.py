#!/usr/bin/env python3
"""Usage: new.py <slug> <category> <YYYY-MM-DD>"""

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
CONTENT_DIR = REPO_ROOT / "content"
NON_CATEGORY_DIRS = {"pages", "images", "media", "_DRAFTS"}

ALIASES: dict[str, str] = {
    "af": "April Fools",
    "april": "April Fools",
    "d": "Drafts",
    "drafts": "Drafts",
    "e": "Essays",
    "essay": "Essays",
    "h": "Hacking",
    "hack": "Hacking",
    "l": "Learning",
    "learn": "Learning",
    "m": "Math",
    "n": "News",
    "per": "Personal",
    "p": "Puzzles",
    "puzz": "Puzzles",
    "rep": "Reports",
    "r": "Reports",
    "t": "Teaching",
    "teach": "Teaching",
}


def get_categories() -> list[str]:
    return [
        d.name
        for d in CONTENT_DIR.iterdir()
        if d.is_dir() and d.name not in NON_CATEGORY_DIRS
    ]


def resolve_category(raw: str, categories: list[str]) -> str:
    for cat in categories:
        if cat.lower() == raw.lower():
            return cat
    resolved = ALIASES.get(raw.lower())
    if resolved and resolved in categories:
        return resolved
    print(f"Unknown category: {raw!r}")
    print(f"Valid categories: {', '.join(sorted(categories))}")
    print(f"Aliases: {', '.join(sorted(ALIASES))}")
    sys.exit(1)


def main() -> None:
    parser = argparse.ArgumentParser(description="Scaffold a new draft post.")
    parser.add_argument("slug", help="URL slug (e.g. my-post-title)")
    parser.add_argument("category", help="Category name or alias (e.g. math, af)")
    parser.add_argument("date", help="Publication date in YYYY-MM-DD format")
    args = parser.parse_args()

    categories = get_categories()
    category = resolve_category(args.category, categories)

    filepath = CONTENT_DIR / category / f"{args.date}-{args.slug}.md"
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
