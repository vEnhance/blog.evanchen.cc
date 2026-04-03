#!/usr/bin/env bash

set -euo pipefail

cd "$(git rev-parse --show-toplevel)"
RECENT_DAYS=${1:-} uv run pelican --listen --autoreload --settings recentconf.py
