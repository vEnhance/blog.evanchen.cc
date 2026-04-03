#!/usr/bin/env bash
# Usage: scripts/publish.sh <slug>
set -euo pipefail
SLUG=${1:?Usage: publish.sh <slug>}
REPO_ROOT=$(git rev-parse --show-toplevel)

BRANCH=$(git -C "$REPO_ROOT" rev-parse --abbrev-ref HEAD)
[[ $BRANCH == "main" ]] || {
  echo "Error: must be on main branch (currently on '$BRANCH')"
  exit 1
}

RELPATH=$(git -C "$REPO_ROOT" ls-tree -r --name-only dev | grep -- "-${SLUG}\.md$" | head -1)
[[ -n $RELPATH ]] || {
  echo "No file found for slug '$SLUG' on dev"
  exit 1
}

mkdir -p "$(dirname "$REPO_ROOT/$RELPATH")"
echo "Writing to $RELPATH$RELPATH"
git -C "$REPO_ROOT" show "dev:$RELPATH" |
  sed 's/^status: draft$/status: published/' |
  tee "$REPO_ROOT/$RELPATH"
