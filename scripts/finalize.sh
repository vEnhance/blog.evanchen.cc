#!/usr/bin/env bash
# Usage: scripts/finalize.sh <slug> [YYYY-MM-DD]
#
set -euo pipefail
SLUG=${1:?Usage: finalize.sh <slug> [YYYY-MM-DD]}
PUBLISH_DATE=${2:-$(date +%F)}

[[ -f pelicanconf.py ]] || {
  echo "Error: run from repo root"
  exit 1
}
[[ $(git rev-parse --abbrev-ref HEAD) == "main" ]] || {
  echo "Error: not on main branch"
  exit 1
}

RELPATH=$(git ls-tree -r --name-only dev | grep -E -- "[0-9]{4}-[0-9]{2}-[0-9]{2}-${SLUG}\.md$" | head -1)
[[ -n $RELPATH ]] || {
  echo "No file found for slug '$SLUG' on dev"
  exit 1
}

NEWRELPATH=${RELPATH/%[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]-${SLUG}.md/${PUBLISH_DATE}-${SLUG}.md}

# Update dev: rename, edit in place, commit
git checkout dev
git mv "$RELPATH" "$NEWRELPATH"
sed -i "s/^status: draft$/status: published/" "$NEWRELPATH"
sed -i "s/^date: .*/date: ${PUBLISH_DATE} 13:37/" "$NEWRELPATH"
git add "$NEWRELPATH"
git commit -m "feat($SLUG): finalize draft"

# Update main: pull the published file into working tree (no auto-commit)
git checkout main
echo "Writing to $NEWRELPATH on main"
git checkout dev -- "$NEWRELPATH"
git commit -m "feat($SLUG): publish"
