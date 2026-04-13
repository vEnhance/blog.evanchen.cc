# blog.evanchen.cc

This are the source files for Evan Chen's personal blog,
<https://blog.evanchen.cc>.

Pull requests to fix typos, repair broken site functionality, and so on
are greatly appreciated (indeed this is a motivation for a public GitHub).
It might also be helpful if you want to see how the site was built.

## Development

### Installation

After installing [uv](https://docs.astral.sh/uv), do

- `uv sync` to install dependencies
- `uv run prek install` to install pre-commit hooks

### Compilation

In theory, you can compile the content with the following:

- `uv run pelican content` to build development site to `output/`
- `uv run pelican content -s publishconf.py` to build the published version
  to `output/` (absolute URL's)
- `uv run pelican --listen` to launch a development server

However, in practice when developing you probably don't need to compile all
100+ posts for testing, or for previewing a single post
(particularly since KaTeX rendering is really slow, this can take minutes).
Instead, the following utility scripts are provided:

- Use `scripts/new.py` to set up a new post.
- `scripts/recent.sh [N]` sets up a dev server
  where only posts in the last N days are rendered.
  By default N = 365, i.e., this renders only the last year of posts.
- `scripts/watch-one.sh <slug>` sets up a dev server
  that only renders a single post specified by the slug.

### Working on a dev branch

You might prefer a workflow where new posts are written on `dev`
or `dev/*`, rather than `main`.
If so, after writing the post on `dev`,
use `.scripts/publish.sh <slug> [YYYY-MM-DD]` to squash onto main.
