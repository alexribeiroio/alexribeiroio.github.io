+++
title = 'Radar de Cloud | Semana 44 de 2026'
description = 'Dez novidades verificadas em custos, capacidade, observabilidade, identidade e operação de agentes na nuvem.'
date = '2026-11-02T05:23:46-03:00'
lastmod = '2026-11-02T05:46:54-03:00'
slug = 'radar-cloud-semana-44-2026'
postId = '40c0e477-98b0-819a-9025-e1b84f94e00e'
draft = false
categorias = ['Cloud']
tags = ['cloud', 'aws', 'azure', 'google-cloud', 'finops', 'operacao']
comments = true
+++

A semana de 26 de outubro a 1º de novembro trouxe opções para ajustar capacidade e custos, além de mudanças na operação de agentes, identidades e ambientes híbridos. O ponto comum é a necessidade de distinguir o que o serviço faz automaticamente daquilo que continua sob responsabilidade da equipe.

Esta edição reúne dez novidades verificadas em AWS, Azure e Google Cloud. Disponibilidade geral, preview e limites regionais aparecem junto de cada notícia, sem transformar economia potencial em resultado garantido.

## Cobertura e destaques

- Semana ISO 44 de 2026, de 26/10 às 00h00 a 01/11 às 23h59:59, em America/Sao_Paulo.
- Fontes e disponibilidade verificadas em 02/11. Datas editoriais sem horário não permitem atribuir um instante exato no fuso brasileiro; divergências entre páginas foram registradas.
- Destaques: Spend Caps, consolidação no ECS, GPUs particionadas, telemetria Lambda, OpenSearch, Azure Arc, eventos de identidade, workflows para agentes, Registry entre projetos e capacidade Aurora.

## 1. Google Cloud coloca Spend Caps em disponibilidade geral

**Anúncio ou divulgação:** 31/10/2026.

**O que mudou.** Os limites de gastos do Cloud Billing Budgets chegaram a GA, com API e reinício mensal automático. Quando o custo estimado ultrapassa o orçamento, novas chamadas de um serviço elegível naquele projeto podem ser pausadas sem apagar os recursos.

**Na prática (análise).** Comece por sandboxes e testes de agentes. Em produção, o bloqueio deve fazer parte do desenho de disponibilidade e da comunicação com os responsáveis pelo serviço.

**Disponibilidade e limites.** Cada limite cobre um projeto e um serviço por mês. Gemini API, Agent Platform, Cloud Run e functions estão na lista; contas de revenda ficam fora do escopo. O bloqueio não é instantâneo, excessos são cobrados e custos fixos continuam. Não há garantia de fatura máxima. A página atual informa 31/10; índices anteriores indicavam 30/10, ambos nesta cobertura. A nova visualização de custos em relatórios ainda diverge entre anúncio e documentação.

