+++
title = 'Radar de Cloud | Semana 42 de 2026'
description = 'As 10 notícias de cloud de 12 a 18/10/2026: Lambda Web Functions, durable functions, EC2 T8i em São Paulo, Azure Enclave e mais, com fontes e limites.'
date = '2026-10-19T08:00:00-03:00'
lastmod = '2026-10-19T08:00:00-03:00'
slug = 'radar-cloud-semana-42-2026'
postId = '3fb0e477-98b0-81bf-b922-feb40fb2accc'
draft = false
categorias = ['Cloud']
tags = ['cloud', 'aws', 'azure', 'google-cloud', 'serverless', 'segurança']
comments = true
+++

Esta edição cobre a semana ISO 42 de 2026, de 12 a 18 de outubro, no horário de Brasília. São dez novidades de AWS, Microsoft Azure e Google Cloud, todas com fonte oficial e data dentro desse recorte.

A AWS concentrou seis delas, a maior parte em serverless e operação. O Lambda ganhou um novo tipo de função que atende HTTP diretamente, as durable functions passaram a aceitar dez vezes mais operações por execução e o failover entre Regiões ganhou novas checagens. Para quem usa São Paulo, chegou a família T8i do EC2, mas Web Functions, AWS Transform e a busca web do AgentCore ainda não estão na Região. A Microsoft anunciou um chip de IA com produção prevista para 2027, colocou um serviço de isolamento em disponibilidade geral e apresentou uma especificação aberta de HSM. O Google Cloud tem a mudança que já está valendo: desde 15/10, integrações novas no Application Integration exigem uma identidade explícita de execução.

Em cada item, o trecho "Na prática" é análise editorial. O restante segue o que dizem as fontes.

## 1. AWS Lambda Web Functions, com CloudFront como porta de entrada

Provedor: AWS. Data: 12/10/2026.

O AWS Lambda é o serviço de funções serverless da AWS: você envia o código e a plataforma cuida dos servidores. A novidade é um novo primitivo, as Web Functions, em que o código atende HTTP diretamente. A função escuta numa porta e pode usar Express ou Hono sem adaptador.

A cobrança muda junto. Você paga pela CPU ativa e pela memória mantida, e a CPU ociosa, enquanto a função espera um banco ou um serviço externo, não é cobrada. Um ambiente quente (uma instância da função já inicializada) atende várias requisições simultâneas, com streaming HTTP nativo, VPC e roteamento multi-Região. As funções atuais passam a se chamar "Lambda Event Functions". Só muda o nome, sem necessidade de redeploy.

No mesmo dia, o Amazon CloudFront, a CDN da AWS, passou a aceitar Web Functions como origem, com OAC (Origin Access Control, que restringe o acesso à origem), WAF (firewall de aplicação web) e domínio próprio, sem custo extra.

Na prática (análise): o Lambda fica mais perto do Cloud Run, o serviço do Google Cloud que executa contêineres atendendo HTTP. Dá para servir SSR (páginas renderizadas no servidor), APIs com streaming e endpoints de inferência sem API Gateway nem adaptadores. Em APIs que passam muito tempo esperando I/O, mudam a arquitetura e o custo.

Disponibilidade e limites: disponível desde 12/10, sem rótulo de preview nem de GA no anúncio da AWS. Só Node.js, nas Regiões us-east-1, us-east-2, us-west-2, Tóquio e Irlanda. Ainda não chegou a São Paulo.

