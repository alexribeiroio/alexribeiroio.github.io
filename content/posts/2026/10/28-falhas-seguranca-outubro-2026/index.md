+++
title = 'Falhas de segurança em outubro: o que aconteceu e quais são os riscos'
description = 'Entenda a sequência de alertas de segurança no Brasil e no mundo: o que aconteceu, quais riscos existem e o que cada caso exige.'
date = '2026-10-28T14:05:00-03:00'
lastmod = '2026-10-28T15:16:00-03:00'
slug = 'falhas-seguranca-outubro-2026'
postId = '044b4a29-88f8-448d-a35b-6aaf09ebea49'
draft = false
categorias = ['Segurança']
tags = ['segurança', 'php', 'nodejs', 'gitlab', 'litellm', 'cadeia-de-suprimentos', 'brasil']
comments = true
+++

Quando um sistema fica fora do ar depois de um alerta de segurança, é fácil imaginar que houve uma invasão. Às vezes, porém, o acesso é interrompido justamente para dar tempo de corrigir uma falha.

Foi o que o Ministério da Gestão informou sobre o SEI, sistema usado por órgãos públicos para tramitar processos e documentos. Em uma [nota de 22 de outubro](https://www.gov.br/gestao/pt-br/assuntos/editoria-defeso-eleitoral/nota-sobre-falha-global-na-linguagem-de-programacao-php/), o ministério explicou que a retirada havia sido preventiva. A mesma nota registrou que a plataforma GOV.BR funcionava normalmente.

Esse foi um dos efeitos mais visíveis, no Brasil, de uma sequência de alertas que envolveu tecnologias usadas em sites, ferramentas de desenvolvimento e aplicações de inteligência artificial.

Você não precisa conhecer cada uma dessas tecnologias para entender o risco. Vamos organizar o que aconteceu entre **17 e 26 de outubro de 2026**, com informações verificadas em **28 de outubro**.

## Por que uma falha pode afetar quem nunca ouviu falar do programa?

Um serviço digital é formado por várias peças. Algumas foram desenvolvidas pela própria organização; outras vieram de fornecedores ou projetos de software. Uma dessas peças pode estar presente em muitos sistemas diferentes.

Quando uma falha aparece, o efeito depende do que ela permite fazer e de como o componente é utilizado. Pode haver risco de interrupção do serviço, acesso indevido a informações ou execução de ações sem autorização. Encontrar uma falha não demonstra, por si só, que esses danos já aconteceram.

Também é importante separar **tentativa de ataque**, quando alguém procura aproveitar a falha, de **comprometimento confirmado**, quando há evidência de que conseguiu afetar um sistema ou componente. Já uma restrição preventiva é uma decisão de proteção, ainda que cause transtorno para quem precisa usar o serviço.

## A linha do tempo, sem complicar

### 17 a 20/10: a identificação de sites também entrou no alerta

Os certificados digitais ajudam o navegador a conferir a identidade do site com o qual está se comunicando. Em **17/10**, a Mozilla recebeu um relato de comprometimento de chaves ligadas a oito certificados intermediários da eMudhra e bloqueou os certificados afetados no Firefox. A divulgação aconteceu em **20/10**.

O risco era permitir a falsificação dessa identificação se um atacante conseguisse interferir na comunicação. A resposta da Mozilla foi voltada aos certificados afetados; não se trata de uma confirmação de invasão de todos os sites que usam certificados digitais. [Relato da Mozilla](https://blog.mozilla.org/security/2026/10/20/protecting-firefox-users-following-the-compromise-of-emudhra-intermediate-certificates/).

### 20 e 21/10: PHP, uma tecnologia usada para fazer sistemas web funcionar

O PHP é usado para executar a lógica de muitos sites e sistemas: receber um formulário, consultar informações ou processar uma solicitação, por exemplo.

O projeto publicou um aviso em **20/10** e correções em **21/10** para duas falhas conhecidas como PHP2Shell. Elas podem permitir que alguém execute comandos sem autorização na máquina que roda o serviço, mesmo sem fazer login. O alcance real depende do ambiente e das condições de exploração. [Avisos do PHP](https://www.php.net/archive/2026.php).

Havia sinais anteriores: em um [relato publicado em 21/10](https://aws.amazon.com/blogs/security/amazon-threat-intelligence-identifies-php2shell-exploitation-prior-to-public-disclosure-in-madpot/), a AWS identificou retrospectivamente uma tentativa de **17/10** em um sistema-isca, preparado para observar ataques. Aquele registro não demonstrava sucesso em sistemas reais.

### 21/10: Node.js e GitLab recebem atualizações

O **Node.js**, outra tecnologia usada para executar aplicações, corrigiu uma falha no processamento de dados compactados. Uma aplicação afetada que descompactasse dados enviados por um atacante poderia parar de funcionar, expor informações ou executar comandos indevidos. A condição de uso importa: o comunicado não informa exploração ativa desse caso. [Node.js](https://nodejs.org/en/blog/vulnerability/october-2026-security-releases).

O **GitLab**, ferramenta usada por equipes para guardar código e organizar o desenvolvimento, também corrigiu uma falha que poderia permitir comandos sem autorização, em determinadas condições. O serviço GitLab.com já estava corrigido no anúncio. Organizações que mantêm sua própria instalação precisavam verificar a atualização correspondente. [GitLab](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-5-1-released/).

### 21/10: no LiteLLM, uma versão foi distribuída com código malicioso

O **LiteLLM** é um componente usado para conectar aplicações a serviços de inteligência artificial. Seu processo de distribuição foi comprometido, e a versão **1.107.0** chegou aos repositórios com código malicioso.

Esse é um ataque à cadeia de fornecimento de software: o problema chega por uma peça que outras aplicações utilizam. Quem usou os arquivos afetados precisa seguir as orientações do fornecedor, incluindo a avaliação de senhas ou chaves de acesso que possam ter ficado expostas. Apenas instalar uma versão diferente não encerra essa avaliação. A [investigação definitiva foi publicada em 23/10](https://docs.litellm.ai/blog/security-incident-oct-21-2026-attack-chain); as [orientações para os afetados](https://docs.litellm.ai/blog/security-incident-oct-21-2026) estão separadas.

### 21 e 22/10: o Brasil adota medidas de proteção

Em **21/10**, o CTIR Gov, responsável por coordenar a resposta a incidentes cibernéticos no governo federal, publicou um alerta sobre as falhas do PHP. A orientação incluía identificar os sistemas afetados e aplicar as correções. [Alerta 93/2026](https://www.gov.br/gsi/pt-br/assuntos/ctir/alertas/2026/alerta-93-2026/).

No dia seguinte, veio a nota do Ministério da Gestão sobre a interrupção preventiva do SEI. Para quem dependia do sistema, houve impacto na operação, mesmo sem uma invasão anunciada. É um exemplo de por que a comunicação precisa explicar tanto o problema quanto a medida tomada para enfrentá-lo.

### 22/10: tentativas são observadas contra sites no Brasil

A empresa de segurança Imperva incluiu o Brasil entre os países com sites alvo de varreduras e tentativas de aproveitar o PHP2Shell. O relatório registrou atividade em **103 países**, dentro dos ambientes observados pela empresa.

Esses números mostram tentativas e alvos, não uma contagem de sites invadidos. A própria fonte faz essa distinção. [Relatório da Imperva](https://www.imperva.com/blog/php2shell-early-attack-activity-through-impervas-lens/).

### 23 e 26/10: retomada de acesso e novas evidências

Em **23/10**, a Autoridade Nacional de Segurança Nuclear informou que o acesso externo ao seu SEI havia sido restabelecido. Essa confirmação vale para aquela instituição, não para todos os órgãos públicos. [Atualização da ANSN](https://www.gov.br/ansn/pt-br/assuntos/noticias/2026/acesso-externo-ao-sei-sera-temporariamente-suspenso-por-medida-de-seguranca).

Em **26/10**, a agência americana de segurança cibernética CISA incluiu as duas falhas originais do PHP no seu catálogo de falhas que já foram usadas em ataques. O boletim não identifica vítimas brasileiras. [Boletim da CISA](https://content.govdelivery.com/accounts/USDHSCISA/bulletins/4309083).

## O que essa sequência mostra sobre Brasil e mundo?

Os casos passaram por partes diferentes da tecnologia: a identificação dos sites, os programas que executam as aplicações, as ferramentas de desenvolvimento e a distribuição de componentes. As fontes consultadas não demonstram que tudo tenha feito parte de um único ataque coordenado.

No Brasil, há registros de alertas, medidas preventivas, retomada de serviço em uma instituição e tentativas observadas por uma empresa de segurança. A apuração deste resumo não estabeleceu quantas organizações brasileiras foram efetivamente comprometidas. A ausência dessa confirmação nas fontes não prova que nenhum ataque tenha ocorrido.

## E o que fazer com essa informação?

**Se você usa esses serviços**, acompanhe os comunicados pelos canais oficiais. Uma interrupção preventiva pode ser parte da proteção. Mantenha navegador e aplicativos atualizados e siga orientações específicas quando um serviço informar que você foi afetado. Uma ação no seu dispositivo não substitui uma correção que precisa ser feita no servidor da organização.

**Se você responde por uma empresa ou por um sistema**, há três perguntas úteis para fazer à equipe ou ao fornecedor:

1. Usamos algum dos componentes afetados? Em quais serviços?
2. A correção já chegou ao ambiente que atende os usuários? Como isso foi conferido?
3. Houve sinais de exploração ou uso de arquivos comprometidos que precisam ser investigados?

A informação mais útil é conseguir ligar o alerta a um serviço real, a um responsável e a uma ação verificada. Isso ajuda a proteger a operação e a explicar a situação com clareza para quem depende dela.

## Para quem vai conferir os detalhes técnicos

As duas falhas PHP2Shell são **CVE-2026-109618 e CVE-2026-109619**. As versões corrigidas pelo projeto PHP em 21/10 foram **8.5.12, 8.4.27, 8.3.36 e 8.2.35**; distribuições podem fornecer seus próprios pacotes corrigidos. Em 26/10, houve também pacotes Windows recompilados com a dependência Brotli atualizada. Confira o pacote efetivamente instalado. [PHP](https://www.php.net/archive/2026.php).

Uma orientação separada trata da **CVE-2026-115560**, que depende de uma combinação incomum de configuração e comportamento da aplicação. Ela não deve ser confundida com as duas falhas originais. [Recomendação 21/2026 do CTIR Gov](https://www.gov.br/gsi/pt-br/assuntos/ctir/recomendacoes/2026/recomendacao-21-2026).

Os identificadores citados para Node.js e GitLab são, respectivamente, **CVE-2026-111497** e **CVE-2026-110264**. CVE é o código usado para identificar e acompanhar uma falha específica; os links de cada caso levam às versões e condições informadas pelos projetos.

*Resumo não exaustivo, verificado em 28/10/2026. Datas de ocorrência, divulgação e correção são diferenciadas quando a fonte permite. Não foram realizados testes em ambientes de clientes.*
