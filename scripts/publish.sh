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

mkdir -p "$(dirname "$REPO_ROOT/$NEWRELPATH")"
echo "Writing to $NEWRELPATH"
git -C "$REPO_ROOT" show "dev:$RELPATH" |
  sed "s/^status: draft$/status: published/" |
  sed "s/^date: .*/date: ${PUBLISH_DATE} 00:00/" |
  tee "$REPO_ROOT/$NEWRELPATH"
