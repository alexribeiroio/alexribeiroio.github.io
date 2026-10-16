#!/usr/bin/env python3
"""Exercise article templates in an isolated build; never publish fixtures."""
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
from html.parser import HTMLParser

class Page(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.schemas = []
        self.buffer = None
        self.images = []
        self.feed(source)
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'script' and attrs.get('type') == 'application/ld+json':
            self.buffer = ''
        if tag == 'img':
            self.images.append(attrs)
    def handle_data(self, data):
        if self.buffer is not None:
            self.buffer += data
    def handle_endtag(self, tag):
        if tag == 'script' and self.buffer is not None:
            self.schemas.extend(json.loads(self.buffer)['@graph'])
            self.buffer = None

with tempfile.TemporaryDirectory(prefix='blog-seo-') as temp:
    root = Path(temp)
    content = root / 'content'
    shutil.copytree('content', content)
    post = content / 'posts' / 'seo-fixture'
    post.mkdir(parents=True)
    (post / 'index.md').write_text('''+++
title = 'Teste técnico <SEO> & metadados'
description = 'Descrição de teste & caracteres especiais.'
date = '2025-01-02T12:00:00-03:00'
lastmod = '2025-01-03T12:00:00-03:00'
slug = 'seo-fixture'
postId = 'seo-fixture-not-editorial'
draft = false
categorias = ['Cloud']
tags = ['Teste técnico']
[cover]
image = 'cover.png'
alt = 'Imagem técnica de teste'
+++

Texto sintético exclusivo para validação local.

## Conteúdo extraível

[Sobre o autor](/sobre/).

![Exemplo com dimensões](cover.png)
''')
    shutil.copyfile('assets/images/social-base.png', post / 'cover.png')
    output = root / 'public'
    subprocess.run(['./scripts/hugo.sh', '--environment', 'production', '--contentDir', str(content), '--destination', str(output), '--panicOnWarning', '--minify'], check=True)
    subprocess.run(['python3', 'scripts/verify-site.py', str(output), '--content-dir', str(content)], check=True)
    html = (output / 'posts/2025/01/seo-fixture/index.html').read_text()
    page = Page(html)
    article = next(n for n in page.schemas if n['@type'] == 'BlogPosting')
    assert article['headline'] == 'Teste técnico <SEO> & metadados'
    assert article['datePublished'] == '2025-01-02T12:00:00-03:00'
    assert article['dateModified'] == '2025-01-03T12:00:00-03:00'
    assert article['image'].endswith('/posts/2025/01/seo-fixture/cover.png')
    assert article['author']['@id'].endswith('/#person')
    assert article['mainEntityOfPage']['@id'].endswith('/seo-fixture/#webpage')
    assert all(i.get('width') and i.get('height') and i.get('alt') for i in page.images)
    assert 'Texto sintético' in html and '<article' in html and 'rel=author' in html
    assert 'https://www.alexribeiro.io/tags/teste-tecnico/' in (output / 'sitemap.xml').read_text()
    assert 'seo-fixture' in (output / 'llms.txt').read_text()
    print('OK: artigo isolado, datas, autoria, imagem do bundle, escape JSON-LD, semântica, tags e descoberta.')
