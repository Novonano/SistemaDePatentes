# 📋 Relatório de Análise de Patentes

**Data:** 24/07/2026 13:36:10
**Busca:** `carbon dots CO2 laser`
**Total de patentes encontradas:** 18
**Modelo de avaliação:** gemma3:4b

---

## 🧭 Protocolo Metodológico

- **Versão:** 1.0
- **Fontes:** Google Patents, Patentscope
- **Etapas:** identification, deduplication, screening, manual_review, full_extraction, synthesis
- **Threshold inclusão:** 7.0
- **Threshold revisão:** 4.5
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
- **Patentes únicas:** 18
- **Duplicatas removidas:** 1
- **Triadas:** 18
- **Incluídas:** 0
- **Em revisão manual:** 7
- **Excluídas:** 11
- **Extrações completas:** 7
- **Sem abstract/snippet:** 1
- **Sem ID:** 0
- **Identidade por conteúdo:** 0
- **Identidade fallback:** 0
- **Duplicatas por família removidas:** 1
- **Falhas de triagem LLM:** 0
- **Falhas totais LLM:** 0

## 🧭 Fluxo PRISMA-Like

- **Identificação:** 19 bruto(s), 18 único(s), 1 duplicata(s) removida(s)
- **Triagem:** 18 triado(s), 0 incluído(s), 7 em revisão, 11 excluído(s)
- **Elegibilidade:** 7 extração(ões) completa(s), 7 revisão(ões) manual(is), 0 adiada(s)
- **Cobertura:** 1 sem abstract/snippet, 0 sem ID
- **Síntese:** 7 registro(s) analisado(s)

## 🧠 Contexto Compartilhado

- **Top patentes no contexto:** 0
- **Clusters no contexto:** 0
- **Roteamento agregado:** 2 rota(s)
- **Slots ativos:** N/A

## ⏱️ Métricas por Etapa

| Etapa | Status | Duração | Itens | Detalhes |
|---|---|---:|---:|---|
| setup | ok | 3.72s | 1 | Verificação do modelo Ollama |
| search | ok | 92.89s | 19 | 18 patentes únicas após dedupe |
| screening | ok | 0.01s | 18 | 0 incluídas, 7 revisão |
| comparative_analysis | ok | 0.00s | 18 | Síntese comparativa gerada |
| whitespace_analysis | ok | 0.00s | 7 | Whitespace analysis estruturada gerada |
| reporting | ok | 0.01s | 18 | Relatórios Markdown e JSON |
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
- **Latência média:** 3.719s
- **Latência máxima:** 3.719s

### screening

- **Chamadas:** 18
- **Sucessos:** 18
- **Falhas:** 0
- **Retries:** 0
- **Cache hits:** 18
- **Pulos por degradação:** 0
- **Latência média:** 0.0s
- **Latência máxima:** 0.0s

### rerank

- **Chamadas:** 7
- **Sucessos:** 7
- **Falhas:** 0
- **Retries:** 0
- **Cache hits:** 7
- **Pulos por degradação:** 0
- **Latência média:** 0.0s
- **Latência máxima:** 0.0s

### evaluation

- **Chamadas:** 7
- **Sucessos:** 7
- **Falhas:** 0
- **Retries:** 0
- **Cache hits:** 7
- **Pulos por degradação:** 0
- **Latência média:** 0.0s
- **Latência máxima:** 0.0s

### comparative

- **Chamadas:** 1
- **Sucessos:** 1
- **Falhas:** 0
- **Retries:** 0
- **Cache hits:** 1
- **Pulos por degradação:** 0
- **Latência média:** 0.0s
- **Latência máxima:** 0.0s

## 🔎 Observabilidade Estruturada

### Rotas

- **screen_only**: total=11, include=0, review=0, exclude=11, llm_errors=0
- **manual_review**: total=7, include=0, review=7, exclude=0, llm_errors=0

### Fontes

- **EPO**: bruto=0, duração=0.00s, diagnósticos=config_missing=1
- **GooglePatents**: bruto=9, duração=26.31s, diagnósticos=nenhum
- **Patentscope**: bruto=10, duração=66.57s, diagnósticos=nenhum

### Falhas

- **Erros de execução:** 0
- **Registros com erro de LLM:** 0
- **Falhas totais do LLM:** 0
- **LLM por operação:** comparative(falhas=0, retries=0, skips=0), evaluation(falhas=0, retries=0, skips=0), healthcheck(falhas=0, retries=0, skips=0), rerank(falhas=0, retries=0, skips=0), screening(falhas=0, retries=0, skips=0)
- **Scraper por tipo de sinal:** config_missing=1

## 📊 Resumo Executivo

**Score médio de relevância:** 0.0/10