Fontes: [AWS Lambda Web Functions](https://aws.amazon.com/about-aws/whats-new/2026/10/aws-lambda-web-functions/) e [CloudFront aceita Lambda Web Functions como origem](https://aws.amazon.com/about-aws/whats-new/2026/10/cloudfront-lambda-web-functions-origin/), ambos de 12/10/2026.

## 2. Lambda durable functions: 10x mais operações, SDK Go GA e GovCloud

Provedor: AWS. Datas: 13/10 (limites), 15/10 (SDK Go) e 16/10/2026 (GovCloud).

As durable functions são funções Lambda que conduzem processos de várias etapas e guardam o progresso em checkpoints, que são registros do estado da execução. O limite de operações duráveis por execução subiu de 3.000 para 30.000, e o checkpoint passou de 256 KB para 1 MB.

Em 15/10, o SDK Durable Execution para Go ficou GA (disponibilidade geral), com teste local via durabletest e o analisador durablelint. Em 16/10, as durable functions chegaram às Regiões GovCloud (US).

Na prática (análise): workflows longos e agentes com milhares de chamadas de modelo ou ferramenta passam a caber numa execução só. Em casos code-first, em que o fluxo é escrito como código, isso concorre com o AWS Step Functions, o serviço de orquestração de workflows da AWS.

Disponibilidade e limites: os novos limites e o SDK Go estão em GA. As Regiões GovCloud (US) foram adicionadas.

Fontes: [aumento dos limites](https://aws.amazon.com/about-aws/whats-new/2026/10/aws-lambda-durable-gen-limit-increase/) (13/10/2026), [SDK para Go](https://aws.amazon.com/about-aws/whats-new/2026/10/aws-lambda-durable-go-sdk-support/) (15/10/2026) e [chegada ao GovCloud](https://aws.amazon.com/about-aws/whats-new/2026/10/durablefunctions-govcloud/) (16/10/2026).

## 3. ARC Region switch ganha quatro capacidades

Provedor: AWS. Data: 14/10/2026.

O Application Recovery Controller (ARC) é o serviço da AWS para recuperar aplicações depois de uma falha. O Region switch é a parte que orquestra a troca entre a Região primária e a Região standby num plano de recuperação de desastres (DR). Ele ganhou quatro capacidades:

- um bloco de execução para o Systems Manager Run Command, que executa comandos nas instâncias;
- payloads no bloco de Lambda customizado;
- checagem de paridade de service quotas (os limites de uso de cada serviço na conta) entre a primária e a standby, com pedido automático de aumento;
- espera pela saúde do target group depois de escalar ECS ou Auto Scaling Groups (ASG).

Na prática (análise): as mudanças atacam duas falhas clássicas de DR multi-Região, que são quota insuficiente e tráfego mandado para capacidade que ainda não está saudável.

Disponibilidade e limites: GA nas Regiões do ARC Region switch.

Fonte: [novidades do ARC Region switch](https://aws.amazon.com/about-aws/whats-new/2026/10/region-switch-target-health-ssm-lambda/), 14/10/2026.

## 4. Bedrock AgentCore: memória de curto prazo por consumo e Web Search em mais Regiões

Provedor: AWS. Datas: 12/10 (preço) e 15/10/2026 (Regiões).

O Amazon Bedrock AgentCore reúne serviços da AWS para executar agentes de IA. A memória de curto prazo dele (STM, de short-term memory) deixa a tarifa por evento e passa a cobrar por consumo: ingestão a US$ 1,00/GB, recuperação a US$ 0,20/GB e armazenamento a US$ 0,10/GB-mês. Na ingestão e na recuperação, o mínimo faturável é 12 KB e o máximo é 64 KB por evento. A memória de longo prazo não muda.

Em 15/10, a ferramenta Web Search do AgentCore chegou a Ohio, Oregon, Sydney e GovCloud (US-West).

Na prática (análise): agentes que gravam muitos eventos pequenos tendem a ficar mais baratos. Vale recalcular o custo dos agentes que já estão em produção.

Disponibilidade e limites: o novo preço vale em todas as Regiões do AgentCore Memory. A Web Search ainda não tem São Paulo na lista anunciada.

Fontes: [preço por consumo da memória do AgentCore](https://aws.amazon.com/about-aws/whats-new/2026/10/agentcore-memory-consumption-based-pricing) (12/10/2026) e [Web Search em mais Regiões](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-bedrock-agentcore/) (15/10/2026).

## 5. EC2 T8i chega a São Paulo

Provedor: AWS. Data: 15/10/2026.

Instâncias burstable têm um nível base de CPU e acumulam créditos para usar em picos de processamento. A família T8i, com Intel Xeon 6 customizado e Nitro de 6ª geração (a base de hardware e virtualização do EC2), está disponível em sa-east-1, a Região de São Paulo.

A AWS fala em até 30% melhor preço-desempenho que a T3 e até 70% mais computação. Os tamanhos vão de nano a medium, com o mesmo sistema de créditos da T3. A t8i.micro e a t8i.small entram no Free Tier.

Na prática (análise): é uma troca direta e de baixo risco para frotas T3 em São Paulo, como bastions, CI e microsserviços pequenos. Confira o preço por hora na Região antes de recomendar a troca.

Disponibilidade e limites: GA em São Paulo e nas outras Regiões listadas no anúncio.

Fonte: [EC2 T8i na América do Sul](https://aws.amazon.com/about-aws/whats-new/2026/10/ec2-t8i-instances-south-america/), 15/10/2026.

## 6. AWS Transform converte código do Azure SDK para o AWS SDK

Provedor: AWS. Data: 16/10/2026.

O AWS Transform é o serviço da AWS que usa agentes para migrar e modernizar código. A conversão de apps .NET cloud-native de Azure para AWS ficou GA em três pares: Azure Functions para Lambda, Blob Storage para S3 e Queue Storage para SQS. A conversão de Cosmos DB para DynamoDB está em preview. O agente gera um plano editável e valida as mudanças.

Na prática (análise): o esforço de migrar .NET de Azure para AWS diminui, mas ainda exige testes funcionais e de desempenho. O ponto mais sensível são os dados, porque sair do Cosmos DB para o DynamoDB muda o modelo.

Disponibilidade e limites: GA, exceto Cosmos DB, que segue em preview. Disponível em 8 Regiões (N. Virginia, Mumbai, Tóquio, Seul, Sydney, Canadá, Frankfurt e Londres), sem São Paulo.

Fonte: [conversão de código de Azure para AWS](https://aws.amazon.com/about-aws/whats-new/2026/10/aws-transform-azure-to-aws-code-conversion/), 16/10/2026.

## 7. Microsoft anuncia o Maia 300 e escala de vários gigawatts para o Azure Maia

Provedor: Microsoft Azure. Data: 12/10/2026.

O Maia 300 é o acelerador de IA de 3ª geração da Microsoft, um chip dedicado a cargas de IA. A empresa espera 40% mais tokens de inferência por megawatt que sistemas com as GPUs líderes e até 7x o throughput em rack do Maia 200, numa configuração de 96 aceleradores.

Os números técnicos divulgados: processo TSMC N2P, memória HBM4 (memória de alta largura de banda) com 18 TB/s, TDP de 950 W e rack de 96 aceleradores com 167 kW e 27,6 TB de HBM. O Maia 200 já está em produção. A partir de 2027, a família Maia vai a implantações de vários gigawatts e passa a ser o principal sistema de inferência dos produtos da Microsoft.

Na prática (análise): é um sinal de queda no custo de inferência no Azure no médio prazo. Não tem efeito imediato, porque a produção é em 2027, e não há preço para clientes.

Disponibilidade e limites: por enquanto é um anúncio. As implantações em produção começam em 2027. Os ganhos de desempenho são expectativa da Microsoft.

Fontes: [anúncio da expansão do Azure Maia](https://blogs.microsoft.com/blog/2026/10/12/microsoft-to-expand-azure-maia-system-to-multi-gigawatt-deployments/), [arquitetura do Maia 300](https://azure.microsoft.com/en-us/blog/deep-dive-into-azure-maia-300-architecture/) e [post de Satya Nadella no X](https://x.com/satyanadella/status/2109631106404487523), todos de 12/10/2026.

## 8. Azure Enclave fica GA

Provedor: Microsoft Azure. Data: 13/10/2026.

O Azure Enclave é um serviço gerenciado para montar ambientes isolados para cargas sensíveis, em Azure e Azure for US Government. Ele segue um modelo "comunidade + enclave": rede isolada por padrão, conexões explícitas, Azure Policy e logging centralizado, com integração ao Sentinel e a outros SIEMs (sistemas que concentram e analisam eventos de segurança).

As acreditações FedRAMP, DoD IL4/5/6 e ICD 503, do governo dos Estados Unidos, ainda estão em andamento.

Na prática (análise): é um padrão pronto para landing zones isoladas em setores regulados. Landing zone é a estrutura inicial de contas, rede e políticas sobre a qual as cargas são implantadas. As certificações citadas ainda não foram concluídas.

Disponibilidade e limites: GA em Azure e Azure Government.

Fonte: [Azure Enclave em disponibilidade geral](https://www.microsoft.com/en-us/microsoft-cloud/blog/us-government/2026/10/13/azure-enclave-is-now-generally-available-managed-workload-isolation-for-government-and-regulated-industries/), 13/10/2026.

## 9. Project Tessera: especificação aberta de HSM integrado (Microsoft, Marvell e Oracle no OCP)

Provedor: Microsoft, com Marvell e Oracle. Data: 13/10/2026.

Um HSM (módulo de segurança de hardware) é o equipamento que guarda chaves criptográficas e executa operações com elas. A Microsoft apresentou o Project Tessera, uma iniciativa aberta de HSM integrado, com Marvell e Oracle, no Open Compute Project (OCP), comunidade que publica especificações abertas de hardware para data centers.

Especificação, protocolos, drivers, firmware e referências de hardware estão no GitHub como open source. A meta é a certificação FIPS 140-3 Nível 3, padrão do governo dos Estados Unidos para módulos criptográficos, com suporte a criptografia pós-quântica (PQC), pensada para resistir a ataques feitos com computadores quânticos. Houve demonstração com o Marvell LiquidSecurity 2, e o projeto também abre um firmware em unikernel para ambientes de computação confidencial, começando por AMD SEV-SNP com OpenVMM.

Na prática (análise): é um movimento para padronizar a raiz de confiança de chaves na nuvem com código auditável, além de abrir um caminho para a PQC. Para clientes, ainda não muda o que se contrata hoje.

Disponibilidade e limites: é uma iniciativa e uma especificação aberta. Não existe um serviço do Azure para contratar. A certificação FIPS 140-3 Nível 3 é um objetivo, ainda não alcançado.

Fonte: [HSM integrado open source no Azure Blog](https://azure.microsoft.com/en-us/blog/advancing-hardware-security-with-open-source-integrated-hsm-technology/), 13/10/2026.

## 10. Google Cloud Application Integration passa a exigir identidade explícita de execução (GCP-2026-068)

Provedor: Google Cloud. Data: boletim GCP-2026-068, publicado em 15/10/2026.

O Application Integration é o serviço do Google Cloud para montar integrações entre sistemas, com gatilhos como agenda ou evento. Uma service account é uma identidade usada por aplicações, e a service account "run-as" é aquela com que a integração executa.

Desde 15/10, integrações novas com gatilho agendado ou por evento não podem ser publicadas nem testadas sem uma service account "run-as". Quem configura precisa do papel Service Account User (permissão iam.serviceAccounts.actAs). As integrações existentes mantêm o comportamento atual por enquanto e entram na mudança numa data posterior, que o Google vai anunciar separadamente, segundo a página de preparação. O boletim está associado à CVE-2026-85298, de severidade High.

Na prática (análise): pipelines que criam integrações sem a service account configurada vão quebrar. Times precisam revisar IaC (infraestrutura como código), permissões e o inventário de integrações antes das próximas fases.

Disponibilidade e limites: obrigatório para integrações novas desde 15/10. As integrações existentes entram depois, em data ainda não anunciada.

Fontes: [boletins de segurança do Application Integration](https://docs.cloud.google.com/application-integration/docs/security-bulletins) (GCP-2026-068, 15/10/2026) e [preparação para as mudanças de autorização](https://docs.cloud.google.com/application-integration/docs/prepare-for-authorization-changes) (atualizada em 13/10/2026).

## O que levar desta semana

A mudança que já está valendo é a do Application Integration. Se o seu time cria integrações agendadas ou por evento no Google Cloud, revise IaC, permissões e o inventário antes das próximas fases.

No Lambda, as Web Functions merecem um teste em APIs Node.js que passam muito tempo esperando I/O, desde que a carga possa rodar numa das cinco Regiões atendidas. As durable functions, com o limite de 30.000 operações, passam a comportar workflows e agentes bem maiores numa execução.

Em São Paulo, a T8i é a candidata para substituir instâncias T3, depois de conferir o preço por hora. Para quem mantém DR multi-Região, as novas checagens do ARC Region switch cobrem quota e saúde da capacidade antes de mandar tráfego. No AgentCore, o novo preço da memória de curto prazo pede um recálculo de custo.

Do lado da Microsoft, o Azure Enclave já está em GA, com as acreditações ainda em andamento. Maia 300 e Project Tessera ficam para acompanhar: o primeiro tem produção prevista para 2027, e o segundo é uma especificação aberta, sem serviço para contratar.

## Referências

- AWS Lambda Web Functions (12/10/2026): https://aws.amazon.com/about-aws/whats-new/2026/10/aws-lambda-web-functions/
- CloudFront com Lambda Web Functions como origem (12/10/2026): https://aws.amazon.com/about-aws/whats-new/2026/10/cloudfront-lambda-web-functions-origin/
- Lambda durable functions, novos limites (13/10/2026): https://aws.amazon.com/about-aws/whats-new/2026/10/aws-lambda-durable-gen-limit-increase/
- Lambda durable functions, SDK para Go (15/10/2026): https://aws.amazon.com/about-aws/whats-new/2026/10/aws-lambda-durable-go-sdk-support/
- Lambda durable functions no GovCloud (16/10/2026): https://aws.amazon.com/about-aws/whats-new/2026/10/durablefunctions-govcloud/
- ARC Region switch (14/10/2026): https://aws.amazon.com/about-aws/whats-new/2026/10/region-switch-target-health-ssm-lambda/
- AgentCore Memory, preço por consumo (12/10/2026): https://aws.amazon.com/about-aws/whats-new/2026/10/agentcore-memory-consumption-based-pricing
- AgentCore Web Search em mais Regiões (15/10/2026): https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-bedrock-agentcore/
- EC2 T8i na América do Sul (15/10/2026): https://aws.amazon.com/about-aws/whats-new/2026/10/ec2-t8i-instances-south-america/
- AWS Transform, conversão de Azure para AWS (16/10/2026): https://aws.amazon.com/about-aws/whats-new/2026/10/aws-transform-azure-to-aws-code-conversion/
- Microsoft, expansão do Azure Maia (12/10/2026): https://blogs.microsoft.com/blog/2026/10/12/microsoft-to-expand-azure-maia-system-to-multi-gigawatt-deployments/
- Azure Blog, arquitetura do Maia 300 (12/10/2026): https://azure.microsoft.com/en-us/blog/deep-dive-into-azure-maia-300-architecture/
- Satya Nadella no X (12/10/2026): https://x.com/satyanadella/status/2109631106404487523
- Azure Enclave GA (13/10/2026): https://www.microsoft.com/en-us/microsoft-cloud/blog/us-government/2026/10/13/azure-enclave-is-now-generally-available-managed-workload-isolation-for-government-and-regulated-industries/
- Project Tessera, Azure Blog (13/10/2026): https://azure.microsoft.com/en-us/blog/advancing-hardware-security-with-open-source-integrated-hsm-technology/
- Application Integration, boletins de segurança (GCP-2026-068, 15/10/2026): https://docs.cloud.google.com/application-integration/docs/security-bulletins
- Application Integration, preparação para as mudanças de autorização (atualizada em 13/10/2026): https://docs.cloud.google.com/application-integration/docs/prepare-for-authorization-changes
