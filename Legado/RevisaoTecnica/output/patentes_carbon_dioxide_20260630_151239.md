# 📋 Relatório de Análise de Patentes

**Data:** 30/06/2026 15:12:39
**Busca:** `carbon dioxide`
**Total de patentes encontradas:** 19
**Modelo de avaliação:** gemma3:4b

---

## 🧭 Protocolo Metodológico

- **Versão:** 1.0
- **Fontes:** Google Patents, Patentscope
- **Etapas:** identification, deduplication, screening, manual_review, full_extraction, synthesis
- **Threshold inclusão:** 0.0
- **Threshold revisão:** 0.0
- **Máximo em revisão manual:** 20

**Critérios de inclusão**
- Alinhamento claro com a query ou seus sinônimos técnicos.
- Documento com título, resumo ou snippet suficientes para análise.
- Potencial técnico relevante para o domínio pesquisado.

**Critérios de exclusão**
- Documentos sem relação técnica com a query.
- Duplicatas de outra fonte ou publicação equivalente.
- Registro sem metadados mínimos para avaliação.

## 📐 Cobertura e Seleção

- **Total bruto coletado:** 19
- **Patentes únicas:** 19
- **Duplicatas removidas:** 0
- **Triadas:** 19
- **Incluídas:** 6
- **Em revisão manual:** 6
- **Excluídas:** 7
- **Extrações completas:** 12
- **Sem abstract/snippet:** 2
- **Sem ID:** 0
- **Identidade por conteúdo:** 0
- **Identidade fallback:** 0
- **Duplicatas por família removidas:** 0
- **Falhas de triagem LLM:** 0
- **Falhas totais LLM:** 0

## 🧭 Fluxo PRISMA-Like

- **Identificação:** 19 bruto(s), 19 único(s), 0 duplicata(s) removida(s)
- **Triagem:** 19 triado(s), 6 incluído(s), 6 em revisão, 7 excluído(s)
- **Elegibilidade:** 12 extração(ões) completa(s), 6 revisão(ões) manual(is), 0 adiada(s)
- **Cobertura:** 2 sem abstract/snippet, 0 sem ID
- **Síntese:** 12 registro(s) analisado(s)

## 🧩 Síntese Temática

### Engenharia Química / Materiais

- **Patentes:** 1
- **Score médio:** 8.20/10
- **Confiança média:** 0.90
- **Evidências citadas:** 2
- **IDs:** US12202743B2

### Economic Optimization

- **Patentes:** 1
- **Score médio:** 8.10/10
- **Confiança média:** 0.95
- **Evidências citadas:** 2
- **IDs:** US12478916B2

### Química, Catálise, Engenharia Química

- **Patentes:** 1
- **Score médio:** 8.10/10
- **Confiança média:** 0.95
- **Evidências citadas:** 2
- **IDs:** US20240059978A1

### Engenharia Química / Tecnologias de Captura de Carbono

- **Patentes:** 1
- **Score médio:** 8.10/10
- **Confiança média:** 0.95
- **Evidências citadas:** 2
- **IDs:** WO2021239747A1

### Engenharia Química / Processamento de Gases

- **Patentes:** 1
- **Score médio:** 8.00/10
- **Confiança média:** 0.95
- **Evidências citadas:** 1
- **IDs:** US20230191322A1

### Engenharia Química / Engenharia Ambiental

- **Patentes:** 1
- **Score médio:** 7.70/10
- **Confiança média:** 0.90
- **Evidências citadas:** 2
- **IDs:** WO2024208966A1

## 🧠 Contexto Compartilhado

- **Top patentes no contexto:** 5
- **Clusters no contexto:** 6
- **Roteamento agregado:** 3 rota(s)
- **Slots ativos:** N/A

## ⏱️ Métricas por Etapa

| Etapa | Status | Duração | Itens | Detalhes |
|---|---|---:|---:|---|
| setup | ok | 2.48s | 1 | Verificação do modelo Ollama |
| search | ok | 93.08s | 19 | 19 patentes únicas após dedupe |
| screening | ok | 0.01s | 19 | 6 incluídas, 6 revisão |
| comparative_analysis | ok | 6.56s | 19 | Síntese comparativa gerada |
| whitespace_analysis | ok | 0.00s | 12 | Whitespace analysis estruturada gerada |
| reporting | ok | 0.01s | 19 | Relatórios Markdown e JSON |
| finalization | ok | 0.00s | 8 | Persistência de artefatos e estado |

## 🌐 Diagnósticos de Coleta

### GooglePatents

- Nenhum sinal relevante detectado.

### Patentscope

- Nenhum sinal relevante detectado.

### EPO

- **config_missing**: EPO_CONSUMER_KEY ou EPO_CONSUMER_SECRET não configurados.

## 📡 Telemetria do LLM

- **Degradado:** não
- **Falhas totais:** 0
- **Falhas consecutivas:** 0

### healthcheck

- **Chamadas:** 1
- **Sucessos:** 1
- **Falhas:** 0
- **Retries:** 0
- **Cache hits:** 0
- **Pulos por degradação:** 0
- **Latência média:** 2.483s
- **Latência máxima:** 2.483s

### screening

- **Chamadas:** 19
- **Sucessos:** 19
- **Falhas:** 0
- **Retries:** 0
- **Cache hits:** 19
- **Pulos por degradação:** 0
- **Latência média:** 0.0s
- **Latência máxima:** 0.0s

### rerank

- **Chamadas:** 6
- **Sucessos:** 6
- **Falhas:** 0
- **Retries:** 0
- **Cache hits:** 6
- **Pulos por degradação:** 0
- **Latência média:** 0.0s
- **Latência máxima:** 0.0s

### evaluation

- **Chamadas:** 12
- **Sucessos:** 12
- **Falhas:** 0
- **Retries:** 0
- **Cache hits:** 12
- **Pulos por degradação:** 0
- **Latência média:** 0.0s
- **Latência máxima:** 0.0s

### comparative

- **Chamadas:** 1
- **Sucessos:** 1
- **Falhas:** 0
- **Retries:** 0
- **Cache hits:** 0
- **Pulos por degradação:** 0
- **Latência média:** 6.557s
- **Latência máxima:** 6.557s

## 🔎 Observabilidade Estruturada

### Rotas

- **screen_only**: total=7, include=0, review=0, exclude=7, llm_errors=0
- **deep_extraction**: total=6, include=6, review=0, exclude=0, llm_errors=0
- **manual_review**: total=6, include=0, review=6, exclude=0, llm_errors=0

### Fontes

- **EPO**: bruto=0, duração=0.00s, diagnósticos=config_missing=1
- **GooglePatents**: bruto=9, duração=27.20s, diagnósticos=nenhum
- **Patentscope**: bruto=10, duração=65.88s, diagnósticos=nenhum

### Falhas

- **Erros de execução:** 0
- **Registros com erro de LLM:** 0
- **Falhas totais do LLM:** 0
- **LLM por operação:** comparative(falhas=0, retries=0, skips=0), evaluation(falhas=0, retries=0, skips=0), healthcheck(falhas=0, retries=0, skips=0), rerank(falhas=0, retries=0, skips=0), screening(falhas=0, retries=0, skips=0)
- **Scraper por tipo de sinal:** config_missing=1

## 📊 Resumo Executivo

**Score médio de relevância:** 8.0/10

