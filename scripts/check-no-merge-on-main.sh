#!/usr/bin/env bash
# Prevent merge commits on the main branch.

BRANCH=$(git rev-parse --abbrev-ref HEAD)
[[ $BRANCH == "main" ]] || exit 0

MERGE_HEAD=$(git rev-parse --git-path MERGE_HEAD)
if [[ -f $MERGE_HEAD ]]; then
  echo "Error: merge commits are not allowed on main"
  exit 1
fi
