#!/usr/bin/env python3
"""Verifica o artefato real antes de enviá-lo ao GitHub Pages (stdlib)."""
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.robotparser import RobotFileParser
from urllib.parse import unquote, urljoin, urlsplit
import json
import argparse
import os
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
        self.meta_urls = []
        self.meta = {}
        self.titles = 0
        self.headings = 0
        self.lang = ''
        self.styles = []
        self.style_buffer = None
        self.ld_json = []
        self.json_buffer = None
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'style':
            self.style_buffer = ''
        if tag == 'html':
            self.lang = attrs.get('lang', '')
        if tag == 'title':
            self.titles += 1
        if tag == 'h1':
            self.headings += 1
        if tag == 'meta':
            self.meta[attrs.get('name') or attrs.get('property') or attrs.get('http-equiv')] = attrs.get('content', '')
        if attrs.get('id'):
            self.ids.add(attrs['id'])
        if tag in {'a', 'link'} and attrs.get('href'):
            self.links.append(attrs['href'])
        if tag in {'script', 'img', 'source'} and attrs.get('src'):
            self.links.append(attrs['src'])
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonical = attrs['href']
        if tag == 'meta' and attrs.get('property') == 'og:url':
            self.meta_urls.append(attrs['content'])
        if tag == 'script' and attrs.get('type') == 'application/ld+json':
            self.json_buffer = ''

    def handle_data(self, data):
        if self.style_buffer is not None:
            self.style_buffer += data
        if self.json_buffer is not None:
            self.json_buffer += data

    def handle_endtag(self, tag):
        if tag == 'style' and self.style_buffer is not None:
            self.styles.append(self.style_buffer)
            self.style_buffer = None
        if tag == 'script' and self.json_buffer is not None:
            self.ld_json.append(json.loads(self.json_buffer))
            self.json_buffer = None


documents = {p: Document(p.read_text()) for p in root.rglob('*.html')}
home = documents.get(root / 'index.html')
if home is None:
    sys.exit('ERRO: index.html não foi gerado.')
base = home.canonical
config_base = tomllib.loads(Path('hugo.toml').read_text())['baseURL']
expected_base = (os.environ.get('BLOG_BASE_URL') or config_base).rstrip('/') + '/'
if base != expected_base:
    errors.append(f'URL canônica da home diverge da configuração: {base} (esperado: {expected_base})')
origin = urlsplit(base).netloc
base_path = urlsplit(base).path


def verify_site_url(url, source):
    if not url or not url.startswith(expected_base):
        errors.append(f'{source}: URL fora do endereço canônico {expected_base}: {url}')


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
    verify_site_url(document.canonical, f'{relative} (canonical)')
    for url in document.meta_urls:
        verify_site_url(url, f'{relative} (Open Graph)')
    if 'refresh' not in document.meta:
        if document.titles != 1 or document.headings != 1 or document.lang != 'pt-BR':
            errors.append(f'{relative}: título, H1 ou idioma inválido')
        for key in ['description', 'og:title', 'og:description', 'og:image', 'og:image:alt', 'twitter:card', 'twitter:title', 'twitter:description', 'twitter:image', 'twitter:image:alt']:
            if not document.meta.get(key):
                errors.append(f'{relative}: metadado ausente: {key}')
        if document.meta.get('og:description') != document.meta.get('description'):
            errors.append(f'{relative}: descrições sociais divergentes')
        if document.meta.get('twitter:image') != document.meta.get('og:image'):
            errors.append(f'{relative}: imagens sociais divergentes')
        image_target = resolve_url(document.meta.get('og:image', ''))
        if image_target is not None and not image_target.is_file():
            errors.append(f'{relative}: imagem social ausente')
    for data in document.ld_json:
        for node in data.get('@graph', [data]):
            if 'url' in node:
                verify_site_url(node['url'], f'{relative} (JSON-LD)')
    page_url = urljoin(base, relative.removesuffix('index.html'))
    for style in document.styles:
        document.links.extend(re.findall(r'url\([\'\"]?([^\)\'\"]+)', style))
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
    'privacidade/index.html',
    'categorias/inteligencia-artificial/index.html',
    'categorias/cloud/index.html', 'categorias/produtividade/index.html',
    '404.html', 'index.json',
    'index.xml', 'posts/index.xml', 'sitemap.xml', 'robots.txt', 'llms.txt',
]:
    if not (root / required).is_file():
        errors.append(f'Saída obrigatória ausente: {required}')

feed_links = []
for xml in root.rglob('*.xml'):
    tree = ET.parse(xml)
    for loc in tree.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc'):
        verify_site_url(loc.text, f'{xml} (sitemap)')
        target = resolve_url(loc.text)
        if target not in documents or 'noindex' in documents[target].meta.get('robots', ''):
            errors.append(f'{xml}: sitemap inclui página ausente ou noindex: {loc.text}')
    for link in tree.findall('./channel/link') + tree.findall('./channel/item/link'):
        verify_site_url(link.text, f'{xml} (RSS)')
    for link in tree.findall('./channel/{http://www.w3.org/2005/Atom}link'):
        verify_site_url(link.get('href'), f'{xml} (Atom)')
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

llms = (root / 'llms.txt').read_text()
llms_links = re.findall(r'\]\((https://[^)]+)\)', llms)
for link in llms_links:
    verify_site_url(link, 'llms.txt')
    target = resolve_url(link)
    if target is None or not target.is_file():
        errors.append(f'llms.txt: link sem destino público: {link}')
for link in feed_links:
    if link not in llms_links:
        errors.append(f'llms.txt: publicação do RSS ausente: {link}')
robots = RobotFileParser()
robots.parse((root / 'robots.txt').read_text().splitlines())
for agent in ['Googlebot', 'bingbot', 'OAI-SearchBot', 'Claude-SearchBot', 'Claude-User']:
    if not robots.can_fetch(agent, base):
        errors.append(f'Busca pública bloqueada: {agent}')
for agent in ['GPTBot', 'ClaudeBot', 'Google-Extended']:
    if robots.can_fetch(agent, base):
        errors.append(f'Coleta para treinamento não bloqueada: {agent}')
for path in ['busca/index.html', '404.html']:
    if 'noindex' not in documents[root / path].meta.get('robots', ''):
        errors.append(f'{path}: noindex ausente')

if errors:
    print('\n'.join(f'ERRO: {error}' for error in errors))
    sys.exit(1)
print(f'OK: {len(documents)} páginas HTML, URLs canônicas, links e assets locais, metadados sociais, JSON-LD, XML/RSS, llms.txt, robots, busca e exclusão de rascunhos verificados.')
