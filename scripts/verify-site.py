#!/usr/bin/env python3
"""Verifica o artefato real antes de enviá-lo ao GitHub Pages (stdlib)."""
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
import json
import argparse
import re
import sys
import tomllib
import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('output', nargs='?', type=Path, default=Path('public'))
parser.add_argument('--content-dir', type=Path, default=Path('content'))
args = parser.parse_args()
root = args.output.resolve()
errors = []


class Document(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links = []
        self.ids = set()
        self.canonical = ''
        self.ld_json = []
        self.json_buffer = None
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'):
            self.ids.add(attrs['id'])
        if tag in {'a', 'link'} and attrs.get('href'):
            self.links.append(attrs['href'])
        if tag in {'script', 'img', 'source'} and attrs.get('src'):
            self.links.append(attrs['src'])
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonical = attrs['href']
        if tag == 'script' and attrs.get('type') == 'application/ld+json':
            self.json_buffer = ''

    def handle_data(self, data):
        if self.json_buffer is not None:
            self.json_buffer += data

    def handle_endtag(self, tag):
        if tag == 'script' and self.json_buffer is not None:
            self.ld_json.append(json.loads(self.json_buffer))
            self.json_buffer = None


documents = {p: Document(p.read_text()) for p in root.rglob('*.html')}
home = documents.get(root / 'index.html')
if home is None:
    sys.exit('ERRO: index.html não foi gerado.')
base = home.canonical
origin = urlsplit(base).netloc
base_path = urlsplit(base).path


def resolve_url(url):
    parsed = urlsplit(url)
    if parsed.netloc != origin or parsed.scheme not in {'http', 'https'}:
        return None
    path = unquote(parsed.path)
    if not path.startswith(base_path):
        errors.append(f'Link fora da base do site: {url}')
        return None
    target = root / path[len(base_path):]
    if path.endswith('/') or target.is_dir():
        target = target / 'index.html'
    return target


for path, document in documents.items():
    relative = path.relative_to(root).as_posix()
    page_url = urljoin(base, relative.removesuffix('index.html'))
    for link in document.links:
        absolute = urljoin(page_url, link)
        target = resolve_url(absolute)
        if target is None:
            continue
        if not target.is_file():
            errors.append(f'{relative}: link local ausente: {link}')
        fragment = unquote(urlsplit(absolute).fragment)
        if fragment and target in documents and fragment not in documents[target].ids:
            errors.append(f'{relative}: âncora ausente: {link}')

for css in root.rglob('*.css'):
    for url in re.findall(r'url\([\'\"]?([^\)\'\"]+)', css.read_text()):
        target = resolve_url(urljoin(urljoin(base, css.relative_to(root).as_posix()), url))
        if target is not None and not target.is_file():
            errors.append(f'Asset CSS ausente: {url}')

for required in [
    'sobre/index.html', 'arquivo/index.html', 'busca/index.html',
    'categorias/index.html', 'tags/index.html', 'licencas/index.html',
    'categorias/inteligencia-artificial/index.html',
    'categorias/cloud/index.html', 'categorias/produtividade/index.html',
    '404.html', 'index.json',
    'index.xml', 'posts/index.xml', 'sitemap.xml', 'robots.txt',
]:
    if not (root / required).is_file():
        errors.append(f'Saída obrigatória ausente: {required}')

feed_links = []
for xml in root.rglob('*.xml'):
    tree = ET.parse(xml)
    items = tree.findall('./channel/item')
    dates = [parsedate_to_datetime(item.findtext('pubDate')) for item in items]
    if dates != sorted(dates, reverse=True):
        errors.append(f'RSS fora de ordem cronológica: {xml}')
    guids = [item.findtext('guid') for item in items]
    if len(guids) != len(set(guids)):
        errors.append(f'Identificadores duplicados no RSS: {xml}')
    for item in items:
        target = resolve_url(item.findtext('link'))
        if target is None or not target.is_file():
            errors.append(f'Artigo do RSS não existe no artefato: {xml}')
    if xml == root / 'index.xml':
        feed_links = [item.findtext('link') for item in items]

index = json.loads((root / 'index.json').read_text())
for item in index:
    if '/posts/' not in urlsplit(item['permalink']).path:
        errors.append('Página institucional encontrada na busca.')
    target = resolve_url(item['permalink'])
    if target is None or not target.is_file():
        errors.append(f'Resultado de busca sem arquivo: {item["permalink"]}')

ids = set()
now = datetime.now(timezone.utc)
for source in (args.content_dir / 'posts').rglob('index.md'):
    meta = tomllib.loads(source.read_text().split('+++', 2)[1])
    required_fields = ['title', 'date', 'slug', 'postId']
    if not meta.get('draft'):
        required_fields += ['description', 'categorias']
    for key in required_fields:
        if not meta.get(key):
            errors.append(f'{source}: campo obrigatório ausente: {key}')
    post_id = meta.get('postId')
    if post_id in ids:
        errors.append(f'postId duplicado: {post_id}')
    ids.add(post_id)
    date = datetime.fromisoformat(str(meta['date']))
    if date.tzinfo is None:
        errors.append(f'{source}: data precisa de fuso horário.')
        continue
    permalink = urljoin(base, f'posts/{date:%Y/%m}/{meta["slug"]}/')
    target = resolve_url(permalink)
    if meta.get('draft') or date > now:
        if target is not None and target.exists():
            errors.append(f'Rascunho/data futura vazou no build de produção: {source}')
        if any(item['permalink'] == permalink for item in index) or permalink in feed_links:
            errors.append(f'Rascunho/data futura vazou na busca/RSS: {source}')
    elif target is None or not target.is_file():
        errors.append(f'Publicação ausente: {source}')

if errors:
    print('\n'.join(f'ERRO: {error}' for error in errors))
    sys.exit(1)
print(f'OK: {len(documents)} páginas HTML, links e assets locais, JSON-LD, XML/RSS, busca e exclusão de rascunhos verificados.')
