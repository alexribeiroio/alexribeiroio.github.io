# Google PageSpeed Insights — 16/10/2026

Medições reais executadas pela interface pública de [PageSpeed Insights](https://pagespeed.web.dev/), com Lighthouse 13.5.0/HeadlessChromium 153.0.8010.36. Mobile: Moto G Power emulado e 4G lento; desktop: área de trabalho emulada e limitação personalizada. Cada relatório oferece as duas abas. Os horários abaixo são UTC (a interface exibiu BRT).

A API pública sem chave retornou HTTP 429 por quota diária esgotada; as medições foram concluídas pela interface oficial, não por Lighthouse local. O PSI mostrou **“Nenhum dado”** de campo nas páginas medidas: as notas são resultados de laboratório, não Core Web Vitals de usuários reais.

## Antes da otimização de desempenho

Commit `97507eaf3a87716ceffe30c0a369b484d4c8ec9e`.

Ordem das notas: desempenho / acessibilidade / práticas recomendadas / SEO.

| Página | Horário UTC | Mobile | Desktop | Relatório |
|---|---|---|---|---|
| Home | 22:31:29 | 98 / 100 / 100 / 100 | 100 / 100 / 100 / 100 | [PSI](https://pagespeed.web.dev/analysis/https-www-alexribeiro-io/fo5vqb9xu5?form_factor=mobile) |
| Sobre | 22:31:46 | 100 / 100 / 100 / 100 | 100 / 100 / 100 / 100 | [PSI](https://pagespeed.web.dev/analysis/https-www-alexribeiro-io-sobre/o1hdgqps8v?form_factor=mobile) |
| Arquivo | 22:32:35 | 98 / 100 / 100 / 100 | 100 / 100 / 100 / 100 | [PSI](https://pagespeed.web.dev/analysis/https-www-alexribeiro-io-arquivo/37iq445yiz?form_factor=mobile) |
| Categoria Cloud, vazia | 22:32:56 | 100 / 100 / 100 / 66 | 100 / 100 / 100 / 66 | [PSI](https://pagespeed.web.dev/analysis/https-www-alexribeiro-io-categorias-cloud/iacdk7yis5?form_factor=mobile) |

Na home mobile, FCP e LCP foram 1,8 s, TBT 0 ms, CLS 0 e Speed Index 2,6 s. No arquivo mobile: 1,8 s / 1,8 s / 0 ms / 0 / 2,7 s. A folha CSS externa foi apontada como bloqueadora da renderização, com economia estimada de cerca de 1.500 ms. Sobre mobile: FCP/LCP 0,8 s, TBT 0 ms, CLS 0,001, Speed Index 0,8 s.

## Ajustes publicados

Commit `cc9394c10116e6511f6114b03f658055bf3caa02`, [deploy concluído](https://github.com/alexribeiroio/alexribeiroio.github.io/actions/runs/38976494590).

- CSS minificado incorporado ao HTML, eliminando a requisição que bloqueava a primeira renderização. Preservados os estilos, a ordem, a licença e a operação sem JavaScript; o custo é repetir cerca de 26 KiB de CSS bruto em cada documento, em vez de reutilizar um arquivo cacheado.
- Fontes locais convertidas sem perda para WOFF2, preservando o mapa de glifos e as métricas de avanço. FontTools 4.67.0/Brotli 1.2.0 foram usados temporariamente, sem nova dependência de runtime ou CI. Os arquivos caíram de 410.536 para 146.644 bytes no disco (64,3%). Isso não deve ser confundido com redução equivalente na transferência: o servidor já comprimia os TTF. TTF originais e licença OFL foram preservados para compatibilidade com CSS cacheado.
- O verificador passou a conferir também os assets referenciados em CSS inline. Build de produção e teste de artigo isolado passaram localmente e no GitHub Actions.

As recomendações seguem [Chrome: recursos que bloqueiam renderização](https://developer.chrome.com/docs/performance/insights/render-blocking) e [web.dev: fontes](https://web.dev/articles/font-best-practices).

## Depois da otimização

Resultados do commit `cc9394c10116e6511f6114b03f658055bf3caa02`, após confirmar no domínio público o HTML com CSS inline e os dois WOFF2.

| Página | Horário UTC | Mobile | Desktop | Mobile / Desktop |
|---|---|---|---|---|
| Home | 22:34:37 | **100 / 100 / 100 / 100** | **100 / 100 / 100 / 100** | [mobile](https://pagespeed.web.dev/analysis/https-www-alexribeiro-io/2yk5rsnpbb?form_factor=mobile) / [desktop](https://pagespeed.web.dev/analysis/https-www-alexribeiro-io/2yk5rsnpbb?form_factor=desktop) |
| Sobre | 22:34:37 | **100 / 100 / 100 / 100** | **100 / 100 / 100 / 100** | [mobile](https://pagespeed.web.dev/analysis/https-www-alexribeiro-io-sobre/pv67h1l64i?form_factor=mobile) / [desktop](https://pagespeed.web.dev/analysis/https-www-alexribeiro-io-sobre/pv67h1l64i?form_factor=desktop) |
| Arquivo | 22:34:39 | **100 / 100 / 100 / 100** | **100 / 100 / 100 / 100** | [mobile](https://pagespeed.web.dev/analysis/https-www-alexribeiro-io-arquivo/v5pwb57dmz?form_factor=mobile) / [desktop](https://pagespeed.web.dev/analysis/https-www-alexribeiro-io-arquivo/v5pwb57dmz?form_factor=desktop) |
| Categoria Cloud, vazia | 22:34:44 | 100 / 100 / 100 / **66** | 100 / 100 / 100 / **66** | [mobile](https://pagespeed.web.dev/analysis/https-www-alexribeiro-io-categorias-cloud/qqoejiota9?form_factor=mobile) / [desktop](https://pagespeed.web.dev/analysis/https-www-alexribeiro-io-categorias-cloud/qqoejiota9?form_factor=desktop) |

Mobile: FCP/LCP e Speed Index ficaram em 0,8 s nas quatro páginas, TBT 0 ms; CLS foi 0 na home/arquivo e 0,001 em Sobre/Cloud. Desktop: FCP/LCP e Speed Index foram 0,2 s na home, 0,3 s em Sobre/arquivo e 0,4 s em Cloud, com TBT 0 ms e CLS 0.

A meta foi atingida nas três páginas indexáveis representativas testadas. Home/arquivo variaram de 98 para 100 em desempenho mobile entre as rodadas; Sobre permaneceu 100. Isso é uma comparação antes/depois com uma rodada por versão, não uma estimativa estatística da variabilidade nem garantia de repetição. Rede, cache, servidor e carga do ambiente do Google podem mudar os resultados. Não há resultado de campo que permita afirmar aprovação de Core Web Vitals.

O PSI deixou de apontar CSS bloqueando a renderização. Ainda apresenta recomendação de cache com economia estimada de 99 KiB, sem impedir nota 100. Prazos de cache são servidos pelo GitHub Pages/CDN; não foram alteradas configurações de conta/CDN ou DNS para remover avisos que não impedem a meta. As notas automáticas 100 de acessibilidade/boas práticas não equivalem a certificação de segurança ou auditoria manual completa.

Os dados resumidos também estão em [pagespeed-results.json](pagespeed-results.json). A home publicada foi conferida visualmente após a otimização, mantendo a aparência. Sitemap, RSS, llms.txt, robots e os WOFF2 públicos corresponderam aos arquivos do build.

## Exceção de indexação

A categoria vazia apresenta somente uma reprovação SEO: **“A página está bloqueada para indexação”**, devido ao `noindex, follow` intencional. As outras oito auditorias SEO aplicáveis passaram. O mesmo mecanismo vale para seções/taxonomias vazias e para a busca interna. A nota 66 não será artificialmente aumentada removendo uma proteção de indexação apenas para cumprir uma meta numérica. Quando existir artigo publicado na categoria, ela se tornará indexável automaticamente.

A meta de 99–100 em todas as quatro categorias para todas as URLs públicas depende de uma decisão: manter páginas vazias/busca fora do índice ou permitir sua indexação. Nenhum rascunho ou artigo sintético foi exposto para fazer medições. Não existe artigo editorial publicado para testar no PSI; seu template foi validado apenas no build local isolado.
