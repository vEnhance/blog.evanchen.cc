import json
import os

from pelican import signals


def write_latest_json(generator):
    articles = generator.articles  # published only, sorted newest-first
    if not articles:
        return

    latest = articles[0]
    description = getattr(latest, "description", None) or getattr(
        latest, "oembed_description", None
    )
    siteurl = generator.settings.get("SITEURL", "").rstrip("/")
    data = {
        "category": latest.category.name,
        "date": latest.date.isoformat(),
        "description": description,
        "slug": latest.slug,
        "tags": [t.name for t in latest.tags],
        "title": latest.title,
        "url": siteurl + "/" + latest.url,
    }

    out = os.path.join(generator.settings["OUTPUT_PATH"], "latest.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def register():
    signals.article_generator_finalized.connect(write_latest_json)
