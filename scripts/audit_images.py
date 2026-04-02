#!/usr/bin/env python3

import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
CONTENT_DIR = ROOT / "content"

IMG_REF_RE = re.compile(r"\./images/([^\s)\"']+)")


def main() -> int:
    errors: list[str] = []

    # image_file -> list of posts that reference it
    image_refs: dict[Path, list[Path]] = {}

    for post in sorted(CONTENT_DIR.rglob("*.md")):
        if "pages" in post.parts:
            continue
        text = post.read_text(encoding="utf-8")
        category_dir = post.parent
        rel = post.relative_to(ROOT)

        # Each ./images/ reference must resolve to an existing file
        for filename in IMG_REF_RE.findall(text):
            img_path = category_dir / "images" / filename
            if not img_path.exists():
                errors.append(f"{rel}: references missing image ./images/{filename}")
            else:
                image_refs.setdefault(img_path, []).append(post)

    # Every image file must be referenced by exactly one post
    for cat_dir in sorted(CONTENT_DIR.iterdir()):
        if not cat_dir.is_dir() or cat_dir.name in ("images", "pages", "media"):
            continue
        images_dir = cat_dir / "images"
        if not images_dir.exists():
            continue
        for img_file in sorted(images_dir.iterdir()):
            if img_file.name.startswith(".") or img_file.name.endswith(".xcf"):
                continue
            refs = image_refs.get(img_file, [])
            rel_img = img_file.relative_to(ROOT)
            if len(refs) == 0:
                errors.append(f"unreferenced image: {rel_img}")
            elif len(refs) > 1:
                post_names = ", ".join(p.name for p in refs)
                errors.append(
                    f"image referenced by multiple posts: {rel_img} ({post_names})"
                )

    for err in errors:
        print(err)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
