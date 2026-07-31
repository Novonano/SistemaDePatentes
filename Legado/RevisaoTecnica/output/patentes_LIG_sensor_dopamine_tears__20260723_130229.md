# 📋 Relatório de Análise de Patentes

**Data:** 23/07/2026 13:02:29
**Busca:** `LIG sensor dopamine tears `
**Total de patentes encontradas:** 20
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

- **Total bruto coletado:** 20
- **Patentes únicas:** 20
- **Duplicatas removidas:** 0
- **Triadas:** 0
- **Incluídas:** 0
- **Em revisão manual:** 20
- **Excluídas:** 0
- **Extrações completas:** 0
- **Sem abstract/snippet:** 0
- **Sem ID:** 1
- **Identidade por conteúdo:** 0
- **Identidade fallback:** 0
- **Duplicatas por família removidas:** 0
- **Falhas de triagem LLM:** 20
- **Falhas totais LLM:** 0

## 🧭 Fluxo PRISMA-Like

- **Identificação:** 20 bruto(s), 20 único(s), 0 duplicata(s) removida(s)
- **Triagem:** 0 triado(s), 0 incluído(s), 20 em revisão, 0 excluído(s)
- **Elegibilidade:** 0 extração(ões) completa(s), 20 revisão(ões) manual(is), 0 adiada(s)
- **Cobertura:** 0 sem abstract/snippet, 1 sem ID
- **Síntese:** 0 registro(s) analisado(s)

## 🧠 Contexto Compartilhado

- **Top patentes no contexto:** 0
- **Clusters no contexto:** 0
- **Roteamento agregado:** 1 rota(s)
- **Slots ativos:** N/A

## ⏱️ Métricas por Etapa

| Etapa | Status | Duração | Itens | Detalhes |
|---|---|---:|---:|---|
| setup | degraded | 30.02s | 1 | Verificação do modelo Ollama |
| search | ok | 123.49s | 20 | 20 patentes únicas após dedupe |
| screening | skipped | 0.00s | 20 | LLM indisponível |
| comparative_analysis | skipped | 0.00s | 20 | LLM indisponível para síntese comparativa |
| whitespace_analysis | skipped | 0.00s | 0 | Whitespace analysis sem corpus elegível |
| reporting | ok | 0.00s | 20 | Relatórios Markdown e JSON |
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
- **Sucessos:** 0
- **Falhas:** 1
- **Retries:** 0
- **Cache hits:** 0
- **Pulos por degradação:** 0
- **Latência média:** 30.019s
- **Latência máxima:** 30.019s

## 🔎 Observabilidade Estruturada

### Rotas

- **unrouted**: total=20, include=0, review=20, exclude=0, llm_errors=20

### Fontes

- **EPO**: bruto=0, duração=0.00s, diagnósticos=config_missing=1
- **GooglePatents**: bruto=10, duração=25.86s, diagnósticos=nenhum
- **Patentscope**: bruto=10, duração=97.63s, diagnósticos=nenhum

### Falhas

- **Erros de execução:** 0
- **Registros com erro de LLM:** 20
- **Falhas totais do LLM:** 0
- **LLM por operação:** healthcheck(falhas=1, retries=0, skips=0)
- **Scraper por tipo de sinal:** config_missing=1

## 📊 Resumo Executivo

**Score médio de relevância:** 0.0/10

