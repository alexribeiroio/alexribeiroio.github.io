#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
if [[ ! ${1:-} =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]]; then
  echo 'Uso: ./scripts/new-post.sh titulo-do-artigo (letras minúsculas sem acentos, números e hífens)' >&2
  exit 1
fi
post_path="posts/$(TZ=America/Sao_Paulo date +%Y/%m/%d)-$1"
./scripts/hugo.sh new content --kind posts "$post_path"
