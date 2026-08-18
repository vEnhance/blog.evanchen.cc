import os
import re
from datetime import date, datetime, timedelta
from pathlib import Path

from pelicanconf import *

CONTENT_DIR = Path(__file__).parent / "content"
ARTICLE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-.+\.md$")
CUTOFF = datetime.now().astimezone().date() - timedelta(
    days=int(os.environ.get("RECENT_DAYS") or 365)
)

ARTICLE_PATHS = [
    str(f.relative_to(CONTENT_DIR))
    for f in CONTENT_DIR.rglob("*.md")
    if (m := ARTICLE_RE.match(f.name)) and date.fromisoformat(m.group(1)) >= CUTOFF
]
