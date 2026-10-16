#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
cache_dir="$PWD/.cache/hugo"
if [[ -x .tools/hugo ]]; then
  exec .tools/hugo "$@" --cacheDir "$cache_dir"
elif command -v hugo >/dev/null 2>&1; then
  exec hugo "$@" --cacheDir "$cache_dir"
else
  echo 'Hugo não encontrado. Execute ./scripts/install-hugo.sh ou instale a versão de .hugo-version.' >&2
  exit 1
fi
