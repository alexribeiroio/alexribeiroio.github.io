# Revisão de SEO — 16/10/2026

## Diagnóstico e decisões

- O commit anterior `9a0d2b8` já corrigiu o domínio canônico para `https://www.alexribeiro.io/`. A home pública confirmou esse canonical e o domínio sem www retornou 301 para www. A configuração e o pipeline foram preservados.
- Não existem artigos publicados: os quatro exemplos continuam com `draft = true`. Nenhum radar semanal foi criado. Um artigo sintético existe somente no teste em diretório temporário, nunca no artefato publicado.
- Títulos descritivos, descrição textual comum ao HTML e cartões, Open Graph e cartões com imagem padrão PNG 1200×630 gerada localmente pelo Hugo. Capas específicas de artigos têm prioridade; as imagens do bundle usam a URL do artigo.
- JSON-LD conecta `Person`, `WebSite`, `WebPage`/`CollectionPage`/`ProfilePage` e `BlogPosting`. Apenas nome, perfis e informações já existentes são usados. Artigos recebem datas de front matter, autoria com link visível, assunto e imagem quando há capa editorial. Não há qualificações inventadas nem datas de build fingindo atualização editorial. Não se presume que toda imagem de terceiros tenha a licença geral do blog.
- Busca interna, 404 e taxonomias/seções vazias têm `noindex, follow`. O sitemap omite páginas noindex; categorias e tags com publicações entram automaticamente. Navegação e RSS permanecem disponíveis. O RSS respeita `hiddenInRss`; os feeds gerais contêm apenas artigos.
- `/llms.txt` é gerado de páginas públicas com descrições, links canônicos, navegação, sitemap e RSS. Artigos entram quando publicados; rascunhos e páginas noindex são excluídos. Não inclui conteúdo privado, instruções para contornar restrições ou permissão de treinamento. É um índice experimental, não garantia de adoção, indexação, ranking ou citação.

## Bots e limites

`OAI-SearchBot` e `Claude-SearchBot` continuam sujeitos à regra pública geral. `GPTBot` e `ClaudeBot` recebem `Disallow: /`, sinalizando exclusão de coleta para treinamento. `Claude-User` também permanece acessível para solicitações de leitores. A documentação da OpenAI distingue `ChatGPT-User` de rastreamento automático e informa que robots.txt pode não se aplicar a solicitações iniciadas pelo usuário. Essas regras não são autenticação nem garantia contra agentes que as ignorem.

`Google-Extended` recebe `Disallow: /`: seu controle cobre treinamento **e grounding** no Gemini/Vertex, sem afetar inclusão ou ranking no Google Search. Googlebot permanece acessível, inclusive para as funcionalidades de IA do Search. Não foram alterados DNS, firewall, permissões, contas ou políticas de branch.

## Desempenho, acessibilidade e extração

O conteúdo principal já é HTML estático com `main`, `article`, um H1, cabeçalhos, links internos e âncoras. Busca tem fallback para arquivo/categorias sem JavaScript; há link para pular ao conteúdo, foco visível e idioma pt-BR. Giscus continua desligado. A revisão adiciona autoria visível com link, datas de atualização em `time`, alternativas textuais sociais e dimensões de imagens locais no corpo para reduzir deslocamento de layout.

A folha CSS minificada tem aproximadamente 26 KiB e passou a ser incorporada ao HTML para eliminar uma requisição que bloqueava a renderização. As fontes WOFF2 locais somam 146.644 bytes, contra 410.536 bytes das TTF originais (redução de 64,3% no tamanho dos arquivos; a transferência anterior já era comprimida pelo servidor), preservando glifos, métricas e licença, com `font-display: swap`. As TTF permanecem disponíveis para compatibilidade com CSS previamente cacheado. A imagem social tem cerca de 43 KiB e é metadado, não imagem no corpo. Não foram adicionados scripts de terceiros. Não há medição de Core Web Vitals com usuários reais nem auditoria completa WCAG. A validação posterior no PageSpeed Insights é documentada em [docs/pagespeed.md](pagespeed.md).

## Validação reproduzível

`make check` executa build de produção com falha em warnings, verifica links/assets/âncoras, canonical, OG, metadados sociais, idioma/H1, JSON-LD, sitemap/RSS, busca, robots e llms.txt, além da exclusão de rascunhos. Em seguida, `scripts/test-seo.py` cria um build isolado com um artigo sintético e verifica autoria, datas, caracteres especiais, imagem do bundle, dimensões, texto HTML, categoria/tag, sitemap, RSS e llms.txt. O diretório temporário é removido ao terminar.

Templates personalizados de `head.html` e do render hook de imagens devem ser comparados ao PaperMod ao atualizar o tema. O snapshot em `themes/PaperMod` não foi modificado.

## Documentação oficial consultada

- [Google: canonical e URLs duplicadas](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)
- [Google: sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)
- [Google: dados estruturados Article](https://developers.google.com/search/docs/appearance/structured-data/article)
- [Google: recursos de IA e fundamentos de SEO](https://developers.google.com/search/docs/appearance/ai-features)
- [Google: Google-Extended](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers#google-extended)
- [OpenAI: crawlers e agentes](https://developers.openai.com/api/docs/bots)
- [Anthropic: finalidades dos três bots e robots.txt](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)
- [Hugo: formatos de saída](https://gohugo.io/configuration/output-formats/) e [sitemap](https://gohugo.io/templates/sitemap/)
- [Open Graph](https://ogp.me/)
- [Proposta llms.txt](https://llmstxt.org/)

As referências descrevem mecanismos e recomendações; nenhum provedor garante inclusão, ranking ou uso de llms.txt.