| # | Patente | Score | Inovação | Domínio |
|---|---------|-------|----------|---------|
| 1 | [CN205569064U](https://patents.google.com/patent/CN205569064U/en) — Super pulse carbon dioxide dot matrix laser therapy apparatu... | 🟡 6.5 (review) | Incremental | Laser Therapy & Biomedical Engineering |
| 2 | [US20240075453A1](https://patents.google.com/patent/US20240075453A1/en) — Selective carbon binding on carbon quantum dots | 🟡 6.5 (review) | Incremental | Materiais Avançados / Química de Carbonos |
| 3 | [US7453918B2](https://patents.google.com/patent/US7453918B2/en) — Pulsed RF high pressure CO2 lasers | 🟡 6.5 (review) | Incremental | Laser Technology |
| 4 | [CN119742647A](https://patents.google.com/patent/CN119742647A/en) — A 10,000-watt radio frequency fast axial flow carbon dioxide... | 🟡 6.5 (review) | Incremental | Laser Technology, Termodinâmica, Sistemas de Resfriamento |
| 5 | [US20240132362A1](https://patents.google.com/patent/US20240132362A1/en) — Quantum dot sensitized photoreduction of carbon dioxide | 🟡 6.3 (review) | Incremental | Fotocatalise, Química de Materiais |
| 6 | [US20210349011A1](https://patents.google.com/patent/US20210349011A1/en) — Laser radar system apparatus for multi-wavelength measuremen... | 🟡 4.9 (review) | Incremental | Remote Sensing & Atmospheric Monitoring |
| 7 | [WO2013154949A2](https://patents.google.com/patent/WO2013154949A2/eng) — Pulsed co2 laser output-pulse shape and power control | 🟡 4.0 (review) | Incremental | Laser Technology & Thermal Management |
| 8 | [US12384680B2](https://patents.google.com/patent/US12384680B2/en) — Laser-induced carbon nanostructures | 🔴 0.0 (exclude) | N/A | Ciência dos Materiais, Nanotecnologia |
| 9 | [CN109705627A](https://patents.google.com/patent/CN109705627A/en) — A method of mesoporous silicon dioxide modified carbon dots ... | 🔴 0.0 (exclude) | N/A | Ciência dos Materiais, Nanotecnologia |
| 10 | [20010048797](https://patentscope.wipo.int/search/en/detail.jsf?docId=US39333852&_cid=P22-MRYZFR-15194-1) — Fully indentifiable optical fiber assemblies | 🔴 0.0 (exclude) | N/A | Engenharia de Materiais, Óptica |
| 11 | [WO/2001/068776](https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2001068776&_cid=P22-MRYZFR-15194-1) — FULLY IDENTIFIABLE OPTICAL FIBER ASSEMBLIES
(FR)
ENSEMBLES D... | 🔴 0.0 (exclude) | N/A | Materiais e Composição |
| 12 | [WO/2006/067380](https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2006067380&_cid=P22-MRYZFR-15194-1) — MARKING OF PIPES
(FR)
MARQUAGE DE TUYAUX | 🔴 0.0 (exclude) | N/A | Engenharia de Materiais, Processamento Industrial |
| 13 | [20240002621](https://patentscope.wipo.int/search/en/detail.jsf?docId=US418579840&_cid=P22-MRYZFR-15194-1) — eTPE
Laser
Marking | 🔴 0.0 (exclude) | N/A | Materiais Poliméricos e Processamento |
| 14 | [20180003565](https://patentscope.wipo.int/search/en/detail.jsf?docId=US209523108&_cid=P22-MRYZFR-15194-1) — Advanced multi-element consumable-disposable products | 🔴 0.0 (exclude) | N/A | Produtos de Consumo |
| 15 | [20140221528](https://patentscope.wipo.int/search/en/detail.jsf?docId=US106950238&_cid=P22-MRYZFR-15194-1) — Advanced multi-element consumable-disposable products | 🔴 0.0 (exclude) | N/A | Engenharia de Produtos |
| 16 | [WO/2022/069664](https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2022069664&_cid=P22-MRYZFR-15194-1) — eTPE
LASER
MARKING
(FR)
MARQUAGE LASER ETPE | 🔴 0.0 (exclude) | N/A | Materiais Poliméricos e Processamento |
| 17 | [6556273](https://patentscope.wipo.int/search/en/detail.jsf?docId=US40134930&_cid=P22-MRYZFR-15194-1) — System for providing pre-processing machine readable encoded... | 🔴 0.0 (exclude) | N/A | Fotografia, Codificação de Dados |
| 18 | [WO/2001/035163](https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2001035163&_cid=P22-MRYZFR-15194-1) — A SYSTEM FOR PROVIDING PRE-PROCESSING MACHINE READABLE ENCOD... | 🔴 0.0 (exclude) | N/A | Processamento de Imagem Cinematográfica |

---

## 🔍 Análise Detalhada das Patentes

### 1. Super pulse carbon dioxide dot matrix laser therapy apparatus

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_b11edeb58983` |
| **Family ID** | `family:370c91b915a68a56fbd9c7397b9d93cfdff09fc6` |
| **ID** | `CN205569064U` |
| **Inventores** | éå»ºè´¢ |
| **Titular** | Shanghai Muorange Medical Devices Co Ltd |
| **Data** | 2016-09-14 |
| **Fonte** | Google Patents |
| **URL** | [CN205569064U](https://patents.google.com/patent/CN205569064U/en) |
| **Triagem** | review |
| **Rota** | manual_review |
| **Motivo da rota** | Triagem indicou revisão humana. |
| **Score de Triagem** | 6.4/10 |
| **Score de Relevância** | 6.5/10 |
| **Nível de Inovação** | Incremental |
| **Domínio Técnico** | Laser Therapy & Biomedical Engineering |
| **Cluster Temático** | Laser-Based Surface Treatment Systems |
| **Papel do CO2** | working_fluid |
| **Papel do Armazenamento** | implicit_or_support_storage |
| **Limite Sistêmico** | cycle_or_transfer_subsystem |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | Laser Beam |
| **Foco das Claims** | Escaneamento e foco do laser em aplicações terapêuticas |
| **Categoria de Exclusão** | cooling_only |
| **Confiança** | 0.75 |
| **Rerank Aplicado** | Sim |
| **Motivo do Rerank** | reranked:decision_confirmed |
| **Revisão Manual** | Sim |
| **Erro LLM** | N/A |

**Abstract:**
> AbstractThe utility model relates to a super pulse carbon dioxide dot matrix laser therapy apparatus, including laser high voltage power supply, laser pipe, focus module, X axle galvanometer scanning system, Y axle galvanometer scanning system, CPU the main control panel, image sensor, laser pipe are connected with laser high voltage power supply, arrival work plane after laser beam line focus module in proper order that the laser pipe sent, X axle galvanometer scanning system, the Y axle galvanometer scanning system, CPU the main control panel respectively with laser high voltage power supply, focus on module, image sensor, X axle and Y axle galvanometer scanning galvanometer scanning 2. Through X axle and Y axle galvanometer scanning system, laser therapy apparatus can carry out flat scanning treatment on a large scale in the XY plane, through the focus module, can adjust the laser focusing plane to treatment skin depths or exceed the symptom of epidermis, through setting up image sensor, can and plan the X axle in advance and Y axle route according to image colour and shape selection laser intensity, avoided human error unnecessarily shining healthy skin.

**Avaliação do LLM:**
Esta patente descreve um dispositivo de terapia a laser que utiliza pontos de carboneto de CO2 e um sistema de varredura galvânica para tratamento de superfície. O sistema permite o escaneamento plano em grande escala e ajuste do foco do laser para diferentes profundidades de penetração na pele. A imagem sensor é utilizada para otimizar a intensidade do laser, evitando danos à pele saudável.

**Extração Estruturada:**
- **Problema:** O problema abordado é a necessidade de um dispositivo de terapia a laser que possa realizar escaneamento preciso e controlado em áreas extensas da pele, minimizando o risco de dano aos tecidos saudáveis.
- **Solução:** A solução proposta é um aparelho de terapia a laser com pontos de carboneto de CO2 e um sistema de varredura galvânica que permite o escaneamento plano em grande escala e ajuste do foco do laser, utilizando um sensor de imagem para otimizar a intensidade.
- **Maturidade:** Inicial

**Achados-chave:**
- Utilização de pontos de carboneto de CO2 para foco do laser.
- Sistema de varredura galvânica para escaneamento plano em grande escala.
- Sensor de imagem integrado para controle da intensidade do laser.

**Vantagens alegadas:**
- Escaneamento plano em grande escala no XY plane
- Ajuste do foco do laser para diferentes profundidades de tratamento
- Minimização de danos à pele saudável através do sensor de imagem

**Limitações:**
- A descrição não detalha o mecanismo exato da super pulsação ou a otimização do ciclo de laser.
- O papel do CO2 como gás ou componente central para o processo de laser é ambíguo.

**Aplicações potenciais:**
- Tratamento dermatológico superficial
- Terapia a laser para rejuvenescimento da pele
- Aplicações em medicina estética

**Evidências citadas:**
> The utility model relates to a super pulse carbon dioxide dot matrix laser therapy apparatus...
> X axle galvanometer scanning system, the Y axle galvanometer scanning system...

---

### 2. Selective carbon binding on carbon quantum dots

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_dd866e6d7249` |
| **Family ID** | `family:b2d64eee6e72c39e1a0ee50e6a5c49eb66a6af26` |
| **ID** | `US20240075453A1` |
| **Inventores** | Michael Broud, David P. Harper, David Keffer |
| **Titular** | University of Tennessee Research Foundation |
| **Data** | 2024-03-07 |
| **Fonte** | Google Patents; Patentscope |
| **URL** | [US20240075453A1](https://patents.google.com/patent/US20240075453A1/en) |
| **Triagem** | review |
| **Rota** | manual_review |
| **Motivo da rota** | Triagem indicou revisão humana. |
| **Score de Triagem** | 7.1/10 |
| **Score de Relevância** | 6.5/10 |
| **Nível de Inovação** | Incremental |
| **Domínio Técnico** | Materiais Avançados / Química de Carbonos |
| **Cluster Temático** | Adsorção Seletiva de Gases / Carbon Dots |
| **Papel do CO2** | stored_thermodynamic_medium |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | CO2 |
| **Foco das Claims** | Preparação e uso de carbon dots para adsorção seletiva de CO2. |
| **Categoria de Exclusão** | industrial_heat_adjacent |
| **Confiança** | 0.75 |
| **Rerank Aplicado** | Sim |
| **Motivo do Rerank** | reranked:decision_confirmed |
| **Revisão Manual** | Sim |
| **Erro LLM** | N/A |

**Abstract:**
> AbstractCarbon quantum dots having selected adsorption of carbon dioxide over nitrogen and oxygen can be prepared by amine modification or nitrogen doping of hydrocarbon-based carbon quantum dots. The carbon quantum dots can be used in various applications for the adsorption of carbon dioxide from the atmosphere and for treating industrial processes that generate carbon dioxide. The carbon quantum dots can be synthesized from lignin and can be paired with a porous activated carbon surface to create a renewable composite material with increased selective adsorption of carbon dioxide.

**Avaliação do LLM:**
Esta patente descreve a preparação de carbon dots utilizando lignin e um suporte de carbono poroso para adsorver seletivamente CO2, com foco em aplicações ambientais como tratamento de processos industriais que geram CO2. A patente explora a modificação química dos carbon dots para aumentar a capacidade de absorção de CO2, mas não aborda diretamente a aplicação em lasers.

**Extração Estruturada:**
- **Problema:** A necessidade de materiais eficientes para a adsorção seletiva de CO2, especialmente em ambientes industriais.
- **Solução:** A solução proposta é a síntese de carbon dots utilizando lignin e um suporte de carbono poroso, com modificação química para melhorar a capacidade de adsorção de CO2.
- **Maturidade:** Inicial

**Achados-chave:**
- Carbon quantum dots podem ser preparados através da modificação com aminas ou dopagem com nitrogênio de carbonos baseados em hidrocarbonetos.
- A combinação de carbon dots sintetizados a partir de lignin com um suporte de carbono poroso resulta em um material composto com aumento na adsorção seletiva de CO2.

**Vantagens alegadas:**
- Adsorção seletiva de CO2 sobre nitrogênio e oxigênio.
- Utilização de materiais renováveis (lignina).

**Limitações:**
- A patente não aborda explicitamente a aplicação dos carbon dots em lasers.
- O impacto da combinação com um suporte de carbono poroso na eficiência do laser não é detalhado.

**Aplicações potenciais:**
- Tratamento de processos industriais que geram CO2.
- Adsorção de CO2 da atmosfera.

**Evidências citadas:**
> The carbon quantum dots can be used in various applications for the adsorption of carbon dioxide from the atmosphere...
> The carbon quantum dots can be paired with a porous activated carbon surface to create a renewable composite material with increased selective adsorption of carbon dioxide.

---

### 3. Pulsed co2 laser output-pulse shape and power control

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_58aec1c9302f` |
| **Family ID** | `family:672607679694fa88e4989a41bac5e04683254ffd` |
| **ID** | `WO2013154949A2` |
| **Inventores** | Peter Rosenthal, John Kennedy, Vern SEGUIN, David ALLIE |
| **Titular** | Coherent Inc |
| **Data** | 2013-10-17 |
| **Fonte** | Google Patents |
| **URL** | [WO2013154949A2](https://patents.google.com/patent/WO2013154949A2/eng) |
| **Triagem** | review |
| **Rota** | manual_review |
| **Motivo da rota** | Triagem indicou revisão humana. |
| **Score de Triagem** | 5.0/10 |
| **Score de Relevância** | 4.0/10 |
| **Nível de Inovação** | Incremental |
| **Domínio Técnico** | Laser Technology & Thermal Management |
| **Cluster Temático** | Controle de Potência em Sistemas Laser |
| **Papel do CO2** | working_fluid |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | cycle_or_transfer_subsystem |
| **Tipo de Ciclo** | power_or_work_cycle |
| **Fonte/Sumidouro Térmico** | laser CO2 |
| **Foco das Claims** | component_or_operation |
| **Categoria de Exclusão** | co2_working_fluid_only |
| **Confiança** | 0.66 |
| **Rerank Aplicado** | Sim |
| **Motivo do Rerank** | reranked:decision_confirmed |
| **Revisão Manual** | Sim |
| **Erro LLM** | N/A |

**Avaliação do LLM:**
Esta patente descreve um laser CO2 pulsado com controle de potência, utilizando CO2 como fluido de trabalho. Embora não mencione explicitamente carbon dots, o documento aborda sistemas de controle de potência e ciclagem de fluidos, que podem ser relevantes para aplicações envolvendo emissão de luz por carbon dots.

**Extração Estruturada:**
- **Problema:** O problema técnico abordado é otimizar a forma da pulsação e o controle de potência em um laser CO2 pulsado.
- **Solução:** A patente propõe um sistema que controla a forma da pulsação e a potência do laser CO2, permitindo ajustes precisos na saída do laser.
- **Maturidade:** Intermediária

**Achados-chave:**
- O documento descreve um sistema de laser CO2 com controle de potência.
- Utiliza o CO2 como fluido de trabalho dentro de um subconjunto de ciclo ou transferência.

**Vantagens alegadas:**
- Controle preciso da forma da pulsação
- Ajuste da potência do laser

**Limitações:**
- Não menciona explicitamente o uso de carbon dots.
- Foco no controle de potência e ciclagem de fluidos.

**Aplicações potenciais:**
- Laser CO2 para corte, soldagem ou gravação

**Evidências citadas:**
> 'Pulsed CO2 laser output-pulse shape and power control'
> 'Cycle or transfer subsystem'

---

### 4. Quantum dot sensitized photoreduction of carbon dioxide

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_48b16c3d81aa` |
| **Family ID** | `family:d428beb9e925d697f23205d1a217bd43d92b5cdc` |
| **ID** | `US20240132362A1` |
| **Inventores** | Francesca Arcudi, Luka Dordevic, Emily A. Weiss, Benjamin Nagasing, Samuel l. Stupp |
| **Titular** | Northwestern University |
| **Data** | 2024-04-25 |
| **Fonte** | Google Patents |
| **URL** | [US20240132362A1](https://patents.google.com/patent/US20240132362A1/en) |
| **Triagem** | review |
| **Rota** | manual_review |
| **Motivo da rota** | Triagem indicou revisão humana. |
| **Score de Triagem** | 5.5/10 |
| **Score de Relevância** | 6.3/10 |
| **Nível de Inovação** | Incremental |
| **Domínio Técnico** | Fotocatalise, Química de Materiais |
| **Cluster Temático** | Fotoredutção de CO2 com QDs |
| **Papel do CO2** | substrato_de_reação |
| **Papel do Armazenamento** | implícito_ou_suporte_ao_armazenamento |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | não_claro |
| **Fonte/Sumidouro Térmico** | não_especificado |
| **Foco das Claims** | sensibilização fotocatalítica com QDs para redução de CO2 |
| **Categoria de Exclusão** | generic_tes |
| **Confiança** | 0.66 |
| **Rerank Aplicado** | Sim |
| **Motivo do Rerank** | reranked:include->review |
| **Revisão Manual** | Sim |
| **Erro LLM** | N/A |

**Abstract:**
> AbstractDisclosed herein are compositions and methods that can achieve photoreduction of CO2to CO in pure water at pH 6-7 with excellent performance parameters. In embodiments, the compositions and methods use CuInS2colloidal quantum dots (QDs) as photosensitizers, and a Co-porphyrin catalyst.

**Avaliação do LLM:**
Esta patente descreve um método para a fotoredutção de CO2 em CO utilizando quantum dots (QDs) contendo CuInS2 como sensibilizadores e um catalisador Co-porphyrin. A reação ocorre em água pura com pH entre 6 e 7, buscando alcançar parâmetros de desempenho excelentes.

**Extração Estruturada:**
- **Problema:** A patente aborda a necessidade de um método eficiente para a fotoredutção de CO2, potencialmente visando o armazenamento do produto CO.
- **Solução:** A solução proposta envolve o uso de QDs de CuInS2 como sensibilizadores fotoquímicos em conjunto com um catalisador Co-porphyrin para promover a redução de CO2 em CO em condições específicas de pH e temperatura.
- **Maturidade:** Inicial

**Achados-chave:**
- Utilização de CuInS2 QDs como fotosensibilizador.
- Reação de fotoredutção de CO2 em água pura com pH 6-7.
- Obtenção de parâmetros de desempenho excelentes.

**Vantagens alegadas:**
- Excelente desempenho na fotoredutção de CO2.
- Utilização de materiais abundantes (CuInS2 QDs).
- Reação em condições brandas (água pura, pH 6-7).

**Limitações:**
- A patente não detalha a escala ou viabilidade da reação para produção em larga escala.
- O impacto ambiental do uso de CuInS2 QDs pode ser uma consideração.

**Aplicações potenciais:**
- Captura e conversão de carbono.
- Produção de CO como matéria-prima química.
- Desenvolvimento de tecnologias de armazenamento de carbono.

**Evidências citadas:**
> AbstractDisclosed herein are compositions and methods that can achieve photoreduction of CO2to CO in pure water...
> In embodiments, the compositions and methods use CuInS2colloidal quantum dots (QDs) as photosensitizers...

---

### 5. Pulsed RF high pressure CO2 lasers

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_978529d55152` |
| **Family ID** | `family:a49e267de9891215778efb749cab6df29c810577` |
| **ID** | `US7453918B2` |
| **Inventores** | Lanny Laughman, Vernon Seguin, Peter P. Chenausky, Robert Henschke, Eric R. Mueller |
| **Titular** | Coherent Inc |
| **Data** | 2008-11-18 |
| **Fonte** | Google Patents |
| **URL** | [US7453918B2](https://patents.google.com/patent/US7453918B2/en) |
| **Triagem** | review |
| **Rota** | manual_review |
| **Motivo da rota** | Triagem indicou revisão humana. |
| **Score de Triagem** | 6.4/10 |
| **Score de Relevância** | 6.5/10 |
| **Nível de Inovação** | Incremental |
| **Domínio Técnico** | Laser Technology |
| **Cluster Temático** | High-Pressure CO2 Lasers |
| **Papel do CO2** | working_fluid |
| **Papel do Armazenamento** | implicit_or_support_storage |
| **Limite Sistêmico** | cycle_or_transfer_subsystem |
| **Tipo de Ciclo** | power_or_work_cycle |
| **Fonte/Sumidouro Térmico** | RF Excitation |
| **Foco das Claims** | system_architecture |
| **Categoria de Exclusão** | co2_working_fluid_only |
| **Confiança** | 0.75 |
| **Rerank Aplicado** | Sim |
| **Motivo do Rerank** | reranked:decision_confirmed |
| **Revisão Manual** | Sim |
| **Erro LLM** | N/A |

**Abstract:**
> AbstractAn improved laser system includes a sealed-off, RF excited, diffusion cooled, high pressure, short pulsed, high peak power waveguide and slab CO2laser that avoids problems typically associated with obtaining a diffused discharge at high gas pressures, without arcing and without corona, while maintaining the unsaturated gain and gas temperature experienced at low pressures and scaling to higher pressures. Such a system has a long operating life-time, and is capable of operation at high gas pressures to obtain relative fast rise and fall time pulses. The system emits relatively short pulse widths, with pulse energies up to and exceeding 30 mJ, with reasonably high pulse repetition rates. The system also has a low pulsed RF power duty cycle, thereby enabling the generation of high peak power pulses, as well as reasonable average power and reasonably high peak powers.

**Avaliação do LLM:**
Esta patente descreve um laser a CO2 de alta pressão que utiliza resfriamento RF e pulsos curtos para evitar problemas comuns associados a altas pressões gasosas, como arcos elétricos e corona. O sistema permite operar em altas pressões para obter tempos de subida e descida dos pulsos rápidos, com energias de pulso até 30 mJ e altas taxas de repetição de pulso. A patente foca na otimização da potência de pico e média do laser.

**Extração Estruturada:**
- **Problema:** O problema abordado é a dificuldade em obter um difusão de descarga confiável e eficiente em lasers a CO2 de alta pressão, que frequentemente levam a arcos elétricos e corona, limitando o desempenho e a vida útil do sistema.
- **Solução:** A solução proposta é um laser a CO2 com resfriamento RF, pulsos curtos e resfriamento por difusão em alta pressão, que elimina esses problemas, permitindo operação em altas pressões para tempos de pulso rápidos e maior potência.
- **Maturidade:** Intermediária

**Achados-chave:**
- O sistema opera em alta pressão para obter tempos de subida e descida dos pulsos rápidos.
- A patente detalha a emissão de pulsos curtos com energias de até 30 mJ e taxas de repetição de pulso razoavelmente altas.
- Utiliza um ciclo de potência RF de baixa carga, permitindo a geração de alta potência de pico.

**Vantagens alegadas:**
- Longa vida útil do sistema
- Capacidade de operar em altas pressões para tempos de pulso rápidos
- Alta potência de pico e média

**Limitações:**
- A patente não menciona explicitamente o uso de 'carbon dots'.
- O foco principal é no laser a CO2 de alta pressão, sem detalhamento sobre aplicações específicas de carbon dots.

**Aplicações potenciais:**
- Processamento de materiais com lasers de alta potência
- Aplicações médicas que requerem pulsos curtos e intensos

**Evidências citadas:**
> "The system emits relatively short pulse widths, with pulse energies up to and exceeding 30 mJ..."
> "The system also has a low pulsed RF power duty cycle, thereby enabling the generation of high peak power pulses"

---

### 6. Laser radar system apparatus for multi-wavelength measurement of atmospheric carbon dioxide concentration and vertical aerosol profile

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_2a9fec0406cd` |
| **Family ID** | `family:570d526d3333197c7b7dc2ae3224623a0f145141` |
| **ID** | `US20210349011A1` |
| **Inventores** | Weibiao CHEN, Yadan Zhu, Jiqiao LIU, Xia Hou, Xiaolei Zhu, Xiuhua MA, Huaguo ZANG, Rui Li |
| **Titular** | Shanghai Institute of Optics and Fine Mechanics of CAS |
| **Data** | 2021-11-11 |
| **Fonte** | Google Patents |
| **URL** | [US20210349011A1](https://patents.google.com/patent/US20210349011A1/en) |
| **Triagem** | review |
| **Rota** | manual_review |
| **Motivo da rota** | Triagem indicou revisão humana. |
| **Score de Triagem** | 5.5/10 |
| **Score de Relevância** | 4.9/10 |
| **Nível de Inovação** | Incremental |
| **Domínio Técnico** | Remote Sensing & Atmospheric Monitoring |
| **Cluster Temático** | Laser-based atmospheric sensing and aerosol profiling |
| **Papel do CO2** | capture_process_stream |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | não especificado |
| **Foco das Claims** | system_architecture |
| **Categoria de Exclusão** | co2_working_fluid_only |
| **Confiança** | 0.66 |
| **Rerank Aplicado** | Sim |
| **Motivo do Rerank** | reranked:decision_confirmed |
| **Revisão Manual** | Sim |
| **Erro LLM** | N/A |

**Abstract:**
> AbstractA laser radar system apparatus for the multi-wavelength measurement of the atmospheric carbon dioxide concentration and a vertical aerosol profile, including: a laser transmitting unit; a dual-pulse laser capable of simultaneously transmitting laser having three wavelengths, i.e., 1572 nm, 1064 nm, and 532 nm; a transmitting beam expander; a receiving telescope system; a visual axis monitoring module; a photoelectric detection unit; and a data acquisition and processing unit. The laser that simultaneously outputs laser having three wavelengths is used in a laser radar system, and an optical differential absorption method and a high spectral resolution detection method are used, such that the atmospheric carbon dioxide concentration and the vertical aerosol profile can be measured simultaneously and high-precision aerosol monitoring is implemented during the high-precision obtaining of the concentration of the greenhouse gas carbon dioxide.

**Avaliação do LLM:**
Esta patente descreve um sistema de radar laser para medição de CO2 atmosférico e perfil aerosol, utilizando múltiplos comprimentos de onda. O sistema emprega uma técnica de absorção diferencial óptica e alta resolução espectral para obter dados precisos de concentração de CO2 e perfil aerosol. A patente foca na arquitetura do sistema e nos métodos ópticos, sem detalhar explicitamente o uso de carbon dots.

**Extração Estruturada:**
- **Problema:** Medir com precisão a concentração de CO2 atmosférico e o perfil vertical de aerossóis simultaneamente, utilizando um sistema de detecção eficiente.
- **Solução:** O sistema utiliza um laser transmitindo múltipla frequência para medir a concentração de CO2 e o perfil aerosol através da análise da absorção diferencial óptica e alta resolução espectral.
- **Maturidade:** Intermediária

**Achados-chave:**
- Utilização de laser com três comprimentos de onda (1572 nm, 1064 nm, e 532 nm).
- Emprego de uma técnica de absorção diferencial óptica e alta resolução espectral para medições precisas.

**Vantagens alegadas:**
- Medição simultânea de concentração de CO2 e perfil aerosol.
- Alta precisão na monitorização de aerossóis.

**Limitações:**
- Não menciona explicitamente o uso de carbon dots.
- Foco principal em arquitetura do sistema e métodos ópticos, sem detalhamento da tecnologia central.

**Aplicações potenciais:**
- Monitoramento ambiental
- Estudos atmosféricos
- Controlo de emissões

**Evidências citadas:**
> The laser that simultaneously outputs laser having three wavelengths is used in a laser radar system…

---

### 7. A 10,000-watt radio frequency fast axial flow carbon dioxide laser

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_b3ff7b05cb8e` |
| **Family ID** | `family:fc6cd731745f7fc53ba3a7d50dba19c027b59844` |
| **ID** | `CN119742647A` |
| **Inventores** | èµµå´é, æ½å¶å¤, é»ç¼, å¯è²æ³½, å¼ åå |
| **Titular** | Changchun Institute of Optics Fine Mechanics and Physics of CAS |
| **Data** | 2025-04-01 |
| **Fonte** | Google Patents |
| **URL** | [CN119742647A](https://patents.google.com/patent/CN119742647A/en) |
| **Triagem** | review |
| **Rota** | manual_review |
| **Motivo da rota** | Triagem indicou revisão humana. |
| **Score de Triagem** | 7.7/10 |
| **Score de Relevância** | 6.5/10 |
| **Nível de Inovação** | Incremental |
| **Domínio Técnico** | Laser Technology, Termodinâmica, Sistemas de Resfriamento |
| **Cluster Temático** | Lasers de Alta Potência e Resfriamento |
| **Papel do CO2** | working_fluid |
| **Papel do Armazenamento** | implicit_or_support_storage |
| **Limite Sistêmico** | cycle_or_transfer_subsystem |
| **Tipo de Ciclo** | power_or_work_cycle |
| **Fonte/Sumidouro Térmico** | cooling_or_refrigeration |
| **Foco das Claims** | component_or_operation |
| **Categoria de Exclusão** | cooling_only |
| **Confiança** | 0.79 |
| **Rerank Aplicado** | Sim |
| **Motivo do Rerank** | reranked:decision_confirmed |
| **Revisão Manual** | Sim |
| **Erro LLM** | N/A |

**Abstract:**
> AbstractTranslated fromChineseæ¬åæå¬å¼äºä¸ç§ä¸ç¦çº§çå°é¢å¿«è½´æµäºæ°§åç¢³æ¿åå¨ï¼åæ¬ï¼æ¾çµçµæåå·æä¸­ç©ºç®¡å£çæ¾çµç»çç®¡ï¼æ¾çµçµæè®¾ç½®å¨æ¾çµç»çç®¡çå¤å£ï¼æ¾çµç»çç®¡ï¼åæ¬ï¼è¿æ°´å­ååºæ°´å­ï¼è¿æ°´å­ååºæ°´å­ä¸ä¸­ç©ºç®¡å£è¿éå½¢æå·å´æ°´è·¯ï¼è¿æ°´å­è®¾ç½®å¨å°é¢å¿«è½´æµäºæ°§åç¢³æ¿åå¨çææ°ç«¯ï¼åºæ°´å­è®¾ç½®å¨å°é¢å¿«è½´æµäºæ°§åç¢³æ¿åå¨è¿æ°ç«¯ï¼å°é¢çµæºï¼å°é¢ééå¨ï¼è¿æ¥å°é¢çµæºåæ¾çµæ¨¡åï¼ç¨äºè°èå°é¢å¿«è½´æµäºæ°§åç¢³æ¿åå¨çææ°ç«¯çæ¸©åº¦ãæ¬åæéè¿è®¾ç½®å°é¢ééå¨ï¼ä½¿ä¸ç¦çº§çå°é¢å¿«è½´æµäºæ°§åç¢³æ¿åå¨è½å¤éè¿æ°´å·çæ¹å¼éä½æ¾çµç®¡ææ°ç«¯åºæ¥çé«æ¸©æ°ä½çæ¸©åº¦ï¼ä¿è¯æ¾çµç®¡è¿æ°ç«¯åææ°ç«¯çæ¸©åº¦ç»´æç¨³å®ï¼ä½¿æ¿åè½å¤è·å¾æ´é«çå¢çï¼æé«æ¿åå¨çè¾åºåçãThe present invention discloses a 10,000-watt radio frequency fast axial flow carbon dioxide laser, comprising: a discharge electrode and a discharge glass tube with a hollow tube wall; the discharge electrode is arranged on the outer wall of the discharge glass tube; the discharge glass tube comprises: a water inlet and a water outlet, the water inlet and the water outlet are connected with the hollow tube wall to form a cooling water path; the water inlet is arranged at the exhaust end of the radio frequency fast axial flow carbon dioxide laser, and the water outlet is arranged at the air inlet end of the radio frequency fast axial flow carbon dioxide laser; a radio frequency power supply, a radio frequency adapter, connecting the radio frequency power supply and the discharge module, and used to adjust the temperature of the exhaust end of the radio frequency fast axial flow carbon dioxide laser. The present invention sets a radio frequency adapter, so that the 10,000-watt radio frequency fast axial flow carbon dioxide laser can reduce the temperature of the high-temperature gas coming out of the exhaust end of the discharge tube by water cooling, ensure that the temperature of the air inlet and exhaust ends of the discharge tube is maintained stable, so that the laser can obtain a higher gain and improve the output power of the laser.

**Avaliação do LLM:**
Esta patente descreve um laser a CO2 de alta potência (10.000 watts) utilizando um sistema de fluxo axial rápido e radiofrequência, com foco na otimização do resfriamento através de um circuito de água. O design incorpora um tubo de descarga com um caminho de água para dissipar o calor, visando aumentar a potência de saída do laser. A patente detalha a integração do sistema de resfriamento com o laser CO2.

**Extração Estruturada:**
- **Problema:** O principal problema abordado é a superaquecimento de lasers a CO2 de alta potência durante operação, limitando sua eficiência e potência de saída.
- **Solução:** A solução proposta é um laser a CO2 que utiliza um sistema de resfriamento por água integrado ao tubo de descarga para controlar a temperatura e manter uma operação estável, permitindo maior potência de saída.
- **Maturidade:** Inicial

**Achados-chave:**
- O laser utiliza um tubo de descarga com uma parede tubular interna e um caminho de água para resfriamento.
- Um circuito de água é usado para remover o calor do extremo de exaustão do laser de fluxo axial rápido, garantindo a estabilidade da temperatura.

**Vantagens alegadas:**
- Aumento da potência de saída do laser devido ao controle térmico eficiente.
- Operação mais estável e confiável do laser através do sistema de resfriamento por água.

**Limitações:**
- A patente se concentra especificamente em um design de 10.000 watts, a escalabilidade para outras potências pode exigir ajustes.
- A dependência de um sistema de resfriamento por água pode adicionar complexidade e custo ao sistema.

**Aplicações potenciais:**
- Sistemas de corte e soldagem a laser
- Pesquisa científica em lasers de alta potência

**Evidências citadas:**
> "a discharge glass tube with a hollow tube wall; the water inlet and the water outlet are connected with the hollow tube wall to form a cooling water path"
> "the water inlet is arranged at the exhaust end of the radio frequency fast axial flow carbon dioxide laser, and the water outlet is arranged at the air inlet end of the radio frequency fast axial flow carbon dioxide laser"

---

### 8. Laser-induced carbon nanostructures

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_088645a041e0` |
| **Family ID** | `family:b42cc9020a3831b52f7625a0c8c0a480895e45b7` |
| **ID** | `US12384680B2` |
| **Inventores** | Marco Caffio, Gabriel Casano CARNICER |
| **Titular** | Integrated Graphene Holding Ltd |
| **Data** | 2025-08-12 |
| **Fonte** | Google Patents |
| **URL** | [US12384680B2](https://patents.google.com/patent/US12384680B2/en) |
| **Triagem** | exclude |
| **Rota** | screen_only |
| **Motivo da rota** | Patente excluída na triagem. |
| **Score de Triagem** | 3.5/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | Ciência dos Materiais, Nanotecnologia |
| **Cluster Temático** | Fabricação de Nanomateriais com Laser |
| **Papel do CO2** | co2_not_central |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | industrial_heat |
| **Foco das Claims** | component_or_operation |
| **Categoria de Exclusão** | generic_tes |
| **Confiança** | 0.62 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> AbstractA method of manufacturing a carbon nanostructure, such as a carbon foam material, is disclosed. The method comprises the steps of: (a) using a first laser beam to irradiate an encapsulated or sub-surface region of a carbon pre-cursor material below a surface of the material, to create carbon foam in that sub-surface region, and a disorganised, amorphous non-graphene material above the carbon foam, and then (b) using a second laser beam to remove or ablate the disorganised, amorphous non-graphene material sitting above the carbon foam, to expose at least some of the carbon foam. The resultant carbon foam material shows a significant D peak; the 2D peak is significantly less than the G peak; and the peak D: peak G ratio is significantly above zero. In appearance and Raman signature, it appears similar to a carbon nano-onion material. It can be used in biosensors, supercapacitors and pseudo-capacitors.

**Evidências citadas:**
> (a) using a first laser beam to irradiate an encapsulated or sub-surface region of a carbon pre-cursor material below a surface of the material, to create carbon foam in that sub-surface region

---

### 9. A method of mesoporous silicon dioxide modified carbon dots are prepared to be calcined method

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_cdb57d537407` |
| **Family ID** | `family:c0f6e1bfbd50bcb1ae7a8a2883a1444a791278fa` |
| **ID** | `CN109705627A` |
| **Inventores** | å¨å´å¹³, å°¹è¶è |
| **Titular** | Donghua University |
| **Data** | 2019-05-03 |
| **Fonte** | Google Patents |
| **URL** | [CN109705627A](https://patents.google.com/patent/CN109705627A/en) |
| **Triagem** | exclude |
| **Rota** | screen_only |
| **Motivo da rota** | Patente excluída na triagem. |
| **Score de Triagem** | 3.5/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | Ciência dos Materiais, Nanotecnologia |
| **Cluster Temático** | Preparação de Carbon Dots e Modificação de Materiais |
| **Papel do CO2** | co2_not_central |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | industrial_heat |
| **Foco das Claims** | component_or_operation |
| **Categoria de Exclusão** | generic_tes |
| **Confiança** | 0.66 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> AbstractTranslated fromChineseæ¬åææ¶åä¸ç§ä»¥é»ç§æ³å¶å¤ä»å­äºæ°§åç¡ä¿®é¥°ç¢³ç¹çæ¹æ³ãè¯¥æ¹æ³ä»¥ä»å­äºæ°§åç¡ä¸ºè½½ä½ï¼ä½¿ç¨é»ç§æ³è®©æ æª¬é¸ãè²å¨ä»å­äºæ°§åç¡éå¶ççº³ç±³ç©ºé´ååçç¢³åååºãè¯¥ä»å­äºæ°§åç¡ä¿®é¥°çç¢³ç¹å·æè¯å¥½çåæ£æ§ï¼åºè²çåç¨³å®æ§åè¾å¥½çè§åææï¼ä¸å¶è§ååçäºçº¢ç§»ç°è±¡ãThe invention relates to a method for preparing mesoporous silica modified carbon dots by a calcination method. The method uses mesoporous silica as a carrier, and uses a calcination method to make citric acid and urea carbonize in the nano-space confined by mesoporous silica. The mesoporous silica-modified carbon dots have good dispersibility, excellent photostability and good fluorescence effect, and their fluorescence undergoes a red-shift phenomenon.

**Evidências citadas:**
> The invention relates to a method for preparing mesoporous silica modified carbon dots by a calcination method.
> The method uses mesoporous silica as a carrier, and uses a calcination method to make citric acid and urea carbonize in the nano-space confined by mesoporous silica.

---

### 10. Fully indentifiable optical fiber assemblies

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_ada95ec7d9a9` |
| **Family ID** | `family:ea1b3254783389da88be337959fb335b104ebc6d` |
| **ID** | `20010048797` |
| **Inventores** | Van Dijk Saskia I., Dias Aylvin J., De Haas Jacob L., Tilley Mark G., Reichert Timothy P. |
| **Titular** | VAN DIJK SASKIA I.
DIAS AYLVIN J.
DE HAAS JACOB L.
TILLEY MARK G.
REICHERT TIMOTHY P. |
| **Data** | 06.12.2001 |
| **Fonte** | Patentscope |
| **URL** | [20010048797](https://patentscope.wipo.int/search/en/detail.jsf?docId=US39333852&_cid=P22-MRYZFR-15194-1) |
| **Triagem** | exclude |
| **Rota** | screen_only |
| **Motivo da rota** | Patente excluída na triagem. |
| **Score de Triagem** | 3.5/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | Engenharia de Materiais, Óptica |
| **Cluster Temático** | Radiação Curável e Agentes Contrastantes |
| **Papel do CO2** | capture_process_stream |
| **Papel do Armazenamento** | implicit_or_support_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | refrigeration_cycle |
| **Fonte/Sumidouro Térmico** | industrial_heat |
| **Foco das Claims** | process_integration |
| **Categoria de Exclusão** | generic_tes |
| **Confiança** | 0.59 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> (EN)The present invention relates to a radiation-curable composition comprising, in the uncured state, at least one monomer or oligomer having a radiation-curable functional group which can form free radicals in the presence of actinic radiation, a photoinitiator for said monomer or oligomer present in an amount sufficient to effect radiation cure of said monomer or oligomers and a contrasting agent which causes an observable change in the cured composition upon exposure to energy from a high energy tunable light source.The invention further relates to an optical fiber ribbon assembly comprising said radiation curable composition and including energy-induced indicia, and to a process for importing indicia to an optical fiber ribbon assembly.

**Evidências citadas:**
> The present invention relates to a radiation-curable composition comprising, in the uncured state, at least one monomer or oligomer having a radiation-curable functional group...
> The invention further relates to an optical fiber ribbon assembly comprising said radiation curable composition...

---

### 11. FULLY IDENTIFIABLE OPTICAL FIBER ASSEMBLIES
(FR)
ENSEMBLES DE FIBRE OPTIQUE ENTIEREMENT IDENTIFIABLES

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_16365a279915` |
| **Family ID** | `family:97bd3f251269b1eba54152eace62a343481d49ac` |
| **ID** | `WO/2001/068776` |
| **Inventores** | VAN DIJK, Saskia, Ingeborg, DIAS, Aylvin, Jorge, Angelo, Athanasius, DE HAAS, Jacob, Leendert, REICHERT, Timothy, Paul, TILLEY, Mark, Gerard |
| **Titular** | DSM N.V.
[NL]/[NL]
(AllExceptUS)
VAN DIJK, Saskia, Ingeborg
[NL]/[NL](UsOnly)
DIAS, Aylvin, Jorge, Angelo, Athanasius
[GB]/[NL](UsOnly)
DE HAAS, Jacob, Leendert
[NL]/[NL](UsOnly)
REICHERT, Timothy, Paul
[US]/[US](UsOnly)
TILLEY, Mark, Gerard
[GB]/[US](UsOnly) |
| **Data** | 20.09.2001 |
| **Fonte** | Patentscope |
| **URL** | [WO/2001/068776](https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2001068776&_cid=P22-MRYZFR-15194-1) |
| **Triagem** | exclude |
| **Rota** | screen_only |
| **Motivo da rota** | Patente excluída na triagem. |
| **Score de Triagem** | 3.5/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | Materiais e Composição |
| **Cluster Temático** | Composições Curáveis por Radiação e Indicadores Ópticos |
| **Papel do CO2** | co2_not_central |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | industrial_heat |
| **Foco das Claims** | component_or_operation |
| **Categoria de Exclusão** | generic_tes |
| **Confiança** | 0.52 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> (EN)The present invention relates to a radiation-curable composition comprising, in the uncured state, at least one monomer or oligomer having a radiation-curable functional group which can form free radicals in the presence of actinic radiation, a photoinitiator for said monomer or oligomer present in an amount sufficient to effect radiation cure of said monomer or oligomers and a contrasting agent which causes an observable change in the cured composition upon exposure to energy from a high energy tunable light source. The invention further relates to an optical fiber ribbon assembly comprising said radiation curable composition and including energy-induced indicia, and to a process for importing indicia to an optical fiber ribbon assembly.(FR)L'invention concerne une composition durcissable par rayonnement comprenant, à l'état non durci : au moins un monomère ou un oligomère doté d'un groupe fonctionnel durcissable par rayonnement, qui peut former des radicaux libres en présence d'un rayonnement actinique ; un photoamorceur en quantité suffisante pour provoquer le durcissement par rayonnement dudit monomère ou oligomère ; un agent de contraste qui crée un changement observable dans la composition durcie, sous l'effet de l'exposition à l'énergie d'une source lumineuse modulable à haute énergie. Ladite invention concerne également un ensemble ruban de fibre optique comportant ladite composition durcissable par rayonnement et une marque induite par énergie. Cette invention porte aussi sur un procédé pour importer une marque vers un ensemble ruban de fibre optique.

**Evidências citadas:**
> The invention further relates to an optical fiber ribbon assembly comprising said radiation curable composition and including energy-induced indicia

---

### 12. MARKING OF PIPES
(FR)
MARQUAGE DE TUYAUX

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_a16fbb141ab9` |
| **Family ID** | `family:fcd297b1ff56cd08bfccfcd1e0f1706cbe458ec9` |
| **ID** | `WO/2006/067380` |
| **Inventores** | BOWMAN, Jeremy |
| **Titular** | UPONOR INNOVATION AB
[SE]/[SE]
(AllExceptUS)
BOWMAN, Jeremy
[GB]/[GB](UsOnly) |
| **Data** | 29.06.2006 |
| **Fonte** | Patentscope |
| **URL** | [WO/2006/067380](https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2006067380&_cid=P22-MRYZFR-15194-1) |
| **Triagem** | exclude |
| **Rota** | screen_only |
| **Motivo da rota** | Patente excluída na triagem. |
| **Score de Triagem** | 3.5/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | Engenharia de Materiais, Processamento Industrial |
| **Cluster Temático** | Marcação por Laser, Carbon Dots |
| **Papel do CO2** | working_fluid |
| **Papel do Armazenamento** | implicit_or_support_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | refrigeration_cycle |
| **Fonte/Sumidouro Térmico** | industrial_heat |
| **Foco das Claims** | component_or_operation |
| **Categoria de Exclusão** | generic_tes |
| **Confiança** | 0.66 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> (EN)A method for the production of a machine readable marking on a plastics pipe, which comprises directing alaseronto a surface of the pipe whereby a machine readable marking is produced.(FR)La présente invention concerne un procédé pour produire des marques pouvant être lues par une machine sur des tuyaux en plastique. Le procédé implique de diriger un laser sur la surface du tuyau, permettant ainsi de produire une marque pouvant être lue par une machine.

**Evidências citadas:**
> A method for the production of a machine readable marking on a plastics pipe, which comprises directing alaseronto a surface of the pipe whereby a machine readable marking is produced.
> La présente invention concerne un procédé pour produire des marques pouvant être lues par une machine sur des tuyaux en plastique. Le procédé implique de diriger un laser sur la surface du tuyau, permettant ainsi de produire une marque pouvant être lue par une machine.

---

### 13. eTPE
Laser
Marking

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_10b20ac8d2a9` |
| **Family ID** | `family:70e832209d591bcb76ff153d345c9896bab98253` |
| **ID** | `20240002621` |
| **Inventores** | Frank THIELBEER, Lisa Marie Schmidt, Theresa Huelsmann, Elmar Poeselt, Peter Gutmann, Uwe Keppeler, Amir Doroodian, Florian Tobias Rapp |
| **Titular** | BASF SE |
| **Data** | 04.01.2024 |
| **Fonte** | Patentscope |
| **URL** | [20240002621](https://patentscope.wipo.int/search/en/detail.jsf?docId=US418579840&_cid=P22-MRYZFR-15194-1) |
| **Triagem** | exclude |
| **Rota** | screen_only |
| **Motivo da rota** | Patente excluída na triagem. |
| **Score de Triagem** | 3.5/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | Materiais Poliméricos e Processamento |
| **Cluster Temático** | Marcação por Laser e Materiais Funcionais |
| **Papel do CO2** | co2_not_central |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | industrial_heat |
| **Foco das Claims** | component_or_operation |
| **Categoria de Exclusão** | generic_tes |
| **Confiança** | 0.58 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> (EN)Laser-markable foamed pellets contain a composition (MI), containing a thermoplastic elastomer (TPE-1) and a color component as component (c1) selected fromlasermarking additives. A process can be used for producing saidlaser-markable foamed pellets. Thelaser-markable foamed pellets according to the present invention can be used for preparing alaser-markable molded body. A process for preparing alaser-markable molded body involves providing and fusing thelaser-markable foal led pellets.

**Evidências citadas:**
> Laser-markable foamed pellets contain a composition (MI), containing a thermoplastic elastomer (TPE-1) and a color component as component (c1) selected from lasermarking additives.

---

### 14. Advanced multi-element consumable-disposable products

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_03338d832e80` |
| **Family ID** | `family:b654f118753e11f75ebac66f7683e08ed2c459bf` |
| **ID** | `20180003565` |
| **Inventores** | Hans O. Ribi |
| **Titular** | Segan Industries, Inc. |
| **Data** | 04.01.2018 |
| **Fonte** | Patentscope |
| **URL** | [20180003565](https://patentscope.wipo.int/search/en/detail.jsf?docId=US209523108&_cid=P22-MRYZFR-15194-1) |
| **Triagem** | exclude |
| **Rota** | screen_only |
| **Motivo da rota** | Patente excluída na triagem. |
| **Score de Triagem** | 1.7/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | Produtos de Consumo |
| **Cluster Temático** | Funcionalidades Adicionais em Produtos |
| **Papel do CO2** | co2_not_central |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | general_thermal_management |
| **Foco das Claims** | component_or_operation |
| **Categoria de Exclusão** | generic_tes |
| **Confiança** | 0.42 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> (EN)The invention involves the incorporation and enablement of multiple interactive elements into high-volume consumables products to increase utility, function and features of the consumable product at minimal incremental cost and adjustment to production and manufacturing processes. The invention further reports processes and compositions that enable consumable products with differentiating features which product would otherwise be deficient for their intended use and application.

**Evidências citadas:**
> The invention further reports processes and compositions that enable consumable products with differentiating features which product would otherwise be deficient for their intended use and application.

---

### 15. Advanced multi-element consumable-disposable products

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_7b0001c43bfd` |
| **Family ID** | `family:1c3e80b7bcb5e7ef632faca8bdf71e231c5b1e87` |
| **ID** | `20140221528` |
| **Inventores** | Hans O. Ribi |
| **Titular** | Segan Industries, Inc. |
| **Data** | 07.08.2014 |
| **Fonte** | Patentscope |
| **URL** | [20140221528](https://patentscope.wipo.int/search/en/detail.jsf?docId=US106950238&_cid=P22-MRYZFR-15194-1) |
| **Triagem** | exclude |
| **Rota** | screen_only |
| **Motivo da rota** | Patente excluída na triagem. |
| **Score de Triagem** | 1.7/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | Engenharia de Produtos |
| **Cluster Temático** | Desenvolvimento de Consumíveis e Funcionalidades Adicionais |
| **Papel do CO2** | co2_not_central |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | general_thermal_management |
| **Foco das Claims** | component_or_operation |
| **Categoria de Exclusão** | generic_tes |
| **Confiança** | 0.42 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> (EN)The invention involves the incorporation and enablement of multiple interactive elements into high-volume consumables products to increase utility, function and features of the consumable product at minimal incremental cost and adjustment to production and manufacturing processes. The invention further reports processes and compositions that enable consumable products with differentiating features which product would otherwise be deficient for their intended use and application.

**Evidências citadas:**
> The invention further reports processes and compositions that enable consumable products with differentiating features which product would otherwise be deficient for their intended use and application.

---

### 16. eTPE
LASER
MARKING
(FR)
MARQUAGE LASER ETPE

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_e34e165b0c23` |
| **Family ID** | `family:ecb2beaa3fbbb082fef153440867368082d34d13` |
| **ID** | `WO/2022/069664` |
| **Inventores** | THIELBEER, Frank, SCHMIDT, Lisa Marie, HUELSMANN, Theresa, POESELT, Elmar, GUTMANN, Peter, KEPPELER, Uwe, DOROODIAN, Amir, RAPP, Florian Tobias |
| **Titular** | BASF SE
[DE]/[DE] |
| **Data** | 07.04.2022 |
| **Fonte** | Patentscope |
| **URL** | [WO/2022/069664](https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2022069664&_cid=P22-MRYZFR-15194-1) |
| **Triagem** | exclude |
| **Rota** | screen_only |
| **Motivo da rota** | Patente excluída na triagem. |
| **Score de Triagem** | 3.5/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | Materiais Poliméricos e Processamento |
| **Cluster Temático** | Marcagem Laser e Aditivos Coloridos |
| **Papel do CO2** | co2_not_central |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | industrial_heat |
| **Foco das Claims** | component_or_operation |
| **Categoria de Exclusão** | generic_tes |
| **Confiança** | 0.62 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> (EN)The present invention relates tolaser-markable foamed pellets comprising a composition (M1) comprising a thermoplastic elastomer (TPE-1) and a color component as component (c1) selected from the group consisting oflasermarking additives as well as a process for producing saidlaser-markable foamed pellets. The present invention further relates to the Use of thelaser-markable foamed pellets according to the present invention for preparing alaser-markable molded body and a process for preparing alaser-markable molded body from the lasermarkable foamed pellets(FR)La présente invention concerne des pastilles expansées pouvant être marquées au laser comportant une composition (M1) comprenant un élastomère thermoplastique (TPE-1) et une composante de couleur en tant que composante (c1) choisie dans le groupe constitué par des additifs de marquage au laser, ainsi qu'un procédé de production desdites pastilles expansées pouvant être marquées au laser. La présente invention concerne en outre l'utilisation des pastilles expansées pouvant être marquées au laser selon la présente invention pour préparer un corps moulé pouvant être marqué au laser et un procédé de préparation d'un corps moulé pouvant être marqué au laser à partir des pastilles expansées pouvant être marquées au laser.

**Evidências citadas:**
> The present invention relates tolaser-markable foamed pellets comprising a composition (M1) comprising a thermoplastic elastomer (TPE-1) and a color component as component (c1) chosen from the group consisting oflasermarking additives

---

### 17. System for providing pre-processing machine readable encoded information markings in a motion picture film

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_50d42a982380` |
| **Family ID** | `family:fe5875a70a08025e7fb54b08ba6dcab87bbdc53e` |
| **ID** | `6556273` |
| **Inventores** | Wheeler, Christopher E., Ahlquist, Gary W., Shaffer, Wayne K., Morton, Roger A. |
| **Titular** | Eastman Kodak Company |
| **Data** | 29.04.2003 |
| **Fonte** | Patentscope |
| **URL** | [6556273](https://patentscope.wipo.int/search/en/detail.jsf?docId=US40134930&_cid=P22-MRYZFR-15194-1) |
| **Triagem** | exclude |
| **Rota** | screen_only |
| **Motivo da rota** | Patente excluída na triagem. |
| **Score de Triagem** | 3.3/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | Fotografia, Codificação de Dados |
| **Cluster Temático** | Sistemas de Codificação e Leitura de Imagens |
| **Papel do CO2** | co2_not_central |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | not_clear |
| **Foco das Claims** | system_architecture |
| **Categoria de Exclusão** | generic_tes |
| **Confiança** | 0.52 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> (EN)A system for providing motion picture photographic film with encoded information, such as unique film footage and frame identification, which can be machine read prior to film processing. This system provides machine readable encoded information markings on the raw stock film which may be read in a camera or other photoprocessing device with a reader prior to or concurrent with the film image capture process. The machine readable encoded information markings may be easily converted into a “video image” for display in a real time video from a CCD imager in the film camera or other device. Furthermore this pre-processing machine readable encoded information may be used in conjunction with optical latent image recorded information which becomes machine or human readable after processing as presently provided by film manufacturer's according to industry standards.

**Evidências citadas:**
> A system for providing motion picture photographic film with encoded information...
> The machine readable encoded information markings may be easily converted into a “video image”

---

### 18. A SYSTEM FOR PROVIDING PRE-PROCESSING MACHINE READABLE ENCODED INFORMATION MARKINGS IN A MOTION PICTURE FILM
(FR)
SYSTEME PERMETTANT DE PRODUIRE DES INSCRIPTIONS DE DONNEES DE PRETRAITEMENT CODEES LISIBLES PAR MACHINE SUR UN FILM CINEMATOGRAPHIQUE

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_52765fd5808d` |
| **Family ID** | `family:8dcf545af8adcff67fceda9ba98c0df9c4b1ffbb` |
| **ID** | `WO/2001/035163` |
| **Inventores** | WHEELER, Christopher, E., AHLQUIST, Gary, Wayne, SHAFFER, Wayne, Kenneth, MORTON, Roger, A. |
| **Titular** | EASTMAN KODAK COMPANY
[US]/[US] |
| **Data** | 17.05.2001 |
| **Fonte** | Patentscope |
| **URL** | [WO/2001/035163](https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2001035163&_cid=P22-MRYZFR-15194-1) |
| **Triagem** | exclude |
| **Rota** | screen_only |
| **Motivo da rota** | Patente excluída na triagem. |
| **Score de Triagem** | 3.3/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | Processamento de Imagem Cinematográfica |
| **Cluster Temático** | Sistemas de Marcação e Identificação em Filmes Cinematográficos |
| **Papel do CO2** | co2_not_central |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | not_clear |
| **Foco das Claims** | system_architecture |
| **Categoria de Exclusão** | generic_tes |
| **Confiança** | 0.49 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> (EN)A system for providing motion picture photographic film (20) with encoded information, such as unique film footage and frame identification, which can be machine read prior to film processing. This system provides machine readable encoded information markings (B) on the raw stock film which may be read in a camera or other photoprocessing device with a reader prior to or concurrent with the film image capture process. The machine readable encoded information markings may be easily converted into a 'video image' for display in a real time video from a CCD imager in the film camera or other device. Furthermore this pre-processing machine readable encoded information may be used in conjunction with optical latent image recorded information which becomes machine or human readable after processing as presently provided by film manufacturer's according to industry standards.(FR)L'invention concerne un système permettant de produire un film (201) cinématographique comprenant une information codée, telle que le métrage spécifique du film et une identification des images, pouvant être lue par une machine avant le traitement du film. Ce système permet de produire des inscriptions d'information codée (B) lisibles par machine sur la pellicule vierge, ces inscriptions pouvant être lues dans une caméra, ou dans un autre dispositif de traitement photographique équipé d'un lecteur, avant le processus de saisie d'image cinématographique ou simultanément à ce dernier. Ces inscriptions d'information codée lisible par machine peuvent être facilement converties en une « image vidéo » pouvant être affichée dans une vidéo en temps réel, au moyen de l'imageur CCD d'une caméra cinématographique ou d'un autre dispositif. En outre cette information codée lisible par machine peut être utilisée conjointement à une information enregistrée sous forme d'image optique latente qui devient lisible par une machine ou par l'homme après avoir subi un traitement conforme aux normes industrielles, tel que celui qu'utilisent actuellement les fabricants de film.

**Evidências citadas:**
> "Este système permet de produire des inscriptions d'information codée (B) lisibles par machine sur la pellicule vierge..."
> "Ces inscriptions d'information codée lisible par machine peuvent être facilement converties en une « image vidéo »"

---

## 🧾 Fila de Revisão Manual

- rec_b3ff7b05cb8e (CN119742647A) | rota=manual_review | motivo=Triagem indicou revisão humana. | erro_llm=N/A
- rec_dd866e6d7249 (US20240075453A1) | rota=manual_review | motivo=Triagem indicou revisão humana. | erro_llm=N/A
- rec_978529d55152 (US7453918B2) | rota=manual_review | motivo=Triagem indicou revisão humana. | erro_llm=N/A
- rec_b11edeb58983 (CN205569064U) | rota=manual_review | motivo=Triagem indicou revisão humana. | erro_llm=N/A
- rec_2a9fec0406cd (US20210349011A1) | rota=manual_review | motivo=Triagem indicou revisão humana. | erro_llm=N/A
- rec_48b16c3d81aa (US20240132362A1) | rota=manual_review | motivo=Triagem indicou revisão humana. | erro_llm=N/A
- rec_58aec1c9302f (WO2013154949A2) | rota=manual_review | motivo=Triagem indicou revisão humana. | erro_llm=N/A

---

## 🔬 Análise Comparativa

### 1. Panorama Geral

- O conjunto comparativo agrega 7 patente(s) e nao deve ser tratado como bloco homogeneo: ha um nucleo direto, fronteiras tecnicas em revisao e adjacencias uteis apenas para delimitar whitespace [IDs: CN119742647A, CN205569064U, US20240075453A1, US7453918B2, US20240132362A1, US20210349011A1, WO2013154949A2]
- O subgrupo mais diretamente alinhado ao núcleo da query é CN119742647A, com foco em armazenamento de CO2, compressão/expansão e controle termodinâmico do meio armazenado [IDs: CN119742647A]
- CN119742647A, CN205569064U, US20240075453A1, US7453918B2, US20240132362A1, US20210349011A1, WO2013154949A2 formam a fronteira tecnica: sao casos proximos do problema, mas ainda ambiguos quanto ao papel exato do CO2 no armazenamento ou na funcao arquitetural central [IDs: CN119742647A, CN205569064U, US20240075453A1, US7453918B2, US20240132362A1, US20210349011A1, WO2013154949A2]
- CN119742647A entram como adjacencia exploratoria: tratam CO2 principalmente como fluido de trabalho em transferencia termica ou distribuicao de energia, de modo que ajudam a delimitar combinacoes pouco cobertas sem virar evidencia de cobertura consolidada [IDs: CN119742647A]

## Análise Comparativa de Patentes – “carbon dots CO2 laser”

### 2. Tendências Identificadas

*   **Otimização de Resfriamento:** A busca por métodos mais eficientes para resfriar lasers a CO2, utilizando água ou RF, continua sendo uma tendência central (CN119742647A, US7453918B2, WO2013154949A2).
*   **Aplicações Terapêuticas:** A utilização de lasers a CO2 com pontos de carboneto para tratamento de superfície emerge como uma área de interesse (CN205569064U).
*   **Adsorção Seletiva de CO2:** O uso de carbon dots em conjunto com materiais porosos para adsorção seletiva de CO2 demonstra um potencial significativo para aplicações ambientais (US20210349011A1, US20240132362A1).
*   **Fotoredutção de CO2:** A exploração da fotoredutção de CO2 utilizando carbon dots como sensibilizadores representa uma fronteira tecnológica promissora (US20240132362A1).
*   **Controle Avançado do Laser:** O controle preciso da forma do pulso e potência para otimizar o desempenho do laser a CO2 é um foco constante (WO2013154949A2).

### 3. Whitespaces e Oportunidades

- Gestao termica transiente, subresfriamento e acoplamentos com captura/reatores aparecem de forma lateral; isso sugere oportunidade em claims de controle, operacao multi-regime e integracao de processo ainda pouco amarradas ao armazenamento central [IDs: CN119742647A, US20240075453A1, US20210349011A1, CN205569064U]
- As patentes em review delimitam fronteiras tecnicas onde o papel do CO2 ainda esta ambiguo entre meio armazenado, fluido de trabalho e interface de troca termica; esse tipo de ambiguidade costuma ser um bom proxy para whitespace exploravel com recorte arquitetural mais especifico [IDs: CN119742647A, CN205569064U, US20240075453A1, US7453918B2]

### 4. Recomendações

- Priorizar arquiteturas centradas em armazenamento explícito de CO2 e controle termodinâmico rigoroso [IDs: CN119742647A]

### 5. Ranking Final

1. **CN119742647A** — CO2 aparece principalmente como fluido de trabalho; armazenamento aparece mais como subsistema de apoio; score 6.5/10 [IDs: CN119742647A]
2. **CN205569064U** — CO2 aparece principalmente como fluido de trabalho; armazenamento aparece mais como subsistema de apoio; score 6.5/10 [IDs: CN205569064U]
3. **US20240075453A1** — CO2 aparece como meio termodinamico armazenado; armazenamento termico explicito como parte central; score 6.5/10 [IDs: US20240075453A1]
4. **US7453918B2** — CO2 aparece principalmente como fluido de trabalho; armazenamento aparece mais como subsistema de apoio; score 6.5/10 [IDs: US7453918B2]
5. **US20240132362A1** — alinhamento técnico sustentado pelas evidências extraídas; score 6.3/10 [IDs: US20240132362A1]
6. **US20210349011A1** — armazenamento termico explicito como parte central; score 4.9/10 [IDs: US20210349011A1]
7. **WO2013154949A2** — CO2 aparece principalmente como fluido de trabalho; armazenamento termico explicito como parte central; score 4.0/10 [IDs: WO2013154949A2]

### 6. Mapa de Evidências por ID

- **Adsorção Seletiva de Gases / Carbon Dots** [IDs: US20240075453A1]
- **Controle de Potência em Sistemas Laser** [IDs: WO2013154949A2]
- **Fotoredutção de CO2 com QDs** [IDs: US20240132362A1]
- **High-Pressure CO2 Lasers** [IDs: US7453918B2]
- **Laser-Based Surface Treatment Systems** [IDs: CN205569064U]
- **Laser-based atmospheric sensing and aerosol profiling** [IDs: US20210349011A1]
- **Lasers de Alta Potência e Resfriamento** [IDs: CN119742647A]

### 7. Ranking por ID

1. **CN119742647A** — score 6.5/10 [IDs: CN119742647A]
2. **CN205569064U** — score 6.5/10 [IDs: CN205569064U]
3. **US20240075453A1** — score 6.5/10 [IDs: US20240075453A1]
4. **US7453918B2** — score 6.5/10 [IDs: US7453918B2]
5. **US20240132362A1** — score 6.3/10 [IDs: US20240132362A1]
6. **US20210349011A1** — score 4.9/10 [IDs: US20210349011A1]
7. **WO2013154949A2** — score 4.0/10 [IDs: WO2013154949A2]

---

## 🧭 Matriz de Whitespaces

- **Patentes selecionadas:** 7
- **Núcleo:** 0
- **Fronteira:** 7
- **Adjacência:** 0

- **control_and_operability_claims**: Ha espaco para claims de controle, operacao transiente e integracao de processo onde o papel do CO2 e do armazenamento ainda esta ambiguo. [core=N/A | frontier=CN119742647A | adjacent=N/A]

---

## ℹ️ Informações do Sistema

- **Gerado por:** Agente de Web Scraping de Patentes
- **Modelo LLM:** gemma3:4b
- **Data de geração:** 24/07/2026 13:36:10
- **Query de busca:** `carbon dots CO2 laser`
- **Status da execução:** completed
- **Tempo total:** 96.6s
- **LLM disponível:** sim
- **Fila de revisão manual:** 7 itens
- **Snapshot hash:** `c0ce3ca3756dce924ad1ec3b95077e1231518006cc235667be35c7c8c002f9c3`
- **Features habilitadas:** require_evidence, enable_thematic_clusters, enable_structural_roles, enable_screening_rerank, enable_prisma, enable_snapshot, enable_comparative_analysis, enable_whitespace_analysis, enable_manual_review_queue
- **Features desabilitadas:** nenhum
- **Versão do pipeline:** 1.1
- **Thresholds snapshot:** include=7.0, review=4.5
- **Cache LLM:** 33 hits, 0 misses, 192 entradas
- **Status do rascunho:** ready