| # | Patente | Score | Inovação | Domínio |
|---|---------|-------|----------|---------|
| 1 | [WO2021222250A1](https://patents.google.com/patent/WO2021222250A1/en) — Laser-induced graphene electrochemical immunosensors | 🔴 0.0 (review) | N/A | N/A |
| 2 | [CN115165998A](https://patents.google.com/patent/CN115165998A/en) — Electrochemical sensor for dopamine detection and preparatio... | 🔴 0.0 (review) | N/A | N/A |
| 3 | [CN108918618A](https://patents.google.com/patent/CN108918618A/en) — A kind of Dopamine Sensor and its preparation and applicatio... | 🔴 0.0 (review) | N/A | N/A |
| 4 | [CN108872343A](https://patents.google.com/patent/CN108872343A/en) — A kind of Dopamine Sensor and its preparation and applicatio... | 🔴 0.0 (review) | N/A | N/A |
| 5 | [CN112479186A](https://patents.google.com/patent/CN112479186A/en) — Method for detecting dopamine with high selectivity based on... | 🔴 0.0 (review) | N/A | N/A |
| 6 | [CN105241868A](https://patents.google.com/patent/CN105241868A/en) — Electrochemiluminescence sensor based on methionine-gold nan... | 🔴 0.0 (review) | N/A | N/A |
| 7 | [CN110006970A](https://patents.google.com/patent/CN110006970A/en) — Preparation method and product and application of electroche... | 🔴 0.0 (review) | N/A | N/A |
| 8 | [CN119246633A](https://patents.google.com/patent/CN119246633A/en) — Working electrode for dopamine electrochemical sensor, dopam... | 🔴 0.0 (review) | N/A | N/A |
| 9 | [rec_64b3458c1dde](https://patents.google.com/patent/TWM590689U/en) — Dopamine chemical sensor | 🔴 0.0 (review) | N/A | N/A |
| 10 | [US20210332489A1](https://patents.google.com/patent/US20210332489A1/en) — Laser-induced graphene electrodes adaptable for electrochemi... | 🔴 0.0 (review) | N/A | N/A |
| 11 | [20250120616](https://patentscope.wipo.int/search/en/detail.jsf?docId=US454142918&_cid=P12-MRXIRX-71771-1) — LASER-INDUCED GRAPHENE NON-ENZYMATIC GLUCOSE
SENSORS
FOR ON ... | 🔴 0.0 (review) | N/A | N/A |
| 12 | [WO/2023/034705](https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2023034705&_cid=P12-MRXIRX-71771-1) — LASER-INDUCED GRAPHENE NON-ENZYMATIC GLUCOSE
SENSORS
FOR ON ... | 🔴 0.0 (review) | N/A | N/A |
| 13 | [2728386](https://patentscope.wipo.int/search/en/detail.jsf?docId=CA94506488&_cid=P12-MRXIRX-71771-1) — NASAL AND OPHTHALMIC DELIVERY OF AQUEOUS CORTICOSTEROID SOLU... | 🔴 0.0 (review) | N/A | N/A |
| 14 | [2002714](https://patentscope.wipo.int/search/en/detail.jsf?docId=EP15030162&_cid=P12-MRXIRX-71771-1) — Neuartige Genunterbrechung, dazugehörige Zusammensetzungen u... | 🔴 0.0 (review) | N/A | N/A |
| 15 | [20090293137](https://patentscope.wipo.int/search/en/detail.jsf?docId=US42902953&_cid=P12-MRXIRX-71771-1) — Novel Gene Disruptions, Compositions and Methods Relating Th... | 🔴 0.0 (review) | N/A | N/A |
| 16 | [2006335053](https://patentscope.wipo.int/search/en/detail.jsf?docId=AU181395466&_cid=P12-MRXIRX-71771-1) — Novel gene disruptions, compositions and methods relating th... | 🔴 0.0 (review) | N/A | N/A |
| 17 | [WO/2007/081608](https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2007081608&_cid=P12-MRXIRX-71771-1) — NOVEL GENE DISRUPTIONS, COMPOSITIONS AND METHODS RELATING TH... | 🔴 0.0 (review) | N/A | N/A |
| 18 | [20110182883](https://patentscope.wipo.int/search/en/detail.jsf?docId=US73308915&_cid=P12-MRXIRX-71771-1) — NOVEL GENE DISRUPTIONS, COMPOSITIONS AND METHODS RELATING TH... | 🔴 0.0 (review) | N/A | N/A |
| 19 | [3155334](https://patentscope.wipo.int/search/en/detail.jsf?docId=CA358706215&_cid=P12-MRXIRX-71771-1) — NMR SYSTEMS AND METHODS FOR THE RAPID DETECTION OF ANALYTES
... | 🔴 0.0 (review) | N/A | N/A |
| 20 | [20210277474](https://patentscope.wipo.int/search/en/detail.jsf?docId=US335377510&_cid=P12-MRXIRX-71771-1) — Methods and compositions for synthetic biomarkers | 🔴 0.0 (review) | N/A | N/A |

---

## 🔍 Análise Detalhada das Patentes

### 1. Laser-induced graphene electrochemical immunosensors

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_4ca678fd8fa5` |
| **Family ID** | `family:d24729ce9fef0fce765d6e926e2d5156ddad985f` |
| **ID** | `WO2021222250A1` |
| **Inventores** | Jonathan CLAUSSEN, Carmen L. GOMES, Raquel Rainier Alves Soares, Robert Hjort, Cicero Cardoso Pola |
| **Titular** | Iowa State University Research Foundation Inc ISURF |
| **Data** | 2021-11-04 |
| **Fonte** | Google Patents |
| **URL** | [WO2021222250A1](https://patents.google.com/patent/WO2021222250A1/en) |
| **Triagem** | review |
| **Rota** | N/A |
| **Motivo da rota** | N/A |
| **Score de Triagem** | 0.0/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | N/A |
| **Cluster Temático** | N/A |
| **Papel do CO2** | N/A |
| **Papel do Armazenamento** | N/A |
| **Limite Sistêmico** | N/A |
| **Tipo de Ciclo** | N/A |
| **Fonte/Sumidouro Térmico** | N/A |
| **Foco das Claims** | N/A |
| **Categoria de Exclusão** | N/A |
| **Confiança** | 0.00 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Sim |
| **Erro LLM** | LLM indisponível. |

**Abstract:**
> AbstractApparatus and methods of fabrication and use of a highly sensitive and label-free laser-induced graphene (LIG) electrode (10) functionalized with biorecognition agents (e.g. antibodies) (18) to electrochemically quantify a target species (e.g. foodborne pathogen Salmonella enterica serovar Typhimurium). In one example, the LIG electrodes are produced by laser induction on polyimide film (12) in ambient conditions, and circumvent need for high-temperature, vacuum environment, and metal seed catalysts commonly associated with graphene-based electrodes fabricated via chemical vapor deposition processes. After functionalization, the LIG biosensors detect a target species across a wide linear range with a low detection limit, and quick response time without need for sample pre-concentration or redox labeling. These LIG immunosensors displayed high selectivity by non-significant response to other bacteria strains, and demonstrate LIG-based electrodes can be used for electrochemical biosensing and immunosensing. One example for rapid, low-cost pathogen detection in food processing facilities before contaminated foods reach the consumer.

---

### 2. Electrochemical sensor for dopamine detection and preparation method and application thereof

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_a3b380e21bf9` |
| **Family ID** | `family:d06f01b66c4c64b70eec8ad17dc782113136186b` |
| **ID** | `CN115165998A` |
| **Inventores** | é©¬è±ä¸, å»å­ç»´ |
| **Titular** | Harbin University of Science and Technology |
| **Data** | 2022-10-11 |
| **Fonte** | Google Patents |
| **URL** | [CN115165998A](https://patents.google.com/patent/CN115165998A/en) |
| **Triagem** | review |
| **Rota** | N/A |
| **Motivo da rota** | N/A |
| **Score de Triagem** | 0.0/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | N/A |
| **Cluster Temático** | N/A |
| **Papel do CO2** | N/A |
| **Papel do Armazenamento** | N/A |
| **Limite Sistêmico** | N/A |
| **Tipo de Ciclo** | N/A |
| **Fonte/Sumidouro Térmico** | N/A |
| **Foco das Claims** | N/A |
| **Categoria de Exclusão** | N/A |
| **Confiança** | 0.00 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Sim |
| **Erro LLM** | LLM indisponível. |

**Abstract:**
> AbstractThe invention discloses an electrochemical sensor for dopamine detection and a preparation method and application thereof, and particularly relates to the field of biomolecule detection. Coating graphene oxide with an amphiphilic surfactant to form an organic soluble graphene oxide compound, dissolving the compound in an organic solvent to prepare an organic solution with a certain concentration, pouring the prepared organic solution on ITO glass under a high humidity condition, obtaining a graphene compound porous membrane on the ITO glass after the organic solvent and water are completely volatilized, and carrying out electrochemical reduction on the membrane under a certain condition to prepare a reduced graphene oxide porous membrane, wherein the reduced graphene oxide porous membrane and the ITO glass jointly form an electrochemical sensor which can be used for detecting dopamine. The invention provides an electrochemical sensor for dopamine detection, which is simple, convenient, nontoxic, cheap, rapid and sensitive.

---

### 3. A kind of Dopamine Sensor and its preparation and application based on sulfonated graphene supported palladium

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_1292a0df852d` |
| **Family ID** | `family:fbba63a1e5637bd969f56bdfd23c63261a93c4fd` |
| **ID** | `CN108918618A` |
| **Inventores** | æ´éè±, èç±å  |
| **Titular** | South China University of Technology SCUT |
| **Data** | 2018-11-30 |
| **Fonte** | Google Patents |
| **URL** | [CN108918618A](https://patents.google.com/patent/CN108918618A/en) |
| **Triagem** | review |
| **Rota** | N/A |
| **Motivo da rota** | N/A |
| **Score de Triagem** | 0.0/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | N/A |
| **Cluster Temático** | N/A |
| **Papel do CO2** | N/A |
| **Papel do Armazenamento** | N/A |
| **Limite Sistêmico** | N/A |
| **Tipo de Ciclo** | N/A |
| **Fonte/Sumidouro Térmico** | N/A |
| **Foco das Claims** | N/A |
| **Categoria de Exclusão** | N/A |
| **Confiança** | 0.00 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Sim |
| **Erro LLM** | LLM indisponível. |

**Abstract:**
> AbstractThe invention belongs to electrochemical sensor technology field, a kind of Dopamine Sensor based on sulfonated graphene supported palladium and its preparation and application are disclosed.The sensor is formed by reference electrode, to the working electrode after electrode and modification, working electrode after the modification is by working electrode and is solidificated in the material identification film of working electrode surface and forms, wherein, the material identification film mainly loads palladium composite material by sulfonated graphene and perfluorinated sulfonic resin is prepared.Sensor of the invention has good selectivity, reproducibility and stability, and electrode catalyst performance is good, can accurately be detected to dopamine, strong antijamming capabilityï¼There is wider detection range, lower detection limit simultaneously.Method of the invention is simple, at low cost.Prepared sensor is for detecting dopamine.

---

### 4. A kind of Dopamine Sensor and its preparation and application based on nitrogen-doped graphene

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_fde35625d301` |
| **Family ID** | `family:2fc43e8bf3c68fc5eb614261128db0c0187d9325` |
| **ID** | `CN108872343A` |
| **Inventores** | é»å½©å¼¯, æ´éè±, æè·çª, çé¯ç«¥ |
| **Titular** | South China University of Technology SCUT |
| **Data** | 2018-11-23 |
| **Fonte** | Google Patents |
| **URL** | [CN108872343A](https://patents.google.com/patent/CN108872343A/en) |
| **Triagem** | review |
| **Rota** | N/A |
| **Motivo da rota** | N/A |
| **Score de Triagem** | 0.0/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | N/A |
| **Cluster Temático** | N/A |
| **Papel do CO2** | N/A |
| **Papel do Armazenamento** | N/A |
| **Limite Sistêmico** | N/A |
| **Tipo de Ciclo** | N/A |
| **Fonte/Sumidouro Térmico** | N/A |
| **Foco das Claims** | N/A |
| **Categoria de Exclusão** | N/A |
| **Confiança** | 0.00 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Sim |
| **Erro LLM** | LLM indisponível. |

**Abstract:**
> AbstractThe invention belongs to electrochemical sensor technology field, a kind of Dopamine Sensor based on nitrogen-doped graphene and its preparation and application are disclosed.The sensor is formed by reference electrode, to the working electrode after electrode and modification, working electrode after modification is by working electrode and is solidificated in the material identification film of working electrode surface and forms, wherein, the material identification film is mainly prepared by nitrogen-doped graphene composite material with perfluorinated sulfonic resin.The invention also discloses the preparation methods of sensor.Sensor of the invention has good selectivity, reproducibility and stability, can accurately be detected to dopamine, strong antijamming capabilityï¼There is wider detection range, lower detection limit simultaneously.Method of the invention is simple, at low cost.Prepared sensor is for detecting dopamine.

---

### 5. Method for detecting dopamine with high selectivity based on electrochemical sensor

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_ca020593ddd1` |
| **Family ID** | `family:39c565e5b73ad5eb3482fec5e5e754183534c0a6` |
| **ID** | `CN112479186A` |
| **Inventores** | èµµé¡º, è·¯å®½ |
| **Titular** | Jiaxing Juetuo Technology Co ltd |
| **Data** | 2021-03-12 |
| **Fonte** | Google Patents |
| **URL** | [CN112479186A](https://patents.google.com/patent/CN112479186A/en) |
| **Triagem** | review |
| **Rota** | N/A |
| **Motivo da rota** | N/A |
| **Score de Triagem** | 0.0/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | N/A |
| **Cluster Temático** | N/A |
| **Papel do CO2** | N/A |
| **Papel do Armazenamento** | N/A |
| **Limite Sistêmico** | N/A |
| **Tipo de Ciclo** | N/A |
| **Fonte/Sumidouro Térmico** | N/A |
| **Foco das Claims** | N/A |
| **Categoria de Exclusão** | N/A |
| **Confiança** | 0.00 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Sim |
| **Erro LLM** | LLM indisponível. |

**Abstract:**
> AbstractThe invention discloses a method for detecting dopamine with high selectivity based on an electrochemical sensor, and relates to the technical field of electrochemical sensors. The electrochemical sensor used in the detection method specifically comprises the following steps: the working electrode, the basement electrode is a glassy carbon electrode, and the compound of NP-NiOsGe/three-dimensional graphene is modified on the surface; the counter electrode is a platinum wire; the reference electrode is a saturated calomel electrode. The electrochemical sensor prepared based on the invention has the advantages of high detection sensitivity, good reproducibility and stability, low detection limit and wide linear detection range, and can realize the specific detection of dopamine.

---

### 6. Electrochemiluminescence sensor based on methionine-gold nanocluster

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_d461537cff92` |
| **Family ID** | `family:625dadd06407ab0cc9e4554f09c66e1ad80aa288` |
| **ID** | `CN105241868A` |
| **Inventores** | å½­è±è, éä¼, éè±ªå, ç®ç¾ä¸½, åç±æ |
| **Titular** | Fujian Medical University |
| **Data** | 2016-01-13 |
| **Fonte** | Google Patents |
| **URL** | [CN105241868A](https://patents.google.com/patent/CN105241868A/en) |
| **Triagem** | review |
| **Rota** | N/A |
| **Motivo da rota** | N/A |
| **Score de Triagem** | 0.0/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | N/A |
| **Cluster Temático** | N/A |
| **Papel do CO2** | N/A |
| **Papel do Armazenamento** | N/A |
| **Limite Sistêmico** | N/A |
| **Tipo de Ciclo** | N/A |
| **Fonte/Sumidouro Térmico** | N/A |
| **Foco das Claims** | N/A |
| **Categoria de Exclusão** | N/A |
| **Confiança** | 0.00 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Sim |
| **Erro LLM** | LLM indisponível. |

**Abstract:**
> AbstractTranslated fromChineseæ¬åæå¬å¼ä¸ç§<b>åºäºç²ç¡«æ°¨é¸</b><b>-</b><b>éçº³ç±³å¢ç°ççµè´åå­¦ååä¼ æå¨</b>ï¼å¶æ¯ä»¥ç²ç¡«æ°¨é¸ä¿æ¤çéçº³ç±³å¢ç°ææä¸ºååä½ï¼è¿ç¡«é¸æ ¹ç¦»å­ä¸ºå±ååºåï¼å°ç²ç¡«æ°¨é¸ä¿æ¤çéçº³ç±³å¢ç°ä¿®é¥°å¨ç»ç¢³çµæä¸ï¼è¿è¡çµåå­¦ååæµè¯ï¼å¹¶å®ç°å¯¹å¤å·´èºçæ£æµãè¯¥ä¼ æå¨å¯¹å¯¹å¤å·´èºæ£æµççº¿æ§èå´ä¸º0.1~4ï¼Î¼mol/Lå4~25ï¼Î¼mol/Lï¼æ£æµéä¸º0.032ï¼Î¼mol/Lãæ¬åææå¾å°çç²ç¡«æ°¨é¸ä¿æ¤çéçº³ç±³å¢ç°å¶å¤æ¹æ³ç»¿è²ç¯ä¿ï¼æä½ç®ä¾¿å¿«æ·ï¼éç°æ§å¥½ï¼å¶å¤çç²ç¡«æ°¨é¸ä¿æ¤çéçº³ç±³å¢ç°çç©ç¸å®¹æ§å¥½ï¼å¹¶å·æè¾å¥½ççµè´åå­¦ååæ§è½ãThe invention discloses an electrochemiluminescence sensor based on <b>methionine</b><b>-</b><b>gold nanocluster</b>, which is based on methionine The protected gold nanocluster material is a luminescent body, and the persulfate ion is a co-reactant. The methionine-protected gold nanocluster is modified on the glassy carbon electrode, and the electrochemiluminescence test is performed, and the detection of dopamine is realized. . The linear range of the sensor for dopamine detection is 0.1~4? Î¼mol/L and 4~25? Î¼mol/L, the detection limit is 0.032? Î¼mol/L. The preparation method of the methionine-protected gold nanoclusters obtained in the present invention is green and environmentally friendly, and the operation is simple and quick, and the reproducibility is good. The prepared methionine-protected gold nanoclusters have good biocompatibility, and have relatively Good electrochemiluminescent properties.

---

### 7. Preparation method and product and application of electrochemical sensor for dopamine detection

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_daeced5ae557` |
| **Family ID** | `family:47efa98f8f27f477b45b45f6046adf7c2a5ff0e9` |
| **ID** | `CN110006970A` |
| **Inventores** | ä½ä¸¹å, çä¸¹, èç¾è±, å¢é, éå½©è¹ |
| **Titular** | Shanghai National Engineering Research Center for Nanotechnology Co Ltd |
| **Data** | 2019-07-12 |
| **Fonte** | Google Patents |
| **URL** | [CN110006970A](https://patents.google.com/patent/CN110006970A/en) |
| **Triagem** | review |
| **Rota** | N/A |
| **Motivo da rota** | N/A |
| **Score de Triagem** | 0.0/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | N/A |
| **Cluster Temático** | N/A |
| **Papel do CO2** | N/A |
| **Papel do Armazenamento** | N/A |
| **Limite Sistêmico** | N/A |
| **Tipo de Ciclo** | N/A |
| **Fonte/Sumidouro Térmico** | N/A |
| **Foco das Claims** | N/A |
| **Categoria de Exclusão** | N/A |
| **Confiança** | 0.00 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Sim |
| **Erro LLM** | LLM indisponível. |

**Abstract:**
> AbstractTranslated fromChineseæ¬åææä¾ä¸ç§ç¨äºå¤å·´èºæ£æµççµåå­¦ä¼ æå¨çå¶å¤æ¹æ³åå¶äº§åååºç¨ï¼æè¿°çä¼ æå¨åæ¬ï¼çµæåºä½ãä¿®é¥°å±åçº³ç±³ç²å­ï¼å¶ä¸­æè¿°ççµæåºä½ä¸ºç»ç¢³æè´¨ççµæåºä½ï¼æè¿°çåå­¦ä¿®é¥°å±ä¸ºæº´éèå±ï¼çº³ç±³ç²å­ä¸ºIrO2âPtï¼è¯¥çµåå­¦ä¼ æå¨è½å¤å®ç°å¯¹å¤å·´èºçå³æ¶æ£æµãè¯¥ä¼ æå¨æ¯åºäºå°çº³ç±³ææ¯ãçµåå­¦åæææ¯åä¼ æå¨å¶å¤ææ¯ç¸ç»åï¼å¼åäºæ°åçç¨äºæ£æµçç©æ ·åä¸­å¤å·´èºççµåå­¦ä¼ æå¨ãæä¾ä¸ç§å¿«éãçµæãç®ä¾¿çç¨äºå¤å·´èºæ£æµççµåå­¦ä¼ æå¨ãThe invention provides a preparation method, product and application of an electrochemical sensor for dopamine detection. The sensor comprises: an electrode substrate, a modified layer and nanoparticles, wherein the electrode substrate is an electrode substrate made of glassy carbon material The chemical modification layer is a bromophenol blue layer; the nanoparticle is IrO2-Pt, and the electrochemical sensor can realize instant detection of dopamine. The sensor is based on the combination of nanotechnology, electrochemical analysis technology and sensor preparation technology to develop a new electrochemical sensor for detecting dopamine in biological samples. A fast, sensitive and simple electrochemical sensor for dopamine detection is provided.

---

### 8. Working electrode for dopamine electrochemical sensor, dopamine electrochemical sensor and application thereof

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_179b3a7db28d` |
| **Family ID** | `family:cbc7a43368bbf29f5c3d10f7800ab72437e8c5dd` |
| **ID** | `CN119246633A` |
| **Inventores** | å§¬åæ³¢, çå¶ç, èå¦®, å¼ å¯ä¸, æ´å½ç§, èæ­¦, å²æ¸ç§, æ¨æ, ä½ä¿æ±, å±å± |
| **Titular** | Henan Xinqiao Tobacco Technology Service Co ltd |
| **Data** | 2025-01-03 |
| **Fonte** | Google Patents |
| **URL** | [CN119246633A](https://patents.google.com/patent/CN119246633A/en) |
| **Triagem** | review |
| **Rota** | N/A |
| **Motivo da rota** | N/A |
| **Score de Triagem** | 0.0/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | N/A |
| **Cluster Temático** | N/A |
| **Papel do CO2** | N/A |
| **Papel do Armazenamento** | N/A |
| **Limite Sistêmico** | N/A |
| **Tipo de Ciclo** | N/A |
| **Fonte/Sumidouro Térmico** | N/A |
| **Foco das Claims** | N/A |
| **Categoria de Exclusão** | N/A |
| **Confiança** | 0.00 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Sim |
| **Erro LLM** | LLM indisponível. |

**Abstract:**
> AbstractTranslated fromChineseæ¬åææ¶åä¸ç§å¤å·´èºçµåå­¦ä¼ æå¨ç¨å·¥ä½çµæãå¤å·´èºçµåå­¦ä¼ æå¨åå¶åºç¨ï¼å±äºçµåå­¦ä¼ æå¨ææ¯é¢åãæ¬åæçå¤å·´èºçµåå­¦ä¼ æå¨ç¨å·¥ä½çµæåæ¬çµæåºåºåä¿®é¥°å¨çµæåºåºè¡¨é¢çç¼ºé·åäºç¡«åé¼ï¼æè¿°ç¼ºé·åäºç¡«åé¼ä¸ºç¡«ç©ºä½ç¼ºé·çäºç¡«åé¼ãç±æè¿°å·¥ä½çµææå»ºçå¤å·´èºçµåå­¦ä¼ æå¨ï¼è½å¢å¼ºæ£æµæ¶å¯¹å¤å·´èºçéæ©æ§ï¼è½å¤æ¾èå°æå¶æåè¡é¸åå°¿é¸ççµåå­¦æ°§åï¼éå¯¹æ§å°è§£å³äºå¤å·´èºæ£æµè¿ç¨ä¸­çä¿¡å·å¹²æ°é®é¢ãThe present invention relates to a working electrode for a dopamine electrochemical sensor, a dopamine electrochemical sensor and its application, and belongs to the technical field of electrochemical sensors. The working electrode for the dopamine electrochemical sensor of the present invention comprises an electrode substrate and defective molybdenum disulfide modified on the surface of the electrode substrate; the defective molybdenum disulfide is molybdenum disulfide with sulfur vacancy defects. The dopamine electrochemical sensor constructed by the working electrode can enhance the selectivity of dopamine during detection, can significantly inhibit the electrochemical oxidation of ascorbic acid and uric acid, and specifically solves the signal interference problem in the dopamine detection process.

---

### 9. Dopamine chemical sensor

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_64b3458c1dde` |
| **Family ID** | `family:019a4516008afce24815f687642c6dab2e5f0c9a` |
| **ID** | `` |
| **Inventores** | ç¿äºæ´, å³ç³ä¹, çé»é |
| **Titular** | é¢ç²å¤§å­¸ |
| **Data** | 2020-02-11 |
| **Fonte** | Google Patents |
| **URL** | [rec_64b3458c1dde](https://patents.google.com/patent/TWM590689U/en) |
| **Triagem** | review |
| **Rota** | N/A |
| **Motivo da rota** | N/A |
| **Score de Triagem** | 0.0/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | N/A |
| **Cluster Temático** | N/A |
| **Papel do CO2** | N/A |
| **Papel do Armazenamento** | N/A |
| **Limite Sistêmico** | N/A |
| **Tipo de Ciclo** | N/A |
| **Fonte/Sumidouro Térmico** | N/A |
| **Foco das Claims** | N/A |
| **Categoria de Exclusão** | N/A |
| **Confiança** | 0.00 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Sim |
| **Erro LLM** | LLM indisponível. |

**Abstract:**
> AbstractTranslated fromChineseä¸ç¨®å¤å·´èºåå­¸ææ¸¬å¨ï¼åæ¬ææ¬é«ãéé ­ãå·¥ä½é»æ¥µãåèé»æ¥µä»¥åå°é»æ¥µçµæï¼æ¬é«å§é¨æå¸éçï¼èéé ­ç¸å°æ¬é«çµåèæå¸ï¼çµåæéé ­ä¸ç«¯æ¥è§¸å¸éçï¼èå·¥ä½é»æ¥µãåèé»æ¥µä»¥åå°é»æ¥µè¨­ç½®æ¼æ¬é«èè©²å¸éçæ¥è§¸ï¼è©²å·¥ä½é»æ¥µåæ¬æç»çç¢³é»æ¥µ(GCEï¼glass carbon electrode)ä»¥åçµåæ¼ç»çç¢³é»æ¥µä¹ä¸éå¥ç±³ç¢³çºç¶­(Au-CNF)ï¼æçºä¸ç¨®å·æé«éæåº¦çåå­¸ç©è³ªææ¸¬å¨å·ï¼å¿«éæºç¢ºæª¢æ¸¬å¤å·´èºãA dopamine chemical sensor includes a body, a needle, a working electrode, a reference electrode, and a counter electrode. The body has an adsorption sheet, and the needle is assembled and disassembled from the body. When the assembly is combined, the end of the needle contacts the adsorption sheet, and the working electrode, The reference electrode and the counter electrode are disposed on the body to contact the adsorption sheet. The working electrode includes a glass carbon electrode (GCE) and one of the glass carbon electrodes (Gnano carbon fiber (Au-CNF)). High-sensitivity chemical sensing device for fast and accurate detection of dopamine.

---

### 10. Laser-induced graphene electrodes adaptable for electrochemical sensing and catalysis

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_bfa14d23f878` |
| **Family ID** | `family:429302c80fc82bb48c3297026895d4ded8e84279` |
| **ID** | `US20210332489A1` |
| **Inventores** | Jonathan Claussen, Carmen L. Gomes, Raquel Rainier Alves Soares, Robert Hjort, Cicero Cardoso Pola |
| **Titular** | Iowa State University Research Foundation Inc ISURF |
| **Data** | 2021-10-28 |
| **Fonte** | Google Patents |
| **URL** | [US20210332489A1](https://patents.google.com/patent/US20210332489A1/en) |
| **Triagem** | review |
| **Rota** | N/A |
| **Motivo da rota** | N/A |
| **Score de Triagem** | 0.0/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | N/A |
| **Cluster Temático** | N/A |
| **Papel do CO2** | N/A |
| **Papel do Armazenamento** | N/A |
| **Limite Sistêmico** | N/A |
| **Tipo de Ciclo** | N/A |
| **Fonte/Sumidouro Térmico** | N/A |
| **Foco das Claims** | N/A |
| **Categoria de Exclusão** | N/A |
| **Confiança** | 0.00 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Sim |
| **Erro LLM** | LLM indisponível. |

**Abstract:**
> AbstractApparatus and methods of fabrication and use of highly effective laser-induced graphene (LIG) electrodes including for electrochemical sensing and catalysis. One example is a sensitive and label-free laser-induced graphene (LIG) electrode functionalized for a specific application. One example of functionalization with antibodies, an enzyme, or an ionophore to electrochemically quantify a target species The LIG electrodes were produced by laser induction on film having a carbon precursor (e.g. polyimide) in ambient conditions, and hence circumvent the need for high-temperature, vacuum environment, and metal seed catalysts commonly associated with graphene-based electrodes fabricated via chemical vapor deposition processes. These results demonstrate how LIG-based electrodes can be used for electrochemical sensing in general. Other examples of applications include, but are not limited to, ion-sensing, pesticide monitoring and detection, and water splitting, using the LIG-based electrode(s) adapted for those purposes.

---

### 11. LASER-INDUCED GRAPHENE NON-ENZYMATIC GLUCOSE
SENSORS
FOR ON BODY MEASUREMENTS

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_ce6b4ec2085f` |
| **Family ID** | `family:e7763cceb03809b444551e588de12801f7a32ee4` |
| **ID** | `20250120616` |
| **Inventores** | Huanyu Cheng |
| **Titular** | The Penn State Research Foundation |
| **Data** | 17.04.2025 |
| **Fonte** | Patentscope |
| **URL** | [20250120616](https://patentscope.wipo.int/search/en/detail.jsf?docId=US454142918&_cid=P12-MRXIRX-71771-1) |
| **Triagem** | review |
| **Rota** | N/A |
| **Motivo da rota** | N/A |
| **Score de Triagem** | 0.0/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | N/A |
| **Cluster Temático** | N/A |
| **Papel do CO2** | N/A |
| **Papel do Armazenamento** | N/A |
| **Limite Sistêmico** | N/A |
| **Tipo de Ciclo** | N/A |
| **Fonte/Sumidouro Térmico** | N/A |
| **Foco das Claims** | N/A |
| **Categoria de Exclusão** | N/A |
| **Confiança** | 0.00 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Sim |
| **Erro LLM** | LLM indisponível. |

**Abstract:**
> (EN)Embodiments relate to a non-enzymatic glucosesensor. The non-enzymatic glucosesensorcomprises one or more electrodes, a microfluidic channel, and at least one inlet, wherein the at least one inlet is configured to deliver a fluid to a microfluidic channel and wherein the microfluidic channel is configured to transport the fluid to the one or more electrodes. At least one of the one or more electrodes is a laser-induced graphene electrode, wherein the laser-induced graphene electrode comprises one or more uniform coatings of metal.

---

### 12. LASER-INDUCED GRAPHENE NON-ENZYMATIC GLUCOSE
SENSORS
FOR ON BODY MEASUREMENTS
(FR)
CAPTEURS DE GLUCOSE NON ENZYMATIQUES AU GRAPHÈNE INDUIT PAR LASER POUR MESURES CORPORELLES

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_d9a330124ef1` |
| **Family ID** | `family:71df663b4369100fdab4ec9faa37fa65849ac65a` |
| **ID** | `WO/2023/034705` |
| **Inventores** | CHENG, Huanyu |
| **Titular** | THE PENN STATE RESEARCH FOUNDATION
[US]/[US] |
| **Data** | 09.03.2023 |
| **Fonte** | Patentscope |
| **URL** | [WO/2023/034705](https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2023034705&_cid=P12-MRXIRX-71771-1) |
| **Triagem** | review |
| **Rota** | N/A |
| **Motivo da rota** | N/A |
| **Score de Triagem** | 0.0/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | N/A |
| **Cluster Temático** | N/A |
| **Papel do CO2** | N/A |
| **Papel do Armazenamento** | N/A |
| **Limite Sistêmico** | N/A |
| **Tipo de Ciclo** | N/A |
| **Fonte/Sumidouro Térmico** | N/A |
| **Foco das Claims** | N/A |
| **Categoria de Exclusão** | N/A |
| **Confiança** | 0.00 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Sim |
| **Erro LLM** | LLM indisponível. |

**Abstract:**
> (EN)Embodiments relate to a non-enzymatic glucosesensor. The non-enzymatic glucosesensorcomprises one or more electrodes, a microfluidic channel, and at least one inlet, wherein the at least one inlet is configured to deliver a fluid to a microfluidic channel and wherein the microfluidic channel is configured to transport the fluid to the one or more electrodes. At least one of the one or more electrodes is a laser-induced graphene electrode, wherein the laser-induced graphene electrode comprises one or more uniform coatings of metal.(FR)Des modes de réalisation concernent un capteur de glucose non enzymatique. Le capteur de glucose non enzymatique comprend une ou plusieurs électrodes, un canal microfluidique, et au moins une entrée, l'au moins une entrée étant conçue pour distribuer un fluide à un canal microfluidique et le canal microfluidique étant conçu pour transporter le fluide vers la ou les électrodes. Au moins l'une des électrodes est une électrode en graphène induit par laser, l'électrode en graphène induit par laser comprenant un ou plusieurs revêtements uniformes de métal.

---

### 13. NASAL AND OPHTHALMIC DELIVERY OF AQUEOUS CORTICOSTEROID SOLUTIONS
(FR)
ADMINISTRATION NASALE ET OPHTALMIQUE DE SOLUTIONS AQUEUSES DE CORTICOSTEROIDES

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_523dc554e6aa` |
| **Family ID** | `family:f8ea6a6aa6ef0d8b5d5d6c230f9f7ed3667b7f91` |
| **ID** | `2728386` |
| **Inventores** | JAMES D. PIPKIN, RUPERT O. ZIMMERER, JOHN M. SIEBERT |
| **Titular** | CYDEX PHARMACEUTICALS, INC. |
| **Data** | 31.12.2008 |
| **Fonte** | Patentscope |
| **URL** | [2728386](https://patentscope.wipo.int/search/en/detail.jsf?docId=CA94506488&_cid=P12-MRXIRX-71771-1) |
| **Triagem** | review |
| **Rota** | N/A |
| **Motivo da rota** | N/A |
| **Score de Triagem** | 0.0/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | N/A |
| **Cluster Temático** | N/A |
| **Papel do CO2** | N/A |
| **Papel do Armazenamento** | N/A |
| **Limite Sistêmico** | N/A |
| **Tipo de Ciclo** | N/A |
| **Fonte/Sumidouro Térmico** | N/A |
| **Foco das Claims** | N/A |
| **Categoria de Exclusão** | N/A |
| **Confiança** | 0.00 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Sim |
| **Erro LLM** | LLM indisponível. |

**Abstract:**
> (EN)The present invention is directed to methods of treating nasal and/or  ophthalmic diseases, symptoms, or disorders  that are therapeutically responsive to corticosteroid therapy by delivering  aqueous solution formulations comprising a corticosteroid to nasal and ophthalmic tissues. The invention is also directed  to methods, systems, devices, and compositions for  delivering aqueous solution formulations comprising a corticosteroid and an  antihistamine to nasal and ophthalmic tissues watering eyes(FR)La présente invention concerne des procédés de traitement de maladies, symptômes ou troubles nasaux et/ou ophtalmiques qui réagissent d'un point de vue thérapeutique au traitement par corticostéroïdes administrés aux tissus nasaux et ophtalmiques sous forme de formulations de solution aqueuse contenant un corticostéroïde. L'invention porte aussi sur des procédés, des systèmes, des dispositifs et des compositions permettant d'administrer des formulations de solution aqueuse contenant un corticostéroïde et un antihistaminique à des tissus nasaux et ophtalmiques.

---

### 14. Neuartige Genunterbrechung, dazugehörige Zusammensetzungen und Verfahren
(EN)
Novel gene disruptions, compositions and methods relating thereto
(FR)
Nouvelles ruptures génétiques, compositions et procédés associés à celles-ci

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_f38e10ba5b6d` |
| **Family ID** | `family:d18e2075a4c8490a06d9cbd94cabaa60b4da8a3a` |
| **ID** | `2002714` |
| **Inventores** | BYERS-HORNER ALLISON ANNE, COMBS KATHERIN, DESAUVAGE FREDERIC, FAN LIANGFEN, FILVAROFF ELLEN, IRVING BRYAN, JUNUTULA JAGATH REDDY, MASSEY ERIN MARIE, MCLAIN DINA REBECCA, MINZE LAURIE JEANNETTE, MONTGOMERY CHARLES A, PAYNE BOBBY JOE, PHILLIPS HEIDI, RANGEL CAROLINA, SHI ZHENG-ZHENG, SPARKS MARY JEAN, STALA JOY, TOWNSEND TERESA GAIL, VOGEL PETER, WILLIS-SEVAUX TRACY ELLEN |
| **Titular** | GENENTECH INC
LEXICON PHARMACEUTICALS INC |
| **Data** | 17.12.2008 |
| **Fonte** | Patentscope |
| **URL** | [2002714](https://patentscope.wipo.int/search/en/detail.jsf?docId=EP15030162&_cid=P12-MRXIRX-71771-1) |
| **Triagem** | review |
| **Rota** | N/A |
| **Motivo da rota** | N/A |
| **Score de Triagem** | 0.0/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | N/A |
| **Cluster Temático** | N/A |
| **Papel do CO2** | N/A |
| **Papel do Armazenamento** | N/A |
| **Limite Sistêmico** | N/A |
| **Tipo de Ciclo** | N/A |
| **Fonte/Sumidouro Térmico** | N/A |
| **Foco das Claims** | N/A |
| **Categoria de Exclusão** | N/A |
| **Confiança** | 0.00 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Sim |
| **Erro LLM** | LLM indisponível. |

**Abstract:**
> (EN)The present invention relates to transgenic animals, as well as compositions and methods relating to the characterization of gene function. Specifically, the present invention provides transgenic mice comprising disruptions in PRO218, PRO228, PRO271, PRO273, PRO295, PRO302, PRO305, PRO326, PRO386, PRO655, PRO162, PRO788, PRO792, PRO940, PRO941, PRO1004, PRO1012, PRO1016, PRO474, PRO5238, PRO1069 PRO1111, PRO1113, PRO1130, PRO1195, PRO1271, PRO1865, PRO1879, PRO3446, PRO3543, PRO4329, PRO4352, PRO5733, PRO9859, PRO9864, PRO9904, PRO9907, PRO10013, PRO90948, PRO28694, PRO16089, PRO19563, PRO19675, PRO20084, PRO21434, PRO50332, PRO38465 or PRO346 genes. Such in vivo studies and characterizations may provide valuable identification and discovery of therapeutics and/or treatments useful in the prevention, amelioration or correction of diseases or dysfunctions associated with gene disruptions such as neurological disorders; cardiovascular, endothelial or angiogenic disorders; eye abnormalities; immunological disorders; oncological disorders; bone metabolic abnormalities or disorders; lipid metabolic disorders; or developmental abnormalities.

---

### 15. Novel Gene Disruptions, Compositions and Methods Relating Thereto

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_4873e210a0a6` |
| **Family ID** | `family:c236cefdf1f7bcf8ddbdd7a0fe07a6d701d0e681` |
| **ID** | `20090293137` |
| **Inventores** | Combs Katherin E., de Sauvage Frederic J., Fan Liangfen, Filvaroff Ellen, Horner Allison A. B., Irving Bryan, Juntula Jagath Reddy, Massey Erin Marie, McLain Dina Rebecca, Minze Laurie Jeanette, Montgomery Charles, Payne Bobby Joe, Philips Heidi, Rangel Carolina, Sevaux Tracy E. W., Shi Zheng-Zheng, Sparks Mary Jean, Stala Joy Anne, Townsend Teresa G., Vogel Peter |
| **Titular** | Genentech, Inc. |
| **Data** | 26.11.2009 |
| **Fonte** | Patentscope |
| **URL** | [20090293137](https://patentscope.wipo.int/search/en/detail.jsf?docId=US42902953&_cid=P12-MRXIRX-71771-1) |
| **Triagem** | review |
| **Rota** | N/A |
| **Motivo da rota** | N/A |
| **Score de Triagem** | 0.0/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | N/A |
| **Cluster Temático** | N/A |
| **Papel do CO2** | N/A |
| **Papel do Armazenamento** | N/A |
| **Limite Sistêmico** | N/A |
| **Tipo de Ciclo** | N/A |
| **Fonte/Sumidouro Térmico** | N/A |
| **Foco das Claims** | N/A |
| **Categoria de Exclusão** | N/A |
| **Confiança** | 0.00 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Sim |
| **Erro LLM** | LLM indisponível. |

**Abstract:**
> (EN)The present invention relates to transgenic animals, as well as compositions and methods relating to the characterization of gene function. Specifically, the present invention provides transgenic mice comprising disruptions in PRO218, PRO228, PRO271, PRO273, PRO295, PRO302, PRO305, PRO326, PRO386, PRO655, PRO162, PRO788, PRO792, PRO940, PRO941, PRO1004, PRO1012, PRO 1016, PRO474, PRO5238, PRO1069, PRO1111, PRO1113, PRO1130, PRO1195, PRO1271, PRO1865, PRO1879, PRO3446, PRO3543, PRO4329, PRO4352, PRO5733, PRO9859, PRO9864, PRO9904, PRO9907, PRO10013, PRO90948, PRO28694, PRO16089, PRO19563, PRO19675, PRO20084, PRO21434, PRO50332, PRO38465 or PRO346 genes. Such in vivo studies and characterizations may provide valuable identification and discovery of therapeutics and/or treatments useful in the prevention, amelioration or correction of diseases or dysfunctions associated with gene disruptions such as neurological disorders; cardiovascular, endothelial or angiogenic disorders; eye abnormalities; immunological disorders; oncological disorders; bone metabolic abnormalities or disorders; lipid metabolic disorders; or developmental abnormalities.

---

### 16. Novel gene disruptions, compositions and methods relating thereto

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_4b6228965ee5` |
| **Family ID** | `family:db464802277ee5afca547677303b6c3258ef1421` |
| **ID** | `2006335053` |
| **Inventores** | Combs, Katherin E., Desauvage, Frederic, Fan, Liangfen, Filvaroff, Ellen, Horner, Allison Anne Byers, Irving, Bryan, Junutula, Jagath Reddy, Massey, Erin Marie, McLain, Dina Rebecca, Minze, Laurie Jeanette, Montgomery, Charles A., Payne, Bobby Joe, Phillips, Heidi, Rangel, Carolina, Sevaux, Tracy Ellen Willis, Shi, Zheng-zheng, Sparks, Mary Jean, Stala, Joy Anne, Townsend, Teresa Gail, Vogel, Peter |
| **Titular** | Genentech, Inc.
Lexicon Pharmaceuticals, Inc. |
| **Data** | 15.05.2008 |
| **Fonte** | Patentscope |
| **URL** | [2006335053](https://patentscope.wipo.int/search/en/detail.jsf?docId=AU181395466&_cid=P12-MRXIRX-71771-1) |
| **Triagem** | review |
| **Rota** | N/A |
| **Motivo da rota** | N/A |
| **Score de Triagem** | 0.0/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | N/A |
| **Cluster Temático** | N/A |
| **Papel do CO2** | N/A |
| **Papel do Armazenamento** | N/A |
| **Limite Sistêmico** | N/A |
| **Tipo de Ciclo** | N/A |
| **Fonte/Sumidouro Térmico** | N/A |
| **Foco das Claims** | N/A |
| **Categoria de Exclusão** | N/A |
| **Confiança** | 0.00 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Sim |
| **Erro LLM** | LLM indisponível. |

**Abstract:**
> (EN)The present invention relates to transgenic animals, as well as compositions and methods relating to the characterization of gene function. Specifically, the present invention provides transgenic mice comprising disruptions in PRO218, PRO228, PRO271, PRO273, PRO295, PRO302, PRO305, PRO326, PRO386, PRO655, PRO162, PRO788, PRO792, PRO940, PRO941, PRO1004, PRO1012, PRO1016, PRO474, PRO5238, PRO1069, PRO1111, PRO1113, PRO1130, PRO1195, PRO1271, PRO1865, PRO1879, PRO3446, PRO3543, PRO4329, PRO4352, PRO5733, PRO9859, PRO9864, PRO9904, PRO9907, PRO10013, PRO90948, PRO28694, PRO16089, PRO19563, PRO19675, PRO20084, PRO21434, PRO50332, PRO38465 or PRO346 genes. Such in vivo studies and characterizations may provide valuable identification and discovery of therapeutics and/or treatments useful in the prevention, amelioration or correction of diseases or dysfunctions associated with gene disruptions such as neurological disorders; cardiovascular, endothelial or angiogenic disorders; eye abnormalities; immunological disorders; oncological disorders; bone metabolic abnormalities or disorders; lipid metabolic disorders; or developmental abnormalities.

---

### 17. NOVEL GENE DISRUPTIONS, COMPOSITIONS AND METHODS RELATING THERETO
(FR)
NOUVELLES DISSOCIATIONS DE GÈNES, COMPOSITIONS ET PROCÉDÉS LES CONCERNANT

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_4eda793a65f1` |
| **Family ID** | `family:9febc3497a8f389587ece109495b4fde6ab7ecd6` |
| **ID** | `WO/2007/081608` |
| **Inventores** | HORNER, Allison, Anne, Byers, COMBS, Katherin, E., DESAUVAGE, Frederic, FAN, Liangfen, FILVAROFF, Ellen, IRVING, Bryan, JUNUTULA, Jagath Reddy, MASSEY, Erin Marie, MCLAIN, Dina Rebecca, MINZE, Laurie Jeanette, MONTGOMERY, Charles, A., PAYNE, Bobby Joe, PHILLIPS, Heidi, RANGEL, Carolina, SHI, Zheng-zheng, SPARKS, Mary Jean, STALA, Joy, Anne, TOWNSEND, Teresa Gail, VOGEL, Peter, SEVAUX, Tracy Ellen Willis |
| **Titular** | GENENTECH, INC.
[US]/[US]
(AllExceptUS)
LEXICON PHARMACEUTICALS, INC.
[US]/[US]
(AllExceptUS)
HORNER, Allison, Anne, Byers
[US]/[US](UsOnly)
COMBS, Katherin, E.
[US]/[US](UsOnly)
DESAUVAGE, Frederic
[BE]/[US](UsOnly)
FAN, Liangfen
[US]/[US](UsOnly)
FILVAROFF, Ellen
[US]/[US](UsOnly)
IRVING, Bryan
[US]/[US](UsOnly)
JUNUTULA, Jagath Reddy
[IN]/[US](UsOnly)
MASSEY, Erin Marie
[US]/[US](UsOnly)
MCLAIN, Dina Rebecca
[US]/[US](UsOnly)
MINZE, Laurie Jeanette
[US]/[US](UsOnly)
MONTGOMERY, Charles, A.
[US]/[US](UsOnly)
PAYNE, Bobby Joe
[US]/[US](UsOnly)
PHILLIPS, Heidi
[US]/[US](UsOnly)
RANGEL, Carolina
[US]/[US](UsOnly)
SHI, Zheng-zheng
[CN]/[US](UsOnly)
SPARKS, Mary Jean
[US]/[US](UsOnly)
STALA, Joy, Anne
[US]/[US](UsOnly)
TOWNSEND, Teresa Gail
[US]/[US](UsOnly)
VOGEL, Peter
[US]/[US](UsOnly)
SEVAUX, Tracy Ellen Willis
[US]/[US](UsOnly) |
| **Data** | 19.07.2007 |
| **Fonte** | Patentscope |
| **URL** | [WO/2007/081608](https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2007081608&_cid=P12-MRXIRX-71771-1) |
| **Triagem** | review |
| **Rota** | N/A |
| **Motivo da rota** | N/A |
| **Score de Triagem** | 0.0/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | N/A |
| **Cluster Temático** | N/A |
| **Papel do CO2** | N/A |
| **Papel do Armazenamento** | N/A |
| **Limite Sistêmico** | N/A |
| **Tipo de Ciclo** | N/A |
| **Fonte/Sumidouro Térmico** | N/A |
| **Foco das Claims** | N/A |
| **Categoria de Exclusão** | N/A |
| **Confiança** | 0.00 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Sim |
| **Erro LLM** | LLM indisponível. |

**Abstract:**
> (EN)The present invention relates to transgenic animals, as well as compositions and methods relating to the characterization of gene function. Specifically, the present invention provides transgenic mice comprising disruptions in PRO218, PRO228, PRO271, PRO273, PRO295, PRO302, PRO305, PRO326, PRO386, PRO655, PRO162, PRO788, PRO792, PRO940, PRO941, PRO1004, PRO1012, PRO1016, PRO474, PRO5238, PRO1069, PRO1111, PRO1113, PRO1130, PRO1195, PRO1271, PRO1865, PRO1879, PRO3446, PRO3543, PRO4329, PRO4352, PRO5733, PRO9859, PRO9864, PRO9904, PRO9907, PRO10013, PRO90948, PRO28694, PRO16089, PRO19563, PRO19675, PRO20084, PRO21434, PRO50332, PRO38465 or PRO346 genes. Such in vivo studies and characterizations may provide valuable identification and discovery of therapeutics and/or treatments useful in the prevention, amelioration or correction of diseases or dysfunctions associated with gene disruptions such as neurological disorders; cardiovascular, endothelial or angiogenic disorders; eye abnormalities; immunological disorders; oncological disorders; bone metabolic abnormalities or disorders; lipid metabolic disorders; or developmental abnormalities.(FR)La présente invention concerne des animaux transgéniques, ainsi que des compositions et des procédés concernant la caractérisation de la fonction génique. Spécifiquement, la présente invention concerne une souris transgénique comprenant des dissociations des gènes PRO218, PRO228, PRO271, PRO273, PRO295, PRO302, PRO305, PRO326, PRO386, PRO655, PRO162, PRO788, PRO792, PRO940, PRO941, PRO1004, PRO1012, PRO1016, PRO474, PRO5238, PRO1069, PRO1111, PRO1113, PRO1130, PRO1195, PRO1271, PRO1865, PRO1879, PRO3446, PRO3543, PRO4329, PRO4352, PRO5733, PRO9859, PRO9864, PRO9904, PRO9907, PRO10013, PRO90948, PRO28694, PRO16089, PRO19563, PRO19675, PRO20084, PRO21434, PRO50332, PRO38465 ou PRO346. Ces études et ces caractérisationsin vivopermettent d'identifier et de découvrir des agents thérapeutiques et/ou des traitements de valeur utiles dans la prévention, l'amélioration ou la correction de maladies ou de dysfonctions associées à des dissociations de gènes, par exemple les troubles neurologiques ; les troubles cardiovasculaires, endothéliaux ou angiogènes ; les anomalies oculaires ; les troubles immunologiques ; les troubles oncologiques ; les anomalies ou les troubles du métabolisme osseux ; les troubles du métabolisme des lipides ; ou les anomalies développementales.

---

### 18. NOVEL GENE DISRUPTIONS, COMPOSITIONS AND METHODS RELATING THERETO

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_b4048237afc7` |
| **Family ID** | `family:7dc166045453313da483d34a1801ddc3f3b281d9` |
| **ID** | `20110182883` |
| **Inventores** | Combs Katherin E., de Sauvage Frederic, Fan Liangfen, Filvaroff Ellen, Horner Allison Anne Byers, Irving Bryan, Junutula Jagath Reddy, Massey Erin Marie, Mclain Dina Rebecca, Minze Laurie Jeanette, Montgomery Charles, Payne Bobby Joe, Phillips Heidi, Rangel Carolina, Sevaux Tracy Ellen Willis, Shi Zheng-Zheng, Sparks Mary Jean, Stala Joy Anne, Townsend Teresa Gail, Vogel Peter |
| **Titular** | Combs Katherin E.
de Sauvage Frederic
Fan Liangfen
Filvaroff Ellen
Horner Allison Anne Byers
Irving Bryan
Junutula Jagath Reddy
Massey Erin Marie
Mclain Dina Rebecca
Minze Laurie Jeanette
Montgomery Charles
Payne Bobby Joe
Phillips Heidi
Rangel Carolina
Sevaux Tracy Ellen Willis
Shi Zheng-Zheng
Sparks Mary Jean
Stala Joy Anne
Townsend Teresa Gail
Vogel Peter |
| **Data** | 28.07.2011 |
| **Fonte** | Patentscope |
| **URL** | [20110182883](https://patentscope.wipo.int/search/en/detail.jsf?docId=US73308915&_cid=P12-MRXIRX-71771-1) |
| **Triagem** | review |
| **Rota** | N/A |
| **Motivo da rota** | N/A |
| **Score de Triagem** | 0.0/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | N/A |
| **Cluster Temático** | N/A |
| **Papel do CO2** | N/A |
| **Papel do Armazenamento** | N/A |
| **Limite Sistêmico** | N/A |
| **Tipo de Ciclo** | N/A |
| **Fonte/Sumidouro Térmico** | N/A |
| **Foco das Claims** | N/A |
| **Categoria de Exclusão** | N/A |
| **Confiança** | 0.00 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Sim |
| **Erro LLM** | LLM indisponível. |

**Abstract:**
> (EN)The present invention relates to transgenic animals, as well as compositions and methods relating to the characterization of gene function. Specifically, the present invention provides transgenic mice comprising disruptions in PRO218, PRO228, PRO271, PRO273, PRO295, PRO302, PRO305, PRO326, PRO386, PRO655, PRO162, PRO788, PRO792, PRO940, PRO941, PRO1004, PRO1012, PRO1016, PRO474, PRO5238, PRO1069, PRO1111, PRO1113, PRO1130, PRO1195, PRO1271, PRO1865, PRO1879, PRO3446, PRO3543, PRO4329, PRO4352, PRO5733, PRO9859, PRO9864, PRO9904, PRO9907, PRO10013, PRO90948, PRO28694, PRO16089, PRO19563, PRO19675, PRO20084, PRO21434, PRO50332, PRO38465 or PRO346 genes. Such in vivo studies and characterizations may provide valuable identification and discovery of therapeutics and/or treatments useful in the prevention, amelioration or correction of diseases or dysfunctions associated with gene disruptions such as neurological disorders; cardiovascular, endothelial or angiogenic disorders; eye abnormalities; immunological disorders; oncological disorders; bone metabolic abnormalities or disorders; lipid metabolic disorders; or developmental abnormalities.

---

### 19. NMR SYSTEMS AND METHODS FOR THE RAPID DETECTION OF ANALYTES
(FR)
SYSTEMES DE RMN ET PROCEDES DE DETECTION RAPIDE D'ANALYTES

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_32c7781ba59f` |
| **Family ID** | `family:bcd7e108902e78ce64cd7d288a24e93b0da6e30e` |
| **ID** | `3155334` |
| **Inventores** | AUDEH, MARK JOHN, BLANCO, MATTHEW, CHEPIN, JAMES FRANKLIN, DEMAS, VASILIKI, DHANDA, RAHUL, FRITZEMEIER, MARILYN LEE, KOH, ISAAC, KUMAR, SONIA, LOWERY, THOMAS JAY, JR., MOZELESKI, BRIAN, NEELY, LORI ANNE, PLOURDE, DANIELLA LYNN, RITTERSHAUS, CHARLES WILLIAM, WELLMAN, PARRIS |
| **Titular** | T2 BIOSYSTEMS, INC. |
| **Data** | 26.04.2012 |
| **Fonte** | Patentscope |
| **URL** | [3155334](https://patentscope.wipo.int/search/en/detail.jsf?docId=CA358706215&_cid=P12-MRXIRX-71771-1) |
| **Triagem** | review |
| **Rota** | N/A |
| **Motivo da rota** | N/A |
| **Score de Triagem** | 0.0/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | N/A |
| **Cluster Temático** | N/A |
| **Papel do CO2** | N/A |
| **Papel do Armazenamento** | N/A |
| **Limite Sistêmico** | N/A |
| **Tipo de Ciclo** | N/A |
| **Fonte/Sumidouro Térmico** | N/A |
| **Foco das Claims** | N/A |
| **Categoria de Exclusão** | N/A |
| **Confiança** | 0.00 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Sim |
| **Erro LLM** | LLM indisponível. |

**Abstract:**
> (EN)This invention features systems and methods for the detection of analytes, and their use in the treatment and diagnosis of disease.

---

### 20. Methods and compositions for synthetic biomarkers

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_c3d095483da3` |
| **Family ID** | `family:0f136cb1543b2a736955d64473ed4434370b47f7` |
| **ID** | `20210277474` |
| **Inventores** | David Suhy, Paul Escarpe, Cyriac Roeding, Justin Lin, Alex Harwig, Shireen Rudina, Leland Harrison Hartwell |
| **Titular** | EARLI Inc. |
| **Data** | 09.09.2021 |
| **Fonte** | Patentscope |
| **URL** | [20210277474](https://patentscope.wipo.int/search/en/detail.jsf?docId=US335377510&_cid=P12-MRXIRX-71771-1) |
| **Triagem** | review |
| **Rota** | N/A |
| **Motivo da rota** | N/A |
| **Score de Triagem** | 0.0/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | N/A |
| **Cluster Temático** | N/A |
| **Papel do CO2** | N/A |
| **Papel do Armazenamento** | N/A |
| **Limite Sistêmico** | N/A |
| **Tipo de Ciclo** | N/A |
| **Fonte/Sumidouro Térmico** | N/A |
| **Foco das Claims** | N/A |
| **Categoria de Exclusão** | N/A |
| **Confiança** | 0.00 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Sim |
| **Erro LLM** | LLM indisponível. |

**Abstract:**
> (EN)The present disclosure encompasses embodiments of nucleic acids comprising genetic elements which are useful for the detection of diseased cells.

---

## 🧾 Fila de Revisão Manual

- rec_fde35625d301 (CN108872343A) | rota= | motivo=LLM indisponível. | erro_llm=LLM indisponível.
- rec_1292a0df852d (CN108918618A) | rota= | motivo=LLM indisponível. | erro_llm=LLM indisponível.
- rec_64b3458c1dde (rec_64b3458c1dde) | rota= | motivo=LLM indisponível. | erro_llm=LLM indisponível.
- rec_a3b380e21bf9 (CN115165998A) | rota= | motivo=LLM indisponível. | erro_llm=LLM indisponível.
- rec_d461537cff92 (CN105241868A) | rota= | motivo=LLM indisponível. | erro_llm=LLM indisponível.
- rec_ce6b4ec2085f (20250120616) | rota= | motivo=LLM indisponível. | erro_llm=LLM indisponível.
- rec_d9a330124ef1 (WO/2023/034705) | rota= | motivo=LLM indisponível. | erro_llm=LLM indisponível.
- rec_4ca678fd8fa5 (WO2021222250A1) | rota= | motivo=LLM indisponível. | erro_llm=LLM indisponível.
- rec_bfa14d23f878 (US20210332489A1) | rota= | motivo=LLM indisponível. | erro_llm=LLM indisponível.
- rec_ca020593ddd1 (CN112479186A) | rota= | motivo=LLM indisponível. | erro_llm=LLM indisponível.
- rec_c3d095483da3 (20210277474) | rota= | motivo=LLM indisponível. | erro_llm=LLM indisponível.
- rec_523dc554e6aa (2728386) | rota= | motivo=LLM indisponível. | erro_llm=LLM indisponível.
- rec_32c7781ba59f (3155334) | rota= | motivo=LLM indisponível. | erro_llm=LLM indisponível.
- rec_b4048237afc7 (20110182883) | rota= | motivo=LLM indisponível. | erro_llm=LLM indisponível.
- rec_4eda793a65f1 (WO/2007/081608) | rota= | motivo=LLM indisponível. | erro_llm=LLM indisponível.
- rec_f38e10ba5b6d (2002714) | rota= | motivo=LLM indisponível. | erro_llm=LLM indisponível.
- rec_4873e210a0a6 (20090293137) | rota= | motivo=LLM indisponível. | erro_llm=LLM indisponível.
- rec_4b6228965ee5 (2006335053) | rota= | motivo=LLM indisponível. | erro_llm=LLM indisponível.
- rec_daeced5ae557 (CN110006970A) | rota= | motivo=LLM indisponível. | erro_llm=LLM indisponível.
- rec_179b3a7db28d (CN119246633A) | rota= | motivo=LLM indisponível. | erro_llm=LLM indisponível.

---

## ℹ️ Informações do Sistema

- **Gerado por:** Agente de Web Scraping de Patentes
- **Modelo LLM:** gemma3:4b
- **Data de geração:** 23/07/2026 13:02:29
- **Query de busca:** `LIG sensor dopamine tears `
- **Status da execução:** completed
- **Tempo total:** 153.5s
- **LLM disponível:** não
- **Fila de revisão manual:** 20 itens
- **Snapshot hash:** `24dfe8c4f1ce4007d20c08a6b9a9e5e051fc257c2b079b6f5dfef503823ef3a7`
- **Features habilitadas:** require_evidence, enable_thematic_clusters, enable_structural_roles, enable_screening_rerank, enable_prisma, enable_snapshot, enable_comparative_analysis, enable_whitespace_analysis, enable_manual_review_queue
- **Features desabilitadas:** nenhum
- **Versão do pipeline:** 1.1
- **Thresholds snapshot:** include=7.0, review=4.5
- **Cache LLM:** 0 hits, 0 misses, 158 entradas
- **Status do rascunho:** blocked
- **Avisos do rascunho:** 1