| # | Patente | Score | Inovação | Domínio |
|---|---------|-------|----------|---------|
| 1 | [US12202743B2](https://patents.google.com/patent/US12202743B2/en) — Direct removal of carbon dioxide from oceanwater based on a ... | 🟢 8.2 (include) | Significativa | Engenharia Química / Materiais |
| 2 | [US12478916B2](https://patents.google.com/patent/US12478916B2/en) — Direct carbon dioxide capture from air | 🟢 8.1 (include) | Incremental | Engenharia Química / Engenharia Ambiental |
| 3 | [US20240059978A1](https://patents.google.com/patent/US20240059978A1/en) — One-step process for the production of hydrocarbons from car... | 🟢 8.1 (include) | Significativa | Química, Catálise, Engenharia Química |
| 4 | [WO2021239747A1](https://patents.google.com/patent/WO2021239747A1/en) — Method for capture of carbon dioxide from ambient air and co... | 🟢 8.1 (include) | Significativa | Engenharia Química / Tecnologias de Captura de Carbono |
| 5 | [US20230191322A1](https://patents.google.com/patent/US20230191322A1/en) — Systems and methods for direct air carbon dioxide capture | 🟢 8.0 (include) | Significativa | Engenharia Química / Processamento de Gases |
| 6 | [WO2024208966A1](https://patents.google.com/patent/WO2024208966A1/en) — Plant and method for capturing carbon dioxide | 🟢 7.7 (include) | Significativa | Engenharia Química / Engenharia Ambiental |
| 7 | [US2665972A](https://patents.google.com/patent/US2665972A/en) — Production of pure carbon dioxide | 🟡 6.5 (review) | Incremental | Processamento de Gases e Termodinâmica |
| 8 | [US8119091B2](https://patents.google.com/patent/US8119091B2/en) — Carbon dioxide capture | 🟡 6.5 (review) | Incremental | Chemical Engineering, Environmental Technology |
| 9 | [US12401048B1](https://patents.google.com/patent/US12401048B1/en) — Metal-carbon dioxide (CO2) battery cell | 🟡 6.5 (review) | Incremental | Eletroquímica, Baterias |
| 10 | [1429678](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135599119&_cid=P21-MR0SB9-98266-1) — APPARATUS FOR SUPPLYING LIQUID
CARBON
DIOXIDE | 🟡 6.5 (review) | Significativa | Controle de Processos, Termodinâmica, Sistemas de Refrigeração |
| 11 | [2047588](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135860928&_cid=P21-MR0SB9-98266-1) — Reclamation of foundry sand | 🟡 6.5 (review) | Incremental | Materiais de Fundição e Processos Recuperativos |
| 12 | [1125505](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135308953&_cid=P21-MR0SB9-98266-1) — Production of
carbon
dioxide
and argon | 🟡 6.5 (review) | Incremental | Chemical Engineering |
| 13 | [1171698](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135354895&_cid=P21-MR0SB9-98266-1) — Dispensing Device | 🔴 0.0 (exclude) | N/A | Dispositivos de Dispensação de Líquidos |
| 14 | [1557123](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135726881&_cid=P21-MR0SB9-98266-1) — METHOD AND APPARATUS FOR REPARING EXTRACTS OF HOPS AND OTHER... | 🔴 0.0 (exclude) | N/A | Processamento de bebidas alcoólicas |
| 15 | [1426573](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135595668&_cid=P21-MR0SB9-98266-1) — WEIGHING MACHINES | 🔴 0.0 (exclude) | N/A | Engenharia de Processos |
| 16 | [1174314](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135357801&_cid=P21-MR0SB9-98266-1) — A Dispensing Device for Gases Under Pressure. | 🔴 0.0 (exclude) | N/A | Engenharia de Fluidos, Instrumentação |
| 17 | [1253973](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135438798&_cid=P21-MR0SB9-98266-1) — LIQUID MOVING SYSTEMS | 🔴 0.0 (exclude) | N/A | Process Control & Instrumentation |
| 18 | [1329637](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135513929&_cid=P21-MR0SB9-98266-1) — TEMPORARY FREEZING OF SOFT OR FLEXIBLE ARTICLES | 🔴 0.0 (exclude) | N/A | Engenharia de Materiais, Refrigeração |
| 19 | [1236064](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135420945&_cid=P21-MR0SB9-98266-1) — IMPROVEMENTS IN OR RELATING TO FIRE EXTINGUISHING COMPOSITIO... | 🔴 0.0 (exclude) | N/A | Extinção de Incêndio |

---

## 🔍 Análise Detalhada das Patentes

### 1. Production of pure carbon dioxide

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_92b6895cc998` |
| **Family ID** | `family:e7e600348e538cf82298836d7987464ddef205c9` |
| **ID** | `US2665972A` |
| **Inventores** | Warren K Lewis, Edwin R Gilliland |
| **Titular** | Standard Oil Development Co |
| **Data** | 1954-01-12 |
| **Fonte** | Google Patents |
| **URL** | [US2665972A](https://patents.google.com/patent/US2665972A/en) |
| **Triagem** | review |
| **Rota** | manual_review |
| **Motivo da rota** | Triagem indicou revisão humana. |
| **Score de Triagem** | 6.7/10 |
| **Score de Relevância** | 6.5/10 |
| **Nível de Inovação** | Incremental |
| **Domínio Técnico** | Processamento de Gases e Termodinâmica |
| **Cluster Temático** | Produção e Purificação de Dióxido de Carbono |
| **Papel do CO2** | produto_químico_principal |
| **Papel do Armazenamento** | não_especificado |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | decomposição_térmica |
| **Fonte/Sumidouro Térmico** | energia_térmica |
| **Foco das Claims** | método_de_produção_de_co2_puro |
| **Categoria de Exclusão** | industrial_heat_adjacent |
| **Confiança** | 0.80 |
| **Rerank Aplicado** | Sim |
| **Motivo do Rerank** | reranked:decision_confirmed |
| **Revisão Manual** | Sim |
| **Erro LLM** | N/A |

**Avaliação do LLM:**
Esta patente descreve um processo para a produção de dióxido de carbono puro, utilizando um método que envolve a decomposição térmica de carbonatos. A invenção se concentra na obtenção de CO2 de alta pureza, embora os detalhes do sistema de armazenamento ou integração termodinâmica sejam limitados.

**Extração Estruturada:**
- **Problema:** A necessidade de produzir dióxido de carbono com alta pureza para aplicações específicas, sem a utilização de métodos convencionais que podem introduzir impurezas.
- **Solução:** A patente propõe um método para a produção de CO2 puro através da decomposição térmica de carbonatos, buscando otimizar o processo para obter um produto com a maior concentração possível de CO2.
- **Maturidade:** Intermediária

**Achados-chave:**
- O processo envolve a decomposição térmica de carbonatos para gerar dióxido de carbono.
- A patente foca na produção de CO2 puro, sem detalhar sistemas de armazenamento ou integração termodinâmica.

**Vantagens alegadas:**
- Produção de dióxido de carbono com alta pureza.
- Possível otimização do processo de decomposição térmica.

**Limitações:**
- Falta de detalhes sobre o sistema de armazenamento ou integração termodinâmica do CO2 produzido.
- Ausência de informações sobre a eficiência do processo em termos de consumo de energia e produção de calor.

**Aplicações potenciais:**
- Produção de dióxido de carbono para aplicações que exigem alta pureza, como refrigeração ou processos químicos.
- Potencial uso em sistemas de armazenamento térmico (embora não explicitamente detalhado).

**Evidências citadas:**
> ‘Production of pure carbon dioxide’ suggests a process involving thermal management.
> The system boundary is defined as ‘process integration’

---

### 2. Direct carbon dioxide capture from air

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_bf9199489578` |
| **Family ID** | `family:450006d06fd5358f368f1f6d3359139d138f6a20` |
| **ID** | `US12478916B2` |
| **Inventores** | Hans De Neve, Wilhelmus Jozef SOPPE, Johannis Alouisius Zacharias Pieterse, Gerard Douwe Elzinga, Cornelis Hendrikus Frijters, Catharina Henriette Maria Van Der Werf |
| **Titular** | Nederlandse Organisatie voor Toegepast Natuurwetenschappelijk Onderzoek TNO |
| **Data** | 2025-11-25 |
| **Fonte** | Google Patents |
| **URL** | [US12478916B2](https://patents.google.com/patent/US12478916B2/en) |
| **Triagem** | include |
| **Rota** | deep_extraction |
| **Motivo da rota** | Há evidência suficiente para extração detalhada. |
| **Score de Triagem** | 9.2/10 |
| **Score de Relevância** | 8.1/10 |
| **Nível de Inovação** | Incremental |
| **Domínio Técnico** | Engenharia Química / Engenharia Ambiental |
| **Cluster Temático** | Economic Optimization |
| **Papel do CO2** | capture_process_stream |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | power_generation |
| **Foco das Claims** | process_integration |
| **Categoria de Exclusão** | N/A |
| **Confiança** | 0.95 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> AbstractThe present invention concerns a device and process for capturing CO2from air. The device comprises (a) a membrane at least partly permeable for air comprising a solid state CO2sorbent; (b) at least one sorption chamber; (c) at least one regeneration chamber; (d) means for transporting the membrane from the sorption chamber to the regeneration chamber and back; (e) an inlet for receiving air located on one end of the membrane and an outlet for discharging air depleted in CO2located on the other end of the membrane in the sorption chamber, wherein the device is configured to allow air to flow from the inlet to the outlet through the membrane; (f) means for flowing stripping gas through the membrane into the regeneration chamber; (g) at least one outlet for discharging CO2, located in the regeneration chamber; and (h) heating means for heating the regeneration chamber. The device according to the invention provides an efficient and low-cost solution for capturing CO2directly from air.

**Avaliação do LLM:**
Esta patente descreve um dispositivo para a captura direta de CO2 do ar, utilizando um sorvente sólido e processos de adsorção/regeneração. O sistema incorpora membranas permeáveis, câmaras de absorção e regeneração, e um meio de transporte do gás. A solução visa fornecer uma maneira eficiente e de baixo custo de capturar CO2 diretamente da atmosfera.

**Extração Estruturada:**
- **Problema:** A necessidade de métodos eficientes e econômicos para a captura direta de CO2 do ar, com o objetivo de reduzir as emissões de gases de efeito estufa.
- **Solução:** O dispositivo proposto utiliza um sistema de membranas e câmaras de adsorção/regeneração para capturar CO2 do ar. O ar flui através da membrana, onde o CO2 é adsorvido por um sorvente sólido, e posteriormente regenerado com calor.
- **Maturidade:** Inicial

**Achados-chave:**
- O dispositivo utiliza uma membrana parcialmente permeável contendo um sorvente sólido de CO2.
- Um sistema de câmaras de absorção e regeneração é empregado para a adsorção e remoção do CO2.

**Vantagens alegadas:**
- Eficiência na captura de CO2 do ar
- Custo reduzido da solução

**Limitações:**
- Dependência de um meio externo para fornecer calor para a regeneração.
- A patente não detalha especificamente o tipo ou as propriedades do sorvente sólido utilizado.

**Aplicações potenciais:**
- Redução de emissões de CO2 em fontes industriais
- Captura direta de CO2 da atmosfera (DAC)

**Evidências citadas:**
> The device comprises (a) a membrane at least partly permeable for air comprising a solid state CO2sorbent;
> The device according to the invention provides an efficient and low-cost solution for capturing CO2directly from air.

---

### 3. One-step process for the production of hydrocarbons from carbon dioxide

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_e3fd7a2fd34b` |
| **Family ID** | `family:ccc9b23fc59ccebd1b1c6849a8995708e0e28cc9` |
| **ID** | `US20240059978A1` |
| **Inventores** | Robert Schuetzle, Dennis Schuetzle, Anja Rumplecker Galloway, Orion Hanbury, Harold Wright |
| **Titular** | Infinium Technology LLC |
| **Data** | 2024-02-22 |
| **Fonte** | Google Patents |
| **URL** | [US20240059978A1](https://patents.google.com/patent/US20240059978A1/en) |
| **Triagem** | include |
| **Rota** | deep_extraction |
| **Motivo da rota** | Há evidência suficiente para extração detalhada. |
| **Score de Triagem** | 9.2/10 |
| **Score de Relevância** | 8.1/10 |
| **Nível de Inovação** | Significativa |
| **Domínio Técnico** | Química, Catálise, Engenharia Química |
| **Cluster Temático** | Química, Catálise, Engenharia Química |
| **Papel do CO2** | substrato_reagente |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | power_or_work_cycle |
| **Fonte/Sumidouro Térmico** | energia renovável (eletrólise de água) |
| **Foco das Claims** | process_integration |
| **Categoria de Exclusão** | N/A |
| **Confiança** | 0.95 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> AbstractThe present invention are new and improved processes and catalysts that can efficiently facilitate the direct carbon dioxide conversion reaction with hydrogen to hydrocarbons in a single reactor at temperatures less than 450Â° C. and more preferably at temperatures from 250Â° C. to 325Â° C. Carbon dioxide is utilized from stationary sources or from direct air capture. Hydrogen is produced by the electrolysis of water using renewable or low carbon electricity.

**Avaliação do LLM:**
Esta patente descreve um processo inovador para a produção de hidrocarbonetos a partir de dióxido de carbono em uma única etapa, utilizando temperaturas controladas abaixo de 450°C. O processo emprega hidrogênio produzido por eletrólise com energia renovável e captura direta de CO2. A patente foca na conversão eficiente do CO2 em hidrocarbonetos.

**Extração Estruturada:**
- **Problema:** A necessidade de processos eficientes para a conversão de dióxido de carbono em produtos valiosos, abordando as preocupações ambientais relacionadas ao excesso de CO2 na atmosfera.
- **Solução:** A patente propõe um processo de uma etapa que converte dióxido de carbono em hidrocarbonetos utilizando temperaturas controladas e hidrogênio produzido a partir de fontes renováveis, otimizando a eficiência da conversão.
- **Maturidade:** Inicial

**Achados-chave:**
- Utilização de temperaturas entre 250°C e 325°C para a reação de conversão de CO2 em hidrocarbonetos.
- Integração do processo com eletrólise de água utilizando energia renovável para a produção de hidrogênio.

**Vantagens alegadas:**
- Conversão eficiente de CO2 em hidrocarbonetos em uma única etapa.
- Utilização de fontes de energia renováveis para a produção de hidrogênio, reduzindo o impacto ambiental.

**Limitações:**
- A patente não detalha especificamente os catalisadores utilizados no processo.
- A viabilidade econômica do processo depende da disponibilidade e custo da energia renovável.

**Aplicações potenciais:**
- Produção de combustíveis sintéticos a partir de CO2.
- Redução das emissões de carbono em processos industriais.

**Evidências citadas:**
> AbstractThe present invention are new and improved processes and catalysts that can efficiently facilitate the direct carbon dioxide conversion reaction with hydrogen to hydrocarbons in a single reactor...
> Carbon dioxide is utilized from stationary sources or from direct air capture.

---

### 4. Carbon dioxide capture

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_bb7ef455d20e` |
| **Family ID** | `family:d74518704aba3dd93362781918a1db8751e01815` |
| **ID** | `US8119091B2` |
| **Inventores** | David Keith, Maryam Mahmoudkhani |
| **Titular** | Carbon Engineering Ltd |
| **Data** | 2012-02-21 |
| **Fonte** | Google Patents |
| **URL** | [US8119091B2](https://patents.google.com/patent/US8119091B2/en) |
| **Triagem** | review |
| **Rota** | manual_review |
| **Motivo da rota** | Triagem indicou revisão humana. |
| **Score de Triagem** | 7.2/10 |
| **Score de Relevância** | 6.5/10 |
| **Nível de Inovação** | Incremental |
| **Domínio Técnico** | Chemical Engineering, Environmental Technology |
| **Cluster Temático** | CO2 Capture and Utilization - Aqueous Solutions |
| **Papel do CO2** | capture_process_stream |
| **Papel do Armazenamento** | implicit_or_support_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | não especificado no abstract, mas implica uso de calor para a causticização. |
| **Foco das Claims** | process_integration |
| **Categoria de Exclusão** | capture_process |
| **Confiança** | 0.85 |
| **Rerank Aplicado** | Sim |
| **Motivo do Rerank** | reranked:decision_confirmed |
| **Revisão Manual** | Sim |
| **Erro LLM** | N/A |

**Abstract:**
> AbstractA method of carbon dioxide capture is disclosed. In a step (a) anhydrous sodium carbonate is separated from a first aqueous solution formed by reacting carbon dioxide and an aqueous solution of sodium hydroxide. In step (b) the anhydrous sodium carbonate is treated by causticization to generate carbon dioxide and sodium hydroxide. The first aqueous solution of step (a) is formed by scrubbing a gas containing carbon dioxide with an aqueous solution of sodium hydroxide.

**Avaliação do LLM:**
Esta patente descreve um método para capturar dióxido de carbono (CO2) utilizando uma solução aquosa de carbonato de sódio anidro e hidróxido de sódio, seguido por um processo de causticização. O foco principal é a captura do CO2 como um fluxo de processo, com potencial para integração em sistemas de armazenamento térmico.

**Extração Estruturada:**
- **Problema:** O problema abordado é a necessidade de métodos eficientes para capturar o dióxido de carbono (CO2) de fluxos gasosos.
- **Solução:** A solução proposta envolve a separação do carbonato de sódio anidro e sua subsequente tratamento por causticização, gerando CO2 e hidróxido de sódio, utilizando uma solução aquosa de NaOH para absorver o CO2.
- **Maturidade:** Intermediária

**Achados-chave:**
- Utiliza carbonato de sódio anidro e hidróxido de sódio em um processo de captura de CO2.
- O processo inclui etapas de separação, causticização e regeneração dos reagentes.
- A patente foca na integração do processo para otimizar a captura e recuperação do CO2.

**Vantagens alegadas:**
- Eficiência na captura de CO2 utilizando soluções aquosas.
- Recuperação de hidróxido de sódio para reutilização no ciclo.
- Potencial para integração em sistemas de armazenamento térmico.

**Limitações:**
- Dependência da concentração e temperatura das soluções aquosas para a eficiência do processo.
- A patente não detalha especificamente o sistema de armazenamento térmico associado.

**Aplicações potenciais:**
- Indústrias que emitem CO2 (cimento, aço, etc.).
- Tecnologias de captura e sequestro de carbono.
- Armazenamento de energia térmica através da utilização do CO2.

**Evidências citadas:**
> "A method of carbon dioxide capture is disclosed."
> "The first aqueous solution of step (a) is formed by scrubbing a gas containing carbon dioxide with an aqueous solution of sodium hydroxide."

---

### 5. Method for capture of carbon dioxide from ambient air and corresponding adsorber structures with a plurality of parallel surfaces

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_c65c389ff2a4` |
| **Family ID** | `family:c7605377da423af2b95849fbe9cfac1a847f58cd` |
| **ID** | `WO2021239747A1` |
| **Inventores** | Alexander SPITERI, Benjamin Megerle, Adelaide CALBRY-MUZYKA, Nathalie CASAS, Jan AndrÃ© Wurzbacher |
| **Titular** | Climeworks AG |
| **Data** | 2021-12-02 |
| **Fonte** | Google Patents |
| **URL** | [WO2021239747A1](https://patents.google.com/patent/WO2021239747A1/en) |
| **Triagem** | include |
| **Rota** | deep_extraction |
| **Motivo da rota** | Há evidência suficiente para extração detalhada. |
| **Score de Triagem** | 9.2/10 |
| **Score de Relevância** | 8.1/10 |
| **Nível de Inovação** | Significativa |
| **Domínio Técnico** | Engenharia Química / Tecnologias de Captura de Carbono |
| **Cluster Temático** | Engenharia Química / Tecnologias de Captura de Carbono |
| **Papel do CO2** | capture_process_stream |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | refrigeration_cycle |
| **Fonte/Sumidouro Térmico** | vapor saturado |
| **Foco das Claims** | process_integration |
| **Categoria de Exclusão** | N/A |
| **Confiança** | 0.95 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> AbstractA DAC method as well as a unit containing an adsorber structure (6) comprising an array of adsorber elements (5) with a support layer (3) and on both sides thereof at least one sorbent layer (1, 2), wherein the adsorber elements are parallel to each other and spaced apart forming parallel fluid passages (7) for flow-through of ambient atmospheric air and/or steam, the method comprising the following sequential and repeating steps: (a) adsorption by flow-through; (b) isolating said sorbent; (c) injecting a stream of saturated steam through said parallel fluid passages (7) and inducing an increase of the temperature; (d) extracting desorbed carbon dioxide from the unit and separating it from steam; (e) bringing the sorbent material to ambient temperature conditions wherein in step (a) the speed of the air through the adsorber structure (6) is in the range of 2-8 m/s, and wherein at least in step (d) the speed of the steam is in the range of at least 0.2 m/s.

**Avaliação do LLM:**
Esta patente descreve um método para a captura de dióxido de carbono da atmosfera utilizando uma estrutura adsorvente com canais paralelos e vapor saturado, focando na adsorção e extração do CO2. O processo envolve a aplicação de vapor sob pressão para induzir a desorção do CO2, seguido pela sua separação. A patente detalha parâmetros operacionais específicos para otimizar o desempenho da captura.

**Extração Estruturada:**
- **Problema:** A necessidade de métodos eficientes e escaláveis para capturar dióxido de carbono diretamente da atmosfera (DAC) é um desafio central na mitigação das mudanças climáticas.
- **Solução:** A patente apresenta uma solução que utiliza uma estrutura adsorvente com canais paralelos e vapor saturado para realizar a captura de CO2, combinando etapas de adsorção, isolamento, injeção de vapor e extração do gás capturado.
- **Maturidade:** Intermediária

**Achados-chave:**
- O método emprega velocidades específicas para o fluxo de ar (2-8 m/s) e vapor (0.2 m/s) durante a adsorção e desorção, otimizando a eficiência da captura.
- A estrutura adsorvente é composta por camadas de sorbente em ambos os lados, com canais paralelos para o fluxo de ar e vapor, maximizando a área de contato e a taxa de transferência de massa.

**Vantagens alegadas:**
- Captura direta de CO2 da atmosfera.
- Utilização de vapor saturado como agente de desorção, reduzindo o consumo de energia.

**Limitações:**
- A patente não aborda diretamente os desafios de escalabilidade e custo da tecnologia DAC.
- A eficiência do processo pode ser influenciada pela composição e pureza do ar atmosférico.

**Aplicações potenciais:**
- Mitigação das mudanças climáticas através da remoção de CO2 da atmosfera.
- Utilização do CO2 capturado como matéria-prima para a produção de produtos químicos ou materiais.

**Evidências citadas:**
> AbstractA DAC method as well as a unit containing an adsorber structure (6) comprising an array of adsorber elements (5) with a support layer (3) and on both sides thereof at least one sorbent layer (1, 2)
> the speed of the air through the adsorber structure (6) is in the range of 2-8 m/s, and wherein at least in step (d) the speed of the steam is in the range of at least 0.2 m/s.

---

### 6. Systems and methods for direct air carbon dioxide capture

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_5b906b66b823` |
| **Family ID** | `family:d78300f0474b5d657cf6a238e8d6873f00dcb1aa` |
| **ID** | `US20230191322A1` |
| **Inventores** | Luke Shors, Zeph Landau, Ethan Cohen-Cole, Rahul Surana |
| **Titular** | Capture6 Corp |
| **Data** | 2023-06-22 |
| **Fonte** | Google Patents |
| **URL** | [US20230191322A1](https://patents.google.com/patent/US20230191322A1/en) |
| **Triagem** | include |
| **Rota** | deep_extraction |
| **Motivo da rota** | Há evidência suficiente para extração detalhada. |
| **Score de Triagem** | 9.2/10 |
| **Score de Relevância** | 8.0/10 |
| **Nível de Inovação** | Significativa |
| **Domínio Técnico** | Engenharia Química / Processamento de Gases |
| **Cluster Temático** | Engenharia Química / Processamento de Gases |
| **Papel do CO2** | capture_process_stream |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | eletroquímico (possivelmente integrado com energia renovável) |
| **Foco das Claims** | process_integration |
| **Categoria de Exclusão** | N/A |
| **Confiança** | 0.95 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> AbstractA method for capturing and sequestering carbon dioxide (CO2) includes receiving and performing an electrochemical process on the input liquid including water and a salt to produce at least one hydroxide-rich stream, and then capturing CO2 from air using the hydroxide-rich stream and a passive air capture system, thereby producing a liquid carbonate solution containing air-captured CO2. Optional steps include disposing of the liquid carbonate solution, precipitating air-captured CO2 from the liquid carbonate solution as solid carbonate and/or a slurry of carbonate, and mixing the liquid carbonate solution with a hydrogen-rich stream produced by the electrochemical process to generate gaseous CO2. Various integrations and synergies among CO2 capture, renewable energy, water desalination, and metal and mineral extraction are provided.

**Avaliação do LLM:**
Esta patente descreve um sistema para captura direta de CO2 do ar através de um processo eletroquímico que utiliza água e sal para produzir uma corrente rica em hidroxi-ídroxi, capturando o CO2 do ar com essa corrente. O sistema também inclui etapas opcionais para a produção de carbonato sólido ou slurry e integração com fontes de energia renováveis.

**Extração Estruturada:**
- **Problema:** A patente aborda o desafio da captura eficiente de CO2 diretamente da atmosfera, buscando uma solução que minimize o impacto ambiental e maximize a utilização de recursos renováveis.
- **Solução:** A solução proposta envolve um processo eletroquímico para gerar uma corrente rica em hidroxi-ídroxi, que é utilizada para capturar o CO2 do ar. A captura resulta na formação de uma solução de carbonato contendo CO2, permitindo a sua posterior utilização ou armazenamento.
- **Maturidade:** Inicial

**Achados-chave:**
- Utilização de um processo eletroquímico com água e sal para gerar uma corrente rica em hidroxi-ídroxi para capturar o CO2 do ar.
- Formação de uma solução de carbonato contendo CO2, que pode ser utilizada para precipitação ou mistura com fluxos ricos em hidrogênio.
- Integração do sistema com outras tecnologias como dessalinização e extração de metais e minerais.

**Vantagens alegadas:**
- Captura direta de CO2 do ar utilizando um processo eletroquímico.
- Utilização de recursos renováveis, como energia hidrogênio-rica.
- Potencial para integração com outras tecnologias de processamento industrial.

**Limitações:**
- A eficiência do sistema depende da otimização das condições eletroquímicas e da eficácia do sistema de captura passiva.
- A escalabilidade do processo pode ser um desafio, dependendo dos custos de materiais e energia.

**Aplicações potenciais:**
- Redução das emissões de CO2 em fontes industriais e elétricas.
- Produção de combustíveis sintéticos a partir de CO2 e água.
- Dessalinização da água utilizando o calor gerado pelo processo eletroquímico.

**Evidências citadas:**
> AbstractA method for capturing and sequestering carbon dioxide (CO2) includes receiving and performing an electrochemical process on the input liquid including water and a salt to produce at least one hydroxide-rich stream…

---

### 7. Metal-carbon dioxide (CO2) battery cell

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_f0f68dc78688` |
| **Family ID** | `family:f5eef92ee3d87ac38ae317ad583c6a7d1b15f2be` |
| **ID** | `US12401048B1` |
| **Inventores** | Muhammad Kashif Aslam, Ali Al Marzouqi |
| **Titular** | United Arab Emirates University |
| **Data** | 2025-08-26 |
| **Fonte** | Google Patents |
| **URL** | [US12401048B1](https://patents.google.com/patent/US12401048B1/en) |
| **Triagem** | review |
| **Rota** | manual_review |
| **Motivo da rota** | Triagem indicou revisão humana. |
| **Score de Triagem** | 7.2/10 |
| **Score de Relevância** | 6.5/10 |
| **Nível de Inovação** | Incremental |
| **Domínio Técnico** | Eletroquímica, Baterias |
| **Cluster Temático** | Baterias com Fluidos Alternativos |
| **Papel do CO2** | working_fluid |
| **Papel do Armazenamento** | implicit_or_support_storage |
| **Limite Sistêmico** | cycle_or_transfer_subsystem |
| **Tipo de Ciclo** | power_or_work_cycle |
| **Fonte/Sumidouro Térmico** | N/A |
| **Foco das Claims** | Fluxo de CO2 através de um catalisador para interação eletroquímica. |
| **Categoria de Exclusão** | industrial_heat_adjacent |
| **Confiança** | 0.75 |
| **Rerank Aplicado** | Sim |
| **Motivo do Rerank** | reranked:decision_confirmed |
| **Revisão Manual** | Sim |
| **Erro LLM** | N/A |

**Abstract:**
> AbstractThe present disclosure is directed to a zero-gap flow-type metal-Carbon dioxide CO2battery cell. The battery cell includes an electrolyte chamber allowing flow of electrolyte and a metal electrode configured as anode, being accommodated in the electrolyte chamber and defined with a plurality of apertures. Further, the battery cell includes a CO2chamber allowing flow of CO2and a gas diffusion electrode (GDE) configured as cathode and accommodated in the CO2chamber. The GDE is defined with a first side and a second side, which is coated with catalyst layer. The catalyst layer abuts a membrane on the metal electrode such that, the electrolyte from the electrolyte chamber flows through the plurality of apertures, penetrates through the membrane and contacts the catalyst layer. Further, CO2from the CO2chamber contacts the second side of the gas diffusion electrode to diffuse through the catalyst and towards the metal electrode.

**Avaliação do LLM:**
Esta patente descreve uma célula de bateria que utiliza CO2 como fluido de trabalho e eletrolita, combinando uma câmara de CO2 com um eletrodo metálico. A patente foca no fluxo do CO2 através de um catalisador para interação com o metal eletrodo, visando a conversão de energia.

**Extração Estruturada:**
- **Problema:** A necessidade de desenvolver sistemas de armazenamento de energia que utilizem fluidos alternativos e processos eletroquímicos.
- **Solução:** A solução proposta é uma célula de bateria 'zero-gap' com câmaras separadas para CO2 e eletrólito, permitindo o fluxo do CO2 através de um catalisador para interação com o eletrodo metálico, gerando energia.
- **Maturidade:** Inicial

**Achados-chave:**
- A patente utiliza uma câmara de CO2 para permitir o fluxo do gás através da célula.
- O sistema inclui um eletrodo metálico configurado como ânodo e um gas diffusion electrode (GDE) configurado como cátodo.

**Vantagens alegadas:**
- Utilização de CO2 como fluido de trabalho e meio eletroquímico.
- Possibilidade de fluxo do CO2 através de um catalisador para interação com o eletrodo.

**Limitações:**
- O abstract não detalha a eficiência ou a estabilidade da bateria.
- A descrição é ambígua sobre os limites do sistema e o papel central do armazenamento.

**Aplicações potenciais:**
- Armazenamento de energia em sistemas eletroquímicos.
- Desenvolvimento de novas tecnologias de baterias.

**Evidências citadas:**
> The battery cell includes an electrolyte chamber allowing flow of electrolyte and a metal electrode configured as anode...
> CO2from the CO2chamber contacts the second side of the gas diffusion electrode to diffuse through the catalyst and towards the metal electrode.

---

### 8. Direct removal of carbon dioxide from oceanwater based on a composite membrane

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_af5baa133fd3` |
| **Family ID** | `family:e440df584d8cb81a97e93389b45db8364766815d` |
| **ID** | `US12202743B2` |
| **Inventores** | Soomin KIM, Ibadillah Ardhi Digdaya, Sreevalli Bokka, Chengxiang Xiang |
| **Titular** | Captura Corp |
| **Data** | 2025-01-21 |
| **Fonte** | Google Patents |
| **URL** | [US12202743B2](https://patents.google.com/patent/US12202743B2/en) |
| **Triagem** | include |
| **Rota** | deep_extraction |
| **Motivo da rota** | Há evidência suficiente para extração detalhada. |
| **Score de Triagem** | 8.2/10 |
| **Score de Relevância** | 8.2/10 |
| **Nível de Inovação** | Significativa |
| **Domínio Técnico** | Engenharia Química / Materiais |
| **Cluster Temático** | Engenharia Química / Materiais |
| **Papel do CO2** | capture_process_stream |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | não especificado no abstract |
| **Foco das Claims** | process_integration |
| **Categoria de Exclusão** | N/A |
| **Confiança** | 0.90 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> AbstractIn a general aspect, a composite contact composite membrane for direct removal of carbon dioxide from oceanwater is presented. In some cases, a composite membrane includes a supporting layer having a first surface and a second, opposite surface; and a carbon dioxide selective layer disposed on the first surface. The carbon dioxide selective layer is configured to contact an aqueous solution including dissolved carbon dioxide and to selectively transport the dissolved carbon dioxide from the aqueous solution through the supporting layer to the second opposite surface.

**Avaliação do LLM:**
Esta patente descreve um método para a remoção direta de dióxido de carbono da água do mar utilizando uma membrana composta. A membrana é projetada para selecionarivamente transportar o CO2 dissolvido da água do mar através da membrana, permitindo a captura do gás. O foco principal é na aplicação de membranas compostas para processos de captura de CO2.

**Extração Estruturada:**
- **Problema:** A necessidade de métodos eficientes e eficazes para remover dióxido de carbono da água do mar, contribuindo para a mitigação das mudanças climáticas.
- **Solução:** A patente apresenta uma membrana composta que utiliza uma camada seletiva para transportar o CO2 dissolvido da água do mar, permitindo sua remoção direta. A membrana é projetada para otimizar a transferência de massa e a separação do CO2.
- **Maturidade:** Inicial

**Achados-chave:**
- A patente detalha a utilização de uma membrana composta com uma camada seletiva para a captura de CO2.
- O abstract menciona o uso da membrana em contato com uma solução aquosa contendo CO2 dissolvido, promovendo o transporte seletivo do gás.

**Vantagens alegadas:**
- Remoção direta e eficiente de CO2 da água do mar.
- Utilização de uma membrana composta para otimizar a captura de CO2.

**Limitações:**
- O tipo de ciclo não está claro, necessitando mais detalhes sobre o regime termodinâmico.
- A patente não especifica detalhadamente as propriedades da membrana ou os parâmetros operacionais ideais.

**Aplicações potenciais:**
- Captura de carbono em larga escala a partir de fontes oceânicas.
- Redução das emissões de CO2 provenientes de processos industriais que utilizam água do mar.

**Evidências citadas:**
> AbstractIn a general aspect, a composite contact composite membrane for direct removal of carbon dioxide from oceanwater is presented.
> The carbon dioxide selective layer is configured to contact an aqueous solution including dissolved carbon dioxide and to selectively transport the dissolved carbon dioxide from the aqueous solution through the supporting layer to the second opposite surface.

---

### 9. Plant and method for capturing carbon dioxide

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_9705af612fc3` |
| **Family ID** | `family:328ef9b7634209b1d47b1faf24de298259c2e171` |
| **ID** | `WO2024208966A1` |
| **Inventores** | Josef Fuchs, Johannes Fuchs, Florian CHIMANI, Aditya Anil BHANDARI, Andreas WALLMÃLLER, Michael FAHRNGRUBER, Benjamin FLEIÃ, Hermann Hofbauer, Stefan MÃ¼ller |
| **Titular** | Dharma Karma Foundation |
| **Data** | 2024-10-10 |
| **Fonte** | Google Patents |
| **URL** | [WO2024208966A1](https://patents.google.com/patent/WO2024208966A1/en) |
| **Triagem** | include |
| **Rota** | deep_extraction |
| **Motivo da rota** | Há evidência suficiente para extração detalhada. |
| **Score de Triagem** | 8.2/10 |
| **Score de Relevância** | 7.7/10 |
| **Nível de Inovação** | Significativa |
| **Domínio Técnico** | Engenharia Química / Engenharia Ambiental |
| **Cluster Temático** | Engenharia Química / Engenharia Ambiental |
| **Papel do CO2** | capture_process_stream |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | não especificado no resumo |
| **Foco das Claims** | cycle_integration |
| **Categoria de Exclusão** | N/A |
| **Confiança** | 0.90 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> AbstractA plant (1) for capturing carbon dioxide (CO2) from a carbon di- oxide laden gas stream (2), comprising: an adsorption device (3) with a container (4) for containing an adsorbent (5) made of solid adsorbent particles (5a) for binding the carbon dioxide (CO2) to the adsorbent (5), the ad- sorption device (3) having an adsorbent inlet (6) and an adsorb- ent outlet (7), a regeneration device (8) for separating the bound carbon dioxide (CO2) from the adsorbent (5), the regeneration device (8) having an adsorbent intake (9) and an adsorbent outtake (10), wherein the adsorbent outlet (7) is connected to the adsorb- ent intake (9) and the adsorbent outtake (10) is connected to the adsorbent inlet (6), wherein a fixed bed regenerator (11) of the regeneration device (8) having a reservoir (12) for the adsorbent (5) and a fluid outlet (14) for withdrawing at least carbon dioxide (CO2) from the reservoir (12), an intake valve (15) being arranged in the adsorbent intake (9), an outtake valve (16) being arranged in the adsorbent out- take (10), wherein the intake and the outtake valve (15, 16) are con- figured to be selectively transferred between an open state al- lowing passage of the adsorbent (5) through the adsorbent intake (9) into the reservoir (12) and through the adsorbent outtake (10) out of the reservoir (12), respectively, and a closed state blocking passage of the adsorbent (5) through the adsorbent in- take (9) into the reservoir (12) and through the adsorbent out- take (10) out of the reservoir (12) in an essentially airtight manner, respectively, a vacuum generation unit (17) for generating a vacuum inside the reservoir (12) in the closed state of the intake and outtake valve (15, 16), respectively.

**Avaliação do LLM:**
Esta patente descreve um sistema para capturar CO2 de um fluxo gasoso usando uma planta que incorpora dispositivos de adsorção e regeneração. O sistema utiliza um ciclo fechado com válvulas seletivas e uma unidade de vácuo para otimizar a separação do CO2 do adsorvente. A tecnologia visa a captura direta de CO2, oferecendo uma solução integrada para o processo.

**Extração Estruturada:**
- **Problema:** A patente aborda o desafio da captura eficiente de CO2 de fluxos gasosos, buscando um método que minimize perdas e maximize a recuperação do gás.
- **Solução:** A solução proposta é um sistema com adsorção e regeneração de CO2, utilizando um ciclo fechado controlado por válvulas e vácuo para otimizar o processo de separação. O sistema inclui um adsorvente sólido e um regenerador para reutilização do material.
- **Maturidade:** Inicial

**Achados-chave:**
- O sistema emprega um ciclo fechado com válvulas seletivas para controlar o fluxo do adsorvente, permitindo a regeneração eficiente do CO2.
- A utilização de uma unidade de vácuo no regenerador contribui para aumentar a eficiência da separação do CO2 do adsorvente.

**Vantagens alegadas:**
- Captura eficiente de CO2 de fluxos gasosos.
- Ciclo fechado que permite a reutilização do adsorvente, reduzindo custos operacionais.

**Limitações:**
- A patente não detalha especificamente as condições de operação (temperatura, pressão) para o sistema.
- A eficiência do processo depende das propriedades do adsorvente utilizado.

**Aplicações potenciais:**
- Indústrias que emitem grandes quantidades de CO2 (e.g., produção de cimento, refino de petróleo).
- Tecnologias de captura e armazenamento de carbono (CCS).

**Evidências citadas:**
> A plant (1) for capturing carbon dioxide (CO2) from a carbon di- oxide laden gas stream (2)
> a regeneration device (8) for separating the bound carbon dioxide (CO2) from the adsorbent (5)

---

### 10. APPARATUS FOR SUPPLYING LIQUID
CARBON
DIOXIDE

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_6ef9ca6982e5` |
| **Family ID** | `family:330959902bcf0da3cfe736228c934db0407244ab` |
| **ID** | `1429678` |
| **Inventores** | N/A |
| **Titular** | DISTILLERS CO
CARBON
DIOXIDE |
| **Data** | 24.03.1976 |
| **Fonte** | Patentscope |
| **URL** | [1429678](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135599119&_cid=P21-MR0SB9-98266-1) |
| **Triagem** | review |
| **Rota** | manual_review |
| **Motivo da rota** | Triagem indicou revisão humana. |
| **Score de Triagem** | 7.2/10 |
| **Score de Relevância** | 6.5/10 |
| **Nível de Inovação** | Significativa |
| **Domínio Técnico** | Controle de Processos, Termodinâmica, Sistemas de Refrigeração |
| **Cluster Temático** | Sistemas de Controle Automatizado para Manipulação de Fluidos Refrigerados |
| **Papel do CO2** | working_fluid |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | cycle_or_transfer_subsystem |
| **Tipo de Ciclo** | refrigeration_cycle |
| **Fonte/Sumidouro Térmico** | cooling_or_refrigeration |
| **Foco das Claims** | component_or_operation |
| **Categoria de Exclusão** | cooling_only |
| **Confiança** | 0.85 |
| **Rerank Aplicado** | Sim |
| **Motivo do Rerank** | reranked:decision_confirmed |
| **Revisão Manual** | Sim |
| **Erro LLM** | N/A |

**Abstract:**
> (EN)1429678 Automatic control of level DISTILLERS CO (CARBONDIOXIDE) Ltd 18 Jan 1974 [28 March 1973] 14925/73 Heading G3R [Also in Division F4]  In apparatus for delivering liquid CO 2  from a heat insulated reservoir 1 through a discharge pipe 5, 5' to a delivery point at 8, a container 7 is connected in the discharge pipe for removal of gaseous CO 2  through an outlet pipe 12 with a valve 11 controlled by a unit 31 which opens the valve when the gas reaches a predetermined volume in the container. As shown the gas is passed to an accumulator 14 and thence to a cooler 17, and is returned as liquid to the reservoir 1. Simpler installations are, however, envisaged in which the gaseous CO 2  is vented to atmosphere or directly to the top of the reservoir. The reservoir is refrigerated by a coil 3. The delivery point is a metering jet 8 connected to a snow-making horn 9, but may alternatively be a connector for filling cylinders or the intake of a rotory pump.  The valve 11 is a solenoid valve and may be controlled by a float-operated switch. Preferably however, the container 7 has a tubular wall 22 forming the outer electrode of a coaxial capacitor, the inner electrode being formed by a perforated tube 27. The two electrodes are connected through a cable 29 to the resonance circuit of a Colpitts oscillator, Fig. 3 (not shown) in the control unit 31. When the container 7 is full of liquid CO 2 , the capacitance between the electrodes 22, 27 is enough to block the oscillator so that there is no input to an amplifying (T2), and a switching transistor (T4) controlled thereby is OFF. The emitter circuit of the transistor contains the coil of a relay (R) with normally open contacts (Ra) in series with the solenoid of the valve 11 which is therefore closed. As gaseous CO 2  collects in the container 7, the liquid level and the capacitance drop with the eventual onset of oscillation. The relay (R) is thereby closed, opening the valve 11  to vent the gas and opening auxiliary contacts (Rb) to disconnect a capacitor (C7) from the oscillator circuit. Oscillation therefore continues until the capacitance between the electrodes 22, 27 increases sufficiently, as the liquid level rises, to offset the effect of the capacitor (C7).

**Avaliação do LLM:**
Esta patente descreve um sistema de controle para a entrega de dióxido de carbono (CO2) líquido, utilizando um circuito ressonante e um capacitor para detectar o nível do fluido em um reservatório. O sistema controla automaticamente a válvula de descarga com base na variação da capacitância, permitindo uma entrega precisa de CO2 líquido.

**Extração Estruturada:**
- **Problema:** O problema abordado é o controle preciso da liberação de CO2 líquido de um reservatório refrigerado, evitando o excesso ou a falta do fluido na aplicação de destino.
- **Solução:** A solução proposta utiliza um circuito ressonante baseado em um capacitor e um oscilador Colpitts para monitorar o nível do CO2 líquido no recipiente. A variação da capacitância resultante da mudança no nível do fluido aciona uma válvula controlada por solenóide, regulando o fluxo de CO2.
- **Maturidade:** Inicial

**Achados-chave:**
- Utilização de um circuito ressonante (Colpitts oscillator) para detectar variações na capacitância devido ao nível do líquido CO2.
- Controle da válvula de descarga através de um transistor e um relé, acionado pela oscilação do circuito ressonante.
- Implementação de um sistema de controle baseado em capacitance para monitorar o volume de CO2 no recipiente.

**Vantagens alegadas:**
- Controle automático da liberação de CO2 líquido.
- Precisão na entrega do fluido, evitando desperdício ou excesso.
- Possibilidade de integração com diversos sistemas de destino (ex: jatos de neve, acumuladores).

**Limitações:**
- A patente depende da estabilidade do oscilador Colpitts e da precisão dos componentes eletrônicos.
- O sistema pode ser sensível a variações de temperatura e pressão.

**Aplicações potenciais:**
- Sistemas de jatos de neve
- Acumulação de CO2 líquido para diversas aplicações industriais
- Controle preciso de processos que utilizam CO2 líquido como fluido de trabalho

**Evidências citadas:**
> "the container 7 has a tubular wall 22 forming the outer electrode of a coaxial capacitor..."
> The valve 11 is controlled by a float-operated switch.

---

### 11. Dispensing Device

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_d7d21bdaf3a1` |
| **Family ID** | `family:f40c29cdabc9eb6718533449e3c8961483f91165` |
| **ID** | `1171698` |
| **Inventores** | MOLE WALTER ERNEST |
| **Titular** | DISTILLERS CO
CARBON
DIOXIDE |
| **Data** | 26.11.1969 |
| **Fonte** | Patentscope |
| **URL** | [1171698](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135354895&_cid=P21-MR0SB9-98266-1) |
| **Triagem** | exclude |
| **Rota** | screen_only |
| **Motivo da rota** | Patente excluída na triagem. |
| **Score de Triagem** | 3.5/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | Dispositivos de Dispensação de Líquidos |
| **Cluster Temático** | Dispensadores de Bebidas com Pressão de Gás |
| **Papel do CO2** | working_fluid |
| **Papel do Armazenamento** | implicit_or_support_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | refrigeration_cycle |
| **Fonte/Sumidouro Térmico** | cooling_or_refrigeration |
| **Foco das Claims** | component_or_operation |
| **Categoria de Exclusão** | generic_tes |
| **Confiança** | 0.59 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> (EN)1, 171, 698. Dispensing liquids by gaseous pressure. DISTILLERS CO. (CARBONDIOXIDE) Ltd. April 11, 1968 (April 11, 1967], No.16511/67. Heading F1R. A dispenser of liquids from a container comprises a body provided with means for attaching the dispenser to the container, a sharp tube capable of piercing a hole in the lid of the container, a seal on the underside of the body surrounding the tube which when the dispenser is attached to the container forms a substantially gas-tight chamber around the tube, the chamber being in communication with the interior of the container via the hole in the lid, a supply ofcarbondioxideunder pressure with which the chamber is in communication via a non-return valve, and a delivery tube housed within the sharp tube which communicates with a dispensing tube projecting from the body of the device. After removal of a dip tube 8, a sharp tube 1 is forced into the lid of a beer can to form a hole. The dip tube 8 is then refitted and a screw thread 3 is screwed into the hole in the lid until a seal 43, which may be of silicone rubber, is in sealing engagement with the lid. A capsule 21 of high-pressurecarbondioxideis placed in a holder 20 and a cap 22 is screwed on, a pin 23 on the cap piercing the capsule. High-pressurecarbondioxidepasses through a pressure reducing valve, a sintered metal filter 34, and a capillary tube 29 to a low-pressure chamber 25. The pressure reducing valve is formed by the engagement of the end of the capillary tube 29 with a polyurethane pad 30, the capillary tube being pressed against the pad by a piston 26 subjected to the pressure in the low-pressure chamber 25 and the opposing force of a spring 27. From the low-pressure chamber 25, the low-pressurecarbondioxidepasses via a duct 39, a duct (38) and a non-return valve (44) into the space between the seal 43 and the sharp tube 1 and thence into the beer can. On depression of a button 5 to the position shown, a bore 11 is brought adjacent a port 12 to allow beer, urged by thecarbondioxideto be delivered via the dip tube 8, bores 10, 11, port 12 and a dispensing tube 13. A relief valve (45) vents excessive pressure to atmosphere. Castellations 55 cooperate with pins (56) depending from the button 5 so that by rotating the button the dispenser can be locked into a non-dispensing state. Instead of a screw thread 3, spring members hooking over the rim of the can may be used. Alternatively, a bayonet-type joint may be used with cans provided with the necessary fitment. The pin 23 can be provided at the other end of the holder 20, projecting from the pad 30. Provision may be made for holding twocarbondioxidecapsules with interchangeable connections to the interior of the can. Thecarbondioxidesupply may be a large cylinder of liquidcarbondioxideunder pressure.

**Evidências citadas:**
> A dispenser of liquids from a container comprises a body provided with means for attaching the dispenser to the container...
> ...High-pressurecarbondioxidepasses through a pressure reducing valve...

---

### 12. METHOD AND APPARATUS FOR REPARING EXTRACTS OF HOPS AND OTHER MATERIALS

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_f897e69f6312` |
| **Family ID** | `family:20d341850811d74a49030cf1bc9873e738b66561` |
| **ID** | `1557123` |
| **Inventores** | N/A |
| **Titular** | DISTILLERS CO
CARBON
DIOXIDE |
| **Data** | 05.12.1979 |
| **Fonte** | Patentscope |
| **URL** | [1557123](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135726881&_cid=P21-MR0SB9-98266-1) |
| **Triagem** | exclude |
| **Rota** | screen_only |
| **Motivo da rota** | Patente excluída na triagem. |
| **Score de Triagem** | 1.7/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | Processamento de bebidas alcoólicas |
| **Cluster Temático** | Extração e Refino |
| **Papel do CO2** | co2_not_central |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | industrial_heat |
| **Foco das Claims** | component_or_operation |
| **Categoria de Exclusão** | generic_tes |
| **Confiança** | 0.49 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Evidências citadas:**
> METHOD AND APPARATUS FOR REPARING EXTRACTS OF HOPS AND OTHER MATERIALS

---

### 13. Reclamation of foundry sand

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_ca73a4e50a56` |
| **Family ID** | `family:03b6ce3e289bafd73ea31817ccf0e386282dcb9a` |
| **ID** | `2047588` |
| **Inventores** | N/A |
| **Titular** | DISTILLERS CO
CARBON
DIOXIDE |
| **Data** | 03.12.1980 |
| **Fonte** | Patentscope |
| **URL** | [2047588](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135860928&_cid=P21-MR0SB9-98266-1) |
| **Triagem** | review |
| **Rota** | manual_review |
| **Motivo da rota** | Triagem indicou revisão humana. |
| **Score de Triagem** | 7.0/10 |
| **Score de Relevância** | 6.5/10 |
| **Nível de Inovação** | Incremental |
| **Domínio Técnico** | Materiais de Fundição e Processos Recuperativos |
| **Cluster Temático** | Reciclagem de Materiais para Fundição com Utilização de CO2 |
| **Papel do CO2** | Carbonating Agent/Agente Carbonatante |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | não_claro |
| **Fonte/Sumidouro Térmico** | CO2 (fonte de calor) |
| **Foco das Claims** | Carbonatação da areia para remoção do aglutinante |
| **Categoria de Exclusão** | industrial_heat_adjacent |
| **Confiança** | 0.80 |
| **Rerank Aplicado** | Sim |
| **Motivo do Rerank** | reranked:include->review |
| **Revisão Manual** | Sim |
| **Erro LLM** | N/A |

**Abstract:**
> (EN)A process for the reclamation of CO2-silicate bonded casting sand includes the step of subjecting the sand after it has been used for casting to treatment withcarbondioxidein the presence of water until substantially all of the reactive soluble alkali metal compounds present in the used sand which are capable of beingcarbonatedarecarbonated. Thiscarbonationstep improves the removal of the binder by a subsequent mechanical attrition step. In effecting the process, a batch of the used sand may be wetted and subjected to a vacuum, the vacuum then being broken by the introduction ofcarbondioxidewhich may be at a superatmospheric pressure.

**Avaliação do LLM:**
Esta patente descreve um processo para a recuperação de areia de fundição que utiliza dióxido de carbono (CO2) em conjunto com água para carbonatar compostos alcalinos solúveis na areia usada em moldagem. O CO2 é aplicado sob vácuo e pressão atmosférica, melhorando a remoção do aglutinante da areia após o processo de carbonatação.

**Extração Estruturada:**
- **Problema:** O problema abordado é a dificuldade de recuperar areia de fundição com ligações silicato-CO2, onde os compostos alcalinos solúveis dificultam a remoção eficiente do aglutinante.
- **Solução:** A solução proposta envolve o tratamento da areia usada com CO2 e água, carbonatando os compostos alcalinos e facilitando sua remoção por atrito mecânico.
- **Maturidade:** Intermediária

**Achados-chave:**
- O processo utiliza CO2 sob vácuo e pressão atmosférica para carbonatar os compostos alcalinos.
- A carbonatação melhora a remoção do aglutinante através de um passo subsequente de atrição mecânica.

**Vantagens alegadas:**
- Melhoria na remoção do aglutinante da areia de fundição.
- Processo mais eficiente para recuperar areia de fundição com ligações silicato-CO2.

**Limitações:**
- O processo depende da disponibilidade e controle da pressão do CO2.
- A eficácia pode variar dependendo da composição específica da areia de fundição.

**Aplicações potenciais:**
- Recuperação de areia de fundição em indústrias metalúrgicas.
- Processamento de resíduos de areia de fundição.

**Evidências citadas:**
> 'the step of subjecting the sand after it has been used for casting to treatment with carbon dioxide...'

---

### 14. WEIGHING MACHINES

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_8b12b55bf8c3` |
| **Family ID** | `family:3e68eec1085a61705bd24ec21d9478df0061186e` |
| **ID** | `1426573` |
| **Inventores** | N/A |
| **Titular** | DISTILLERS CO
CARBON
DIOXIDE |
| **Data** | 03.03.1976 |
| **Fonte** | Patentscope |
| **URL** | [1426573](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135595668&_cid=P21-MR0SB9-98266-1) |
| **Triagem** | exclude |
| **Rota** | screen_only |
| **Motivo da rota** | Patente excluída na triagem. |
| **Score de Triagem** | 3.5/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | Engenharia de Processos |
| **Cluster Temático** | Controle de Processos e Pesagem |
| **Papel do CO2** | working_fluid |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | refrigeration_cycle |
| **Fonte/Sumidouro Térmico** | industrial_heat |
| **Foco das Claims** | system_architecture |
| **Categoria de Exclusão** | generic_tes |
| **Confiança** | 0.56 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> (EN)1426573 Automatic weighing DISTILLERS CO (CARBONDIOXIDE) Ltd 15 Feb 1974 [27 Feb 1973] 9566/73 Heading G1W The filling of a cylinder with liquidcarbondioxideis controlled by a weighing machine having a dial, a pointer, a permanent magnet 7 mounted on the pointer or an arm 6 moving with pointer, normally open reed switches 9, 10, 11 operable by the magnet, and a control circuit (Fig. 3). The filling apparatus comprises a continuously running pump 21 having its inlet connected to a supply a by-pass 25 containing a solenoid valve 18 and connecting the outlet of the pump to the supply, and a connection 29 containing a solenoid valve 19 and to which the cylinder to be filled is connected. The control circuit includes an A.C. transformer 12, a D.C. relay R including a diode rectifying network, solenoids 16, 16 which energized respectively open and close valve 18, and solenoid 17 which when energized opens valve 19. In use, an empty cylinder is placed on the weighing machine which is then adjusted until the pointer reads zero, and reed switch 9 is therefore closed. Switch 15 is used to select reed switch 10 or 11 according to the size of the cylinder and switch 13 is pressed to energize relay R. Holding contacts Ra maintain the relay energized when switch 13 is released. When relay R is energized contacts Rb energize solenoids 16 17 so that valve 18 is closed and valve 19 is open. When reed switch 10 or 11 is closed by magnet 7, the coil of relay R is short circuited, contacts Ra open and contacts Rb switch over causing solenoid 17 to be de-energized and solenoid 16 to be energized, thus closing valve 19 and opening valve 18. Switch 31 is then operated to open solenoid valve 28 to vent connection 29 to atmosphere. The filling apparatus includes a non-return valve 24, a safety valve 26 and a damping chamber 27. In damping chamber 27, a heating element 28 maintains a body of gas which damps out the pulses produced by pump 21.

**Evidências citadas:**
> Automatic weighing DISTILLERS CO (CARBONDIOXIDE) Ltd
> The filling of a cylinder with liquidcarbondioxideis controlled by a weighing machine

---

### 15. A Dispensing Device for Gases Under Pressure.

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_56073152026b` |
| **Family ID** | `family:c6553ae6f938f4ff3b91fe1eb94d906b9949a390` |
| **ID** | `1174314` |
| **Inventores** | GODFERY GORDON REGINALD |
| **Titular** | DISTILLERS CO
CARBON
DIOXIDE |
| **Data** | 17.12.1969 |
| **Fonte** | Patentscope |
| **URL** | [1174314](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135357801&_cid=P21-MR0SB9-98266-1) |
| **Triagem** | exclude |
| **Rota** | screen_only |
| **Motivo da rota** | Patente excluída na triagem. |
| **Score de Triagem** | 3.5/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | Engenharia de Fluidos, Instrumentação |
| **Cluster Temático** | Dispositivos de Dispensa de Gases Industriais |
| **Papel do CO2** | working_fluid |
| **Papel do Armazenamento** | implicit_or_support_storage |
| **Limite Sistêmico** | dedicated_storage_system |
| **Tipo de Ciclo** | refrigeration_cycle |
| **Fonte/Sumidouro Térmico** | cooling_or_refrigeration |
| **Foco das Claims** | system_architecture |
| **Categoria de Exclusão** | generic_tes |
| **Confiança** | 0.59 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> (EN)1,174,314. Valves. DISTILLERS CO. (CARBONDIOXIDE) Ltd. 22 May, 1968 [25 May, 1967], No. 24270/67. Heading F2V. Universal dispensing device for supplyingcarbondioxideat suitable reduced pressures to various appliances such as, soda syphones, fire extinguishers, dinghies, life-rafts and tyre inflators from a container comprises a reducing valve 12, 14 operated by a diaphragm 13 exposed to pressure in an outlet chamber 13. A loading spring 17 for the diaphragm is adjustable by a screwed retainer 16 connected through a rack and pinion device to pins 31 slidable in an outlet connection 28 and adapted to form a bayonet connection with the appliance. The appliances are arranged so that connection can only be made when the device is adjusted to supply the gas at the required pressure. A trigger operated valve 25 is in series with the reducing valve. The latter comprises a capillary tube 12 connected to the diaphragm and passing through an 0-ring seal to engage a seat 14 carried in a porous plug 10. A piercing member 6 opens the container as the device is coupled. The setting is indicated on a plate 5. A relief valve 19 is included.

**Evidências citadas:**
> Universal dispensing device for supplyingcarbondioxideat suitable reduced pressures to various appliances such as, soda syphones, fire extinguishers, dinghies, life-rafts and tyre inflators from a container comprises a reducing valve 12, 14 operated by a diaphragm 13 exposed to pressure in an outlet chamber 13.
> A loading spring 17 for the diaphragm is adjustable by a screwed retainer 16 connected through a rack and pinion device to pins 31 slidable in an outlet connection 28 and adapted to form a bayonet connection with the appliance.

---

### 16. LIQUID MOVING SYSTEMS

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_2885e29b76f1` |
| **Family ID** | `family:8f3c47a7541169f9bfccf3fcd0c1034d666f7b1c` |
| **ID** | `1253973` |
| **Inventores** | EVANS ARTHUR JAMES |
| **Titular** | DISTILLERS CO
CARBON
DIOXIDE |
| **Data** | 17.11.1971 |
| **Fonte** | Patentscope |
| **URL** | [1253973](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135438798&_cid=P21-MR0SB9-98266-1) |
| **Triagem** | exclude |
| **Rota** | screen_only |
| **Motivo da rota** | Patente excluída na triagem. |
| **Score de Triagem** | 3.5/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | Process Control & Instrumentation |
| **Cluster Temático** | Liquid Level Monitoring and Gas Handling |
| **Papel do CO2** | capture_process_stream |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | cycle_or_transfer_subsystem |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | industrial_heat |
| **Foco das Claims** | component_or_operation |
| **Categoria de Exclusão** | generic_tes |
| **Confiança** | 0.56 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> (EN)1,253,973. Liquid level control. DISTILLERS CO. (CARBONDIOXIDE) Ltd. Jan. 13, 1970 [Oct.22, 1968], No. 50060/68. Heading G1H. In equipment in which beer is drawn by a pump from a bulk container through a pipe 1 into a glass cylinder 3 and leaves through a pipe 2, a reed switch 4 is arranged adjacent or above the pipe 1 and a float containing a magnet 9, floats on the beer, the arrangement is such that ascarbondioxidegas collects in the cylinder 3 the beer level 18 and hence the float 5 drops until the magnet 9 actuates switch 4 to close a contact in a switch 10 to isolate a circuit 11, controlling the pump, and complete a circuit to a warning lamp. A valve 7 is manually operated to allow all the gas to escape through a pipe 6 and then closed and a push button operated to resume normal operation. In a modification, Fig. 2 (not shown) the float is provided with two magnets and two reed switches one of which is in circuit with the valve 6.

**Evidências citadas:**
> In equipment in which beer is drawn by a pump from a bulk container through a pipe 1 into a glass cylinder 3 and leaves through a pipe 2, a reed switch 4 is arranged adjacent or above the pipe 1...
> A valve 7 is manually operated to allow all the gas to escape through a pipe 6 and then closed...

---

### 17. TEMPORARY FREEZING OF SOFT OR FLEXIBLE ARTICLES

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_f5e5b1067795` |
| **Family ID** | `family:496cfed63af8a2f3e291b72b4633a23e88258e66` |
| **ID** | `1329637` |
| **Inventores** | N/A |
| **Titular** | DISTILLERS CO
CARBON
DIOXIDE |
| **Data** | 12.09.1973 |
| **Fonte** | Patentscope |
| **URL** | [1329637](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135513929&_cid=P21-MR0SB9-98266-1) |
| **Triagem** | exclude |
| **Rota** | screen_only |
| **Motivo da rota** | Patente excluída na triagem. |
| **Score de Triagem** | 3.5/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | Engenharia de Materiais, Refrigeração |
| **Cluster Temático** | Processamento de Materiais Flexíveis com Refrigeração Controlada |
| **Papel do CO2** | refrigerant_loop |
| **Papel do Armazenamento** | implicit_or_support_storage |
| **Limite Sistêmico** | cycle_or_transfer_subsystem |
| **Tipo de Ciclo** | refrigeration_cycle |
| **Fonte/Sumidouro Térmico** | cooling_or_refrigeration |
| **Foco das Claims** | component_or_operation |
| **Categoria de Exclusão** | cooling_only |
| **Confiança** | 0.59 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> (EN)1329637 Chilling flexible articles DISTILLERS CO (CARBONDIOXIDE) Ltd 29 March 1972 [23 April 1971] 10925/71 Heading F4H A rubber tube 15 is temporarily made rigid by freezing in an enclosure 1 supplied with a liquid refrigerant, e.g. liquidcarbondioxide, through an external control valve 8 having a metering jet 12 and a closure member 13 which is operated to open the valve, the jet communicating with the interior of the enclosure by a duet 3 having a diameter many times that of the jet 12. The tube moves in the same direction as the cold vapour, i.e. right to left, and passes out of the enclosure through an opening in an end wall 5. The enclosure is insulated at 2, The valve is opened intermittently to keep the temperature at the desired level by a pulse generator 14 acting through a solenoid. The provision of a wide duct downstream of the metering jet prevents the jet becoming blocked withcarbondioxideice and dirt. The rigid tube 15 is passed to a braiding machine where it is braided with wire or cord.

**Evidências citadas:**
> "liquidcarbondioxide..."
> "The tube moves in the same direction as the cold vapour, i.e. right to left,..."

---

### 18. Production of
carbon
dioxide
and argon

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_a058d6ba7b0a` |
| **Family ID** | `family:4182dac94ef4ab93116303b8a3595f59094e5316` |
| **ID** | `1125505` |
| **Inventores** | WEIR THOMAS, WHELDON ALFRED GORDON |
| **Titular** | DISTILLERS CO
CARBON
DIOXIDE |
| **Data** | 28.08.1968 |
| **Fonte** | Patentscope |
| **URL** | [1125505](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135308953&_cid=P21-MR0SB9-98266-1) |
| **Triagem** | review |
| **Rota** | manual_review |
| **Motivo da rota** | Triagem indicou revisão humana. |
| **Score de Triagem** | 7.2/10 |
| **Score de Relevância** | 6.5/10 |
| **Nível de Inovação** | Incremental |
| **Domínio Técnico** | Chemical Engineering |
| **Cluster Temático** | Separação de Gases, Combustão |
| **Papel do CO2** | capture_process_stream |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | combustão |
| **Foco das Claims** | Separação de produtos de combustão |
| **Categoria de Exclusão** | industrial_heat_adjacent |
| **Confiança** | 0.75 |
| **Rerank Aplicado** | Sim |
| **Motivo do Rerank** | reranked:decision_confirmed |
| **Revisão Manual** | Sim |
| **Erro LLM** | N/A |

**Abstract:**
> (EN)1,125,505.Carbondioxideand argon. DISTILLERS CO. (CARBONDIOXIDE) Ltd. 30 May, 1967 [23 June, 1966], No. 28050/66. Heading C1A. [Also in Division F4]Carbondioxideand argon are produced by subjecting a mixture of argon, oxygen, and acarbon-containing compound or compounds to complete combustion and separating the combustion products to obtain a CO 2  fraction and an Ar fraction. The mixture of Ar and oxygen may be obtained from the liquefaction and fractional distillation of air. The combustible compound may be a heavy fuel oil. The combustion products may be separated by subjecting them to cooling, drying, liquefaction and distillation steps. Should a sulphur-impurecarbon-containing compound be used, sulphurdioxidemay be removed in the distillation step as a high boiling base product,

**Avaliação do LLM:**
Esta patente descreve um processo para a produção de dióxido de carbono e argônio através da combustão completa de uma mistura contendo argon, oxigênio e um composto carbonáceo, seguido pela separação dos produtos de combustão. O processo utiliza etapas como resfriamento, secagem, liquefação e destilação para obter as frações desejadas.

**Extração Estruturada:**
- **Problema:** O problema abordado é a produção eficiente de dióxido de carbono e argônio a partir de uma mistura gasosa, buscando um método de separação eficaz dos componentes.
- **Solução:** A solução proposta envolve a combustão da mistura de gases e subsequente separação por meio de processos de destilação, utilizando etapas como resfriamento e liquefação para isolar o dióxido de carbono e o argônio.
- **Maturidade:** Intermediária

**Achados-chave:**
- O processo utiliza uma mistura de argon, oxigênio e um composto carbonáceo, incluindo óleo combustível pesado, para a combustão.
- A separação dos produtos de combustão é realizada através de resfriamento, secagem, liquefação e destilação.

**Vantagens alegadas:**
- Produção simultânea de dióxido de carbono e argônio.
- Utilização de componentes de ar comprimido como fonte de argon e oxigênio.

**Limitações:**
- O processo é descrito como uma abordagem geral de combustão e destilação, sem foco específico em captura ou armazenamento de CO2.
- A remoção de enxofre do composto carbonáceo é mencionada apenas como um passo opcional.

**Aplicações potenciais:**
- Produção de gases industriais (dióxido de carbono e argônio).
- Processos de destilação e separação de componentes gasosos.

**Evidências citadas:**
> "subjecting a mixture of argon, oxygen, and a carbon-containing compound..."
> The description focuses on separation steps rather than CO2 storage or utilization.

---

### 19. IMPROVEMENTS IN OR RELATING TO FIRE EXTINGUISHING COMPOSITIONS

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_0170e12f0248` |
| **Family ID** | `family:8f727f23456e3a1d56f525161457f4b4056c7aea` |
| **ID** | `1236064` |
| **Inventores** | WHELDON ALBERT GORDON |
| **Titular** | DISTILLERS CO
CARBON
DIOXIDE |
| **Data** | 16.06.1971 |
| **Fonte** | Patentscope |
| **URL** | [1236064](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135420945&_cid=P21-MR0SB9-98266-1) |
| **Triagem** | exclude |
| **Rota** | screen_only |
| **Motivo da rota** | Patente excluída na triagem. |
| **Score de Triagem** | 3.5/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | Extinção de Incêndio |
| **Cluster Temático** | Compostos Extintores e Fluidos Refrigerantes |
| **Papel do CO2** | working_fluid |
| **Papel do Armazenamento** | implicit_or_support_storage |
| **Limite Sistêmico** | cycle_or_transfer_subsystem |
| **Tipo de Ciclo** | refrigeration_cycle |
| **Fonte/Sumidouro Térmico** | firefighting |
| **Foco das Claims** | component_or_operation |
| **Categoria de Exclusão** | generic_tes |
| **Confiança** | 0.59 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> (EN)1,236,064. Fire extinguishing slurries. DISTILLERS CO. (CARBONDIOXIDE) Ltd. 27 Oct., 1969 [19 Oct., 1968], No. 49685/68. Heading ASA. A slurry of solid CO 2  in a liquid fireextinguishing agent for fire-fighting purposes is produced by mixing liquid Co 2  and the liquid extinguishant under pressure such that a solution of one in the other is formed, and releasing the solution at a lower pressure when the slurry is required. Bromochlorodifluoromethane (BCF) is preferred. The two liquids are pumped into a container maintained at 30‹ to -80‹C., e.g. in a ratio 3:1 CO 2 :BCF by volume. The solution may be released via a cyclone separator.

**Evidências citadas:**
> Fire extinguishing slurries. DISTILLERS CO. (CARBONDIOXIDE) Ltd. 27 Oct., 1969 [19 Oct., 1968], No. 49685/68.
> The two liquids are pumped into a container maintained at 30‹ to -80‹C.

---

## 🧾 Fila de Revisão Manual

- rec_6ef9ca6982e5 (1429678) | rota=manual_review | motivo=Triagem indicou revisão humana. | erro_llm=N/A
- rec_bb7ef455d20e (US8119091B2) | rota=manual_review | motivo=Triagem indicou revisão humana. | erro_llm=N/A
- rec_f0f68dc78688 (US12401048B1) | rota=manual_review | motivo=Triagem indicou revisão humana. | erro_llm=N/A
- rec_a058d6ba7b0a (1125505) | rota=manual_review | motivo=Triagem indicou revisão humana. | erro_llm=N/A
- rec_ca73a4e50a56 (2047588) | rota=manual_review | motivo=Triagem indicou revisão humana. | erro_llm=N/A
- rec_92b6895cc998 (US2665972A) | rota=manual_review | motivo=Triagem indicou revisão humana. | erro_llm=N/A

---

## 🔬 Análise Comparativa

### 1. Panorama Geral

- O conjunto comparativo agrega 12 patente(s) e nao deve ser tratado como bloco homogeneo: ha um nucleo direto, fronteiras tecnicas em revisao e adjacencias uteis apenas para delimitar whitespace [IDs: US12202743B2, US12478916B2, US20240059978A1, WO2021239747A1, US20230191322A1, WO2024208966A1, 1125505, 1429678, 2047588, US12401048B1, US2665972A, US8119091B2]
- O subgrupo mais diretamente alinhado ao núcleo da query é US12202743B2, com foco em armazenamento de CO2, compressão/expansão e controle termodinâmico do meio armazenado [IDs: US12202743B2]
- 1125505, 1429678, 2047588, US12401048B1, US2665972A, US8119091B2 formam a fronteira tecnica: sao casos proximos do problema, mas ainda ambiguos quanto ao papel exato do CO2 no armazenamento ou na funcao arquitetural central [IDs: 1125505, 1429678, 2047588, US12401048B1, US2665972A, US8119091B2]
- 1125505 entram como adjacencia exploratoria: tratam CO2 principalmente como fluido de trabalho em transferencia termica ou distribuicao de energia, de modo que ajudam a delimitar combinacoes pouco cobertas sem virar evidencia de cobertura consolidada [IDs: 1125505]

## Análise Comparativa de Patentes Relacionadas a Captura de Dióxido de Carbono (CO2)

**1. Panorama Geral**

A análise das patentes fornecidas revela um estado da arte diversificado na captura de dióxido de carbono, com foco principal em abordagens diretas e indiretas. O conjunto de patentes demonstra uma clara tendência para a captura direta de CO2 do ar ou da água do mar, utilizando membranas, sorventes sólidos e processos eletroquímicos [IDs: US12202743B2, US12478916B2, US20230191322A1, WO2021239747A1].  No entanto, também existem abordagens que exploram a conversão de CO2 em produtos químicos de valor agregado, como hidrocarbonetos [IDs: US20240059978A1], e métodos para a separação e purificação do CO2 [IDs: US2665972A].  Além disso, há patentes que se concentram em sistemas de controle para o manuseio de CO2 líquido [IDs: 1429678] e na utilização de CO2 como fluido de trabalho em baterias [IDs: US12401048B1], demonstrando uma fronteira técnica que busca explorar novas aplicações do composto.  Finalmente, a patente WO2024208966A1 representa uma abordagem mais abrangente com foco na integração de processos e tecnologias de captura em sistemas de ciclo fechado [IDs: WO2024208966A1]. A patente 1125505, embora em fase de revisão, fornece contexto sobre métodos tradicionais de separação.

**2. Tendências Identificadas**

*   **Captura Direta do Ar:** Uma tendência dominante é a captura direta de CO2 do ar, utilizando tecnologias como adsorção e regeneração [IDs: US12478916B2, WO2021239747A1, US20230191322A1].
*   **Membranas Compostas:** O uso de membranas compostas para a remoção seletiva de CO2 da água do mar é uma abordagem promissora [IDs: US12202743B2].
*   **Conversão Química:** A conversão de CO2 em produtos químicos de valor agregado, como hidrocarbonetos, está ganhando atenção [IDs: US20240059978A1].
*   **Integração de Processos:**  Há um esforço crescente para integrar a captura de CO2 com outros processos industriais, visando otimizar o uso de recursos e reduzir custos [IDs: WO2024208966A1, US8119091B2].
*   **Soluções Aquosas:** O uso de soluções aquosas contendo carbonatos para a captura de CO2 é uma abordagem comum [IDs: US8119091B2, 1125505].

**3. Whitespaces e Oportunidades**

*   **Eficiência Energética em Captura do Ar:** A maior parte das patentes focada na captura direta do ar não aborda a questão da eficiência energética, que é um dos maiores desafios dessa tecnologia [IDs: US12478916B2, WO2021239747A1, US20230191322A1]. Existe uma oportunidade para desenvolver sistemas de captura do ar com menor consumo de energia.
*   **Membranas Inteligentes:** O desenvolvimento de membranas inteligentes que respondam a mudanças nas condições ambientais (temperatura, umidade) poderia melhorar a eficiência da remoção de CO2 [IDs: US12202743B2].
*   **Integração com Energias Renováveis:** A integração da captura de CO2 com fontes de energia renovável (solar, eólica) pode reduzir o impacto ambiental do processo [IDs: US20240059978A1, WO2024208966A1].
*   **Novos Materiais Adsorventes:** A busca por novos materiais adsorventes com maior capacidade de captura de CO2 e menor custo é uma área promissora [IDs: US12478916B2, WO2021239747A1].
*   **Processos em Escala Industrial:** A maioria das patentes se concentra em tecnologias em escala laboratorial ou piloto. Há uma necessidade de desenvolver processos que possam ser implementados em escala industrial [IDs: US20230191322A1, WO2024208966A1].

**4. Recomendações**

*   **Pesquisa em Eficiência Energética:** Investir em pesquisa para desenvolver tecnologias de captura de CO2 com menor consumo de energia é crucial.
*   **Desenvolvimento de Materiais Avançados:** Explorar novos materiais adsorventes e membranas com propriedades otimizadas pode aumentar a eficiência da captura.
*   **Integração com Energias Renováveis:**  Priorizar a integração da captura de CO2 com fontes de energia renovável para criar sistemas sustentáveis.
*   **Estudos de Viabilidade em Escala Industrial:** Realizar estudos de viabilidade para avaliar a implementação das tecnologias de captura de CO2 em escala industrial.

**5. Ranking Final**

1.  **US12478916B2** (Captura Direta do Ar - Eficiência e Escalabilidade) [IDs: US12478916B2]
2.  **US12202743B2** (Membranas Compostas - Potencial de Aplicação em Água Do Mar) [IDs: US12202743B2]
3.  **WO2021239747A1** (Captura do Ar com Estruturas Adsorventes – Escalabilidade e Integração) [IDs: WO2021239747A1]
4.  **US20230191322A1** (Sistema Eletroquímico de Captura - Inovação na Tecnologia) [IDs: US20230191322A1]
5.  **US20240059978A1** (Conversão Química do CO2 – Valor Agregado) [IDs: US20240059978A1]
6.  **WO2024208966A1** (Integração de Processos - Sistema Completo) [IDs: WO2

### 3. Whitespaces e Oportunidades

- O whitespace mais promissor esta na combinacao entre arquiteturas de ciclo/transferencia termica com CO2 e armazenamento explicito do inventario termico, porque esses elementos ainda aparecem fragmentados entre nucleo, fronteira e adjacencia [IDs: US12202743B2, US12478916B2, US20240059978A1, WO2021239747A1]
- Gestao termica transiente, subresfriamento e acoplamentos com captura/reatores aparecem de forma lateral; isso sugere oportunidade em claims de controle, operacao multi-regime e integracao de processo ainda pouco amarradas ao armazenamento central [IDs: 1125505, US12478916B2, US20240059978A1, WO2021239747A1]
- As patentes em review delimitam fronteiras tecnicas onde o papel do CO2 ainda esta ambiguo entre meio armazenado, fluido de trabalho e interface de troca termica; esse tipo de ambiguidade costuma ser um bom proxy para whitespace exploravel com recorte arquitetural mais especifico [IDs: 1125505, 1429678, 2047588, US12401048B1]

### 4. Recomendações

- Priorizar arquiteturas centradas em armazenamento explícito de CO2 e controle termodinâmico rigoroso [IDs: US12202743B2]

### 5. Ranking Final

1. **US12202743B2** — armazenamento termico explicito como parte central; score 8.2/10 [IDs: US12202743B2]
2. **US12478916B2** — armazenamento termico explicito como parte central; score 8.1/10 [IDs: US12478916B2]
3. **US20240059978A1** — armazenamento termico explicito como parte central; score 8.1/10 [IDs: US20240059978A1]
4. **WO2021239747A1** — armazenamento termico explicito como parte central; score 8.1/10 [IDs: WO2021239747A1]
5. **US20230191322A1** — armazenamento termico explicito como parte central; score 8.0/10 [IDs: US20230191322A1]
6. **WO2024208966A1** — armazenamento termico explicito como parte central; score 7.7/10 [IDs: WO2024208966A1]
7. **1125505** — armazenamento termico explicito como parte central; ênfase em refrigeração/sub-resfriamento, mais adjacente ao núcleo da query; score 6.5/10 [IDs: 1125505]
8. **1429678** — CO2 aparece principalmente como fluido de trabalho; armazenamento termico explicito como parte central; score 6.5/10 [IDs: 1429678]
9. **2047588** — armazenamento termico explicito como parte central; score 6.5/10 [IDs: 2047588]
10. **US12401048B1** — CO2 aparece principalmente como fluido de trabalho; armazenamento aparece mais como subsistema de apoio; score 6.5/10 [IDs: US12401048B1]
11. **US2665972A** — alinhamento técnico sustentado pelas evidências extraídas; score 6.5/10 [IDs: US2665972A]
12. **US8119091B2** — armazenamento aparece mais como subsistema de apoio; score 6.5/10 [IDs: US8119091B2]

### 6. Mapa de Evidências por ID

- **Baterias com Fluidos Alternativos** [IDs: US12401048B1]
- **CO2 Capture and Utilization - Aqueous Solutions** [IDs: US8119091B2]
- **Economic Optimization** [IDs: US12478916B2]
- **Engenharia Química / Engenharia Ambiental** [IDs: WO2024208966A1]
- **Engenharia Química / Materiais** [IDs: US12202743B2]
- **Engenharia Química / Processamento de Gases** [IDs: US20230191322A1]
- **Engenharia Química / Tecnologias de Captura de Carbono** [IDs: WO2021239747A1]
- **Produção e Purificação de Dióxido de Carbono** [IDs: US2665972A]
- **Química, Catálise, Engenharia Química** [IDs: US20240059978A1]
- **Reciclagem de Materiais para Fundição com Utilização de CO2** [IDs: 2047588]
- **Separação de Gases, Combustão** [IDs: 1125505]
- **Sistemas de Controle Automatizado para Manipulação de Fluidos Refrigerados** [IDs: 1429678]

### 7. Ranking por ID

1. **US12202743B2** — score 8.2/10 [IDs: US12202743B2]
2. **US12478916B2** — score 8.1/10 [IDs: US12478916B2]
3. **US20240059978A1** — score 8.1/10 [IDs: US20240059978A1]
4. **WO2021239747A1** — score 8.1/10 [IDs: WO2021239747A1]
5. **US20230191322A1** — score 8.0/10 [IDs: US20230191322A1]
6. **WO2024208966A1** — score 7.7/10 [IDs: WO2024208966A1]
7. **1125505** — score 6.5/10 [IDs: 1125505]
8. **1429678** — score 6.5/10 [IDs: 1429678]
9. **2047588** — score 6.5/10 [IDs: 2047588]
10. **US12401048B1** — score 6.5/10 [IDs: US12401048B1]
11. **US2665972A** — score 6.5/10 [IDs: US2665972A]
12. **US8119091B2** — score 6.5/10 [IDs: US8119091B2]

---

## 🧭 Matriz de Whitespaces

- **Patentes selecionadas:** 12
- **Núcleo:** 6
- **Fronteira:** 6
- **Adjacência:** 0

- **hybrid_cycle_storage_architecture**: Combinar ciclos/transferencia com CO2 e armazenamento termico explicitamente reivindicado ainda aparece fragmentado entre nucleo e borda tecnica. [core=US12202743B2, US12478916B2, US20240059978A1 | frontier=1125505, 1429678, 2047588 | adjacent=N/A]
- **control_and_operability_claims**: Ha espaco para claims de controle, operacao transiente e integracao de processo onde o papel do CO2 e do armazenamento ainda esta ambiguo. [core=US12202743B2, US12478916B2, US20240059978A1 | frontier=1429678 | adjacent=N/A]

---

## ℹ️ Informações do Sistema

- **Gerado por:** Agente de Web Scraping de Patentes
- **Modelo LLM:** gemma3:4b
- **Data de geração:** 30/06/2026 15:12:39
- **Query de busca:** `carbon dioxide`
- **Status da execução:** completed
- **Tempo total:** 102.1s
- **LLM disponível:** sim
- **Fila de revisão manual:** 6 itens
- **Snapshot hash:** `fc9fc220794fa77369ec6b47564b741a402e20f1d75be6ca183440d59e03eeae`
- **Features habilitadas:** require_evidence, enable_thematic_clusters, enable_structural_roles, enable_screening_rerank, enable_prisma, enable_snapshot, enable_comparative_analysis, enable_whitespace_analysis, enable_manual_review_queue
- **Features desabilitadas:** nenhum
- **Versão do pipeline:** 1.1
- **Thresholds snapshot:** include=0.0, review=0.0
- **Cache LLM:** 37 hits, 1 misses, 104 entradas
- **Status do rascunho:** ready