"""
sort_tags
===================================

This plugin adds tags_sorted_article_length to the context,
which is a list of tuples (Tag, [Articles]) that is sorted
by number of Articles first and Tag second.

https://github.com/ingwinlu/sort_tags/blob/master/sort_tags.py
"""

from operator import itemgetter
from pelican import signals


def sort_tags_by_articles_size(generator):
    def extract_and_size(item):
        articles = itemgetter(1)(item)
        tag_lower = (itemgetter(0)(item)).slug.lower()
        return (-len(articles), tag_lower)

    generator.context["tags_sorted_by_article_length"] = sorted(
        generator.tags.items(), key=extract_and_size, reverse=False
    )


def register():
    signals.article_generator_finalized.connect(sort_tags_by_articles_size)
