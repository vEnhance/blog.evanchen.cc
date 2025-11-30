AUTHOR = "Evan Chen 《陳誼廷》"
SITENAME = "Power Overwhelming"
SITESUBTITLE = "The blog of Evan Chen"
SITEURL = ""

PATH = "content"

TIMEZONE = "US/Eastern"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_PAGES_ON_MENU = True
MENU_INTERNAL_PAGES = (
    ("All", "archives", "archives/index.html"),
    ("Cats", "categories", "categories/index.html"),
)
MENUITEMS = (("Exit", "https://web.evanchen.cc"),)

DEFAULT_CATEGORY = "Uncategorized"
USE_FOLDER_AS_CATEGORY = True

CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"
CATEGORIES_SAVE_AS = "categories/index.html"
TAG_URL = "tag/{slug}"
TAG_SAVE_AS = "tag/{slug}/index.html"
ARCHIVES_SAVE_AS = "archives/index.html"

DEFAULT_PAGINATION = 10
PAGINATION_PATTERNS = (
    (1, "{url}", "{save_as}"),
    (2, "{base_name}/page/{number}/", "{base_name}/page/{number}/index.html"),
)

STATIC_PATHS = ["images", "media"]

ARTICLE_URL = "{slug}/"
ARTICLE_SAVE_AS = "{slug}/index.html"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

THEME = "theme"

PLUGINS = [
    "pelican_redirect",
    "pelican_katex",
]

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown_extensions.figure_caption": {},
    },
    "output_format": "html5",
}

SUMMARY_MAX_LENGTH = 150

OUTPUT_PATH = "/tmp/blog.evanchen.cc/"

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
