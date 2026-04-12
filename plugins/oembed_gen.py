"""
oembed_gen
==========

Generates an ``oembed.json`` file in each article's output directory
(alongside ``index.html``), and injects the oEmbed discovery ``<link>``
tag into each article's HTML after all other plugins have run.

The ``<link>`` tag is injected via the ``content_written`` signal using
``soup.new_tag()``, which guarantees correct void-element serialization
(avoiding the stray ``</link>`` that results from BeautifulSoup re-parsing
a template-rendered ``<link>`` tag).

The corresponding ``og:description`` and ``meta description`` overrides
are handled by the article.html template via ``article.oembed_description``.

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


def inject_oembed_link(path, context):
    """Inject the oEmbed discovery <link> tag into each article's HTML file.

    Runs via content_written (after the SEO plugin's own pass) so that
    soup.new_tag() produces a proper void element with no stray </link>.
    """
    article = context.get("article")
    if not article:
        return

    siteurl = context.get("SITEURL", "").rstrip("/")

    with open(path, encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    if not soup.head:
        return

    link = soup.new_tag(
        "link",
        attrs={
            "rel": "alternate",
            "type": "application/json+oembed",
            "href": f"{siteurl}/{article.slug}/oembed.json",
            "title": article.title,
        },
    )
    soup.head.append(link)

    with open(path, "w", encoding="utf-8") as f:
        f.write(str(soup))


def register():
    signals.article_generator_finalized.connect(generate_oembed)
    signals.content_written.connect(inject_oembed_link)
