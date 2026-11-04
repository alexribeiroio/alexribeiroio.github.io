+++
title = 'GitLab: falha crítica com exploração ativa exige atualização'
description = 'Alerta para GitLab autogerenciado: versões afetadas pela CVE-2026-97229, correções e cuidados para investigar possíveis sinais de comprometimento.'
date = '2026-11-04T06:12:00-03:00'
lastmod = '2026-11-04T06:12:00-03:00'
slug = 'gitlab-falha-critica-exploracao-ativa'
postId = 'c6df3569-b8d2-4ede-88b7-f2f12327f7f4'
draft = false
categorias = ['Segurança']
tags = ['segurança', 'gitlab']
comments = true
+++

Se você administra um GitLab próprio, confira a versão instalada e priorize as correções de segurança. A **CVE-2026-97229** permite, sob determinadas condições, execução de código no servidor sem autenticação. O GitLab classificou a falha com **CVSS 10,0**.

A [CISA confirmou exploração ativa](https://content.govdelivery.com/accounts/USDHSCISA/bulletins/4310049) ao incluir a vulnerabilidade no catálogo KEV em **29 de outubro de 2026**.

## O que significa o número da notícia

A [reportagem de 2 de novembro](https://www.bleepingcomputer.com/news/security/over-1-000-gitlab-servers-vulnerable-to-code-execution-attacks/) cita mais de mil instâncias vulneráveis expostas à internet, segundo levantamento do Shadowserver de 1º de novembro.

Esse número não significa mil invasões confirmadas. Também não é uma contagem atualizada em tempo real. Ele mostra que havia instalações expostas mesmo depois da disponibilização da correção.

## Versões afetadas e correções

Segundo o [comunicado oficial do GitLab](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-4-2-released/), a CVE-2026-97229 afeta GitLab Community Edition e Enterprise Edition nas seguintes faixas:

- **19.2.x anteriores a 19.2.8**;
- **19.3.x anteriores a 19.3.5**;
- **19.4.x anteriores a 19.4.2**.

As primeiras versões corrigidas foram publicadas em **12 de outubro**. GitLab.com e GitLab Dedicated já estavam corrigidos, conforme o comunicado. O foco deste alerta é quem mantém sua própria instalação.

**Não pare nas primeiras versões corrigidas.** Em 21 de outubro, houve [outra atualização crítica, para a CVE-2026-110264](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-5-1-released/). Planeje a atualização para o patch mais recente compatível com sua linha suportada e siga o caminho de upgrade indicado pelo GitLab.

## Checklist para a equipe

1. **Inventarie as instalações.** Identifique versões, responsáveis e exposição à internet.
2. **Priorize a atualização.** Depois da execução, valide a versão efetivamente instalada.
3. **Investigue sinais de exploração.** Revise logs e as detecções publicadas pelo GitLab. Aplicar o patch não comprova que a instância não foi comprometida antes.
4. **Acione a resposta a incidentes se houver indícios.** A atualização e a investigação precisam ser tratadas como atividades complementares.

Essas são orientações defensivas. Não representam uma conclusão sobre qualquer ambiente específico.

Encaminhe este alerta para quem administra o GitLab na sua equipe.

## Fontes e data de consulta

- [GitLab: correções de 12/10/2026](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-4-2-released/).
- [CISA: boletim oficial de 29/10/2026](https://content.govdelivery.com/accounts/USDHSCISA/bulletins/4310049).
- [GitLab: correção crítica posterior, de 21/10/2026](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-5-1-released/).
- [BleepingComputer: reportagem de 02/11/2026](https://www.bleepingcomputer.com/news/security/over-1-000-gitlab-servers-vulnerable-to-code-execution-attacks/).

Informações consultadas em **4 de novembro de 2026**. A contagem de instâncias é atribuída à reportagem, não a uma medição própria.
