+++
title = 'Radar de IA | Semana 45 de 2026'
description = 'Dez novidades verificadas: segurança ofensiva com IA, agentes na AWS, código para agentes, vídeo e imagem.'
date = '2026-11-09T07:00:00-03:00'
lastmod = '2026-11-09T08:05:00-03:00'
slug = 'radar-ia-semana-45-2026'
draft = false
categorias = ['Inteligência Artificial']
tags = ['ia', 'agentes', 'segurança', 'modelos', 'aws']
comments = true
+++
Entre 2 e 8 de novembro, as novidades de IA giraram em torno de três perguntas práticas: quem pode usar modelos de segurança ofensiva, onde rodar agentes dentro da conta da empresa e o que muda quando agentes de código passam a gerar volume de trabalho.

Esta edição reúne dez anúncios e publicações técnicas conferidos nas páginas originais. Cada item separa o que mudou, a análise e os limites.

## Cobertura e destaques

- Semana ISO 45 de 2026: de 02/11 às 00h00 até 08/11 às 21h, em America/Sao_Paulo. O domingo foi pesquisado até o horário de fechamento desta edição.
- Verificação de disponibilidade em 08/11/2026. Quando a página não informa horário, a data é a do anúncio.
- Destaques: GPT-6 Cyber, o pipeline que validou 948 exploits no Linux, Web Answer no AgentCore, Claude Code em sessões remotas e o Pando da OpenAI.
- Não entrou: itens do Anthropic e da Meta sem data confirmada dentro da janela, e anúncios que a AWS publicou na semana anterior e apareceram só no resumo semanal de 02/11.

## 1. GPT-6 Cyber chega com acesso restrito

Anúncio: 05/11/2026.

O que mudou. A OpenAI apresentou o GPT-6 Cyber, modelo de segurança para encontrar e validar vulnerabilidades exploráveis. No ExploitGym, que mede se o modelo consegue explorar uma falha já indicada, ele marca 48,5%, contra 32,1% do GPT-5.6 Cyber. Em um teste de alinhamento, evitou explorar serviços fora do escopo em 99,93% dos casos sem o prompt de implantação e em 100% com ele. Pesquisadores da empresa usaram o modelo para desenvolver 948 exploits de escalada de privilégio no Linux e achar 81 vulnerabilidades graves até então desconhecidas no Firefox; a Mozilla já publicou correções para várias.

Na prática (análise). Para um time de segurança, o ponto central é o acesso, não o benchmark. O modelo está atrás de um processo de aprovação, e a pergunta útil é se a sua organização cabe no programa Daybreak e quem vai operar a ferramenta dentro do escopo autorizado.

Disponibilidade e limites. O GPT-6 Cyber está disponível pela API e pelo Codex, inicialmente para um grupo selecionado de clientes Daybreak Red aprovados, com expansão gradual prometida. O GPT-5.6 Cyber passa a ficar disponível para todos os clientes Daybreak Red. Os números de benchmark são da própria OpenAI.

