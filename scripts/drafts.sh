#!/usr/bin/env bash

set -euo pipefail

REPO_ROOT=$(git rev-parse --show-toplevel)
grep -rl "^status: draft" "$REPO_ROOT/content/" --include="*.md" | sort
