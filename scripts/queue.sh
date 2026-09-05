#!/usr/bin/env bash
# Usage: scripts/queue.sh
# Lists the publication queue, i.e. every post under content/ that dev has and
# main doesn't:
#   draft   still marked "status: draft"; needs scripts/stage.sh
#   staged  graduated from draft on dev;  needs scripts/finalize.sh
# Word counts cover the body only (frontmatter excluded). Works from any branch.

set -euo pipefail

REPO_ROOT=$(git rev-parse --show-toplevel)
cd "$REPO_ROOT"

# On dev, read the working tree so uncommitted writing counts; from any other
# branch, read the dev branch itself.
[[ $(git rev-parse --abbrev-ref HEAD) == "dev" ]] && ON_DEV=1 || ON_DEV=0

if [[ -t 1 && -z ${NO_COLOR:-} ]]; then
  BOLD=$'\e[1m' DIM=$'\e[2m' CYAN=$'\e[36m' GREEN=$'\e[32m' YELLOW=$'\e[33m' RESET=$'\e[0m'
else
  BOLD='' DIM='' CYAN='' GREEN='' YELLOW='' RESET=''
fi

read_post() {
  if ((ON_DEV)); then cat -- "$1"; else git show "dev:$1"; fi
}

declare -A ON_MAIN=()
while IFS= read -r path; do
  ON_MAIN[$path]=1
done < <(git ls-tree -r --name-only main -- content)

if ((ON_DEV)); then
  mapfile -t CANDIDATES < <(find content -type f -name "*.md" | sort)
else
  mapfile -t CANDIDATES < <(git ls-tree -r --name-only dev -- content | grep "\.md$" | sort)
fi

ROWS=()
TOTAL_WORDS=0
N_DRAFT=0
N_STAGED=0
W_STATUS=6 W_CATEGORY=8 W_DATE=4 W_SLUG=4 W_WORDS=5 # header label widths

for path in "${CANDIDATES[@]}"; do
  [[ -n ${ON_MAIN[$path]:-} ]] && continue

  content=$(read_post "$path")
  if grep -q "^status: draft$" <<<"$content"; then
    status=draft
    ((++N_DRAFT))
  else
    status=staged
    ((++N_STAGED))
  fi

  # Everything past the closing --- of the frontmatter is body.
  words=$(awk 'body { print } /^---$/ { if (++n == 2) body = 1 }' <<<"$content" | wc -w)
  TOTAL_WORDS=$((TOTAL_WORDS + words))

  category=$(basename "$(dirname "$path")")
  base=$(basename "$path" .md)
  if [[ $base =~ ^([0-9]{4}-[0-9]{2}-[0-9]{2})-(.+)$ ]]; then
    date=${BASH_REMATCH[1]} slug=${BASH_REMATCH[2]}
  else
    date="-" slug=$base
  fi

  ((${#status} > W_STATUS)) && W_STATUS=${#status}
  ((${#category} > W_CATEGORY)) && W_CATEGORY=${#category}
  ((${#date} > W_DATE)) && W_DATE=${#date}
  ((${#slug} > W_SLUG)) && W_SLUG=${#slug}
  ((${#words} > W_WORDS)) && W_WORDS=${#words}
  # Fields are laid out in sort order, so plain sort does the work.
  ROWS+=("$status	$date	$category	$slug	$words")
done

((${#ROWS[@]})) || exit 0

mapfile -t ROWS < <(printf "%s\n" "${ROWS[@]}" |
  LC_ALL=C sort -t$'\t' -k1,1 -k2,2 -k3,3 -k4,4)

printf "%s%-*s  %-*s  %-*s  %-*s  %*s%s\n" \
  "$BOLD" "$W_STATUS" STATUS "$W_CATEGORY" CATEGORY "$W_DATE" DATE \
  "$W_SLUG" SLUG "$W_WORDS" WORDS "$RESET"

for row in "${ROWS[@]}"; do
  IFS=$'\t' read -r status date category slug words <<<"$row"
  [[ $status == staged ]] && status_color=$GREEN || status_color=$YELLOW
  printf "%s%-*s%s  %s%-*s%s  %s%-*s%s  %-*s  %s%*s%s\n" \
    "$status_color" "$W_STATUS" "$status" "$RESET" \
    "$CYAN" "$W_CATEGORY" "$category" "$RESET" \
    "$DIM" "$W_DATE" "$date" "$RESET" \
    "$W_SLUG" "$slug" \
    "$GREEN" "$W_WORDS" "$words" "$RESET"
done

plural() {
  if (($1 == 1)); then echo "$1 $2"; else echo "$1 ${2}s"; fi
}

printf "%s%s (%s, %d staged), %'d words%s\n" \
  "$DIM" "$(plural "$((N_DRAFT + N_STAGED))" post)" "$(plural "$N_DRAFT" draft)" \
  "$N_STAGED" "$TOTAL_WORDS" "$RESET"
