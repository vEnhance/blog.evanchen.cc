"""
Pelican plugin to add class="autolink" to bare-URL links.

Markdown autolinks like <https://example.com> render as:
    <a href="https://example.com">https://example.com</a>

This plugin detects links where the visible text equals the href and adds
class="autolink" so they can be styled distinctly (e.g. monospace font).
"""

from bs4 import BeautifulSoup
from pelican import signals


def mark_autolinks(content):
    if not content._content:
        return

    soup = BeautifulSoup(content._content, "html.parser")
    changed = False

    for tag in soup.find_all("a", href=True):
        if tag.get_text() == tag["href"]:
            existing = tag.get("class", [])
            if "autolink" not in existing:
                tag["class"] = existing + ["autolink"]
                changed = True

    if changed:
        content._content = str(soup)


def process_articles(generator):
    for article in getattr(generator, "articles", []):
        mark_autolinks(article)
    for draft in getattr(generator, "drafts", []):
        mark_autolinks(draft)


def process_pages(generator):
    for page in getattr(generator, "pages", []):
        mark_autolinks(page)


def register():
    signals.article_generator_finalized.connect(process_articles)
    signals.page_generator_finalized.connect(process_pages)
