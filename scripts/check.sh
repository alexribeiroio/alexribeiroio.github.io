#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
args=(--gc --minify --cleanDestinationDir --panicOnWarning --printPathWarnings)
if [[ -n ${BLOG_BASE_URL:-} ]]; then
  args+=(--baseURL "${BLOG_BASE_URL%/}/")
fi
./scripts/hugo.sh "${args[@]}" "$@"
python3 scripts/verify-site.py public
