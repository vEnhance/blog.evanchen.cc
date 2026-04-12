"""
oembed_gen
==========

Generates an ``oembed.json`` file in each article's output directory
(alongside ``index.html``).  The JSON follows the oEmbed 1.0 spec
(type=rich) and includes:

  version, type, title, author_name, author_url,
  provider_name, provider_url, url, description (extension), html, width

The corresponding ``<link rel="alternate" type="application/json+oembed">``
tag is added by the article.html template.

Settings
--------
OEMBED_DESCRIPTION_LENGTH (int, default 200)
    Maximum number of plain-text characters to include in the description.
"""

import json
import re
from pathlib import Path

from bs4 import BeautifulSoup
from pelican import signals

DEFAULT_DESCRIPTION_LENGTH = 200


def _plain_text(html: str, max_chars: int) -> str:
    """Strip HTML tags and return the first *max_chars* chars of plain text."""
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text(separator=" ")
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > max_chars:
        # Break at a word boundary so we don't cut mid-word.
        text = text[:max_chars].rsplit(" ", 1)[0] + "\u2026"
    return text


def generate_oembed(generator):
    siteurl = generator.settings.get("SITEURL", "").rstrip("/")
    author = generator.settings.get("AUTHOR", "")
    sitename = generator.settings.get("SITENAME", "")
    max_chars = generator.settings.get(
        "OEMBED_DESCRIPTION_LENGTH", DEFAULT_DESCRIPTION_LENGTH
    )

    for article in generator.articles:
        article_url = siteurl + "/" + article.slug + "/"
        description = _plain_text(article._content, max_chars)
        article.oembed_description = description

        data = {
            "version": "1.0",
            "type": "rich",
            "title": article.title,
            "author_name": author,
            "author_url": siteurl + "/",
            "provider_name": sitename,
            "provider_url": siteurl + "/",
            "url": article_url,
            "description": description,
            "html": (
                f"<blockquote>"
                f'<b><a href="{article_url}">{article.title}</a></b>'
                f"<p>{description}</p>"
                f"<footer>{author} \u2014 "
                f'<a href="{siteurl}/">{sitename}</a></footer>'
                f"</blockquote>"
            ),
            "width": 800,
            "height": None,
        }

        out_dir = Path(generator.output_path) / article.slug
        out_dir.mkdir(parents=True, exist_ok=True)
        with open(out_dir / "oembed.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)


def register():
    signals.article_generator_finalized.connect(generate_oembed)
