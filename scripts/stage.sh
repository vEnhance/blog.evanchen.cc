#!/usr/bin/env bash
# Usage: scripts/stage.sh <slug> [YYYY-MM-DD]
# Run from the dev worktree. Renames draft, marks published, commits to dev.

set -euo pipefail
SLUG=${1:?Usage: stage.sh <slug> [YYYY-MM-DD]}
PUBLISH_DATE=${2:-$(date +%F)}

[[ -f pelicanconf.py ]] || { echo "Error: run from repo root"; exit 1; }
[[ $(git rev-parse --abbrev-ref HEAD) == "dev" ]] || { echo "Error: not on dev branch"; exit 1; }

OLDPATH=$(git ls-tree -r --name-only HEAD | grep -E -- "[0-9]{4}-[0-9]{2}-[0-9]{2}-${SLUG}\.md$" | head -1) || true
[[ -n $OLDPATH ]] || { echo "No file found for slug '$SLUG' on dev"; exit 1; }
NEWPATH=${OLDPATH/%[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]-${SLUG}.md/${PUBLISH_DATE}-${SLUG}.md}

git mv "$OLDPATH" "$NEWPATH"
sed -i "s/^status: draft$/status: published/" "$NEWPATH"
sed -i "s/^date: .*/date: ${PUBLISH_DATE} 13:37/" "$NEWPATH"
git add "$NEWPATH"
PREK_QUIET=1 git commit -m "feat($SLUG): finalize draft on dev" --quiet
git show --oneline --stat