Fonte: [GPT-6 Cyber, OpenAI](https://openai.com/index/introducing-gpt-6-cyber)

## 2. Um pipeline autônomo validou 948 exploits no kernel Linux

Publicação: 04/11/2026.

O que mudou. A OpenAI descreveu um pipeline que busca, valida, explora e corrige falhas. Em uma execução no kernel Linux, ele analisou 2.308 achados candidatos, reproduziu 1.724 vulnerabilidades e produziu 948 exploits de escalada local de privilégio. O custo de API foi de US$ 1,2 milhão. Pesquisadores humanos revisaram os resultados antes do reporte, e a empresa gerou patches candidatos para os mantenedores.

Na prática (análise). O gargalo se desloca da descoberta para a priorização, a validação e a aplicação de correções. Quem opera Linux em produção deve esperar mais relatórios e manter a rotina de patch em dia.

Disponibilidade e limites. É pesquisa em ambiente controlado, não um produto. Os números vêm da OpenAI, sem verificação independente, e se referem a uma execução específica. O texto cita um modelo de segurança "futuro" como motor do pipeline; o GPT-6 Cyber, anunciado no dia seguinte, aparece como o modelo usado pelos pesquisadores.

Fonte: [A thousand fewer paths to root, OpenAI](https://openai.com/index/a-thousand-fewer-paths-to-root)

## 3. Pando e Pierre: a OpenAI investe em controle de código para agentes

Publicações: 02/11/2026 (Pando) e 04/11/2026 (Pierre).

O que mudou. A OpenAI contou como construiu o Pando, um backend compatível com Git que hoje sustenta todo o desenvolvimento no monorepo da empresa. Segundo o texto, a latência mediana de push caiu quase 5x e o sistema entrega quase 1 petabyte de dados Git por dia. Dois dias depois, anunciou a compra da Pierre Computer Company, dona do Code Storage e das bibliotecas Trees e Diffs usadas no app do Codex.

Na prática (análise). Com agentes, cada engenheiro passa a ter várias mudanças em CI ao mesmo tempo. Controle de versão, clones e revisão de código viram uma questão de capacidade, não só de fluxo de trabalho.

Disponibilidade e limites. O Pando é interno; a OpenAI diz que explora formas de compartilhar a tecnologia, sem data. A compra da Pierre depende de aprovações regulatórias, os projetos open source continuam abertos e clientes do Code Storage podem continuar usando o serviço.

Fontes: [Scaling Git at OpenAI](https://openai.com/index/scaling-git-at-openai) · [OpenAI to acquire Pierre](https://openai.com/index/openai-to-acquire-pierre)

## 4. Web Answer chega à disponibilidade geral no Bedrock AgentCore

Anúncio: 05/11/2026.

O que mudou. O Web Answer é uma ferramenta gerenciada que recebe uma pergunta e devolve uma resposta sintetizada, com citações, em uma única chamada. Ele planeja as próprias buscas, roda várias em paralelo e decide quando já reuniu evidência suficiente. O time controla o alcance com listas de domínios permitidos e bloqueados e filtros de data de publicação.

Na prática (análise). Quem montava pipeline próprio de busca, recuperação, síntese e citação ganha uma alternativa gerenciada. A avaliação passa por qualidade das citações, controle de domínios e custo por chamada.

Disponibilidade e limites. Está em US East (N. Virginia), com preço por chamada; o anúncio não traz o valor. Funciona como alvo no AgentCore Gateway, é chamado por MCP, usa autenticação IAM e a AWS informa zero data egress.

Fonte: [Web Answer, AWS](https://aws.amazon.com/about-aws/whats-new/2026/11/web-answer-amazon-bedrock/)

## 5. Claude Code em sessões remotas no AgentCore

Publicação: 06/11/2026.

O que mudou. A AWS publicou um exemplo, o sample-remote-coding-agent, que roda o Claude Code como agente remoto no AgentCore Runtime. Cada tarefa executa em uma sessão isolada dentro da conta AWS do cliente e devolve um pull request do GitHub para revisão. O texto mostra como os controles de dados do Bedrock continuam valendo.

Na prática (análise). Rodar o agente na própria conta aproxima o trabalho de IAM, logs e rede que o time já governa. A manutenção do exemplo passa a ser de quem o adotar.

Disponibilidade e limites. É código de exemplo, não um serviço novo. A AWS recomenda ativar zero data retention na Região (conferindo se o modelo suporta), fixar um perfil de inferência geográfico quando houver requisito de residência e testar o guardrail com as tarefas reais.

Fonte: [Extend Claude Code to remote sessions on Amazon Bedrock AgentCore, AWS](https://aws.amazon.com/blogs/machine-learning/extend-claude-code-to-remote-sessions-on-amazon-bedrock-agentcore-with-security-controls/)

## 6. @GitHub no Slack e no Teams em disponibilidade geral

Registro: 06/11/2026.

O que mudou. O changelog do GitHub anuncia @GitHub no Slack e no Teams para investigar bugs, criar issues, implementar mudanças e abrir pull requests sem sair da conversa. Entram o Canvas no Teams (plano, alterações e prévias ao lado da conversa), um início mais curto, que identifica o repositório pela mensagem, e a atribuição "Created from a Slack/Teams conversation" nas issues e PRs.

Na prática (análise). A atribuição ajuda a auditar o que veio de agente. O ganho de velocidade não dispensa testes e revisão antes do merge.

Disponibilidade e limites. O Teams já foi tratado na edição 44, com o anúncio da Microsoft de 30/10, que listou requisitos de licença e permissões. O texto do changelog não repete esses requisitos nem informa preços.

Fonte: [@GitHub in Slack and Teams, GitHub Changelog](https://github.blog/changelog/2026-11-06-github-copilot-in-slack-and-teams-is-generally-available)

## 7. Kimi K3.1 Pro (Highspeed) chega ao Amazon Bedrock

Anúncio: 06/11/2026.

O que mudou. O Kimi K3.1 Pro, da Moonshot AI, passou a estar disponível no Bedrock. Segundo a Moonshot, é um modelo open weight, multimodal nativo, com janela de 1 milhão de tokens e classe de 3 trilhões de parâmetros. A variante Highspeed prioriza tokens de saída por segundo.

Na prática (análise). Modelos open weight dentro do mesmo limite de segurança e governança do Bedrock facilitam comparar custo e qualidade com modelos proprietários em tarefas de código e documentos.

Disponibilidade e limites. Está disponível em todas as Regiões do Bedrock por inferência entre Regiões, com cache explícito de prompt. Se houver requisito de residência, vale confirmar onde as requisições são processadas. O anúncio não informa preço, e as melhorias de capacidade são relatos da Moonshot.

Fonte: [Kimi K3.1 Pro no Amazon Bedrock, AWS](https://aws.amazon.com/about-aws/whats-new/2026/11/moonshot-ai-kimi-k3-1-pro-on-amazon-bedrock)

## 8. Gemini Omni 1.2 Flash gera vídeos de até 15 segundos

Anúncio: 05/11/2026.

O que mudou. O Google liberou o Gemini Omni 1.2 Flash em disponibilidade geral na Gemini API e no Gemini for business. O modelo gera e edita vídeo nativamente por até 15 segundos (eram 10 no Omni 1.1), com duração ajustável de 3 a 15 segundos, edição em várias etapas e melhor aderência a imagens e áudios de referência. O preço caiu 30%, para US$ 0,07 por segundo em 720p.

Na prática (análise). Pelo preço informado, um clipe de 15 segundos em 720p custa cerca de US$ 1,05 (conta feita aqui, sem considerar tentativas de refazer). Rascunhar em 360p ou 720p e corrigir com edições é o caminho que o Google indica para controlar o gasto.

Disponibilidade e limites. Há integração com Flow, Vids e Google Ads. No app Gemini, os clipes de 15 segundos estão sendo liberados para assinantes Google AI Ultra.

Fonte: [Gemini Omni 1.2 Flash, Google](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/)

## 9. Images 2.6 ganha velocidade e GIFs

Anúncio: 04/11/2026 (data da página; o feed da OpenAI marca 03/11 às 21h no horário de Brasília).

O que mudou. O Images 2.6 gera imagens 50% mais rápido e cria GIFs. Na API, há dois modelos: GPT-Image-2.6 Flare, que com qualidade baixa gera imagens em cerca de seis segundos, e GPT-Image-2.6 Sunburst, para mais detalhe e consistência entre edições. A OpenAI diz que são criadas 4 bilhões de imagens por semana entre ChatGPT, Codex e API.

Na prática (análise). Escolher entre Flare e Sunburst vira uma decisão de custo e prazo por caso de uso: rascunhos e layouts rápidos de um lado, peças finais do outro.

Disponibilidade e limites. Disponível globalmente no ChatGPT e no Codex em todos os planos e na API. O preço está em página separada e não foi conferido nesta edição.

Fonte: [Introducing Images 2.6, OpenAI](https://openai.com/index/introducing-images-2-6)

## 10. Google Cloud propõe cinco regras para avaliar agent skills

Publicação: 03/11/2026.

O que mudou. O Google Cloud publicou um guia para avaliar arquivos SKILL.md antes que inflem o contexto do agente. Uma das regras: quando a comparação entre agente com e sem a skill dá diferença zero, o motivo mais comum é que o agente nunca carregou a skill, porque o roteador lê só o nome e a descrição do cabeçalho. A avaliação roda em CI, e as skills cujo ganho cai a zero com um modelo novo são removidas.

Na prática (análise). Quem mantém skills próprias pode adotar duas medidas simples: testar com e sem a skill e revisar descrições que se sobrepõem.

Disponibilidade e limites. É uma prática publicada, não um produto. Esta edição conferiu a abertura e o fechamento do artigo; as regras intermediárias devem ser lidas na fonte.

Fonte: [Five rules for evaluating agent skills, Google Cloud](https://cloud.google.com/blog/topics/developers-practitioners/evaluate-agent-skills-before-they-bloat-your-context-window/)

## O que priorizar nesta semana

Para segurança, o recado é de capacidade: modelos e pipelines já validam centenas de explorações em um kernel, então o ciclo de patch e a priorização de vulnerabilidades merecem revisão. Para quem constrói agentes, o AgentCore reúne três peças (Web Answer, sessões remotas e Gateway) que valem uma prova de conceito com custo por tarefa medido. Antes de ampliar permissões de qualquer agente, defina o que ele pode executar e como interromper a tarefa.

## Limitações desta edição

- Não foram encontrados itens datados dentro da janela nos blogs da Anthropic e da Meta; a página da Anthropic traz itens sem data visível e outros anteriores à semana.
- O GPT-6.1 Terra no Bedrock e o Step Functions como ferramenta de agente aparecem no resumo semanal da AWS de 02/11, mas se referem à semana anterior.
- Os feeds do AWS Machine Learning Blog, do GitHub e do Google Cloud são curtos e podem ter deixado itens de início de semana fora da coleta.
- O radar diário não tinha notícias guardadas para esta semana; a coleta veio dos feeds e da pesquisa direta nas fontes.
