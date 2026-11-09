+++
title = 'Radar de Cloud | Semana 45 de 2026'
description = 'Dez novidades verificadas: segurança de AMIs, migração para Iceberg, SLA do Cognito, Kafka no Lambda e banco para agentes.'
date = '2026-11-09T07:10:00-03:00'
lastmod = '2026-11-09T08:05:00-03:00'
slug = 'radar-cloud-semana-45-2026'
draft = false
categorias = ['Cloud']
tags = ['cloud', 'aws', 'google-cloud', 'segurança', 'dados']
comments = true
+++
Entre 2 e 8 de novembro, a AWS concentrou os anúncios que mexem com rotina de operação: varredura de imagens antes do uso, inventário de software, controle de custo por snapshot e SLA de autenticação. O Google Cloud entrou com um banco PostgreSQL pensado para agentes de código.

Esta edição reúne dez novidades conferidas nas páginas originais. Cada item separa o que mudou, a análise e os limites.

## Cobertura e destaques

- Semana ISO 45 de 2026: de 02/11 às 00h00 até 08/11 às 21h, em America/Sao_Paulo. O domingo foi pesquisado até o horário de fechamento desta edição.
- Verificação de disponibilidade em 08/11/2026. A data de cada item é a do anúncio na página oficial.
- Destaques: Inspector para AMIs, migração gerenciada de Hive para Iceberg, SLA de 99,99% no Cognito Plus e AlloyDB Express.
- Descartados como ruído: expansões de Região, GovCloud e novas famílias de instância, salvo efeito claro para clientes.

## 1. Amazon Inspector passa a escanear AMIs do EC2

Anúncio: 02/11/2026.

O que mudou. O Inspector agora identifica vulnerabilidades em AMIs sem lançar instâncias e sem instalar software. É possível manter avaliação contínua do catálogo de AMIs ou fazer varreduras pontuais no console do EC2, em uma conta ou na organização. Os resultados também chegam ao Security Hub. A partir deles, a configuração Allowed AMIs permite definir critérios de segurança que as AMIs precisam cumprir para ser usadas, aplicada à organização com Declarative Policies. Pipelines do EC2 Image Builder podem integrar a varredura e bloquear a distribuição de AMIs fora do padrão.

Na prática (análise). A checagem sai do momento do deploy e vai para a origem da imagem. Para quem mantém AMIs de ouro, o ponto de partida é ligar a varredura contínua no catálogo e decidir o critério mínimo do Allowed AMIs.

Disponibilidade e limites. Disponível em todas as Regiões comerciais onde o Inspector existe. A cobrança segue o Inspector; os valores estão na página de preços do serviço e não constam do anúncio.

