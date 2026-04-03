import os
import re
from datetime import date, timedelta
from pathlib import Path

from pelicanconf import *  # noqa: F401, F403

CONTENT_DIR = Path(__file__).parent / "content"
ARTICLE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-.+\.md$")
CUTOFF = date.today() - timedelta(days=int(os.environ.get("RECENT_DAYS") or 365))

ARTICLE_PATHS = [
    str(f.relative_to(CONTENT_DIR))
    for f in CONTENT_DIR.rglob("*.md")
    if (m := ARTICLE_RE.match(f.name)) and date.fromisoformat(m.group(1)) >= CUTOFF
]
