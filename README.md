# Alex Ribeiro · Blog

Blog pessoal em português sobre IA, cloud e produtividade.
Hugo + PaperMod, modo escuro por padrão e alternância para claro.
Sem newsletter, analytics ou cadastro próprio.

## Desenvolvimento

Use **Hugo 0.168.0** (versão fixada em `.hugo-version`), Git e Python 3.11+
para as verificações. O build não precisa de Node, Go ou banco de dados.

```sh
make setup      # instala Hugo em .tools/ no Linux x86_64, com SHA256 verificado
make serve      # http://localhost:1313, apenas conteúdo publicável
make preview    # inclui rascunhos, com aviso de prévia e noindex
make check      # build de produção + links, RSS, taxonomias e exclusão de rascunhos
```

Em outros sistemas, instale a mesma versão pelo [guia do Hugo](https://gohugo.io/installation/).
Os comandos também estão disponíveis em `scripts/`, sem depender de Make.

## Criar e publicar um artigo

```sh
./scripts/new-post.sh meu-artigo
```

O comando usa a data atual de São Paulo e cria uma pasta com `index.md`.
Para uma data específica, use `./scripts/hugo.sh new content --kind posts
posts/2026/10/16-meu-artigo` (sem `/index.md` ao final). O archetype cria um
rascunho com identificador permanente. Edite os campos:

```toml
title = 'Título do artigo'
description = 'Um resumo curto para as listas, o RSS e o compartilhamento.'
date = '2026-10-16T10:00:00-03:00'
lastmod = '2026-10-16T10:00:00-03:00'
slug = 'meu-artigo'
postId = 'identificador-gerado-pelo-archetype'
draft = true
categorias = ['Cloud']
tags = ['aws', 'arquitetura']
comments = true
```

Escreva em Markdown no `index.md` e mantenha as imagens junto ao artigo.
Use imagens locais com texto alternativo, por exemplo `![Descrição](diagrama.webp)`.
Categorias iniciais: `Inteligência Artificial`, `Cloud` e `Produtividade`.
Use `categorias`, não `categories`, no front matter. Tags devem ser curtas e consistentes.
Opiniões ficam dentro do assunto correspondente; `opinião` pode ser uma tag,
conforme a escrita, sem constituir uma categoria. O cadastro das categorias
acompanha a grafia do termo, inclusive acentos (`inteligência-artificial`);
as URLs públicas removem os acentos (`/categorias/inteligencia-artificial/`).

A URL é `/posts/AAAA/MM/slug/`. A ordenação é pela data do artigo, da mais
recente para a mais antiga. Não altere `postId` após a publicação: ele conecta
o artigo aos comentários e identifica o item no RSS, mesmo após mudar de domínio.
Ao mudar uma URL publicada, adicione `aliases = ['/caminho-antigo/']` no artigo.

Revise em `make preview`. Para publicar, mude `draft` para `false`, rode
`make check` e envie suas alterações à `main`. O workflow só publica após as
verificações. Rascunhos e datas futuras ficam fora do build de produção.
Publicações futuras só aparecem após um novo build depois da data: este
projeto não configura agendamento automático.

As quatro publicações de exemplo permanecem em **rascunho**. Servem para
testar layout, categorias, código, busca e arquivo; não representam opiniões
ou notícias escritas pelo autor. Você pode removê-las ou substituí-las.
A página Sobre é uma apresentação inicial curta e deve ser revisada antes do lançamento.

## GitHub Pages

O workflow `.github/workflows/pages.yml` segue o fluxo oficial de artefatos
do Pages, com actions fixadas por commit:

- Pull requests para `main`: build e verificações, sem publicação.
- Push na `main`: build, verificações e publicação.
- Execução manual em Actions: publica quando selecionada a `main`.

Para ativar no GitHub, após enviar os arquivos:

1. Abra **Settings → Pages → Build and deployment → Source → GitHub Actions**.
2. Confira se Actions pode executar no repositório e se o ambiente
   `github-pages` permite a branch `main`.
3. Execute **Actions → Validar e publicar blog → Run workflow** na `main`, ou
   faça um novo push. Sem Pages habilitado, a etapa de configuração não conclui.
4. Confira o deployment e abra `https://www.alexribeiro.io/`.

Somente o conteúdo de `public/` vira artefato de deploy. Essa pasta, os
caches e o binário Hugo ficam fora do Git. O tema está incluído no
repositório, sem submódulos, para permitir clones e builds simples.

### Domínio alexribeiro.io

A URL canônica é **https://www.alexribeiro.io/**, declarada em `baseURL`
no `hugo.toml`. O domínio sem `www` redireciona para essa versão.
Para configurar ou alterar o domínio:

1. Verifique a propriedade do domínio no GitHub e configure **Custom domain**
   em Settings → Pages.
2. Configure o DNS conforme a [documentação oficial](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site).
3. Aguarde a emissão do certificado e habilite **Enforce HTTPS**.
4. Mantenha `baseURL` em `hugo.toml` alinhada ao domínio canônico com HTTPS e publique.
5. Verifique navegação, URLs canônicas, sitemap e RSS no endereço final.

O workflow preserva a URL declarada no Hugo, sem substituí-la pela URL
informada pelo Pages. O build verifica as canônicas, os metadados, os feeds e
o sitemap contra essa configuração. Ao usar GitHub Actions, o domínio é configurado no
Pages; não é necessário criar um `CNAME` neste repositório.

## Comentários com Giscus

A integração existe, mas está **desativada até a configuração no GitHub**.
Nenhum script do Giscus é carregado enquanto estiver desativada.

1. Habilite **Discussions** no repositório público.
2. Instale o [app Giscus](https://github.com/apps/giscus) apenas no repositório desejado.
3. Crie uma categoria `Comentários`, preferencialmente no formato **Announcements**.
4. Em [giscus.app/pt](https://giscus.app/pt), selecione o repositório e a categoria.
5. Copie `data-repo-id` e `data-category-id` para `params.giscus.repoId` e
   `params.giscus.categoryId` em `hugo.toml`; confirme o nome da categoria e
   altere `enabled = true`.

O código usa mapeamento `specific`, com `postId` como termo e busca estrita.
Não use título, URL ou pathname como mapeamento, para preservar as conversas
após a troca de domínio. A integração acompanha a alternância claro/escuro.
Só posts com `comments = true` recebem o widget, e prévias ficam sem comentários.

Valide login, criação, resposta e moderação em um artigo real após ativar.
Os leitores usam conta GitHub; não há cadastro próprio ou chat em tempo real.
O Giscus carrega recursos de terceiros e usa o fluxo OAuth do GitHub para
comentar. Caso configure restrições de origem no serviço, autorize os dois domínios durante a migração.

## Estrutura e manutenção

- `content/posts/AAAA/MM/DD-slug/index.md`: conteúdo e imagens por publicação.
- `content/sobre/`: biografia pública.
- `content/categorias/` e `content/tags/`: páginas de navegação por assunto.
- `layouts/`: adaptações pontuais de navegação, listas, busca, RSS e comentários.
- `assets/css/extended/blog.css`: identidade visual; fontes locais em `static/fonts/`.
- `archetypes/posts/index.md`: modelo para novos artigos.
- `theme-source.toml`: origem, commit e SHA256 do snapshot PaperMod.
- `themes/PaperMod/`: tema original, sem modificações.

O RSS geral fica em `/index.xml`, com até 30 artigos recentes; há feeds em
`/posts/index.xml` e nas páginas de categorias e tags. Páginas institucionais
não entram no RSS nem na busca. O sitemap é gerado em `/sitemap.xml`.

Para atualizar o tema, obtenha um novo snapshot do repositório oficial,
substitua `themes/PaperMod/` e atualize `theme-source.toml`. Compare os
templates personalizados com o upstream, execute `make check` e revise
as prévias de desktop e celular. Ao atualizar Hugo, altere a versão e o
checksum juntos e valide o build antes de publicar.

## Licenças

- Código original, configuração e documentação técnica: [MIT](LICENSE).
- Conteúdo editorial original: [CC BY-SA 4.0](LICENSE-CONTENT.md), salvo aviso específico.
- PaperMod: MIT e avisos das bibliotecas preservados em `themes/PaperMod/`.
- IBM Plex Sans: SIL OFL 1.1, em `static/fonts/OFL.txt`.
- Identidade visual, favicon e fotografias pessoais: fora da licença editorial geral.

Materiais de terceiros mantêm os direitos e licenças de seus titulares.
Os comentários pertencem aos seus autores. A licença editorial não é
automaticamente aplicada a eles.

## SEO e descoberta

A [revisão técnica de SEO](docs/seo.md) documenta canonical, metadados,
dados estruturados, sitemap, bots e limites de validação. `/llms.txt` é
gerado automaticamente do conteúdo público; não oferece autorização de
treinamento. `make check` também testa o template de artigo com um build
temporário isolado, sem publicar exemplos ou rascunhos.

Os [resultados reais do Google PageSpeed Insights](docs/pagespeed.md)
registram as medições mobile/desktop, os relatórios e a exceção de SEO
das categorias vazias mantidas fora do índice.
