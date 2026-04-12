import os

AUTHOR = "Evan Chen 《陳誼廷》"
SITENAME = "Power Overwhelming"
SITESUBTITLE = "The blog of Evan Chen"
SITEDESCRIPTION = "Evan Chen's blog. Math, Linux, teaching, puzzle hunts, and the like."
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
    ("Cats", "categories", "categories/index.html"),
    ("All", "archives", "archives/index.html"),
)

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

STATIC_PATHS = []

ARTICLE_URL = "{slug}/"
ARTICLE_SAVE_AS = "{slug}/index.html"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

THEME = "theme"

PLUGIN_PATHS = ["plugins"]
PLUGINS = [
    "auto_attach",
    "pelican_redirect",
    "pelican_katex",
    "sidenotes",
    "seo",
    "autolink_style",
    "all_articles",
    "sort_tags",
    "cf_redirects",
]

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown_ext_custom.separate_blockquotes": {},
        "markdown_ext_custom.figure_caption": {},
        "mdx_truly_sane_lists": {},
        "markdown.extensions.smarty": {},
    },
    "output_format": "html5",
}

SUMMARY_MAX_LENGTH = 150

# On dev, output stuff to /tmp
OUTPUT_PATH = os.path.expanduser("~/.cache/blog.evanchen.cc/")

AUTHORS_SAVE_AS = ""

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

SEO_ENHANCER_AUTHOR_FACEBOOK_PROFILES = {
    AUTHOR: "https://www.facebook.com/evanchenmath/",
}
