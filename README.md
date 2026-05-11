# blog.evanchen.cc

These are the source files for Evan Chen's personal blog,
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
(particularly since KaTeX rendering is really slow).
Instead, the following utility scripts are provided:

- `scripts/recent.sh [N]` sets up a dev server
  where only posts in the last N days are rendered.
  By default, N = 365, i.e., this renders only the last year of posts.
- `scripts/watch-one.sh <slug>` sets up a dev server
  that only renders a single post specified by the slug.

### Working on a dev branch (for writing new posts)

When I am drafting brand-new posts,
I do so on a separate branch `dev` rather than `main`.
That way the Git history for `main` remains clean,
rather than seeing the long revision history of the posts being edited.
(Writing is rewriting, you know?)

I actually use a separate worktree altogether for this workflow.
But you can also switch branches manually.

The workflow goes as follows:

1. `git merge main` in `dev` to bring `dev` up to date.

2. `./scripts/new.py` is used on `dev` to create a new post.
   The date is set as December 31, 2099,
   since I really hope that I can finish the post by then.

3. Slowly work on the post (often over way-too-many months).

4. When the post is ready to publish, run `./scripts/stage.sh <slug> [YYYY-MM-DD]` on `dev`.
   This changes the status from `draft` to `published` and updates the date.

5. Once the post is ready to bring into main,
   run `./scripts/finalize.sh <slug>` on `main` to copy the finalized post in.
   This creates a commit `feat(slug): publish on main`.

6. Again, `git merge main` in `dev` to bring `dev` up to date with the published post.

To preserve my sanity,
commits from `dev` NEVER appear directly on `main`.
In other words, besides the `finalize.sh` script that simply copies
the completed drafts off the `dev` branch,
the `main` branch never receives anything from the `dev` branch.

There's another `./scripts/drafts.sh` that lists the current drafts,
which works on any branch.
