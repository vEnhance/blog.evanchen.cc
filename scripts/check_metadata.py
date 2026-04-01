#!/usr/bin/env python3

import re
import sys
from pathlib import Path

FILENAME_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-(.+)\.md$")


def check_file(path: Path):
    with open(path) as f:
        assert f.readline().strip() == "---", f"{path} did not start with dashes"
        assert f.readline().startswith("title:"), f"{path} has no title"
        assert (date_line := f.readline()).startswith("date:"), f"{path} has no date"
        assert (slug_line := f.readline()).startswith("slug:"), f"{path} has no slug"
        assert f.readline().strip().startswith("tags:"), f"{path} has no tags"

    date_val = date_line[5:].strip()[:10]
    slug_val = slug_line[5:].strip()
    assert (m := FILENAME_RE.match(path.name)) is not None, (
        f"{path} is not named correctly"
    )
    assert m.group(1) == date_val, f"{path} has wrong date (expected {date_val})"
    assert m.group(2) == slug_val, f"{path} has wrong slug (expected {slug_val})"


if __name__ == "__main__":
    files = [Path(f) for f in sys.argv[1:] if f.endswith(".md")]
    for path in files:
        check_file(path)
    print(f"{len(files)} checked and all passed")
