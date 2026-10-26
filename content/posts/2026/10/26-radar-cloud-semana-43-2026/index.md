+++
title = 'Radar de Cloud | Semana 43 de 2026'
description = 'As 10 notícias de cloud de 19 a 25/10/2026: fallback no AgentCore Gateway, JSON por schema no Bedrock, vozes pt-BR no Polly, ECS Gateway e mais.'
date = '2026-10-26T08:00:00-03:00'
lastmod = '2026-10-26T08:00:00-03:00'
slug = 'radar-cloud-semana-43-2026'
postId = '4050e477-98b0-813c-8247-eddf38357856'
draft = false
categorias = ['Cloud']
tags = ['cloud', 'aws', 'google-cloud', 'azure', 'agentes', 'infraestrutura']
comments = true
+++

Esta edição cobre a semana ISO 43 de 2026, de 19 a 25 de outubro, no horário de Brasília. São dez novidades de AWS, Google Cloud e Microsoft, todas com fonte oficial e data dentro desse recorte.

A AWS concentrou seis delas, e três mexem no que os times de agentes vinham resolvendo no próprio código: fallback de modelo no AgentCore Gateway, JSON garantido por schema em todos os modelos Claude no Bedrock e uma checagem de grounding que aceita tom de conversa. Também vieram o TorchNeuron, que leva o PyTorch ao Trainium, duas vozes em português do Brasil no Amazon Polly e o Amazon ECS Gateway, um ingress gerenciado que já está em São Paulo. Vários dos recursos de IA ainda não chegaram à região de São Paulo, e isso aparece nos limites de cada item.

O Google trouxe três: busca corporativa com RAG gerenciado no Gemini do Google Distributed Cloud air-gapped (em preview), o Gemini no Google Sheets analisando dados do BigQuery e o Confidential G4, com GPUs NVIDIA Blackwell, em GA. Da Microsoft, a ferramenta de automação de navegador do Foundry entrou em GA.

Duas siglas aparecem em quase todos os itens. GA (general availability) é a disponibilidade geral do recurso, fora da fase de testes. Preview é essa fase de testes, antes do GA. Em cada item, o trecho "Na prática" é análise editorial; o restante segue o que dizem as fontes.

## 1. AWS para agentes: fallback de modelo no AgentCore Gateway, Continuum em GA e filtros na busca web do Bedrock

AWS · 22/10/2026 (AgentCore Gateway e Continuum) e 23/10/2026 (busca web do Bedrock)

**O que mudou:** o Amazon Bedrock AgentCore reúne serviços da AWS para executar agentes de IA. Um deles, o AgentCore Gateway, passou a aceitar as chamadas InvokeModel e InvokeModelWithResponseStream do Bedrock. Assim, uma integração que já usa o SDK do Bedrock pode apontar para o gateway e alcançar qualquer provedor por um endpoint governado.

O gateway também ganhou fallback. Quando o destino principal sofre throttling (limitação de requisições), fica sem capacidade ou cai, a requisição segue uma cadeia ordenada definida em regra. Um circuit breaker, mecanismo que deixa de chamar um destino que está falhando, pula os destinos com falha.

No mesmo dia, o AWS Continuum for code vulnerabilities entrou em GA. Ele monta um grafo de contexto do ambiente (topologia, identidades e alcance de rede), cruza esse grafo com achados que já existem e escaneia o código. Depois confirma se a falha é explorável numa sandbox isolada, prioriza pelo impacto e entrega a correção como pull request, com prova de exploração. Começa no modo Learn, em que propõe mudanças para aprovação, e pode passar ao Enforce, em que age sozinho dentro de guardrails.

Em 23/10, a busca web do Bedrock, na ferramenta web_search da Responses API, ganhou listas de até 100 domínios permitidos ou até 100 bloqueados e um parâmetro de localização do usuário.