Fonte: [Inspector para AMIs, AWS](https://aws.amazon.com/about-aws/whats-new/2026/11/ec2-amis-scanned-through-inspector/)

## 2. S3 Tables migra tabelas Hive para Iceberg de forma gerenciada

Anúncio: 04/11/2026.

O que mudou. O S3 Tables passa a migrar tabelas Apache Hive para Apache Iceberg por uma operação via API. O serviço cuida de validação, checagem de compatibilidade, conversão de tipos, recompressão e compactação, e gera um relatório de compatibilidade antes de copiar dados. É possível sincronizar quantas vezes for preciso sem parar as escritas na tabela de origem, exceto por alguns minutos durante o cutover.

Na prática (análise). A migração deixa de exigir pipelines próprios. O relatório de compatibilidade é o melhor primeiro passo para estimar o esforço em um data lake legado.

Disponibilidade e limites. Disponível em dez Regiões (N. Virginia, Ohio, Oregon, Mumbai, Singapura, Sydney, Tóquio, Frankfurt, Irlanda e Estocolmo). No lançamento, só tabelas Hive em Parquet registradas no AWS Glue, na mesma conta e Região.

Fontes: [Anúncio no blog da AWS](https://aws.amazon.com/blogs/aws/amazon-s3-tables-now-offer-managed-migration-of-apache-hive-tables-to-apache-iceberg/) · [Página What's New](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-s3-tables-managed-migration-hive-to-iceberg/)

## 3. DynamoDB ganha bulk put items a partir do S3

Anúncio: 05/11/2026.

O que mudou. O DynamoDB agora grava dados do S3 em tabelas existentes sem pipeline próprio e sem gerenciar capacidade da tabela. Cada item aceita sua própria condition expression, o que permite gravações só de inserção ou protegidas por versão. A camada Standard atende a maioria dos casos; a Accelerated, os mais urgentes. Os usos citados são atualizações diárias, enriquecimento de catálogo, backfills e migrações.

Na prática (análise). Para cargas periódicas que hoje passam por Lambda ou Glue, vale comparar custo e complexidade. A condição por item reduz o risco de sobrescrever dados mais novos.

Disponibilidade e limites. A camada Standard está em todas as Regiões comerciais e no GovCloud (US); a lista da Accelerated está em página própria. O anúncio não traz preços.

Fonte: [Bulk put items, AWS](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-dynamodb-now-supports-bulk-put-items/)

## 4. Security Hub ganha inventário de SBOM

Anúncio: 06/11/2026.

O que mudou. O Security Hub passa a mostrar um inventário contínuo, para toda a organização, dos pacotes e aplicações instalados em instâncias EC2, imagens do ECR e funções Lambda. Ele usa os SBOMs que o Inspector já gera, com lista por pacote, versão, tipo e número de recursos afetados, filtros por conta e Região e consulta pela API.

Na prática (análise). Quando sai uma vulnerabilidade em uma biblioteca, o inventário permite saber onde ela está sem varrer ambiente por ambiente.

Disponibilidade e limites. Está incluído no Security Hub Essentials sem custo adicional e não exige nova configuração, mas depende de o Inspector estar ativo, e o Inspector tem preço próprio. Disponível nas Regiões do Security Hub.

Fonte: [SBOM no Security Hub, AWS](https://aws.amazon.com/about-aws/whats-new/2026/11/security-hub-sbom-inventory/)

## 5. Cognito Plus sobe o SLA para 99,99%

Anúncio: 05/11/2026, com efeito desde 01/11/2026.

O que mudou. O compromisso de disponibilidade mensal do Amazon Cognito subiu de 99,9% para 99,99% em user pools do plano Plus. Pools já no Plus entram automaticamente. Essentials e Lite continuam em 99,9%.

Na prática (análise). Em um mês de 30 dias, 99,9% admite cerca de 43 minutos de indisponibilidade e 99,99% cerca de 4 minutos (conta feita aqui). Para sistemas em que o login é caminho crítico, a decisão passa a pesar o custo do Plus contra esse compromisso, que é contratual e não uma garantia técnica.

Disponibilidade e limites. A troca de plano pode ser feita por console, CLI ou SDKs. O Plus inclui proteção contra ameaças, como autenticação adaptativa. O anúncio não informa preços; os termos e exclusões estão no SLA do Cognito.

Fonte: [SLA do Cognito Plus, AWS](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-cognito-sla-update/)

## 6. Lambda ganha filas para Kafka autogerenciado

Anúncio: 02/11/2026.

O que mudou. Event source mappings de Kafka autogerenciado, incluindo ofertas gerenciadas como o Confluent Cloud, passam a ter o modo Queue, baseado em share groups. Vários event pollers podem consumir da mesma partição, cada um com até 10 invocações simultâneas, e o paralelismo deixa de depender do número de partições.

Na prática (análise). Serve para eventos independentes em que a velocidade importa mais que a ordem, como codificação de mídia, notificações e telemetria. Antes era preciso aumentar partições ou usar outra fila.

Disponibilidade e limites. O modo Queue não preserva a ordem da partição. Exige cluster Kafka com share groups, como o Apache Kafka 4.2 ou superior. Disponível nas Regiões comerciais com Kafka ESM autogerenciado, com preço padrão do Lambda e cobrança de EPU no modo provisionado.

Fonte: [Filas para Kafka no Lambda, AWS](https://aws.amazon.com/about-aws/whats-new/2026/11/aws-lambda-queue-kafka-esm/)

## 7. EC2 publica a métrica ImdsV1Enabled

Anúncio: 05/11/2026.

O que mudou. O EC2 passa a publicar no CloudWatch a métrica ImdsV1Enabled, que mostra quais instâncias ainda aceitam o IMDSv1. Ela permite montar painéis e alarmes para acompanhar a migração para o IMDSv2 entre contas e Regiões.

Na prática (análise). O alarme serve como fila de trabalho da migração. Instâncias com IMDSv1 ativo entram na lista de remediação em vez de depender de scripts próprios.

Disponibilidade e limites. Disponível em todas as Regiões, sem custo adicional.

Fonte: [Métrica ImdsV1Enabled, AWS](https://aws.amazon.com/about-aws/whats-new/2026/11/ec2-imdsv1enabled-cloudwatch-metric/)

## 8. RDS mostra o custo de cada snapshot

Anúncio: 02/11/2026.

O que mudou. Antes, o custo de snapshots do RDS aparecia agregado por instância no Cost and Usage Report e no Cost Explorer. Agora, com tags de alocação de custo nos snapshots, é possível ver quanto cada um custa.

Na prática (análise). Ajuda a achar snapshots manuais esquecidos e a decidir política de retenção com número na mão.

Disponibilidade e limites. Ativado por padrão em todos os snapshots, sem custo adicional, para todas as engines do RDS nas Regiões comerciais e no GovCloud (US).

Fonte: [Cobrança por snapshot, AWS](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-rds-per-snapshot-billing/)

## 9. AlloyDB Express entra em preview com scale-to-zero

Anúncio: 04/11/2026.

O que mudou. O Google Cloud lançou em preview o AlloyDB Express, versão do AlloyDB para PostgreSQL voltada a desenvolvedores e agentes de código. O banco é criado em menos de dois segundos por gcloud, API REST, MCP, Terraform ou console, e pausa sozinho após 15 minutos sem uso, voltando em segundos quando chega uma consulta.

Na prática (análise). Bancos efêmeros para testes de CI e protótipos deixam de custar compute parado. O Google diz que o ambiente pode crescer até produção, e isso precisa ser validado quando o serviço sair do preview.

Disponibilidade e limites. Em preview, com 50 CUs gratuitos por mês. Compute ativo: US$ 0,115 por CU-hora, cobrado por segundo; pausado: US$ 0,00; armazenamento: US$ 0,30 por GB-mês.

Fonte: [AlloyDB Express, Google Cloud](https://cloud.google.com/blog/products/databases/introducing-alloydb-express-for-rapid-testing-and-prototyping/)

## 10. Amazon Q Developer no console agora é o AWS assistant

Anúncio: 05/11/2026.

O que mudou. O Amazon Q Developer no AWS Management Console e nos apps móveis passa a se chamar AWS assistant, com as mesmas orientações e ações sobre a conta.

Na prática (análise). É uma mudança de nome. Materiais internos, treinamentos e políticas que citam o Q Developer no console podem precisar de ajuste.

Disponibilidade e limites. Disponível globalmente e, hoje, gratuito. Assinantes do Q Developer Pro mantêm os recursos do plano. O anúncio trata do console e dos apps móveis, não de outras superfícies do produto.

Fonte: [AWS assistant, AWS](https://aws.amazon.com/about-aws/whats-new/2026/11/q-developer-renamed-aws-assistant/)

## O que priorizar nesta semana

Em segurança, ligue a varredura de AMIs, ative o inventário de SBOM onde o Inspector já roda e acompanhe a métrica de IMDSv1. Em custo, ative as tags nos snapshots do RDS e revise retenção. Em dados, rode o relatório de compatibilidade do S3 Tables antes de planejar uma migração para Iceberg.

## Limitações desta edição

- Itens do Azure Updates não entraram: as páginas oficiais renderizam por JavaScript e não puderam ser lidas. Além disso, a retirada do Azure Fluid Relay aparece com data diferente no feed (2 de junho de 2027) e em um espelho de terceiros (2 de fevereiro de 2027); a data precisa ser confirmada na fonte da Microsoft antes de qualquer citação.
- O lançamento do Compute Engine API multi-versioning (Google Cloud, 04/11) foi conferido, mas ficou fora do corte de dez itens.
- Os feeds do Google Cloud Blog, AWS Machine Learning Blog e GitHub são curtos e podem não cobrir toda a semana.
- Cloud não tem radar diário; esta edição partiu dos feeds e da pesquisa direta nas fontes.
