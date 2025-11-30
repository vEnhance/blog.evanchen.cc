from pelican import signals


def add_all_articles(generators):
    all_articles = []
    for gen in generators:
        if hasattr(gen, "articles"):
            all_articles = gen.articles
            break

    for gen in generators:
        gen.context["all_articles"] = all_articles


def register():
    signals.all_generators_finalized.connect(add_all_articles)
