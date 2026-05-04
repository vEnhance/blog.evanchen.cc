#!/usr/bin/env bash
# Usage: scripts/publish.sh <slug> [YYYY-MM-DD]
set -euo pipefail
SLUG=${1:?Usage: publish.sh <slug> [YYYY-MM-DD]}
PUBLISH_DATE=${2:-$(date +%F)}
REPO_ROOT=$(git rev-parse --show-toplevel)

BRANCH=$(git -C "$REPO_ROOT" rev-parse --abbrev-ref HEAD)
[[ $BRANCH == "main" ]] || {
  echo "Error: must be on main branch (currently on '$BRANCH')"
  exit 1
}

RELPATH=$(git -C "$REPO_ROOT" ls-tree -r --name-only dev | grep -E -- "[0-9]{4}-[0-9]{2}-[0-9]{2}-${SLUG}\.md$" | head -1)
[[ -n $RELPATH ]] || {
  echo "No file found for slug '$SLUG' on dev"
  exit 1
}

NEWRELPATH=${RELPATH/%[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]-${SLUG}.md/${PUBLISH_DATE}-${SLUG}.md}

# Write transformed content to a temp file (avoids $() stripping trailing newlines)
TMPFILE=$(mktemp)
trap 'rm -f "$TMPFILE"' EXIT
git -C "$REPO_ROOT" show "dev:$RELPATH" \
  | sed "s/^status: draft$/status: published/" \
  | sed "s/^date: .*/date: ${PUBLISH_DATE} 13:37/" \
  > "$TMPFILE"

# Update main: write new file with publish date (no auto-commit)
mkdir -p "$(dirname "$REPO_ROOT/$NEWRELPATH")"
echo "Writing to $NEWRELPATH on main"
cp "$TMPFILE" "$REPO_ROOT/$NEWRELPATH"

# Update dev: git mv + same content changes, auto-committed via worktree
WORKTREE=$(mktemp -d)
trap 'git -C "$REPO_ROOT" worktree remove --force "$WORKTREE" 2>/dev/null; rm -f "$TMPFILE"' EXIT
git -C "$REPO_ROOT" worktree add -q "$WORKTREE" dev
mkdir -p "$(dirname "$WORKTREE/$NEWRELPATH")"
git -C "$WORKTREE" mv "$RELPATH" "$NEWRELPATH"
cp "$TMPFILE" "$WORKTREE/$NEWRELPATH"
git -C "$WORKTREE" add "$NEWRELPATH"
git -C "$WORKTREE" commit -m "feat: publish $SLUG"
git -C "$REPO_ROOT" worktree remove "$WORKTREE"

echo "Done. Dev committed. Review $NEWRELPATH on main, then commit."
