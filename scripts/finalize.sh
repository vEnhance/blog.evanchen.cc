#!/usr/bin/env bash
# Usage: scripts/finalize.sh <slug>
# Run from the main worktree after running stage.sh on dev.

set -euo pipefail
SLUG=${1:?Usage: finalize.sh <slug>}

[[ -f pelicanconf.py ]] || {
  echo "Error: run from repo root"
  exit 1
}
[[ $(git rev-parse --abbrev-ref HEAD) == "main" ]] || {
  echo "Error: not on main branch"
  exit 1
}

NEWPATH=$(git ls-tree -r --name-only dev | grep -E -- "[0-9]{4}-[0-9]{2}-[0-9]{2}-${SLUG}\.md$" | head -1) || true
[[ -n $NEWPATH ]] || {
  echo "No file found for slug '$SLUG' on dev. Did you run scripts/stage.sh first?"
  exit 1
}

# Safety check: refuse to publish if still marked as draft
grep -q "^status: draft$" <(git show "dev:$NEWPATH") && {
  echo "Error: file still has 'status: draft' on dev. Run scripts/stage.sh first."
  exit 1
}

# Restore file from dev into main working tree and commit
git restore --source=dev -- "$NEWPATH"
git add "$NEWPATH"
PREK_QUIET=1 git commit -m "feat($SLUG): publish on main" --quiet
git show --oneline --stat
