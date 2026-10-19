+++
title = 'Radar de IA | Semana 42 de 2026'
description = 'Gemini 4 Argon, pesos do Muse Spark Open, revisão de código por IA em GA e a data de saída do GPT-4o da API: a IA de 12 a 18/10/2026.'
date = '2026-10-19T08:00:00-03:00'
lastmod = '2026-10-19T08:00:00-03:00'
slug = 'radar-ia-semana-42-2026'
postId = '3fb0e477-98b0-81de-8845-db2dc00f1c85'
draft = false
categorias = ['Inteligência Artificial']
tags = ['ia', 'modelos', 'agentes', 'open-source', 'segurança', 'programação']
comments = true
+++

Esta edição do Radar de IA cobre a semana ISO 42 de 2026, de segunda, 12/10, a domingo, 18/10, no horário de Brasília. São dez notícias, cada uma com data de publicação dentro desse intervalo e fonte oficial do fornecedor.

A semana teve modelos novos dos dois lados. O Google liberou o Gemini 4 Argon e a Meta lançou o Muse Wonder, ambos com preço público por token, enquanto Muse Spark Open, Nemotron 3.5 Super VL e Timestral saíram com pesos abertos. Na programação, a revisão de código e a correção de vulnerabilidades com IA ficaram GA na Anthropic e no GitHub. Para quem mantém integrações, o item mais urgente é operacional: a OpenAI marcou para 14/01/2027 o desligamento de GPT-4o, GPT-4o mini, GPT-4.1 e GPT-4.1 mini na API.

Alguns termos aparecem em quase todos os itens. GA (general availability, ou disponibilidade geral) indica que o fornecedor liberou o recurso para uso amplo, depois da fase de testes chamada preview. Token é a unidade em que os modelos medem o texto processado, e os preços de API são dados por milhão de tokens de entrada (o que você envia) e de saída (o que o modelo gera). Os trechos "Na prática" são análise editorial, não afirmações das fontes.

## 1. Gemini 4 Argon fica disponível globalmente

Google · 13/10/2026

**O que mudou:** o Google liberou o Gemini 4 Argon, seu novo modelo de fronteira, nome dado aos modelos mais capazes de cada fornecedor. Desenvolvedores e empresas acessam o modelo pela API, no AI Studio e na Gemini platform, no tier pago. Assinantes Google AI Ultra podem usá-lo no Google Antigravity, e assinantes Ultra e Pro, no app Gemini e no AI Mode da Busca. No Google Cloud, ele chegou no mesmo dia ao Gemini for business e à API, com o ID `gemini-4-argon`.

O preço introdutório é de US$ 2 por milhão de tokens de entrada e US$ 10 por milhão de tokens de saída, válido até 30/11/2026. Depois disso, passa a US$ 4 e US$ 20. A entrada em cache, quando o serviço reaproveita uma entrada já processada, tem 95% de desconto. Na Gemini API, o limite é de 1M tokens, unificado para entrada e saída. O Google cita refatorações de grandes bases de código feitas com o modelo, como a do Chromium.

**Na prática (análise):** é um novo concorrente de topo para agentes de código e tarefas de várias etapas. Antes de migrar, vale um benchmark com as suas próprias tarefas. Na conta de custo, lembre que o preço introdutório tem data para acabar.

**Disponibilidade e limites:** GA global. Preço introdutório até 30/11/2026. Nos apps, o acesso depende do plano (Ultra ou Pro).

