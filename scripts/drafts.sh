#!/usr/bin/env bash

set -euo pipefail

REPO_ROOT=$(git rev-parse --show-toplevel)
BRANCH=$(git -C "$REPO_ROOT" rev-parse --abbrev-ref HEAD)

if [[ $BRANCH == "main" ]]; then
  git -C "$REPO_ROOT" grep -l "^status: draft" dev -- "*.md" \
    | sed 's/^dev://' \
    | sort
else
  grep -rl "^status: draft" "$REPO_ROOT/content/" --include="*.md" | sort
fi
