+++
title = 'Radar de IA | Semana 44 de 2026'
description = 'Oito novidades verificadas: modelos, custos de API, programação com agentes e controles de operação.'
date = '2026-11-02T05:23:46-03:00'
lastmod = '2026-11-02T05:46:54-03:00'
slug = 'radar-ia-semana-44-2026'
postId = '40c0e477-98b0-8181-ae10-eeeb42b9c442'
draft = false
categorias = ['Inteligência Artificial']
tags = ['ia', 'agentes', 'modelos', 'programacao', 'seguranca']
comments = true
+++

Entre 26 de outubro e 1º de novembro, as novidades de IA passaram por escolhas bem práticas: qual modelo usar, como acompanhar seus custos e onde manter a revisão humana quando um agente executa tarefas.

Esta edição reúne oito anúncios e divulgações técnicas verificados em fontes primárias. Há lançamentos disponíveis, funções em beta e uma retirada futura; cada situação está separada abaixo.

## Cobertura e destaques

- Semana ISO 44 de 2026: 26/10 às 00h00 até 01/11 às 23h59:59, em America/Sao_Paulo.
- Verificação de disponibilidade em 02/11/2026. As datas editoriais nem sempre incluem horário e fuso; não foi inferido um instante exato nas bordas da semana.
- Destaques: GPT-6.1 Terra, pesos do Mistral Large 4, custos no Claude, prazo do Opus fast, GitHub no Teams, arquivos no Gemini e duas leituras sobre segurança de agentes.

## 1. GPT-6.1 Terra: modelo visual com preço de API definido

**Anúncio ou divulgação:** 26/10/2026.

**O que mudou.** A OpenAI apresentou o GPT-6.1 Terra para tarefas que combinam raciocínio visual, uso do computador e escrita. O modelo chega à API como gpt-6.1-terra e está em distribuição no Work e no Codex.

**Na prática (análise).** Em uma automação visual, o preço por token é apenas parte da conta. O teste útil compara custo por tarefa concluída, qualidade da leitura da tela e frequência de intervenção humana.

**Disponibilidade e limites.** O preço padrão informado é US$ 1 por milhão de tokens de entrada, US$ 0,05 para entrada em cache e US$ 5 de saída. A disponibilidade depende de produto, plano e configurações; não é um lançamento na aba Chat. A documentação também exclui residência de inferência nos Emirados Árabes Unidos.