**Fontes (13/10/2026):** [Google, anúncio do Gemini 4 Argon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/) · [Google Antigravity](https://antigravity.google/blog/gemini-4-argon-in-google-antigravity/) · [Google Cloud](https://cloud.google.com/blog/products/ai-machine-learning/gemini-4-argon-available-on-google-cloud) · [Google DeepMind no X](https://x.com/GoogleDeepMind/status/2110039274922131792)

## 2. Meta libera os pesos do Muse Spark Open

Meta · 15/10/2026

**O que mudou:** a Meta liberou os pesos do Muse Spark Open. Pesos são os parâmetros aprendidos no treinamento; com eles em mãos, dá para executar o modelo na sua própria infraestrutura, e por isso modelos distribuídos assim são chamados de open-weight.

O Muse Spark Open é multimodal, ou seja, trabalha com mais de um tipo de dado, e usa a arquitetura MoE (mixture of experts). Nela, o modelo é dividido em partes especializadas e só algumas são acionadas a cada etapa. Por isso a Meta informa dois números: 816B parâmetros no total e 42B ativos. A janela de contexto é de 1M tokens, e o foco é código e agentes.

Os pesos estão no Hugging Face, no Amazon SageMaker AI, no Google Cloud Model Garden e no Microsoft Foundry. O modelo chegou ao SageMaker JumpStart no mesmo dia. Também há APIs em Baseten, Fireworks, Groq, Modal, Nebius, OpenRouter e Together, e o modelo roda em SGLang, vLLM, TensorRT-LLM, Transformers, MLX e llama.cpp. A Meta cita a execução em dois Mac Studio M5 Ultra. A licença, chamada Muse Model License, tem termos comerciais limitados.

**Na prática (análise):** é uma opção open-weight de grande porte para quem precisa rodar o modelo em infraestrutura própria, por soberania de dados ou para ter custo previsível. O porte exige muita memória, e a licença precisa ser lida antes de qualquer uso comercial.

**Disponibilidade e limites:** os pesos estão disponíveis, mas a licença limita o uso comercial.

**Fontes (15/10/2026):** [Meta, anúncio do Muse Spark Open](https://research.meta.ai/blog/muse-spark-open) · [AWS, Muse Spark Open no SageMaker JumpStart](https://aws.amazon.com/about-aws/whats-new/2026/01/muse-spark-open-on-sagemaker-jumpstart/) · [AI at Meta no X](https://x.com/AIatMeta/status/2110779754274292212)

## 3. Meta lança Muse Wonder e Muse Wonder Full

Meta · 12/10/2026

**O que mudou:** a Meta lançou o Muse Wonder no Muse Code e na Meta Model API. O preço é de US$ 4 por milhão de tokens de entrada e US$ 20 por milhão de saída, com entrada em cache a US$ 0,20, e o contexto é de 1M tokens. A versão Muse Wonder Full fica restrita às assinaturas Power e Maximum Usage do Muse Code. O Maximum Usage é um plano novo, com 80x o limite do plano Everyday.

**Na prática (análise):** a Meta entra no mercado pago de modelos de fronteira para desenvolvedores. Os benchmarks divulgados são da própria Meta, então é preciso validar o modelo com tarefas reais.

**Disponibilidade e limites:** o Muse Wonder está na API paga. O Muse Wonder Full só é oferecido pela assinatura do Muse Code.

**Fontes:** [Meta, Build with Muse Wonder (12/10/2026)](https://dev.meta.ai/resources/blog/build-with-muse-wonder) · [AI at Meta no X (14/10/2026, repercussão do anúncio)](https://x.com/AIatMeta/status/2110517571149807685)

## 4. Claude Code Review fica GA

Anthropic · 15/10/2026

**O que mudou:** a Anthropic tornou o Code Review GA para os planos Team e Enterprise. A ferramenta revisa pull requests no GitHub. Um pull request (PR) é a proposta de alteração de código que passa por revisão antes de ser incorporada ao projeto. No Code Review, vários agentes analisam o PR, verificam os próprios achados e deixam comentários nas linhas do código, organizados por severidade. A ferramenta não aprova nem bloqueia o PR.

Segundo a Anthropic, as revisões ficaram cerca de 3x mais rápidas que no preview, passando de cerca de 20 minutos para 6 a 10 minutos. Os admins escolhem o nível de revisão por repositório: Quick, Standard ou Deep. O uso é cobrado à parte, em créditos. Organizações Enterprise elegíveis podem resgatar pelo menos US$ 10.000 em créditos até 15/01/2027, e os créditos expiram 30 dias após o resgate.

**Na prática (análise):** a revisão automática de PR deixa a fase de experimento. Ela serve como primeira passada antes do revisor humano, principalmente em times com muito código gerado por agentes. As restrições de compliance abaixo pesam na decisão.

**Disponibilidade e limites:** GA para Team e Enterprise, no GitHub, inclusive no GitHub Enterprise Server (GHES). Não está disponível com Zero Data Retention (a configuração em que o fornecedor não retém os dados enviados), com configuração HIPAA (a lei americana que protege dados de saúde) nem com chaves de criptografia gerenciadas pelo cliente (CMEK).

**Fontes:** [Anthropic, Code Review is now generally available](https://claude.com/resources/articles/code-review-is-now-generally-available) (a página não mostra data) · [documentação do Code Review](https://code.claude.com/docs/en/code-review) · [Claude Devs no X (15/10/2026, 19h51 BRT)](https://x.com/ClaudeDevs/status/2110866210573386065)

## 5. GitHub: AI Scan para PRs e agentic autofix ficam GA

GitHub (Microsoft) · 15/10/2026

**O que mudou:** foram dois anúncios no mesmo dia, ambos GA.

O primeiro é o AI Scan para pull requests. Ele complementa o CodeQL, o mecanismo de análise de código do GitHub, e encontra vulnerabilidades em linguagens que o CodeQL não cobre, como PHP, Shell, Terraform/HCL, Dockerfile, JSP e Blazor. Os achados são consultivos: aparecem no PR, mas não bloqueiam o merge.

O segundo é o agentic autofix. Você atribui um alerta de code scanning ao Copilot, que explora o código, gera e valida uma correção e abre um PR em rascunho com ela.

**Na prática (análise):** a segurança de IaC (infrastructure as code, a infraestrutura descrita em arquivos como os do Terraform) e de scripts entra no fluxo de PR sem ferramenta extra. Atenção ao custo: os dois recursos consomem Code Security AI Credits, e o autofix também consome minutos de GitHub Actions.

**Disponibilidade e limites:** GA. O AI Scan cobre repositórios públicos; nos privados, exige GitHub Code Security ou Advanced Security, e não exige licença do Copilot. O autofix precisa ser habilitado por organização ou enterprise e não está disponível para Enterprise Managed Users.

**Fontes (15/10/2026):** [GitHub Changelog, AI Scan for pull requests](https://github.blog/changelog/2026-10-15-ai-scan-for-pull-requests-generally-available/) · [GitHub Changelog, agentic autofix](https://github.blog/changelog/2026-10-15-agentic-autofix-for-code-scanning-alerts-general-availability/)

## 6. OpenAI marca o desligamento de GPT-4o, GPT-4o mini, GPT-4.1 e GPT-4.1 mini na API

OpenAI · aviso em 14/10/2026, desligamento em 14/01/2027

**O que mudou:** a OpenAI notificou a descontinuação de gpt-4o (versões 2024-08-06 e 2024-11-20), gpt-4o-mini, gpt-4.1 e gpt-4.1-mini. Esses modelos serão removidos da API em 14/01/2027, e o substituto recomendado é o gpt-6-luna. Os fine-tunes, versões ajustadas com dados próprios a partir desses modelos, seguem o mesmo cronograma.

Como contexto, e não como novidade da semana: uma leva anterior, que inclui gpt-4, gpt-4-turbo, o1, o3-mini, o4-mini e gpt-image-1, entre outros, desliga em 23/10/2026. O aviso dessa leva saiu em 22/04/2026.

**Na prática (análise):** é um item de operação. Quem tem integração fixada nesses IDs precisa inventariar código, fallbacks e jobs agendados e testar o substituto antes da data.

**Disponibilidade e limites:** os modelos já estão marcados como deprecated, com desligamento em data fixa.

**Fonte:** [OpenAI, página de descontinuações da API](https://developers.openai.com/api/docs/deprecations) (aviso de 14/10/2026)

## 7. GPT-Live-1.1 chega ao ChatGPT e a API ganha prompt-to-voice

OpenAI · 15/10/2026 (ChatGPT) e 16/10/2026 (API)

**O que mudou:** o GPT-Live-1.1 e sua versão mini, o GPT-Live-1.1 Quip, chegaram ao ChatGPT Voice com sotaques mais naturais e novas vozes em francês, alemão, hindi, japonês, coreano e espanhol mexicano. O post oficial diz "rolling out today to all users. Coming soon to the API".

Em 16/10, a API ganhou o prompt-to-voice: você descreve em texto a voz que quer, a API cria essa voz personalizada e você pode reutilizá-la nas sessões GPT-Live. Criar a voz é grátis, e a fala segue a cobrança normal. O changelog da API lista nove novas vozes.

**Na prática (análise):** agentes de voz, como os de atendimento e de URA (a unidade de resposta audível dos atendimentos telefônicos), ganham identidade de voz sem precisar gravar um locutor. Não há português entre os idiomas novos listados.

**Disponibilidade e limites:** no ChatGPT, em rollout para todos os usuários, e as vozes variam por região e por conta. Na API, o prompt-to-voice está disponível para todos os clientes desde 16/10. O GPT-Live-1.1 em si ainda não está na API: o post oficial diz "Coming soon to the API".

**Fontes:** [ChatGPT release notes (15/10/2026)](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) · [changelog da API da OpenAI (16/10/2026)](https://developers.openai.com/api/docs/changelog) · [OpenAI no X](https://x.com/OpenAI/status/2110797830361436604)

## 8. NVIDIA lança o Nemotron 3.5 Super VL, modelo aberto multimodal

NVIDIA · 15/10/2026

**O que mudou:** a NVIDIA lançou o Nemotron 3.5 Super VL, um modelo aberto com arquitetura MoE (a mesma ideia de partes especializadas do item 2), com 120B parâmetros no total e 12B ativos. Ele entende texto, imagem, vídeo e documentos, faz raciocínio e uso de ferramentas e tem contexto de até 1M tokens.

Os pesos em BF16, um formato numérico de 16 bits, estão no Hugging Face sob a licença OpenMDW-1.1. O modelo também sai como NIM, o formato da NVIDIA para servir modelos como microsserviço, e teve suporte no vLLM desde o dia do lançamento. No Amazon SageMaker JumpStart, onde chegou em 16/10, roda em NVFP4 nas instâncias G7 e em BF16 nas p5en.

**Na prática (análise):** é uma opção aberta mais leve que o Muse Spark Open para agentes que precisam ler telas, PDFs e diagramas.

**Disponibilidade e limites:** pesos abertos. Também disponível via NIM e no SageMaker JumpStart.

**Fontes:** [NVIDIA Developer Blog (15/10/2026)](https://developer.nvidia.com/blog/nvidia-nemotron-3-5-super-vl-powers-specialized-agents-with-multimodal-reasoning/) · [AWS, Nemotron 3.5 Super VL no SageMaker JumpStart (16/10/2026)](https://aws.amazon.com/about-aws/whats-new/2026/01/nvidia-nemotron-3.5-super-vl-on-sagemaker-jumpstart/) · [NVIDIA no X](https://x.com/nvidia/status/2110750157272719562)

## 9. Mistral lança o Timestral, modelos para séries temporais

Mistral AI · 15/10/2026

**O que mudou:** a Mistral lançou o Timestral, sua primeira família de modelos de fundação para séries temporais, que são dados medidos ao longo do tempo. A família tem quatro tamanhos: 5M, 28M, 123M e 209M parâmetros.

O Timestral faz previsão probabilística (que indica a faixa de incerteza do resultado), multivariada (várias séries relacionadas ao mesmo tempo) e zero-shot (sem treinar o modelo para aquela série específica). Ele aceita covariáveis passadas e futuras, que são variáveis de apoio à previsão, e roda de forma eficiente em CPU. A Mistral reporta 1º lugar nos benchmarks GIFT-Eval, TIME e fev-bench com o modelo de 209M. Os pesos estão no Hugging Face, e o fine-tuning é feito pelo Mistral Forge.

**Na prática (análise):** serve para prever capacidade, demanda e métricas de observabilidade sem treinar um modelo para cada série. Os rankings foram declarados pela própria Mistral.

**Disponibilidade e limites:** pesos públicos.

**Fontes (15/10/2026):** [Mistral, anúncio do Timestral](https://mistral.ai/news/timestral/) · [Timestral-209M no Hugging Face](https://huggingface.co/mistralai/Timestral-209M)

## 10. GPT-6 Pro no ChatGPT ganha agentes em paralelo

OpenAI · 16/10/2026

**O que mudou:** segundo as release notes do ChatGPT, o GPT-6 Pro na aba Chat passa a responder mais rápido e a usar melhor plugins e ferramentas. Ele também pode dividir uma tarefa entre vários agentes em paralelo e mostrar o progresso de cada um. A opção de raciocínio Pro usa o GPT-6 Astra. No X, o post original da OpenAI foi editado, e a versão final fala em "GPT-6 Astra Pro… Now available to Pro users in the Chat tab".

**Na prática (análise):** a novidade reforça a orquestração multiagente, em que vários agentes dividem uma tarefa, dentro do produto de consumo. Para empresas, o acesso depende das configurações do workspace.

**Disponibilidade e limites:** em rollout para usuários Pro elegíveis. Em workspaces gerenciados, depende de configuração e elegibilidade.

**Fontes (16/10/2026):** [ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) · [OpenAI no X, versão editada](https://x.com/OpenAI/status/2111192259073094035) ([post original](https://x.com/OpenAI/status/2111185504746213705))

## O que levar desta semana

Se você mantém integrações na API da OpenAI, comece pelo item 6. Procure no código, nos fallbacks e nos jobs agendados os IDs gpt-4o, gpt-4o-mini, gpt-4.1 e gpt-4.1-mini, que saem em 14/01/2027, e aproveite para confirmar que nada depende da leva que desliga em 23/10/2026.

Se o seu time avalia revisão de código ou segurança com IA, o Claude Code Review e o AI Scan com agentic autofix do GitHub já estão em GA. A decisão passa pelo custo em créditos, pelo escopo de repositórios e pelas restrições de compliance de cada um. Nenhum deles aprova o PR no lugar de uma pessoa.

Para os modelos novos, abertos ou pagos, os benchmarks citados vêm dos próprios fornecedores. Um teste com tarefas do seu dia a dia, com o custo anotado, ajuda a decidir se algum deles merece substituir o que você usa hoje.

### Referências

1. Gemini 4 Argon: [Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/), [Google Antigravity](https://antigravity.google/blog/gemini-4-argon-in-google-antigravity/), [Google Cloud](https://cloud.google.com/blog/products/ai-machine-learning/gemini-4-argon-available-on-google-cloud), [X](https://x.com/GoogleDeepMind/status/2110039274922131792)
2. Muse Spark Open: [Meta](https://research.meta.ai/blog/muse-spark-open), [AWS](https://aws.amazon.com/about-aws/whats-new/2026/01/muse-spark-open-on-sagemaker-jumpstart/), [X](https://x.com/AIatMeta/status/2110779754274292212)
3. Muse Wonder: [Meta](https://dev.meta.ai/resources/blog/build-with-muse-wonder), [X](https://x.com/AIatMeta/status/2110517571149807685)
4. Claude Code Review: [anúncio](https://claude.com/resources/articles/code-review-is-now-generally-available), [documentação](https://code.claude.com/docs/en/code-review), [X](https://x.com/ClaudeDevs/status/2110866210573386065)
5. GitHub AI Scan e agentic autofix: [AI Scan](https://github.blog/changelog/2026-10-15-ai-scan-for-pull-requests-generally-available/), [agentic autofix](https://github.blog/changelog/2026-10-15-agentic-autofix-for-code-scanning-alerts-general-availability/)
6. Descontinuações da OpenAI: [documentação](https://developers.openai.com/api/docs/deprecations)
7. GPT-Live-1.1 e prompt-to-voice: [ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes), [changelog da API](https://developers.openai.com/api/docs/changelog), [X](https://x.com/OpenAI/status/2110797830361436604)
8. Nemotron 3.5 Super VL: [NVIDIA](https://developer.nvidia.com/blog/nvidia-nemotron-3-5-super-vl-powers-specialized-agents-with-multimodal-reasoning/), [AWS](https://aws.amazon.com/about-aws/whats-new/2026/01/nvidia-nemotron-3.5-super-vl-on-sagemaker-jumpstart/), [X](https://x.com/nvidia/status/2110750157272719562)
9. Timestral: [Mistral](https://mistral.ai/news/timestral/), [Hugging Face](https://huggingface.co/mistralai/Timestral-209M)
10. GPT-6 Pro: [ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes), [X, versão editada](https://x.com/OpenAI/status/2111192259073094035), [X, original](https://x.com/OpenAI/status/2111185504746213705)