**Fontes:** [Anúncio oficial](https://cloud.google.com/blog/topics/cost-management/google-cloud-spend-caps-now-generally-available) · [Documentação e referência](https://docs.cloud.google.com/billing/docs/how-to/budgets-spend-caps)

**Tags:** google-cloud, finops, governanca, custos.

## 2. ECS Managed Instances consolida tarefas entre instâncias

**Anúncio ou divulgação:** 28/10/2026.

**O que mudou.** O otimizador do ECS Managed Instances passou a avaliar várias instâncias subutilizadas em conjunto, redistribuindo tarefas em menos máquinas. A atualização também abrange Spot e verifica capacidade substituta antes da troca, com início da nova capacidade antes da parada da anterior.

**Na prática (análise).** É uma oportunidade para revisar frotas com folga persistente de capacidade. A economia deve ser medida junto com o efeito do reposicionamento nas aplicações, especialmente quando há interrupções ou estado local.

**Disponibilidade e limites.** O anúncio informa aplicação automática a capacity providers novos e existentes, em todas as regiões AWS, sem custo adicional pelo recurso. As tarifas dos serviços continuam. O parâmetro ScaleInAfter controla a espera e pode desativar a otimização; suas escolhas devem acompanhar a tolerância do workload.

**Fontes:** [Anúncio oficial](https://aws.amazon.com/about-aws/whats-new/2026/10/ecs-managed-instances-consolidation/) · [Documentação e referência](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-instances-infrastructure-optimization.html)

**Tags:** aws, ecs, containers, finops, spot.

## 3. SageMaker divide uma GPU entre componentes de inferência

**Anúncio ou divulgação:** 30/10/2026.

**O que mudou.** O SageMaker AI adicionou particionamento de GPU a endpoints de inferência em tempo real. A tecnologia MIG da NVIDIA permite até sete partições, conforme o hardware, com memória e capacidade de processamento dedicadas. A aplicação continua invocando o componente pelo nome.

**Na prática (análise).** Modelos de embeddings, rerankers e classificadores que não ocupam uma GPU inteira são candidatos a testes de consolidação. Compare latência e utilização real antes de atribuir economia ao novo arranjo.

**Disponibilidade e limites.** Disponível para P4d, P5, G7 e G7e em sete regiões, sem São Paulo na lista. CPU, RAM, rede e armazenamento do host continuam compartilhados. Alterar o layout exige outro endpoint; métricas de utilização de GPU/CPU/memória não são publicadas nesses endpoints. Preço por partição ou percentual de economia não foram confirmados.

**Fontes:** [Anúncio oficial](https://aws.amazon.com/about-aws/whats-new/2026/10/sagemaker-gpu-partitioning/) · [Documentação e referência](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-components-accelerator-partitioning.html)

**Tags:** aws, sagemaker, gpu, inferencia, finops.

## 4. Lambda durable functions recebe telemetria e consulta via MCP

**Anúncio ou divulgação:** 28/10/2026.

**O que mudou.** A AWS anunciou um plugin que reúne o histórico de uma execução durável e exporta os registros para destinos como S3, CloudWatch, DynamoDB, Aurora e OpenSearch. Um servidor MCP complementar permite consultar esse material em modo somente leitura. Há opções de amostragem e remoção de dados sensíveis.

**Na prática (análise).** Um histórico consolidado pode ajudar a investigar fluxos distribuídos por várias invocações. Antes de conectar um agente, defina quais entradas e saídas podem ser registradas e por quanto tempo serão mantidas.

**Disponibilidade e limites.** O anúncio cobre as regiões com Lambda durable functions e SDKs TypeScript, Python, Java e Go. Exige configuração do plugin e do MCP. O exportador não tem custo adicional anunciado; armazenamento e serviços de destino seguem suas próprias tarifas. Não substitui logs e tracing existentes.

**Fontes:** [Anúncio oficial](https://aws.amazon.com/about-aws/whats-new/2026/10/lambda-durable-telemetry/) · [Documentação e referência](https://docs.aws.amazon.com/durable-execution/sdk-reference/observability/telemetry/)

**Tags:** aws, lambda, observabilidade, mcp, operacao.

## 5. OpenSearch Serverless amplia opções para séries temporais

**Anúncio ou divulgação:** 28/10/2026.

**O que mudou.** A nova geração do OpenSearch Serverless ganhou collections de séries temporais para logs, métricas, traces e eventos. Uma camada warm permite manter dados menos acessados fora da camada hot, com política de envelhecimento. O anúncio também inclui alertas e detecção de anomalias.

**Na prática (análise).** Reveja a retenção por frequência de consulta. O custo total depende de ingestão, armazenamento e consultas; uma camada de armazenamento mais econômica não garante redução proporcional da fatura.

**Disponibilidade e limites.** Disponível nas regiões com OpenSearch Serverless, segundo o anúncio, com até 100 TB de armazenamento hot por collection. Não é o UltraWarm de domínios provisionados. Valores regionais não foram verificados; exemplos da página de preços não foram tratados como cotação.

**Fontes:** [Anúncio oficial](https://aws.amazon.com/about-aws/whats-new/2026/10/time-series-collection-next-generation-opensearch-serverless/) · [Documentação e referência](https://aws.amazon.com/opensearch-service/pricing/) · [Documentação e referência](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless.html)

**Tags:** aws, opensearch, observabilidade, storage, finops.

## 6. Azure Arc torna geral a atualização automática do agente

**Anúncio ou divulgação:** 28/10/2026.

**O que mudou.** A Microsoft anunciou GA da atualização automática do Connected Machine agent. A adesão é opcional, com implantação em lotes, e pode ser administrada por Azure Policy, portal, CLI ou no processo de onboarding.

**Na prática (análise).** A função ajuda a reduzir agentes desatualizados em uma frota híbrida. Antes de ampliar o uso, teste um grupo e documente as exceções. O escopo é o agente de conexão do Arc, não o sistema operacional nem as aplicações.

**Disponibilidade e limites.** A documentação atual exige agente 1.67 ou posterior e cobre somente Azure público. Windows requer PowerShell RemoteSigned; Linux, cron. A atualização do agente não exige reinício do servidor. Resultados de busca antigos ainda citavam preview e versão 1.57; a página canônica atual foi usada. Preço incremental não confirmado.

**Fontes:** [Anúncio oficial](https://techcommunity.microsoft.com/blog/azurearcblog/simplify-azure-arc-agent-updates-with-automatic-agent-upgrade-now-generally-avai/4568413) · [Documentação e referência](https://techcommunity.microsoft.com/tag/azure%20arc?messages.widget.messagelistfornodebyrecentactivitywidget-tab-main-messages-list-for-tag-widget-0=newest) · [Documentação e referência](https://learn.microsoft.com/en-us/azure/azure-arc/servers/automatic-agent-upgrade)

**Tags:** azure, azure-arc, hybrid-cloud, operacao, seguranca.

## 7. Identity Store envia alterações de identidade ao EventBridge

**Anúncio ou divulgação:** 28/10/2026.

**O que mudou.** O AWS Identity Store passou a emitir eventos sobre criação, alteração e exclusão de usuários, grupos e associações. Esses eventos podem alimentar auditoria e integrações com aplicações ou SIEM, sistemas usados para correlacionar eventos de segurança.

**Na prática (análise).** O recurso permite conectar uma mudança de identidade a um tratamento operacional verificável. Os consumidores precisam lidar com repetição e falhas; receber um evento não equivale a revogar automaticamente todas as sessões de um usuário.

**Disponibilidade e limites.** Disponível nas regiões com IAM Identity Center, com eventos nas regiões habilitadas da instância. Não há custo adicional do recurso além das tarifas padrão do EventBridge. As ações posteriores precisam ser implementadas e autorizadas separadamente.

**Fontes:** [Anúncio oficial](https://aws.amazon.com/about-aws/whats-new/2026/10/aws-identity-store-change-notifications/)

**Tags:** aws, iam, eventbridge, seguranca, governanca.

## 8. Step Functions pode ser ferramenta de agentes no AgentCore

**Anúncio ou divulgação:** 29/10/2026.

**O que mudou.** Workflows Standard e Express do Step Functions podem ser expostos como ferramentas MCP no AgentCore Gateway. O agente decide quando chamar o processo e quais entradas enviar; a sequência continua definida no workflow.

**Na prática (análise).** O desenho permite usar um agente para iniciar um procedimento já delimitado. Comece por processos de baixo risco, com escopo IAM e pontos de aprovação claros, em vez de dar acesso amplo às ferramentas.

**Disponibilidade e limites.** Disponível nas regiões do AgentCore Gateway, com Step Functions na mesma região. Aplicam-se as tarifas normais dos dois serviços. Standard e Express têm diferenças de operações e histórico que precisam ser conferidas no conector. Fixar a máquina de estados não elimina a necessidade de controlar permissões.

**Fontes:** [Anúncio oficial](https://aws.amazon.com/about-aws/whats-new/2026/10/step-functions-workflows-ai-agent-tools/) · [Documentação e referência](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-target-connector-step-functions.html)

**Tags:** aws, step-functions, agentcore, mcp, agentes, arquitetura.

## 9. Agent Registry testa gestão entre projetos

**Anúncio ou divulgação:** 30/10/2026.

**O que mudou.** A nota de lançamento apresenta, em preview, fronteiras de gestão entre projetos. Um projeto central pode descobrir agentes, servidores MCP e ferramentas de projetos membros, enquanto a execução permanece nesses projetos.

**Na prática (análise).** Um inventário central pode facilitar a identificação de responsáveis e a separação entre desenvolvimento e produção. Registrar uma ferramenta não substitui a autorização para executá-la nem a revisão das permissões IAM.

**Disponibilidade e limites.** A novidade é a função entre projetos, não o lançamento do Registry inteiro. A agregação ocorre somente na mesma localização; skills standalone e alguns recursos não são agregados. Preço específico não verificado. A entrada é de 30/10 e o rodapé marca 29/10, ambos dentro da semana; não foi inferido horário exato.

**Fontes:** [Documentação e referência](https://docs.cloud.google.com/agent-registry/release-notes) · [Documentação e referência](https://docs.cloud.google.com/agent-registry/boundaries-and-topology)

**Tags:** google-cloud, agent-registry, agentes, mcp, governanca.

## 10. Aurora PostgreSQL serverless amplia o teto para 384 ACUs

**Anúncio ou divulgação:** 27/10/2026.

**O que mudou.** O limite de capacidade do Aurora PostgreSQL serverless passou de 256 para 384 ACUs, unidades de capacidade do serviço. O novo teto exige Platform Version 4 e versões compatíveis do PostgreSQL.

**Na prática (análise).** Workloads que atingiam o limite anterior podem reavaliar a capacidade máxima antes de mudar de arquitetura. Aumentar o teto também aumenta a capacidade que pode ser consumida e cobrada durante um pico.

**Disponibilidade e limites.** A documentação relaciona PostgreSQL 18.4, 17.10, 16.14, 15.18 e 14.23 com Platform Version 4. Nessa plataforma, o anúncio permite elevar o máximo sem downtime; plataformas anteriores exigem manutenção. A cobertura regional exata e tarifas não foram confirmadas. Aurora MySQL continua com teto de 256 ACUs na documentação consultada.

**Fontes:** [Anúncio oficial](https://aws.amazon.com/about-aws/whats-new/2026/10/aurora-serverless-supports-384-acu/) · [Documentação e referência](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2-administration.html)

**Tags:** aws, aurora, postgresql, serverless, bancos-de-dados.

## Como transformar os anúncios em testes úteis

Separe experimentos de produção. Um Spend Cap pode ser adequado para conter uma prova de conceito, mas o mesmo bloqueio pode afetar um serviço que precisa permanecer disponível. Consolidação de instâncias ou GPUs também precisa de uma medição anterior e posterior, com carga comparável.

Nos recursos de agentes e identidade, explicite a fronteira de autorização. Um evento, um registro no catálogo ou uma ferramenta MCP dá contexto e capacidade técnica; a política da aplicação ainda precisa definir o que pode acontecer em seguida.

Para a operação híbrida, mudanças graduais facilitam o diagnóstico. Use grupos de teste, monitore falhas e mantenha os requisitos de versão documentados. As fontes em cada item permitem acompanhar a evolução dos previews e das restrições depois desta edição.