**Fontes:** [Anúncio da OpenAI](https://openai.com/index/introducing-gpt-6-1-terra/) · [Notas do ChatGPT](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) · [Notas de modelos](https://help.openai.com/en/articles/9624314-model-release-notes)

**Tags:** openai, modelos, agentes, computer-use, custos.

## 2. Mistral libera pesos melhorados do Large 4

**Anúncio ou divulgação:** 29/10/2026.

**O que mudou.** A Mistral disponibilizou os pesos de uma versão melhorada do Large 4. O preview inicial era de 6/10: a novidade desta semana é a distribuição dos pesos, acompanhada de preços e condições de licenciamento.

**Na prática (análise).** Hospedagem própria pode ajudar quando há requisitos de controle de dados e customização. A avaliação precisa incluir capacidade de hardware, operação e licença, além do desempenho do modelo.

**Disponibilidade e limites.** Os pesos foram disponibilizados no Hugging Face. A licença exige acordo comercial separado para negócios Model-as-a-Service. A variante especializada em cibersegurança continua restrita a parceiros aprovados. Preços de API anunciados por milhão de tokens: US$ 0,70 de entrada, US$ 0,07 em cache e US$ 2,10 de saída; regiões não detalhadas.

**Fontes:** [Anúncio da Mistral](https://mistral.ai/news/mistral-large-4-oss/) · [Índice de notícias da Mistral](https://mistral.ai/news/) · [Pesos e licença no repositório oficial](https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B)

**Tags:** mistral, modelos, open-weights, programacao, seguranca.

## 3. Claude ganha uma API unificada de consumo e custos

**Anúncio ou divulgação:** 29/10/2026.

**O que mudou.** A Usage and Cost Analytics API entrou em beta. Ela permite consultar consumo e custo por dimensões como modelo, workspace, chave de API e usuário ou conta de serviço. Os endpoints anteriores passaram a ser legados, mas continuam suportados.

**Na prática (análise).** Essas dimensões ajudam a atribuir despesas às aplicações e investigar aumentos de consumo. A API fornece informação para gestão; não impõe um teto de gastos por conta própria.

**Disponibilidade e limites.** O acesso exige o cabeçalho beta e permissões administrativas apropriadas. No Claude Platform on AWS, as consultas são regionais e algumas dimensões não estão disponíveis. Não foi informado preço adicional para a função.

**Fontes:** [Notas da plataforma Claude](https://platform.claude.com/docs/en/release-notes/overview) · [Documentação de custos e consumo](https://platform.claude.com/docs/en/manage-claude/usage-cost-analytics-api)

**Tags:** anthropic, finops, observabilidade, api.

## 4. Opus 4.8 fast tem retirada marcada para 30 de novembro

**Anúncio ou divulgação:** 30/10/2026.

**O que mudou.** A Anthropic anunciou a depreciação do modo rápido do Opus 4.8. A remoção está prevista para 30/11/2026: depois disso, requisições a claude-opus-4-8 com speed: "fast" retornarão erro. A migração indicada é para o Opus 5.5.

**Na prática (análise).** O passo prático é localizar esse parâmetro em aplicações e agentes, testar a troca e revisar o custo antes do prazo. O aviso trata desse modo de inferência, não da retirada integral do modelo.

**Disponibilidade e limites.** O fast mode do 4.8 ainda aparece como research preview. No 5.5, está disponível na Claude API, no serviço gerenciado pela Anthropic no Google Cloud e no Foundry. Preço: US$ 8 de entrada e US$ 40 de saída por milhão de tokens, com modificadores de cache e residência. Batch API e Priority Tier não são compatíveis.

**Fontes:** [Notas da plataforma Claude](https://platform.claude.com/docs/en/release-notes/overview) · [Preço e limites do fast mode](https://platform.claude.com/docs/en/build-with-claude/fast-mode)

**Tags:** anthropic, operacao, migracao, custos.

## 5. GitHub no Teams chega a GA com revisão no Canvas

**Anúncio ou divulgação:** 30/10/2026.

**O que mudou.** A experiência GitHub no Teams saiu de preview e chegou à disponibilidade geral (GA). O Canvas permite acompanhar plano, alterações e pull request na conversa. O anúncio também reúne suporte a vários repositórios, ferramentas via MCP e escolha de modelo; o fluxo de notificações para PR já havia sido apresentado em 26/10.

**Na prática (análise).** Para equipes que trabalham no Teams, o fluxo pode levar o contexto de uma discussão até uma proposta de código. Testes, revisão e decisão de merge continuam etapas distintas da tarefa delegada ao agente.

**Disponibilidade e limites.** A disponibilidade geral exige licença Copilot, consentimento de recurso no Microsoft 365, aplicativo permitido no Teams e recursos de agente, sandboxes e cobrança de CLI habilitados no GitHub. O anúncio não detalha preços ou regiões. O texto foi conferido na reprodução integral do índice oficial da Microsoft.

**Fontes:** [Anúncio da Microsoft](https://techcommunity.microsoft.com/blog/microsoftteamsblog/the-github-app-in-microsoft-teams-is-now-generally-available/4569136) · [Reprodução no índice oficial Microsoft](https://techcommunity.microsoft.com/tag/product%20updates) · [Documentação de integração e permissões](https://docs.github.com/en/copilot/how-tos/copilot-integrations/integrate-cloud-agent-with-teams)

**Tags:** microsoft, github, programacao, agentes, mcp.

## 6. Gemini passa a editar arquivos dentro da conversa

**Anúncio ou divulgação:** 29/10/2026.

**O que mudou.** O Google anunciou criação, visualização e edição de documentos, PDFs, apresentações, planilhas e código no chat do Gemini. É possível fazer ajustes manualmente ou solicitar alterações em partes do arquivo.

**Na prática (análise).** A aproximação entre conversa e artefato reduz a necessidade de alternar ferramentas durante uma revisão. Cálculos, referências e formatação final ainda precisam ser conferidos antes de distribuir o material.

**Disponibilidade e limites.** O anúncio abrange os usuários e idiomas atendidos pelo aplicativo. PDFs funcionam na web e no celular; os demais formatos citados ficam na web. Não foi anunciada uma API equivalente nem cobrança adicional específica.

**Fontes:** [Anúncio do Google](https://blog.google/innovation-and-ai/products/gemini-app/edit-files-directly/)

**Tags:** google, gemini, produtividade, documentos.

## 7. GTIG documenta o abuso de agentes em intrusões

**Anúncio ou divulgação:** 30/10/2026.

**O que mudou.** GTIG e Mandiant publicaram uma investigação sobre frameworks como ARTEX, Hexstrike e CAIRN empregados em intrusões reais. A divulgação é desta semana; as atividades analisadas incluem casos observados desde o fim de agosto.

**Na prática (análise).** A defesa precisa acompanhar ações rápidas com credenciais válidas. Credenciais de curta duração, privilégio mínimo e correlação entre identidade, endpoint e cloud são pontos concretos para revisar em uma avaliação de exposição.

**Disponibilidade e limites.** É um relatório público, não um novo produto ou modelo. A pesquisa registra erros e atividade ruidosa, além de tentativas bem-sucedidas. Projeções de agentes mais furtivos não devem ser confundidas com capacidades já demonstradas. Preços e regiões de um lançamento não se aplicam.

**Fontes:** [Relatório GTIG e Mandiant](https://cloud.google.com/blog/topics/threat-intelligence/artex-and-friends-enter-agentic-offensive-frameworks)

**Tags:** google, gtig, seguranca, agentes, resposta-a-incidentes.

## 8. OpenAI descreve monitoramento em camadas para agentes

**Anúncio ou divulgação:** 29/10/2026.

**O que mudou.** A OpenAI detalhou um sistema que combina triagem, revisão por modelos, investigação e resposta humana. Em uma simulação retrospectiva de um incidente anterior, o monitor identificou a saída do ambiente isolado em cerca de 30 minutos.

**Na prática (análise).** O desenho ajuda a pensar a operação de agentes: registrar ações, correlacionar sinais e definir quem pode interromper a execução. Esses mecanismos complementam o isolamento e as permissões mínimas.

**Disponibilidade e limites.** O texto descreve mecanismos internos e aplicações específicas, não uma API comercial disponível para qualquer integração. Há falsos positivos e partes ainda em expansão. Os 30 minutos são um resultado retrospectivo específico, sem garantia de detecção e sem representar um incidente novo em 29/10.

**Fontes:** [Anúncio da OpenAI](https://openai.com/index/how-we-detect-frontier-model-misalignment/)

**Tags:** openai, seguranca, agentes, observabilidade.

## O que priorizar nesta semana

Para quem já opera agentes, a retirada do Opus 4.8 fast oferece uma ação com prazo definido: inventariar chamadas e testar a migração. Para novas provas de conceito, vale comparar modelos com uma tarefa representativa e medir custo por execução concluída, em vez de escolher somente pelo preço de tokens.

Os relatos de segurança também pedem critérios observáveis. Antes de ampliar acesso, defina quais ações o agente pode executar, quais exigem revisão e como interromper a tarefa. Um bom resultado em demonstração não substitui esse acompanhamento em operação.

Os artigos citados em cada destaque são as referências desta edição.
