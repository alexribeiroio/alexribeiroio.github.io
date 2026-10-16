#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
version=$(tr -d '\n' < .hugo-version)
if [[ $(uname -s) != Linux || $(uname -m) != x86_64 ]]; then
  echo 'Este instalador atende Linux x86_64. Instale a versão de .hugo-version pelo site oficial: https://gohugo.io/installation/' >&2
  exit 1
fi
mkdir -p .tools
download_dir=$(mktemp -d)
trap 'rm -rf "$download_dir"' EXIT
curl --fail --location --retry 3 --silent --show-error \
  "https://github.com/gohugoio/hugo/releases/download/v${version}/hugo_${version}_linux-amd64.tar.gz" \
  --output "$download_dir/hugo.tar.gz"
checksum=$(tr -d '\n' < .hugo-linux-amd64.sha256)
printf '%s  %s\n' "$checksum" "$download_dir/hugo.tar.gz" | sha256sum --check --status
tar -xzf "$download_dir/hugo.tar.gz" -C .tools hugo
.tools/hugo version