**Na prática (análise):** com o fallback no gateway, manter o agente de pé quando um modelo fica sem capacidade deixa de ser tarefa do código de cada time, e a governança multi-provedor fica num lugar só. O Continuum responde à aceleração na descoberta de falhas com correção em escala, e começar no Learn antes de passar ao Enforce é o caminho prudente. O filtro de domínios restringe as fontes da busca, mas não atende residência de dados no Brasil.

**Disponibilidade e limites:** o recurso do Gateway está em todas as regiões do serviço, exceto China. O Continuum está nas regiões listadas na tabela de regiões da AWS. Os filtros da busca web estão só em us-east-1, us-east-2, us-west-2 e GovCloud (US-West), sem São Paulo.

**Fontes (data):** [AgentCore Gateway com InvokeModel e fallback](https://aws.amazon.com/about-aws/whats-new/2026/10/agentcore-gateway-invokemodel-fallback/) (22/10/2026) · [AWS Continuum for code vulnerabilities em GA](https://aws.amazon.com/about-aws/whats-new/2026/10/aws-continuum-for-code-vulnerabilities-is-now-generally-available) (22/10/2026) · [filtros de domínio e localização na busca web do Bedrock](https://aws.amazon.com/about-aws/whats-new/2026/10/bedrock-web-search-domain-user-location/) (23/10/2026)

## 2. Amazon Bedrock: encurtamento de prompt no Advanced Prompt Optimization e nível Standard no contextual grounding do Guardrails

AWS · 20/10/2026

**O que mudou:** o Advanced Prompt Optimization do Bedrock ganhou o prompt shortening, que encurta o prompt mantendo ou melhorando a nota numa avaliação definida pelo cliente. Ele só devolve a versão otimizada se ela for mais curta e tiver nota igual ou maior; se não for, volta o original. Mostra a taxa de compressão e os tokens antes e depois, e aceita qualquer método de avaliação, como LLM como juiz ou avaliadores em Lambda.

No mesmo dia, o Guardrails, a camada de filtros e checagens do Bedrock, ganhou o nível Standard para as checagens de contextual grounding, que avaliam se a resposta se apoia no contexto fornecido. O Standard aceita respostas com raciocínio ou tom de conversa, pontua de forma mais consistente respostas de mesmo sentido escritas com palavras diferentes e cobre mais idiomas que o Classic. Guardrails existentes continuam no Classic até serem alterados, e o preço é o mesmo do Classic.

**Na prática (análise):** menos tokens de entrada significam menos custo e menor tempo até o primeiro token em prompts que incharam. O Grounding Standard torna a checagem de alucinação usável em chatbots conversacionais. A exigência de inferência entre regiões e a ausência de São Paulo pesam para quem precisa de residência de dados.

**Disponibilidade e limites:** o shortening está em todas as regiões do Advanced Prompt Optimization. O Grounding Standard está em GA em Norte da Virgínia, Ohio, Norte da Califórnia, Oregon, Frankfurt, Irlanda, Milão, Paris, Espanha, Estocolmo e Tóquio, sem São Paulo, e exige um guardrail profile com inferência entre regiões.

**Fontes (data):** [prompt shortening no Advanced Prompt Optimization](https://aws.amazon.com/about-aws/whats-new/2026/10/bedrock-prompt-optimization-shortening/) (20/10/2026) · [nível Standard no contextual grounding do Guardrails](https://aws.amazon.com/about-aws/whats-new/2026/10/bedrock-guardrails-grounding-standard/) (20/10/2026)

## 3. Amazon Bedrock passa a garantir JSON por schema em todos os modelos Claude

AWS e Anthropic · 19/10/2026 (AWS ML Blog) e 20/10/2026 (What's New)

**O que mudou:** saída estruturada é a resposta do modelo num formato definido antes da chamada, como um JSON com campos fixos. O Bedrock passou a oferecer isso para todos os modelos Anthropic Claude, nos endpoints bedrock-runtime e bedrock-mantle.

São dois mecanismos. No primeiro, você define o formato de saída com um JSON Schema, e a resposta sempre segue esse schema. No segundo, o strict tool use, o Bedrock valida os parâmetros das chamadas de ferramentas. Os dois funcionam com lote e streaming e, no bedrock-runtime, com inferência entre regiões.

Há limites técnicos. O recurso aceita um subconjunto do JSON Schema Draft 2020-12 e exige `additionalProperties: false`. A gramática é compilada na primeira chamada e fica em cache por 24 horas por conta. Restrições numéricas (`minimum`, `maximum`), de tamanho de string e schemas recursivos são aceitos, mas não são aplicados na geração.

**Na prática (análise):** boa parte da lógica de parsing e de nova tentativa em extração, classificação e function calling deixa de ser necessária. Os limites numéricos e de tamanho ainda precisam ser validados na aplicação, assim como os cortes por max_tokens e as recusas do modelo.

**Disponibilidade e limites:** GA, nos dois endpoints, nas regiões de cada modelo Claude. O post não menciona custo adicional.

**Fontes (data):** [saídas estruturadas para modelos Claude no Bedrock, AWS ML Blog](https://aws.amazon.com/blogs/machine-learning/structured-outputs-for-anthropic-claude-models-on-amazon-bedrock/) (19/10/2026) · [histórico de documentação do Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-ug-doc-history.html)

## 4. AWS anuncia o TorchNeuron, backend nativo de PyTorch para o Trainium

AWS, PyTorch e Hugging Face · 19/10/2026 (PyTorch Blog) e 20/10/2026 (beta pública e What's New)

**O que mudou:** o Trainium é o chip próprio da AWS para IA. O TorchNeuron é um backend nativo de PyTorch para o Trainium2 e o Trainium3: o código roda com `.to('neuron')`, e o que já usa `torch.accelerator` roda sem alteração.

Ele suporta execução eager (com um modo adaptive eager experimental), `torch.compile` com backend neuron, as APIs distribuídas padrão (DDP, FSDP2, paralelismo de tensor e de pipeline) e kernels via Neuron Kernel Interface. As bibliotecas Transformers, Diffusers e TRL, da Hugging Face, passam a suportar Trainium. TorchAO e FP8 estão em beta privado.

A Deepgram relata cerca de 60% mais segundos de áudio processados por dólar que suas GPUs de referência, nos benchmarks que avaliou.

**Na prática (análise):** adaptar o código é a parte cara de ir para o Trainium. Se a compatibilidade se confirmar, o chip vira uma opção real de custo. Como o TorchNeuron está em beta, vale medir com um modelo real antes de prometer economia.

**Disponibilidade e limites:** beta pública, código aberto (Apache 2.0), em github.com/aws-neuron/torch-neuronx. A instalação é por `pip install torch-neuronx`, pelo repositório pip do AWS Neuron.

**Fontes (data):** [Introducing TorchNeuron, PyTorch Blog](https://pytorch.org/blog/introducing-torchneuron-native-pytorch-backend-for-aws-trainium/) (19/10/2026)

## 5. Amazon Polly troca o modelo do motor Generative e ganha duas vozes em português do Brasil

AWS · 20/10/2026

**O que mudou:** o Amazon Polly é o serviço da AWS que transforma texto em fala. O motor Generative dele passou a usar um novo modelo, com fala mais natural e baixa latência, sem mudança de código. Chegaram 14 vozes novas em nove locales, entre elas Leo e Carolina em português do Brasil, e dois idiomas novos, hindi e finlandês.

Números, e-mails e endereços soam mais confiáveis, e o SSML (a linguagem de marcação usada para controlar a fala) continua igual. O Polly Generative também chegou ao GovCloud.

**Na prática (análise):** em agentes de voz e URAs (unidades de resposta audível, o atendimento automático por telefone) na AWS, como o Amazon Connect com LLM, vozes em pt-BR e uma leitura melhor de números e endereços resolvem problemas comuns no atendimento brasileiro. Como o motor não está em São Paulo, latência e residência de dados entram na conta.

**Disponibilidade e limites:** Norte da Virgínia, Oregon, Frankfurt, Zurique, Londres, Sydney, Seul, Singapura, Tóquio, Canadá (Central) e GovCloud (US-West). O anúncio não traz mudança de preço.

**Fontes (data):** [Amazon Polly Generative](https://aws.amazon.com/about-aws/whats-new/2026/10/polly-generative/) (20/10/2026)

## 6. Gemini no Google Distributed Cloud air-gapped ganha busca corporativa com RAG gerenciado (preview)

Google e NVIDIA · 20/10/2026

**O que mudou:** o Google Distributed Cloud (GDC) air-gapped é a versão da nuvem do Google para ambientes fisicamente isolados. RAG (retrieval-augmented generation) é a técnica em que o modelo busca trechos em documentos antes de responder.

O GDC air-gapped ganhou busca corporativa com Gemini, acelerada por NVIDIA Blackwell Ultra. Em preview, há um RAG totalmente gerenciado que roda dentro do perímetro físico, sem conexão com a internet pública nem com a infraestrutura global do Google Cloud. Os usuários sobem arquivos numa conversa e pedem para achar, resumir, comparar ou traduzir. As respostas citam as fontes, e as conversas persistem entre sessões.

**Na prática (análise):** o recurso tira de quem opera o ambiente a montagem de OCR, banco vetorial e interface para ter RAG num ambiente isolado. O alvo é governo, defesa e setor regulado.

**Disponibilidade e limites:** preview, sem preço no post.

**Fontes (data):** [RAG gerenciado dentro do perímetro soberano, Google Cloud Blog](https://cloud.google.com/blog/topics/hybrid-cloud/managed-rag-search-inside-the-sovereign-perimeter-gemini-on-gdc-enterprise-search) (20/10/2026)

## 7. Gemini no Google Sheets passa a analisar dados do BigQuery em linguagem natural

Google · 19/10/2026 (início do rollout)

**O que mudou:** o Connected Sheets liga uma planilha do Google Sheets a dados do BigQuery, o data warehouse do Google Cloud. Nessas planilhas, o Gemini agora responde perguntas consultando o conjunto completo no BigQuery, aceita perguntas de acompanhamento e monta painéis: apresenta um plano e cria uma aba com fórmulas de banco, tabelas dinâmicas e gráficos conectados e atualizáveis.

O recurso vem ligado por padrão, sem controle de administrador, para quem tem permissão de consultar os dados conectados.

**Na prática (análise):** parte dos relatórios pontuais sai da fila do time de dados. Ao mesmo tempo, mais gente passa a consultar dados sensíveis, então vale revisar as permissões no BigQuery antes do rollout.

**Disponibilidade e limites:** rollout gradual a partir de 19/10, em até 15 dias, nos canais Rapid Release e Scheduled Release. Planos: Business Standard e Plus, Enterprise Standard e Plus, Google AI Pro e Ultra, Google AI Pro for Education e AI Expanded Access.

**Fontes (data):** [Gemini no Google Sheets com dados do BigQuery, Google Workspace Updates](https://workspaceupdates.googleblog.com/2026/10/analyze-bigquery-data-using-natural-language-with-Gemini-in-Google-Sheets.html) (19/10/2026)

## 8. Microsoft Foundry: ferramenta de automação de navegador para agentes entra em GA

Microsoft · 19/10/2026

**O que mudou:** a Browser Automation Tool do Microsoft Foundry entrou em GA. Ela dá ao agente um navegador gerenciado, baseado em Playwright Workspaces, para navegar, ler páginas, preencher formulários e executar fluxos de várias etapas a partir de instruções em linguagem natural.

Funciona com prompt agents, hosted agents (inclusive os do Microsoft Agent Framework) e o harness do GitHub Copilot. Alcança sites públicos e aplicações privadas atrás de uma VNet do Azure e é exposta por Toolboxes, com endpoint compatível com MCP (Model Context Protocol, o protocolo aberto para conectar ferramentas a agentes). Inclui Live View, Take control, aprovação antes de ações sensíveis, Entra e Azure RBAC.

**Na prática (análise):** a ferramenta atende sistemas sem API, como portais de fornecedor e aplicações legadas, e é uma alternativa gerenciada a manter navegadores headless. O risco de injeção de prompt pelo conteúdo das páginas continua, e a própria Microsoft recomenda tratar a web como não confiável e exigir aprovação humana.

**Disponibilidade e limites:** GA, sem preço no post. O Playwright Workspace é provisionado à parte.

**Fontes (data):** [Browser Automation Tool em GA, Microsoft Foundry Blog](https://devblogs.microsoft.com/foundry/browser-automation-tool-ga/) (19/10/2026)

## 9. Amazon ECS Gateway: ingress gerenciado para serviços no ECS

AWS · 20/10/2026

**O que mudou:** o Amazon ECS é o serviço da AWS para rodar containers, e ingress é a entrada do tráfego externo até esses serviços. O ECS Gateway é um recurso novo que provisiona e gerencia Application Load Balancers (ALB) e os recursos de apoio na conta do cliente.

O time de plataforma define os padrões de rede uma vez no gateway e o associa a um ou mais clusters. Os times de aplicação só fazem opt-in, pelo parâmetro gateway connector, via console, CLI, API, SDKs ou CloudFormation.

O roteamento é por host, com até 25 serviços compartilhando um ALB e um hostname DNS único por serviço. O ECS cuida do ciclo de vida: cria o primeiro ALB quando o primeiro serviço se conecta, adiciona outros quando a capacidade é atingida e remove os que não são mais necessários. As métricas padrão do ALB ficam no CloudWatch, junto com a saúde dos targets do ELB.

**Na prática (análise):** o recurso reduz o trabalho repetitivo de montar ALB, target groups e regras para cada serviço e dá ao time de plataforma um ponto central de governança da entrada. Compartilhar um ALB entre até 25 serviços tende a cortar o custo de load balancer em ambientes com muitos serviços pequenos.

**Disponibilidade e limites:** serviços ECS em modo de rede awsvpc, em todos os launch types, em todas as regiões comerciais da AWS, incluindo São Paulo. Não há custo adicional; paga-se só a infraestrutura provisionada.

**Fontes (data):** [Amazon ECS Gateway](https://aws.amazon.com/about-aws/whats-new/2026/10/announcing-amazon-ecs-gateway/) (20/10/2026)

## 10. Google Cloud: Confidential G4 com GPUs NVIDIA RTX PRO 6000 Blackwell entra em GA

Google e NVIDIA · 21/10/2026

**O que mudou:** computação confidencial é a proteção dos dados também durante o processamento, além do armazenamento e do tráfego. O Confidential Computing chegou em GA às instâncias G4 com NVIDIA RTX PRO 6000 Blackwell Server Edition, integrado ao AI Hypercomputer. Está em 36 zonas, em vários modelos de consumo, em VMs do Compute Engine e nós do GKE.

A proteção usa chaves de hardware não exportáveis, atestação remota verificável e criptografia transparente de memória. Pesos, prompts e saídas ficam protegidos inclusive de administradores do host, do hypervisor e de acesso do provedor. Tudo roda com imagens Ubuntu padrão, drivers NVIDIA e bibliotecas CUDA-X, sem refatoração. O suporte ao Confidential Space, que permite compartilhar dados de forma segura entre partes, chega ao GA "nas próximas semanas", segundo o Google.

**Na prática (análise):** abre caminho para inferência com dados sensíveis ou com modelos proprietários em GPU na nuvem, sem reescrever a aplicação. É útil em saúde, em finanças e quando o modelo é propriedade intelectual de terceiro.

**Disponibilidade e limites:** GA em 36 zonas, que o post não lista. O Confidential Space ainda está em rollout, e o post não traz preço.

**Fontes (data):** [Confidential G4 em GA, Google Cloud Blog](https://cloud.google.com/blog/topics/ai-infrastructure/confidential-g4-gpus-are-ga/) (21/10/2026)

## O que levar desta semana

Para quem roda agentes na AWS, três mudanças tiram trabalho do código: o fallback de modelo no AgentCore Gateway, o JSON garantido por schema nos modelos Claude do Bedrock e o Grounding Standard no Guardrails. Antes de adotar, confira a região e o que continua com você. A busca web com filtros e o Grounding Standard não estão em São Paulo, e as saídas estruturadas não aplicam na geração os limites numéricos nem os de tamanho.

Em São Paulo, o Amazon ECS Gateway é o recurso da semana que já dá para testar, em serviços com modo de rede awsvpc. As vozes Leo e Carolina do Polly atendem o português do Brasil, mas rodam fora do país, então latência e residência de dados entram na conta.

Em segurança, o Continuum começa no modo Learn, que só propõe correções, e na automação de navegador do Foundry a própria Microsoft recomenda exigir aprovação humana. No Google, o Confidential G4 já está em GA em 36 zonas, a busca com RAG no GDC air-gapped segue em preview e o Gemini no Sheets chega ligado por padrão, o que pede uma revisão das permissões no BigQuery. O TorchNeuron, em beta pública, merece um teste com modelo real antes de qualquer conta de economia.

### Referências

- AgentCore Gateway com InvokeModel e fallback (22/10/2026): https://aws.amazon.com/about-aws/whats-new/2026/10/agentcore-gateway-invokemodel-fallback/
- AWS Continuum for code vulnerabilities em GA (22/10/2026): https://aws.amazon.com/about-aws/whats-new/2026/10/aws-continuum-for-code-vulnerabilities-is-now-generally-available
- Busca web do Bedrock com filtros de domínio e localização (23/10/2026): https://aws.amazon.com/about-aws/whats-new/2026/10/bedrock-web-search-domain-user-location/
- Prompt shortening no Advanced Prompt Optimization (20/10/2026): https://aws.amazon.com/about-aws/whats-new/2026/10/bedrock-prompt-optimization-shortening/
- Nível Standard no contextual grounding do Guardrails (20/10/2026): https://aws.amazon.com/about-aws/whats-new/2026/10/bedrock-guardrails-grounding-standard/
- Saídas estruturadas para modelos Claude no Bedrock, AWS ML Blog (19/10/2026): https://aws.amazon.com/blogs/machine-learning/structured-outputs-for-anthropic-claude-models-on-amazon-bedrock/
- Histórico de documentação do Amazon Bedrock: https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-ug-doc-history.html
- TorchNeuron, PyTorch Blog (19/10/2026): https://pytorch.org/blog/introducing-torchneuron-native-pytorch-backend-for-aws-trainium/
- Amazon Polly Generative (20/10/2026): https://aws.amazon.com/about-aws/whats-new/2026/10/polly-generative/
- Gemini no GDC air-gapped com RAG gerenciado, Google Cloud Blog (20/10/2026): https://cloud.google.com/blog/topics/hybrid-cloud/managed-rag-search-inside-the-sovereign-perimeter-gemini-on-gdc-enterprise-search
- Gemini no Google Sheets com BigQuery, Google Workspace Updates (19/10/2026): https://workspaceupdates.googleblog.com/2026/10/analyze-bigquery-data-using-natural-language-with-Gemini-in-Google-Sheets.html
- Browser Automation Tool em GA, Microsoft Foundry Blog (19/10/2026): https://devblogs.microsoft.com/foundry/browser-automation-tool-ga/
- Amazon ECS Gateway (20/10/2026): https://aws.amazon.com/about-aws/whats-new/2026/10/announcing-amazon-ecs-gateway/
- Confidential G4 em GA, Google Cloud Blog (21/10/2026): https://cloud.google.com/blog/topics/ai-infrastructure/confidential-g4-gpus-are-ga/
