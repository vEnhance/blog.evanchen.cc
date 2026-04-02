#!/usr/bin/env python3
"""Mass-edit post tags via CSV.

Usage:
    python3 scripts/tags.py export              # writes tags.csv
    python3 scripts/tags.py export -o FILE
    python3 scripts/tags.py import              # reads tags.csv
    python3 scripts/tags.py import -i FILE
"""

import argparse
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
CONTENT_DIR = ROOT / "content"
SKIP_DIRS = {"pages", "images", "media"}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def iter_posts() -> list[tuple[Path, str]]:
    """Return (path, category_name) for all non-page posts, sorted by date."""
    results = []
    for cat_dir in sorted(CONTENT_DIR.iterdir()):
        if not cat_dir.is_dir() or cat_dir.name in SKIP_DIRS:
            continue
        for post in sorted(cat_dir.glob("*.md")):
            results.append((post, cat_dir.name))

    # Sort by date field so CSV rows are chronological
    def sort_key(item):
        path, _ = item
        text = path.read_text(encoding="utf-8")
        meta = _parse_frontmatter(text) or {}
        return meta.get("date", "")

    results.sort(key=sort_key)
    return results


def _parse_frontmatter(text: str) -> dict[str, str] | None:
    if not text.startswith("---\n"):
        return None
    meta: dict[str, str] = {}
    for line in text[4:].split("\n"):
        if line == "---":
            break
        if ":" in line:
            key, _, val = line.partition(":")
            meta[key.strip()] = val.strip()
    return meta


def _tags_from_str(s: str) -> list[str]:
    return sorted(t.strip() for t in s.split(",") if t.strip())


def _set_tags(text: str, tags: list[str]) -> str:
    """Replace the tags: line inside the front matter."""
    if not text.startswith("---\n"):
        return text
    lines = text.split("\n")
    in_fm = True  # we already know line 0 is ---
    for i, line in enumerate(lines[1:], start=1):
        if line == "---":
            break
        if in_fm and line.startswith("tags:"):
            new_val = ", ".join(tags)
            lines[i] = f"tags: {new_val}".rstrip()
            break
    return "\n".join(lines)


def _find_post(category: str, date: str, slug: str) -> Path | None:
    """Locate a post file, trying fast path first then slug scan."""
    date_part = date[:10]
    fast = CONTENT_DIR / category / f"{date_part}-{slug}.md"
    if fast.exists():
        return fast
    # Fallback: scan category dir for matching slug in metadata
    cat_dir = CONTENT_DIR / category
    if not cat_dir.is_dir():
        return None
    for candidate in sorted(cat_dir.glob("*.md")):
        meta = _parse_frontmatter(candidate.read_text(encoding="utf-8"))
        if meta and meta.get("slug") == slug:
            return candidate
    return None


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------


def cmd_export(output: Path) -> int:
    posts = iter_posts()

    # Build tag frequency map
    tag_freq: dict[str, int] = {}
    rows = []
    for post_path, category in posts:
        meta = _parse_frontmatter(post_path.read_text(encoding="utf-8"))
        if not meta:
            continue
        tags = _tags_from_str(meta.get("tags", ""))
        rows.append(
            {
                "title": meta.get("title", ""),
                "category": category,
                "date": meta.get("date", ""),
                "slug": meta.get("slug", ""),
                "tags": tags,
            }
        )
        for tag in tags:
            tag_freq[tag] = tag_freq.get(tag, 0) + 1

    # Tags ordered by frequency desc, then alphabetically for ties
    all_tags = sorted(tag_freq, key=lambda t: (-tag_freq[t], t))

    with output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["title", "category", "date", "slug"] + all_tags)
        for row in rows:
            cells = ["1" if t in row["tags"] else "" for t in all_tags]
            writer.writerow(
                [row["title"], row["category"], row["date"], row["slug"]] + cells
            )

    print(f"Exported {len(rows)} posts with {len(all_tags)} distinct tags -> {output}")
    return 0


def cmd_import(input_path: Path) -> int:
    with input_path.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        tag_columns = header[4:]
        rows = list(reader)

    updated = errors = 0
    for row in rows:
        if len(row) < 4:
            continue
        _title, category, date, slug = row[0], row[1], row[2], row[3]

        post_path = _find_post(category, date, slug)
        if post_path is None:
            print(f"ERROR: cannot find post slug={slug!r} in {category!r}")
            errors += 1
            continue

        # Tags are whichever columns contain "1"
        new_tags = sorted(
            tag_columns[i]
            for i, cell in enumerate(row[4:])
            if i < len(tag_columns) and cell.strip() == "1"
        )

        text = post_path.read_text(encoding="utf-8")
        new_text = _set_tags(text, new_tags)
        if new_text != text:
            post_path.write_text(new_text, encoding="utf-8")
            updated += 1

    print(f"Imported: {updated} post(s) updated, {errors} error(s).")
    return 1 if errors else 0


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(description="Mass-edit post tags via CSV.")
    sub = parser.add_subparsers(dest="cmd", required=True)

    exp = sub.add_parser("export", help="Export tags incidence matrix to CSV")
    exp.add_argument(
        "-o",
        "--output",
        default="tags.csv",
        metavar="FILE",
        help="output CSV file (default: tags.csv)",
    )

    imp = sub.add_parser("import", help="Read edited CSV and write tags back to posts")
    imp.add_argument(
        "-i",
        "--input",
        default="tags.csv",
        metavar="FILE",
        help="input CSV file (default: tags.csv)",
    )

    args = parser.parse_args()
    if args.cmd == "export":
        return cmd_export(Path(args.output))
    else:
        return cmd_import(Path(args.input))


if __name__ == "__main__":
    sys.exit(main())
