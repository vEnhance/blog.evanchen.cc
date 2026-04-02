"""
cf_redirects
============

Generates a Cloudflare Pages ``_redirects`` file in the output directory,
mapping old WordPress-style URLs to the current slugs.

Each article may carry an ``original_url`` metadata field whose value is the
old WordPress path (e.g. ``2019/01/31/math-contest-platitudes-v3/``).
This plugin collects all such fields and writes one redirect rule per article:

    /2019/01/31/math-contest-platitudes-v3/    /platitudes/    301
"""

from pathlib import Path

from pelican import signals


def write_redirects(generator):
    redirects: list[tuple[str, str]] = []

    for article in generator.articles:
        original_url = article.metadata.get("original_url", "").strip()
        if not original_url:
            continue
        old = "/" + original_url.strip("/") + "/"
        new = "/" + article.slug + "/"
        if old != new:
            redirects.append((old, new))

    if not redirects:
        return

    redirects.sort()
    col = max(len(old) for old, _ in redirects) + 2
    lines = [f"{old:<{col}}{new:<30}301\n" for old, new in redirects]

    out = Path(generator.output_path)
    out.mkdir(parents=True, exist_ok=True)
    (out / "_redirects").write_text("".join(lines))


def register():
    signals.article_generator_finalized.connect(write_redirects)
