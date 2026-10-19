+++
title = 'Privacidade e cookies'
description = 'Como este blog usa analytics com consentimento e o que você controla.'
hideMeta = true
ShowToc = false
ShowPostNavLinks = false
searchHidden = true
hiddenInRss = true
+++

## Resumo

Este blog pode usar [PostHog](https://posthog.com/) para entender visitas e interações de forma agregada, com o objetivo de melhorar o conteúdo e a navegação. **Nada é carregado até você aceitar** no aviso de cookies.

Não há cadastro próprio, newsletter nem login neste site. Não usamos gravação de sessão (session replay).

## O que pode ser coletado (somente com aceite)

- Páginas visitadas e referências de origem
- Eventos de uso, como alternância de tema, buscas (apenas o tamanho da consulta, não o texto), cliques em links externos e profundidade de leitura em artigos
- Dados técnicos habituais de analytics (por exemplo, tipo de navegador e resolução), conforme a configuração do PostHog

Perfis detalhados de pessoa só existem para visitantes identificados; neste blog não há identificação de conta.

## Consentimento e controle

Na primeira visita em produção, um aviso permite **Aceitar** ou **Recusar**. A escolha fica salva neste navegador. Você pode alterar depois pelo link **Cookies** no rodapé ou [abrindo o aviso novamente](#cookies).

- **Aceitar:** carrega o PostHog e passa a registrar pageviews e os eventos descritos.
- **Recusar:** o script de analytics não é carregado (ou a captura é desligada, se já tiver sido aceita antes).

## Terceiros

Com o aceite, o navegador fala com os servidores do PostHog (`us.i.posthog.com` e assets relacionados). A política deles está em [posthog.com/privacy](https://posthog.com/privacy).

Comentários (Giscus), quando ativados, são um serviço separado e exigem conta GitHub; veja a página [Licenças](/licencas/).

## Contato

Dúvidas sobre privacidade neste site: abra uma issue no [repositório do blog](https://github.com/alexribeiroio/alexribeiroio.github.io) ou use os canais listados em [Sobre](/sobre/).
