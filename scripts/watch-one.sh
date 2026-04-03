#!/usr/bin/env bash
# Usage: scripts/watch-one.sh <slug>

set -euo pipefail

SLUG=${1:?Usage: watch-one.sh <slug>}

REPO_ROOT=$(git rev-parse --show-toplevel)
FILE=$(find "$REPO_ROOT/content" -name "*-${SLUG}.md" | head -1)
[[ -n $FILE ]] || {
  echo "No file found for slug: $SLUG"
  exit 1
}

RELPATH=$(realpath --relative-to="$REPO_ROOT/content" "$FILE")

cd "$REPO_ROOT"
echo "Rendering only the article $FILE..."
uv run pelican content -l -r -e "ARTICLE_PATHS=[\"$RELPATH\"]"
