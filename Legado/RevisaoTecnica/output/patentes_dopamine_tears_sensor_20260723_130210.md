# 📋 Relatório de Análise de Patentes

**Data:** 23/07/2026 13:02:10
**Busca:** `dopamine tears sensor`
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
- **Triadas:** 20
- **Incluídas:** 0
- **Em revisão manual:** 6
- **Excluídas:** 14
- **Extrações completas:** 6
- **Sem abstract/snippet:** 2
- **Sem ID:** 0
- **Identidade por conteúdo:** 0
- **Identidade fallback:** 0
- **Duplicatas por família removidas:** 0
- **Falhas de triagem LLM:** 0
- **Falhas totais LLM:** 0

## 🧭 Fluxo PRISMA-Like

- **Identificação:** 20 bruto(s), 20 único(s), 0 duplicata(s) removida(s)
- **Triagem:** 20 triado(s), 0 incluído(s), 6 em revisão, 14 excluído(s)
- **Elegibilidade:** 6 extração(ões) completa(s), 6 revisão(ões) manual(is), 0 adiada(s)
- **Cobertura:** 2 sem abstract/snippet, 0 sem ID
- **Síntese:** 6 registro(s) analisado(s)

## 🧠 Contexto Compartilhado

- **Top patentes no contexto:** 0
- **Clusters no contexto:** 0
- **Roteamento agregado:** 2 rota(s)
- **Slots ativos:** N/A

## ⏱️ Métricas por Etapa

| Etapa | Status | Duração | Itens | Detalhes |
|---|---|---:|---:|---|
| setup | ok | 4.21s | 1 | Verificação do modelo Ollama |
| search | ok | 103.40s | 20 | 20 patentes únicas após dedupe |
| screening | ok | 1505.89s | 20 | 0 incluídas, 6 revisão |
| comparative_analysis | ok | 154.44s | 20 | Síntese comparativa gerada |
| whitespace_analysis | ok | 0.00s | 6 | Whitespace analysis estruturada gerada |
| reporting | ok | 0.00s | 20 | Relatórios Markdown e JSON |
| finalization | ok | 0.00s | 8 | Persistência de artefatos e estado |

## 🌐 Diagnósticos de Coleta

### GooglePatents

- **blocked_or_captcha**: Sinal de bloqueio/CAPTCHA detectado na resposta.

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
- **Latência média:** 4.212s
- **Latência máxima:** 4.212s

### screening

- **Chamadas:** 20
- **Sucessos:** 20
- **Falhas:** 0
- **Retries:** 0
- **Cache hits:** 0
- **Pulos por degradação:** 0
- **Latência média:** 36.209s
- **Latência máxima:** 87.244s

### rerank

- **Chamadas:** 7
- **Sucessos:** 7
- **Falhas:** 0
- **Retries:** 0
- **Cache hits:** 0
- **Pulos por degradação:** 0
- **Latência média:** 37.727s
- **Latência máxima:** 44.969s

### evaluation

- **Chamadas:** 6
- **Sucessos:** 6
- **Falhas:** 0
- **Retries:** 0
- **Cache hits:** 0
- **Pulos por degradação:** 0
- **Latência média:** 86.266s
- **Latência máxima:** 171.334s

### comparative

- **Chamadas:** 1
- **Sucessos:** 1
- **Falhas:** 0
- **Retries:** 0
- **Cache hits:** 0
- **Pulos por degradação:** 0
- **Latência média:** 154.431s
- **Latência máxima:** 154.431s

## 🔎 Observabilidade Estruturada

### Rotas

- **screen_only**: total=14, include=0, review=0, exclude=14, llm_errors=0
- **manual_review**: total=6, include=0, review=6, exclude=0, llm_errors=0

### Fontes

- **EPO**: bruto=0, duração=0.00s, diagnósticos=config_missing=1
- **GooglePatents**: bruto=10, duração=32.89s, diagnósticos=blocked_or_captcha=1
- **Patentscope**: bruto=10, duração=70.51s, diagnósticos=nenhum

### Falhas

- **Erros de execução:** 0
- **Registros com erro de LLM:** 0
- **Falhas totais do LLM:** 0
- **LLM por operação:** comparative(falhas=0, retries=0, skips=0), evaluation(falhas=0, retries=0, skips=0), healthcheck(falhas=0, retries=0, skips=0), rerank(falhas=0, retries=0, skips=0), screening(falhas=0, retries=0, skips=0)
- **Scraper por tipo de sinal:** blocked_or_captcha=1, config_missing=1

## 📊 Resumo Executivo

**Score médio de relevância:** 0.0/10

| # | Patente | Score | Inovação | Domínio |
|---|---------|-------|----------|---------|
| 1 | [CN116448850A](https://patents.google.com/patent/CN116448850A/en) — Detection device for dopamine in tear, preparation method an... | 🟡 6.5 (review) | Significativa | Eletroquímica, Sensores Biológicos, Gerenciamento Térmico |
| 2 | [CN108872343A](https://patents.google.com/patent/CN108872343A/en) — A kind of Dopamine Sensor and its preparation and applicatio... | 🟡 6.5 (review) | Incremental | Sensores eletroquímicos, materiais compósitos, grafeno dopado com nitrogênio |
| 3 | [CN1395094A](https://patents.google.com/patent/CN1395094A/en) — Electrochemical sensor for determining dopamine | 🟡 6.5 (review) | Incremental | Eletroquímica, Sensores Químicos, Química de Materiais |
| 4 | [CN112578011A](https://patents.google.com/patent/CN112578011A/en) — Sensor and detection method for detecting dopamine and uric ... | 🟡 6.5 (review) | Significativa | Eletroquímica, Sensores, Materiais 2D (MXene) |
| 5 | [CN105241868A](https://patents.google.com/patent/CN105241868A/en) — Electrochemiluminescence sensor based on methionine-gold nan... | 🟡 6.5 (review) | Incremental | Biosensing, Eletroquímica, Nanotecnologia |
| 6 | [JP5390399B2](https://patents.google.com/patent/JP5390399B2/en) — Ocular sensor for detection of analytes in tears | 🟡 6.2 (review) | Incremental | Biossensores Biomédicos e Química Analítica |
| 7 | [US7658119B2](https://patents.google.com/patent/US7658119B2/nl) — Biomimetic tactile sensor | 🔴 0.0 (exclude) | N/A | Sensores Tácteis e Biomecânica |
| 8 | [US20170173262A1](https://patents.google.com/patent/US20170173262A1/en) — Medical systems, devices and methods | 🔴 0.0 (exclude) | N/A | Medicina / Monitoramento Biológico |
| 9 | [US20220273907A1](https://patents.google.com/patent/US20220273907A1/en) — Method and apparatus for neuroenhancement to enhance emotion... | 🔴 0.0 (exclude) | N/A | Neurociência, Neuroestimulação |
| 10 | [US8265725B2](https://patents.google.com/patent/US8265725B2/en) — Signal processing for continuous analyte sensor | 🔴 0.0 (exclude) | N/A | Processamento de Sinais, Biossensores |
| 11 | [WO/2021/188084](https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2021188084&_cid=P10-MRXHSI-51243-1) — A MEASUREMENT SYSTEM FOR
TEAR
CHEMICALS IN THE
TEAR
FOR DIAG... | 🔴 0.0 (exclude) | N/A | Diagnóstico Médico / Biossensores |
| 12 | [20150201837](https://patentscope.wipo.int/search/en/detail.jsf?docId=US145058030&_cid=P10-MRXHSI-51243-1) — Non-invasive health indicator monitoring system and using me... | 🔴 0.0 (exclude) | N/A | Monitoramento de Saúde |
| 13 | [20180289326](https://patentscope.wipo.int/search/en/detail.jsf?docId=US231562967&_cid=P10-MRXHSI-51243-1) — Ocular devices and methods for the employment thereof | 🔴 0.0 (exclude) | N/A | Medicina Ocular / Diagnóstico Clínico |
| 14 | [WO/2018/187693](https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2018187693&_cid=P10-MRXHSI-51243-1) — OCULAR DEVICES AND METHODS FOR THE EMPLOYMENT THEREOF
(FR)
D... | 🔴 0.0 (exclude) | N/A | Biotecnologia, Dispositivos Médicos |
| 15 | [WO/2012/009322](https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2012009322&_cid=P10-MRXHSI-51243-1) — METHODS AND DEVICE FOR TUNING MULTIPLEXED MARKERS FOR DISEAS... | 🔴 0.0 (exclude) | N/A | Eletroquímica, Biossensores, Diagnóstico Médico |
| 16 | [20130183243](https://patentscope.wipo.int/search/en/detail.jsf?docId=US86177550&_cid=P10-MRXHSI-51243-1) — Methods and device for tuning multiplexed markers for diseas... | 🔴 0.0 (exclude) | N/A | Sensores Eletroquímicos, Diagnóstico Médico |
| 17 | [20240049994](https://patentscope.wipo.int/search/en/detail.jsf?docId=US422369809&_cid=P10-MRXHSI-51243-1) — ONE-TOUCH FINGERTIP SWEAT
SENSOR
AND PERSONALIZED DATA PROCE... | 🔴 0.0 (exclude) | N/A | Biossensores, Monitoramento Biomédico |
| 18 | [3210742](https://patentscope.wipo.int/search/en/detail.jsf?docId=CA406582873&_cid=P10-MRXHSI-51243-1) — ONE-TOUCH FINGERTIP SWEAT
SENSOR
AND PERSONALIZED DATA PROCE... | 🔴 0.0 (exclude) | N/A | Biossensores, Monitoramento Biomédico |
| 19 | [WO/2022/170361](https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2022170361&_cid=P10-MRXHSI-51243-1) — ONE-TOUCH FINGERTIP SWEAT
SENSOR
AND PERSONALIZED DATA PROCE... | 🔴 0.0 (exclude) | N/A | Biossensores e Bioenergia |
| 20 | [2022216341](https://patentscope.wipo.int/search/en/detail.jsf?docId=AU406509324&_cid=P10-MRXHSI-51243-1) — ONE-TOUCH FINGERTIP SWEAT
SENSOR
AND PERSONALIZED DATA PROCE... | 🔴 0.0 (exclude) | N/A | Biossensores, Monitoramento Biomédico |

---

## 🔍 Análise Detalhada das Patentes

### 1. Detection device for dopamine in tear, preparation method and application

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_245e60bec916` |
| **Family ID** | `family:37bd14cf5a2babb42206f23f39cb49c4ac8259da` |
| **ID** | `CN116448850A` |
| **Inventores** | çè³è³, æ±å³°, é«æé, çé |
| **Titular** | Tianjin University |
| **Data** | 2023-07-18 |
| **Fonte** | Google Patents |
| **URL** | [CN116448850A](https://patents.google.com/patent/CN116448850A/en) |
| **Triagem** | review |
| **Rota** | manual_review |
| **Motivo da rota** | Triagem indicou revisão humana. |
| **Score de Triagem** | 7.4/10 |
| **Score de Relevância** | 6.5/10 |
| **Nível de Inovação** | Significativa |
| **Domínio Técnico** | Eletroquímica, Sensores Biológicos, Gerenciamento Térmico |
| **Cluster Temático** | Detecção Biomolecular com Eletrônica e Termodinâmica |
| **Papel do CO2** | stored_thermodynamic_medium |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | cycle_or_transfer_subsystem |
| **Tipo de Ciclo** | refrigeration_cycle |
| **Fonte/Sumidouro Térmico** | não especificado, mas implica um sistema de controle térmico |
| **Foco das Claims** | system_architecture |
| **Categoria de Exclusão** | low_alignment |
| **Confiança** | 0.71 |
| **Rerank Aplicado** | Sim |
| **Motivo do Rerank** | reranked:include->review |
| **Revisão Manual** | Sim |
| **Erro LLM** | N/A |

**Abstract:**
> AbstractTranslated fromChineseæ¬å¬å¼æåºäºä¸ç§æ³ªæ¶²ä¸­å¤å·´èºçæ£æµè£ç½®ï¼åæ¬ï¼çµåå­¦è¯ç(1)ï¼å¤å·´èºç¹å¼ææèè(2)ï¼è´è½½å¨çµåå­¦è¯çä¸ï¼ä»¥å¨çµåå­¦è¯çæ½å çµåçæåµä¸å¬åæè¿°æ³ªæ¶²ä¸­çå¤å·´èºåå­åçæ°§åååºä½¿å¤å·´èºåå­å¤±å»çµå­ï¼ä»èå¨çµåå­¦è¯çä¸­äº§çååºçµæµï¼ä»¥åå£³ä½(3)ï¼å£³ä½ä¸å½¢æéå­ï¼éå­éç¨äºä¸çµåå­¦è¯ç(1)ç»åå½¢æéç¨äºå®¹çº³æè¿°æ³ªæ¶²ççµè§£æ± ãæ¬å¬å¼è¿æåºäºä¸ç§æ³ªæ¶²ä¸­å¤å·´èºçæ£æµè£ç½®çæå»ºæ¹æ³ä»¥åå¯¹æ³ªæ¶²ä¸­å¤å·´èºå«éçæµéæ¹æ³ãThe disclosure proposes a detection device for dopamine in tears, comprising: an electrochemical chip (1), a dopamine-specific sensitive film (2), loaded on the electrochemical chip to catalyze the Oxidation reaction of dopamine molecules in tears causes dopamine molecules to lose electrons, thereby generating a corresponding current in the electrochemical chip, and a shell (3), forming a through hole on the shell, which is suitable for combining with the electrochemical chip (1) An electrolytic cell suitable for containing the tear fluid is formed. The present disclosure also proposes a method for constructing a detection device for dopamine in tears and a method for measuring the content of dopamine in tears.

**Avaliação do LLM:**
Esta patente descreve um dispositivo de detecção de dopamina em lágrimas que utiliza um chip eletroquímico e uma película sensível para catalisar a oxidação da dopamina, gerando corrente. O sistema inclui uma estrutura de invólucro com um orifício para acomodar o chip eletroquímico e um eletrólito contendo a amostra de lágrimas. A patente foca em um ciclo termodinâmico que envolve armazenamento térmico.

**Extração Estruturada:**
- **Problema:** A necessidade de um dispositivo portátil e preciso para detectar níveis de dopamina nas lágrimas, com potencial para aplicações médicas e diagnósticas.
- **Solução:** A solução proposta é um dispositivo de detecção que utiliza um chip eletroquímico e uma película sensível para quantificar a dopamina em amostras de lágrimas. O sistema incorpora armazenamento térmico para otimizar o processo de detecção.
- **Maturidade:** Inicial

**Achados-chave:**
- Utilização de um chip eletroquímico com uma película sensível para detectar dopamina através da oxidação.
- Incorporação de um invólucro com um orifício para acomodar o chip eletroquímico e um eletrólito contendo a amostra de lágrimas.

**Vantagens alegadas:**
- Detecção precisa e portátil de dopamina em lágrimas.
- Utilização de armazenamento térmico para otimizar a reação de detecção.

**Limitações:**
- A patente não detalha especificamente o mecanismo exato do armazenamento térmico ou sua influência no desempenho da detecção.
- O impacto da temperatura na estabilidade e sensibilidade dos componentes eletroquímicos pode ser um fator limitante.

**Aplicações potenciais:**
- Diagnóstico médico para avaliar condições neurológicas e psiquiátricas.
- Monitoramento de pacientes com doenças relacionadas ao estresse ou ansiedade.
- Pesquisa em neurociência e desenvolvimento de novos tratamentos.

**Evidências citadas:**
> "an electrolytic cell suitable for containing the tear fluid is formed."
> "æ¬å¬å¼æåºäºä¸ç§æ³ªæ¶²ä¸­å¤å·´èºçæ£æµè£ç½"

---

### 2. Biomimetic tactile sensor

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_1ae1a8298b15` |
| **Family ID** | `family:8fc49a262e5115e6fdb54e10736fdae0e9531f80` |
| **ID** | `US7658119B2` |
| **Inventores** | Gerald E. Loeb, Roland Johansson |
| **Titular** | University of Southern California USC |
| **Data** | 2010-02-09 |
| **Fonte** | Google Patents |
| **URL** | [US7658119B2](https://patents.google.com/patent/US7658119B2/nl) |
| **Triagem** | exclude |
| **Rota** | screen_only |
| **Motivo da rota** | Patente excluída na triagem. |
| **Score de Triagem** | 3.5/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | Sensores Tácteis e Biomecânica |
| **Cluster Temático** | Detecção de Alterações Superficiais |
| **Papel do CO2** | co2_not_central |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | general_thermal_management |
| **Foco das Claims** | component_or_operation |
| **Categoria de Exclusão** | generic_tes |
| **Confiança** | 0.60 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Evidências citadas:**
> Biomimetic tactile sensor

---

### 3. A kind of Dopamine Sensor and its preparation and application based on nitrogen-doped graphene

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
| **Rota** | manual_review |
| **Motivo da rota** | Triagem indicou revisão humana. |
| **Score de Triagem** | 5.3/10 |
| **Score de Relevância** | 6.5/10 |
| **Nível de Inovação** | Incremental |
| **Domínio Técnico** | Sensores eletroquímicos, materiais compósitos, grafeno dopado com nitrogênio |
| **Cluster Temático** | Desenvolvimento de sensores químicos para a detecção de neurotransmissores. |
| **Papel do CO2** | Não especificado (o foco principal é na detecção de dopamina) |
| **Papel do Armazenamento** | N/A |
| **Limite Sistêmico** | Sensor individual |
| **Tipo de Ciclo** | Não claro (implícito em processos eletroquímicos) |
| **Fonte/Sumidouro Térmico** | N/A |
| **Foco das Claims** | Desenvolvimento e aplicação de um sensor de dopamina baseado em grafeno nitrogenado dopado. |
| **Categoria de Exclusão** | cooling_only |
| **Confiança** | 0.63 |
| **Rerank Aplicado** | Sim |
| **Motivo do Rerank** | reranked:include->review |
| **Revisão Manual** | Sim |
| **Erro LLM** | N/A |

**Abstract:**
> AbstractThe invention belongs to electrochemical sensor technology field, a kind of Dopamine Sensor based on nitrogen-doped graphene and its preparation and application are disclosed.The sensor is formed by reference electrode, to the working electrode after electrode and modification, working electrode after modification is by working electrode and is solidificated in the material identification film of working electrode surface and forms, wherein, the material identification film is mainly prepared by nitrogen-doped graphene composite material with perfluorinated sulfonic resin.The invention also discloses the preparation methods of sensor.Sensor of the invention has good selectivity, reproducibility and stability, can accurately be detected to dopamine, strong antijamming capabilityï¼There is wider detection range, lower detection limit simultaneously.Method of the invention is simple, at low cost.Prepared sensor is for detecting dopamine.

**Avaliação do LLM:**
Esta patente descreve um sensor de dopamina baseado em grafeno nitrogenado dopado, utilizando uma membrana de identificação do eletrodo formada por este material composto com resina de perfluorosulfônica. O sensor apresenta boa seletividade, reprodutibilidade e estabilidade, permitindo a detecção precisa da dopamina com amplo alcance e baixo limite de detecção. Os métodos de preparação do sensor são simples e econômicos.

**Extração Estruturada:**
- **Problema:** A necessidade de um sensor de dopamina altamente sensível, seletivo e estável para aplicações em diversas áreas, como monitoramento biológico e diagnóstico médico.
- **Solução:** A patente apresenta um novo sensor de dopamina baseado em grafeno nitrogenado dopado, que oferece melhor desempenho em comparação com sensores existentes devido à sua alta área superficial, excelente condutividade elétrica e capacidade de detecção seletiva da dopamina.
- **Maturidade:** Inicial

**Achados-chave:**
- O sensor demonstra boa seletividade, reprodutibilidade e estabilidade na detecção de dopamina.
- A membrana de identificação do eletrodo formada por grafeno nitrogenado dopado com resina de perfluorosulfônica melhora o desempenho do sensor.

**Vantagens alegadas:**
- Alta sensibilidade e precisão na detecção de dopamina
- Amplo alcance de detecção e baixo limite de detecção
- Boa seletividade e estabilidade
- Métodos de preparação simples e econômicos

**Limitações:**
- O documento não detalha especificamente as condições operacionais ideais para o sensor (temperatura, pH, etc.).
- A patente não aborda a escalabilidade da produção do material de grafeno nitrogenado dopado.

**Aplicações potenciais:**
- Monitoramento biológico de níveis de dopamina
- Diagnóstico médico para doenças neurológicas e psiquiátricas
- Análise ambiental de dopamina

**Evidências citadas:**
> "The sensor is formed by reference electrode..."
> "The invention also discloses the preparation methods of sensor."

---

### 4. Electrochemical sensor for determining dopamine

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_bc447a4191dd` |
| **Family ID** | `family:8bc9532b2ed16a9d7eabec4fa5596539a0c1ad82` |
| **ID** | `CN1395094A` |
| **Inventores** | è¡èæ°´, å´åº·åµ, å­å»¶ä¸ |
| **Titular** | Wuhan University WHU |
| **Data** | 2003-02-05 |
| **Fonte** | Google Patents |
| **URL** | [CN1395094A](https://patents.google.com/patent/CN1395094A/en) |
| **Triagem** | review |
| **Rota** | manual_review |
| **Motivo da rota** | Triagem indicou revisão humana. |
| **Score de Triagem** | 5.3/10 |
| **Score de Relevância** | 6.5/10 |
| **Nível de Inovação** | Incremental |
| **Domínio Técnico** | Eletroquímica, Sensores Químicos, Química de Materiais |
| **Cluster Temático** | Detecção Eletroquímica de Biomoléculas |
| **Papel do CO2** | not_central |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | not_applicable |
| **Foco das Claims** | Sensor eletroquímico para dopamina com filme sensível de Nafion e nanotubos de carbono. |
| **Categoria de Exclusão** | low_alignment |
| **Confiança** | 0.63 |
| **Rerank Aplicado** | Sim |
| **Motivo do Rerank** | reranked:decision_confirmed |
| **Revisão Manual** | Sim |
| **Erro LLM** | N/A |

**Abstract:**
> AbstractTranslated fromChineseæ¬åææ¶åä¸ç§æµå®å¤å·´èºççµåå­¦ä¼ æå¨ï¼åæ¬ç»ç¢³çµæï¼ç»ç¢³çµæçè¡¨é¢æ¶è¦æç¢³çº³ç±³ç®¡ï¼é³ç¦»å­äº¤æ¢èåç©Nafionææèï¼æ¬åæä»¥é³ç¦»å­äº¤æ¢èåç©Nafionä¸ºåæ£åï¼å¯ä»¥å¾å®¹æå°å°æ§è´¨ååç¨³å®çç¢³çº³ç±³ç®¡åæ£å¨ä¹éä¸­ï¼ä»¥è¯¥åæ£æ¶²æ¶è¦å¨ç»ç¢³çµæè¡¨é¢å¶å¾çææèä¸ç»ç¢³çµæææççµåå­¦ä¼ æå¨æµå®å¤å·´èºä¸ä»éæ©æ§åçµæåº¦é«ï¼èä¸å¨é«æµåº¦æåè¡é¸åå°¿é¸å­å¨ä¸ï¼ä»å¯¹ä½æµåº¦çå¤å·´èºæéæ©æ§ååºãThe invention relates to an electrochemical sensor for measuring dopamine, which comprises a glassy carbon electrode, and the surface of the glassy carbon electrode is coated with a carbon nanotube-cation exchange polymer Nafion sensitive film. The invention uses the cation exchange polymer Nafion as a dispersant, which can It is easy to disperse carbon nanotubes with very stable properties in ethanol. The electrochemical sensor composed of a sensitive film and a glassy carbon electrode formed by coating the dispersion on the surface of a glassy carbon electrode is not only high in selectivity and sensitivity, but also high in sensitivity. And in the presence of high concentrations of ascorbic acid and uric acid, there is still a selective response to low concentrations of dopamine.

**Avaliação do LLM:**
Esta patente descreve um sensor eletroquímico para dopamina que utiliza uma membrana de Nafion com nanotubos de carbono para melhorar a dispersão e estabilidade do material sensível. O sensor demonstra alta seletividade e sensibilidade, especialmente em concentrações baixas de dopamina, mesmo na presença de interferentes como ácido ascórbico e ácido úrico.

**Extração Estruturada:**
- **Problema:** O problema abordado é a necessidade de um sensor eletroquímico com alta seletividade e sensibilidade para a detecção de dopamina, especialmente em ambientes complexos com outras substâncias que podem interferir na medição.
- **Solução:** A solução proposta é um sensor eletroquímico que utiliza uma membrana de Nafion com nanotubos de carbono como filme sensível, otimizando a dispersão e estabilidade do material para melhorar o desempenho da detecção de dopamina.
- **Maturidade:** Intermediária

**Achados-chave:**
- O uso de Nafion como dispersante para carbon nanotubes resulta em um filme sensível estável e com alta capacidade de dispersão.
- O sensor demonstra seletividade e sensibilidade à dopamina, mesmo na presença de altas concentrações de ácido ascórbico e ácido úrico.

**Vantagens alegadas:**
- Alta seletividade e sensibilidade para a detecção de dopamina.
- Estabilidade do filme sensível devido à dispersão otimizada dos nanotubos de carbono.

**Limitações:**
- O documento não detalha o desempenho em condições operacionais complexas ou em amostras biológicas reais.
- A patente foca primariamente na detecção de dopamina e não aborda diretamente a captura ou armazenamento de CO2.

**Aplicações potenciais:**
- Monitoramento de níveis de dopamina em fluidos biológicos (sangue, urina).
- Diagnóstico médico para doenças neurológicas.
- Análise química e monitoramento ambiental.

**Evidências citadas:**
> "The invention relates to an electrochemical sensor for measuring dopamine..."
> The abstract mentions Nafion, a polymer used in sensors, not CO2 storage or capture.

---

### 5. Sensor and detection method for detecting dopamine and uric acid

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_2056c5d6639a` |
| **Family ID** | `family:b71646276671f9adf96c434a857d376f5e35e3b8` |
| **ID** | `CN112578011A` |
| **Inventores** | è£æé£, å°¤å©æ¥, é¢ææ¼, èæé, æ¢è, å®çç, å¼ å¨, åé¦é¹ |
| **Titular** | Jinan Guoke Medical Engineering Technology Development Co ltd |
| **Data** | 2021-03-30 |
| **Fonte** | Google Patents |
| **URL** | [CN112578011A](https://patents.google.com/patent/CN112578011A/en) |
| **Triagem** | review |
| **Rota** | manual_review |
| **Motivo da rota** | Triagem indicou revisão humana. |
| **Score de Triagem** | 5.3/10 |
| **Score de Relevância** | 6.5/10 |
| **Nível de Inovação** | Significativa |
| **Domínio Técnico** | Eletroquímica, Sensores, Materiais 2D (MXene) |
| **Cluster Temático** | Detecção Biomolecular Eletroquímica |
| **Papel do CO2** | não relevante (o CO2 não é o foco principal da invenção) |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | Sensor eletroquímico individual |
| **Tipo de Ciclo** | não especificado |
| **Fonte/Sumidouro Térmico** | não relevante |
| **Foco das Claims** | Construção e funcionalidade do sensor eletroquímico baseado em MXene-PPy. |
| **Categoria de Exclusão** | low_alignment |
| **Confiança** | 0.63 |
| **Rerank Aplicado** | Sim |
| **Motivo do Rerank** | reranked:decision_confirmed |
| **Revisão Manual** | Sim |
| **Erro LLM** | N/A |

**Abstract:**
> AbstractThe invention discloses a sensor and a detection method for detecting dopamine and uric acid, wherein the sensor is prepared by the following method: 1) preparing MXene-PPy nano composite material; 2) and modifying the prepared MXene-PPy nano composite material on the surface of a substrate electrode to prepare the sensor. According to the invention, the PPy nanowire is subjected to in-situ oxidation polymerization on the surface of the MXene nanosheet of the two-dimensional material, so that large-scale preparation can be realized and the cost is low; the constructed composite material system has high catalytic activity, high conductivity and anti-interference capability, has large specific surface area, increases catalytic sites on the surface of an electrode, and is beneficial to sensing and detecting a target object; the electrochemical sensor constructed by the invention can still realize the independent or simultaneous identification and detection of dopamine and uric acid in the presence of ascorbic acid, achieves a wide detection range and a low detection limit for the sensing and detection of the dopamine and the uric acid, and simultaneously shows better electrochemical stability and reproducibility.

**Avaliação do LLM:**
Esta patente descreve um sensor eletroquímico para a detecção de dopamina e ácido úrico, utilizando um material composto MXene-PPy modificado em um eletrodo. O sensor apresenta alta atividade catalítica, condutividade e estabilidade, permitindo a identificação independente ou simultânea de dopamina e ácido úrico com baixo limite de detecção.

**Extração Estruturada:**
- **Problema:** A necessidade de um sensor robusto e preciso para a detecção de dopamina e ácido úrico, especialmente em ambientes complexos com interferentes como ascorbato.
- **Solução:** A solução proposta é um sensor baseado em um material composto MXene-PPy que é modificado em um eletrodo, maximizando a área superficial e a atividade catalítica para uma detecção mais sensível e seletiva.
- **Maturidade:** Inicial

**Achados-chave:**
- Utilização de MXene-PPy nano composite material para aumentar a área superficial e atividade catalítica.
- Modificação do material em um eletrodo melhora a estabilidade e reprodutibilidade do sensor, permitindo a detecção simultânea de dopamina e ácido úrico.

**Vantagens alegadas:**
- Amplamente aplicável devido ao baixo custo de produção em larga escala.
- Alta sensibilidade e especificidade na detecção de dopamina e ácido úrico, mesmo na presença de interferentes.

**Limitações:**
- O documento não especifica detalhes sobre a otimização do material ou as condições operacionais para diferentes aplicações.
- A estabilidade do sensor em longo prazo e sua performance em amostras biológicas complexas não são totalmente abordadas.

**Aplicações potenciais:**
- Diagnóstico médico, monitoramento de doenças neurológicas e metabólicas.
- Análise ambiental, detecção de poluentes e biomarcadores.

**Evidências citadas:**
> 'The electrochemical sensor constructed by the invention can still realize the independent or simultaneous identification and detection of dopamine and uric acid...'

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
| **Rota** | manual_review |
| **Motivo da rota** | Triagem indicou revisão humana. |
| **Score de Triagem** | 5.3/10 |
| **Score de Relevância** | 6.5/10 |
| **Nível de Inovação** | Incremental |
| **Domínio Técnico** | Biosensing, Eletroquímica, Nanotecnologia |
| **Cluster Temático** | Detecção eletroluminescência de neurotransmissores |
| **Papel do CO2** | Co-reator (persulfato) |
| **Papel do Armazenamento** | Não aplicável |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | Não aplicável |
| **Foco das Claims** | Desenvolvimento de um sensor eletroluminescência para dopamina. |
| **Categoria de Exclusão** | generic_tes |
| **Confiança** | 0.59 |
| **Rerank Aplicado** | Sim |
| **Motivo do Rerank** | reranked:decision_confirmed |
| **Revisão Manual** | Sim |
| **Erro LLM** | N/A |

**Abstract:**
> AbstractTranslated fromChineseæ¬åæå¬å¼ä¸ç§<b>åºäºç²ç¡«æ°¨é¸</b><b>-</b><b>éçº³ç±³å¢ç°ççµè´åå­¦ååä¼ æå¨</b>ï¼å¶æ¯ä»¥ç²ç¡«æ°¨é¸ä¿æ¤çéçº³ç±³å¢ç°ææä¸ºååä½ï¼è¿ç¡«é¸æ ¹ç¦»å­ä¸ºå±ååºåï¼å°ç²ç¡«æ°¨é¸ä¿æ¤çéçº³ç±³å¢ç°ä¿®é¥°å¨ç»ç¢³çµæä¸ï¼è¿è¡çµåå­¦ååæµè¯ï¼å¹¶å®ç°å¯¹å¤å·´èºçæ£æµãè¯¥ä¼ æå¨å¯¹å¯¹å¤å·´èºæ£æµççº¿æ§èå´ä¸º0.1~4ï¼Î¼mol/Lå4~25ï¼Î¼mol/Lï¼æ£æµéä¸º0.032ï¼Î¼mol/Lãæ¬åææå¾å°çç²ç¡«æ°¨é¸ä¿æ¤çéçº³ç±³å¢ç°å¶å¤æ¹æ³ç»¿è²ç¯ä¿ï¼æä½ç®ä¾¿å¿«æ·ï¼éç°æ§å¥½ï¼å¶å¤çç²ç¡«æ°¨é¸ä¿æ¤çéçº³ç±³å¢ç°çç©ç¸å®¹æ§å¥½ï¼å¹¶å·æè¾å¥½ççµè´åå­¦ååæ§è½ãThe invention discloses an electrochemiluminescence sensor based on <b>methionine</b><b>-</b><b>gold nanocluster</b>, which is based on methionine The protected gold nanocluster material is a luminescent body, and the persulfate ion is a co-reactant. The methionine-protected gold nanocluster is modified on the glassy carbon electrode, and the electrochemiluminescence test is performed, and the detection of dopamine is realized. . The linear range of the sensor for dopamine detection is 0.1~4? Î¼mol/L and 4~25? Î¼mol/L, the detection limit is 0.032? Î¼mol/L. The preparation method of the methionine-protected gold nanoclusters obtained in the present invention is green and environmentally friendly, and the operation is simple and quick, and the reproducibility is good. The prepared methionine-protected gold nanoclusters have good biocompatibility, and have relatively Good electrochemiluminescent properties.

**Avaliação do LLM:**
Esta patente descreve um sensor de eletroluminescência baseado em um cluster de nanopartículas ouro-metionina para detecção de dopamina. O sensor utiliza persulfato como co-reator e apresenta um intervalo linear de detecção de dopamina entre 0,1 e 4 µmol/L e um limite de detecção de 0,032 µmol/L. A patente foca na construção de um sensor eletroquímico para a detecção de dopamina.

**Extração Estruturada:**
- **Problema:** A necessidade de um método sensível e preciso para detectar dopamina, com potencial aplicação em biossensores.
- **Solução:** A patente propõe um sensor eletroluminescência que utiliza um cluster de nanopartículas ouro-metionina como elemento luminescente, acionado por persulfato, para a detecção de dopamina. A modificação do eletrodo com este material permite a detecção da dopamina através de um processo eletroquímico.
- **Maturidade:** Inicial

**Achados-chave:**
- O sensor apresenta um intervalo linear de detecção de dopamina entre 0,1 e 4 µmol/L e um limite de detecção de 0,032 µmol/L.
- A metodologia para preparar os clusters de ouro-metionina é considerada verde e ambientalmente amigável.

**Vantagens alegadas:**
- Alta sensibilidade na detecção de dopamina
- Metodologia de preparação simples, rápida e ecologicamente correta
- Boa biocompatibilidade dos materiais utilizados

**Limitações:**
- O intervalo linear de detecção pode ser restritivo para algumas aplicações.
- A sensibilidade pode ser afetada por interferências em amostras biológicas complexas.

**Aplicações potenciais:**
- Diagnóstico médico (monitoramento de níveis de dopamina)
- Pesquisa neurocientífica
- Desenvolvimento de dispositivos portáteis para detecção de dopamina

**Evidências citadas:**
> "The methionine-protected gold nanocluster is modified on the glassy carbon electrode, and the electrochemiluminescence test is performed..."
> "The linear range of the sensor for dopamine detection is 0.1~4? Î¼mol/L and 4~25? Î¼mol/L"

---

### 7. Medical systems, devices and methods

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_9bf5a8b7dc60` |
| **Family ID** | `family:a4a427bfa8d08de01240cd80d33877732f1a382b` |
| **ID** | `US20170173262A1` |
| **Inventores** | FranÃ§ois Paul VELTZ |
| **Titular** | Individual |
| **Data** | 2017-06-22 |
| **Fonte** | Google Patents |
| **URL** | [US20170173262A1](https://patents.google.com/patent/US20170173262A1/en) |
| **Triagem** | exclude |
| **Rota** | screen_only |
| **Motivo da rota** | Patente excluída na triagem. |
| **Score de Triagem** | 3.3/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | Medicina / Monitoramento Biológico |
| **Cluster Temático** | Sensores Biomédicos, Monitoramento Contínuo |
| **Papel do CO2** | co2_not_central |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | dedicated_storage_system |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | general_thermal_management |
| **Foco das Claims** | component_or_operation |
| **Categoria de Exclusão** | generic_tes |
| **Confiança** | 0.52 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> AbstractThere is disclosed a medical system comprising one or more sensors associated with one or more actuators. Various embodiments describe sensors and/or actuators, logic circuits, user interfaces, association schemes, communication schemes, security schemes, cryptographic schemes, medical management rules, social mechanisms, energy management schemes, time and/or space schemes, body analytes and/or biomarkers, blood glucose and/or interstitial glucose sensors, drug delivery devices, continuous glucose monitoring devices, as well as flash glucose monitoring devices. Methods, software and other hardware aspects are described.

**Evidências citadas:**
> AbstractThere is disclosed a medical system comprising one or more sensors associated with one or more actuators.

---

### 8. Ocular sensor for detection of analytes in tears

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_f7a5c817a31a` |
| **Family ID** | `family:b95487efa9f6d97fd5a2860036dc2261267f7672` |
| **ID** | `JP5390399B2` |
| **Inventores** | ãã¥ã©ã¼ï¼ã¢ãã |
| **Titular** | Eyesense AG |
| **Data** | 2014-01-15 |
| **Fonte** | Google Patents |
| **URL** | [JP5390399B2](https://patents.google.com/patent/JP5390399B2/en) |
| **Triagem** | review |
| **Rota** | manual_review |
| **Motivo da rota** | Triagem indicou revisão humana. |
| **Score de Triagem** | 4.8/10 |
| **Score de Relevância** | 6.2/10 |
| **Nível de Inovação** | Incremental |
| **Domínio Técnico** | Biossensores Biomédicos e Química Analítica |
| **Cluster Temático** | Detecção de Neurotransmissores em Líquidos Corporais |
| **Papel do CO2** | capture_process_stream |
| **Papel do Armazenamento** | Não especificado no resumo. |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | Não especificado no resumo, mas provavelmente envolve um ciclo de leitura e análise contínua. |
| **Fonte/Sumidouro Térmico** | Não especificado no resumo. |
| **Foco das Claims** | Detecção e quantificação da dopamina em lágrimas usando um sensor ocular. |
| **Categoria de Exclusão** | generic_tes |
| **Confiança** | 0.63 |
| **Rerank Aplicado** | Sim |
| **Motivo do Rerank** | reranked:decision_confirmed |
| **Revisão Manual** | Sim |
| **Erro LLM** | N/A |

**Avaliação do LLM:**
Esta patente descreve um sensor ocular para a detecção de analitos em lágrimas, especificamente focado na detecção de dopamina. O dispositivo utiliza um sistema de aquisição e análise de sinais para quantificar a concentração da dopamina nas lágrimas, potencialmente para fins diagnósticos ou monitoramento.

**Extração Estruturada:**
- **Problema:** A necessidade de uma metodologia precisa e não invasiva para medir os níveis de dopamina em lágrimas para diagnóstico médico ou pesquisa.
- **Solução:** O sensor ocular proposto utiliza um método de detecção baseado em sinais ópticos ou eletroquímicos, integrando componentes de aquisição de dados e processamento para determinar a concentração de dopamina nas lágrimas. O sistema é projetado para ser portátil e fácil de usar.
- **Maturidade:** Inicial

**Achados-chave:**
- O sensor ocular é projetado para detectar analitos em lágrimas, com foco na dopamina.
- O sistema incorpora componentes de aquisição e análise de sinais para quantificar a concentração do analito.

**Vantagens alegadas:**
- Detecção não invasiva de dopamina nas lágrimas.
- Potencial para aplicações diagnósticas e monitoramento em tempo real.

**Limitações:**
- A patente não fornece detalhes sobre a sensibilidade ou especificidade do sensor.
- Dependência da precisão dos métodos de aquisição e análise de sinais.

**Aplicações potenciais:**
- Diagnóstico de doenças neurológicas relacionadas à dopamina.
- Monitoramento em tempo real da resposta ao tratamento em pacientes com distúrbios da dopamina.

**Evidências citadas:**
> 'Ocular sensor for detection of analytes in tears' – Implies a system involving tear collection and analysis.

---

### 9. Method and apparatus for neuroenhancement to enhance emotional response

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_0ffcc4a2aadd` |
| **Family ID** | `family:78804768499aefd6aad05557ccd7988e50d6f2f1` |
| **ID** | `US20220273907A1` |
| **Inventores** | Alexander Poltorak |
| **Titular** | Neuroenhancement Lab LLC |
| **Data** | 2022-09-01 |
| **Fonte** | Google Patents |
| **URL** | [US20220273907A1](https://patents.google.com/patent/US20220273907A1/en) |
| **Triagem** | exclude |
| **Rota** | screen_only |
| **Motivo da rota** | Patente excluída na triagem. |
| **Score de Triagem** | 3.5/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | Neurociência, Neuroestimulação |
| **Cluster Temático** | Transferência de estados mentais, Modulação neural |
| **Papel do CO2** | co2_not_central |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | not_clear |
| **Foco das Claims** | process_integration |
| **Categoria de Exclusão** | low_alignment |
| **Confiança** | 0.59 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> AbstractA method of transplanting a desired emotional state from a donor to a recipient, comprising determining an emotional state of the donor; recording neural correlates of the emotional state of the donor who is in the desired emotional state; analyzing neural correlates of the emotional state of the donor to decode at least one of a temporal and a spatial pattern corresponding to the desirable emotional state; converting said at least one of a temporal and a spatial pattern corresponding to the desirable emotional state into a neurostimulation pattern; storing the neurostimulation pattern in the nonvolatile memory; retrieving the neurostimulation pattern from the nonvolatile memory; stimulating the recipient's brain with at least one stimulus modulated with the neurostimulation pattern to induce the desired emotional state in the recipient.

**Evidências citadas:**
> AbstractA method of transplanting a desired emotional state from a donor to a recipient...

---

### 10. Signal processing for continuous analyte sensor

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_23898b43a5bc` |
| **Family ID** | `family:c371df53800cad7d64c9fa5bfabaf2bb449ff11f` |
| **ID** | `US8265725B2` |
| **Inventores** | James H. Brauker, Victoria E. Carr-Brendel, Paul V. Goode, Apurv Ullas Kamath, James Patrick Thrower, Ben Xavier |
| **Titular** | Dexcom Inc |
| **Data** | 2012-09-11 |
| **Fonte** | Google Patents |
| **URL** | [US8265725B2](https://patents.google.com/patent/US8265725B2/en) |
| **Triagem** | exclude |
| **Rota** | screen_only |
| **Motivo da rota** | Patente excluída na triagem. |
| **Score de Triagem** | 3.5/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | Processamento de Sinais, Biossensores |
| **Cluster Temático** | Estimativa de Dados de Analitos Contínuos |
| **Papel do CO2** | co2_not_central |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | general_thermal_management |
| **Foco das Claims** | component_or_operation |
| **Categoria de Exclusão** | low_alignment |
| **Confiança** | 0.64 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> AbstractSystems and methods for dynamically and intelligently estimating analyte data from a continuous analyte sensor, including receiving a data stream, selecting one of a plurality of algorithms, and employing the selected algorithm to estimate analyte values. Additional data processing includes evaluating the selected estimative algorithms, analyzing a variation of the estimated analyte values based on statistical, clinical, or physiological parameters, comparing the estimated analyte values with corresponding measure analyte values, and providing output to a user. Estimation can be used to compensate for time lag, match sensor data with corresponding reference data, warn of upcoming clinical risk, replace erroneous sensor data signals, and provide more timely analyte information encourage proactive behavior and preempt clinical risk.

**Evidências citadas:**
> AbstractSystems and methods for dynamically and intelligently estimating analyte data from a continuous analyte sensor…

---

### 11. A MEASUREMENT SYSTEM FOR
TEAR
CHEMICALS IN THE
TEAR
FOR DIAGNOSING DISEASES
(FR)
SYSTÈME DE MESURE DE PRODUITS CHIMIQUES LACRYMAUX DANS LA LARME POUR DIAGNOSTIQUER DES MALADIES

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_059270d33d03` |
| **Family ID** | `family:70852e9679b13a08d988595e16764ca2f42c2a84` |
| **ID** | `WO/2021/188084` |
| **Inventores** | VARLIBAS, Figen, MOHSENI, Amin Tatabaei, ILBAY, Sultan, OYTUN, Faruk |
| **Titular** | VSY BIYOTEKNOLOJI VE ILAC SANAYI ANONIM SIRKETI
[TR]/[TR] |
| **Data** | 23.09.2021 |
| **Fonte** | Patentscope |
| **URL** | [WO/2021/188084](https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2021188084&_cid=P10-MRXHSI-51243-1) |
| **Triagem** | exclude |
| **Rota** | screen_only |
| **Motivo da rota** | Patente excluída na triagem. |
| **Score de Triagem** | 3.5/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | Diagnóstico Médico / Biossensores |
| **Cluster Temático** | Detecção química em fluidos corporais |
| **Papel do CO2** | co2_not_central |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | not_clear |
| **Foco das Claims** | component_or_operation |
| **Categoria de Exclusão** | generic_tes |
| **Confiança** | 0.68 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> (EN)The measurement system (1) of the present invention comprises a detecting biosensor set (6) which changes colour according to the amount oftearchemicals, includingdopamine, glucose, ascorbate, lactate and proteins, present in thetear. When the measurement process is completed, the detecting biosensor set (6) is analyzed visually, and therefore the level of various chemicals in thetearsuch asdopaminecan be detected.(FR)Le système de mesure (1) de la présente invention comprend un ensemble de biocapteurs de détection (6) qui change de couleur en fonction de la quantité de produits chimiques lacrymaux, notamment la dopamine, le glucose, l'ascorbate, le lactate et les protéines, présents dans la larme. Lorsque le processus de mesure est achevé, l'ensemble de biocapteurs de détection (6) est analysé visuellement, et par conséquent le niveau de divers produits chimiques dans la larme telle que la dopamine peut être détecté.

**Evidências citadas:**
> The measurement system (1) comprises a detecting biosensor set (6) which changes colour according to the amount of tearchemicals, includingdopamine...
> When the measurement process is completed, the detecting biosensor set (6) is analyzed visually, and therefore the level of various chemicals in thetearsuch asdopaminecan be detected.

---

### 12. Non-invasive health indicator monitoring system and using method thereof

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_f4a64eff2003` |
| **Family ID** | `family:ef5f1674a18e96f80a13e97bb22de46d80ff0d22` |
| **ID** | `20150201837` |
| **Inventores** | Yong Won Song, Su Youn Lee, Ji Yeon Lee, Jung Ah Lim, Ji Won Choi, Byung Ki Cheong, Jin Seok Kim, Ho Seong Jang, Hyun Jung Yi |
| **Titular** | KOREA INSTITUTE OF SCIENCE AND TECHNOLOGY |
| **Data** | 23.07.2015 |
| **Fonte** | Patentscope |
| **URL** | [20150201837](https://patentscope.wipo.int/search/en/detail.jsf?docId=US145058030&_cid=P10-MRXHSI-51243-1) |
| **Triagem** | exclude |
| **Rota** | screen_only |
| **Motivo da rota** | Patente excluída na triagem. |
| **Score de Triagem** | 3.5/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | Monitoramento de Saúde |
| **Cluster Temático** | Sensores e Monitoramento Biológico |
| **Papel do CO2** | co2_not_central |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | dedicated_storage_system |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | general_thermal_management |
| **Foco das Claims** | component_or_operation |
| **Categoria de Exclusão** | generic_tes |
| **Confiança** | 0.52 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> (EN)The present invention relates to a non-invasive health indicator monitoring system including a sensing module, an electric power storage module, and a circuit module to collect health indicator information by contacting with a subject. In addition, the present invention also relates to a method for monitoring health indicator continuously by using the health indicator monitoring system.

**Evidências citadas:**
> The present invention relates to a non-invasive health indicator monitoring system including a sensing module,...

---

### 13. Ocular devices and methods for the employment thereof

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_016a4eafc1bc` |
| **Family ID** | `family:195aeeac3c663a7723e714a2bf78ba6256be3b25` |
| **ID** | `20180289326` |
| **Inventores** | Eugene Orloff, Paul V. Braun, Eleonora Orloff, Yang Fei |
| **Titular** | TearDX LLC |
| **Data** | 11.10.2018 |
| **Fonte** | Patentscope |
| **URL** | [20180289326](https://patentscope.wipo.int/search/en/detail.jsf?docId=US231562967&_cid=P10-MRXHSI-51243-1) |
| **Triagem** | exclude |
| **Rota** | screen_only |
| **Motivo da rota** | Patente excluída na triagem. |
| **Score de Triagem** | 3.5/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | Medicina Ocular / Diagnóstico Clínico |
| **Cluster Temático** | Detecção e Análise de Biomarcadores em Lágrimas |
| **Papel do CO2** | co2_not_central |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | dedicated_storage_system |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | not_clear |
| **Foco das Claims** | component_or_operation |
| **Categoria de Exclusão** | low_alignment |
| **Confiança** | 0.66 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> (EN)An ocular device is disclosed along with methods for the employment thereof. In one aspect, a device for placement into a lacrimal punctum or conjunctival sac of a person includes one or moresensormaterials responsive to one or more components of the chemical composition of the person'stears. Eachsensormaterial is configured to present atear-based color from a plurality oftear-based colors indicative of a medical condition of the person. In some embodiments, phenylboronic acid could be employed as asensormaterial(s). In some embodiments, material(s) emitting radiation when excited by other radiation could be employed as asensormaterial. In another aspect, methods for employing the ocular device are disclosed.

**Evidências citadas:**
> In one aspect, a device for placement into a lacrimal punctum or conjunctival sac of a person includes one or moresensormaterials responsive to one or more components of the chemical composition of the person'stears.
> Eachsensormaterial is configured to present atear-based color from a plurality oftear-based colors indicative of a medical condition of the person.

---

### 14. OCULAR DEVICES AND METHODS FOR THE EMPLOYMENT THEREOF
(FR)
DISPOSITIFS OCULAIRES ET LEURS PROCÉDÉS D'UTILISATION

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_bb170214473f` |
| **Family ID** | `family:50b770679ec57c6e31cb9d44d9d21ec2f6b28a44` |
| **ID** | `WO/2018/187693` |
| **Inventores** | ORLOFF, Eugene, BRAUN, Paul, V., ORLOFF, Eleonora, FEI, Yang |
| **Titular** | TEARDX LLC
[US]/[US] |
| **Data** | 11.10.2018 |
| **Fonte** | Patentscope |
| **URL** | [WO/2018/187693](https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2018187693&_cid=P10-MRXHSI-51243-1) |
| **Triagem** | exclude |
| **Rota** | screen_only |
| **Motivo da rota** | Patente excluída na triagem. |
| **Score de Triagem** | 3.5/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | Biotecnologia, Dispositivos Médicos |
| **Cluster Temático** | Detecção e Monitoramento de Biomarcadores em Lágrimas |
| **Papel do CO2** | co2_not_central |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | dedicated_storage_system |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | not_clear |
| **Foco das Claims** | component_or_operation |
| **Categoria de Exclusão** | low_alignment |
| **Confiança** | 0.63 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> (EN)An ocular device is disclosed along with methods for the employment thereof. In one aspect, a device for placement into a lacrimal punctum or conjunctival sac of a person includes one or moresensormaterials responsive to one or more components of the chemical composition of the person'stears. Eachsensormaterial is configured to present atear-based color from a plurality oftear-based colors indicative of a medical condition of the person. In some embodiments, phenylboronic acid could be employed as asensormaterial(s). In some embodiments, material(s) emitting radiation when excited by other radiation could be employed as asensormaterial. In another aspect, methods for employing the ocular device are disclosed.(FR)L'invention concerne un dispositif oculaire et ses procédés d'utilisation. Selon un aspect, un dispositif destiné à être implanté dans le point lacrymal ou le sac conjonctival d'une personne comprend un ou plusieurs matériaux de capteur sensibles à un ou plusieurs composants de la composition chimique des larmes de ladite personne. Chaque matériau de capteur est conçu pour présenter une couleur basée sur les larmes parmi une pluralité de couleurs basées sur les larmes indiquant un état de santé de la personne. Dans certains modes de réalisation, l'acide phénylboronique pourrait être utilisé à titre de matériau(x) de capteur. Dans d'autres, un ou des matériaux émettant un rayonnement quand ils sont excités par un autre rayonnement pourraient être utilisés comme matériau(x) de capteur. Selon un autre aspect, des procédés d'utilisation du dispositif oculaire selon l'invention sont décrits.

**Evidências citadas:**
> In one aspect, a device for placement into a lacrimal punctum or conjunctival sac of a person includes one or moresensormaterials responsive to one or more components of the chemical composition of the person'stears.
> Eachsensormaterial is configured to present atear-based color from a plurality oftear-based colors indicative of a medical condition of the person.

---

### 15. METHODS AND DEVICE FOR TUNING MULTIPLEXED MARKERS FOR DISEASE ASSAY
(FR)
PROCÉDÉS ET DISPOSITIF DE RÉGLAGE DE MARQUEURS MULTIPLEXÉS POUR DOSAGE PATHOLOGIQUE

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_5792a83d7226` |
| **Family ID** | `family:8e193223db61d5fd5b1c28377ed8834fb271448d` |
| **ID** | `WO/2012/009322` |
| **Inventores** | LA BELLE, Jeffrey, DEMIROK, Ugur |
| **Titular** | ARIZONA BOARD OF REGENTS, A BODY CORPORATE OF THE STATE OF ARIZONA, ACTING FOR AND ON BEHALF OF ARIZONA STATE UNIVERSITY
[US]/[US]
(AllExceptUS)
LA BELLE, Jeffrey
[US]/[US](UsOnly)
DEMIROK, Ugur
[US]/[US](UsOnly) |
| **Data** | 19.01.2012 |
| **Fonte** | Patentscope |
| **URL** | [WO/2012/009322](https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2012009322&_cid=P10-MRXHSI-51243-1) |
| **Triagem** | exclude |
| **Rota** | screen_only |
| **Motivo da rota** | Patente excluída na triagem. |
| **Score de Triagem** | 3.5/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | Eletroquímica, Biossensores, Diagnóstico Médico |
| **Cluster Temático** | Detecção Biomarcadores em Sistemas Eletroquímicos |
| **Papel do CO2** | co2_not_central |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | not_clear |
| **Foco das Claims** | component_or_operation |
| **Categoria de Exclusão** | generic_tes |
| **Confiança** | 0.59 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> (EN)The present invention relates to a diagnostic device and methods of using the same for diagnostic assays for monitoring the presence of biological samples wherein the device allows for the determination of at least two assay components on onesensor. More specifically, the invention relates to a multi-marker electrochemical impedance spectroscopysensorcomprising a plurality of molecular recognition elements wherein thesensorcomprises multiple different molecular recognition element types that are tuned in a manner that alters the frequency of the molecular recognition element type such that it is at a detectably different frequency to the frequency of other molecular recognition element types on the samesensor.(FR)Cette invention concerne un dispositif de diagnostic et des procédés pour l'utiliser à des fins de dosages diagnostiques visant à surveiller la présence d'échantillons biologiques, ledit dispositif permettant de déterminer au moins deux composants à doser sur un seul capteur. Plus spécifiquement, l'invention concerne un capteur multi-marqueurs de spectroscopie d'impédance électrochimique comprenant une pluralité d'éléments de reconnaissance moléculaires, ledit capteur comprenant de multiples types d'éléments de reconnaissance moléculaires différents qui sont réglés d'une manière qui modifie la fréquence du type d'élément de reconnaissance moléculaire pour qu'il soit à une fréquence différente, sur le plan de la détection, de la fréquence des autres types d'éléments de reconnaissance moléculaires sur le même capteur.

**Evidências citadas:**
> The present invention relates to a diagnostic device and methods of using the same for diagnostic assays for monitoring the presence of biological samples wherein the device allows for the determination of at least two assay components on onesensor.
> More specifically, the invention relates to a multi-marker electrochemical impedance spectroscopysensorcomprising a plurality of molecular recognition elements

---

### 16. Methods and device for tuning multiplexed markers for disease assay

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_5987972a3b34` |
| **Family ID** | `family:6df81555ca82bf75d3299edda630de5611c09fe8` |
| **ID** | `20130183243` |
| **Inventores** | Jeffrey LaBelle, Ugur Demirok |
| **Titular** | Jeffrey LaBelle
ARIZONA BOARD OF REGENTS ON BEHALF OF ARIZONA STATE UNIVERSITY
Ugur Demirok |
| **Data** | 18.07.2013 |
| **Fonte** | Patentscope |
| **URL** | [20130183243](https://patentscope.wipo.int/search/en/detail.jsf?docId=US86177550&_cid=P10-MRXHSI-51243-1) |
| **Triagem** | exclude |
| **Rota** | screen_only |
| **Motivo da rota** | Patente excluída na triagem. |
| **Score de Triagem** | 3.3/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | Sensores Eletroquímicos, Diagnóstico Médico |
| **Cluster Temático** | Detecção de Biomarcadores em Sensores |
| **Papel do CO2** | co2_not_central |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | general_thermal_management |
| **Foco das Claims** | component_or_operation |
| **Categoria de Exclusão** | low_alignment |
| **Confiança** | 0.52 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> (EN)The present invention relates to a diagnostic device and methods of using the same for diagnostic assays for monitoring the presence of biological samples wherein the device allows for the determination of at least two assay components on onesensor. More specifically, the invention relates to a multi-marker electrochemical impedance spectroscopysensorcomprising a plurality of molecular recognition elements wherein thesensorcomprises multiple different molecular recognition element types that are tuned in a manner that alters the frequency of the molecular recognition element type such that it is at a detectably different frequency to the frequency of other molecular recognition element types on the samesensor.

**Evidências citadas:**
> The invention relates to a multi-marker electrochemical impedance spectroscopysensorcomprising a plurality of molecular recognition elements

---

### 17. ONE-TOUCH FINGERTIP SWEAT
SENSOR
AND PERSONALIZED DATA PROCESSING FOR RELIABLE PREDICTION OF BLOOD BIOMARKER CONCENTRATIONS

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_6e979406ac26` |
| **Family ID** | `family:4b5571851c04698f0ee4815676cfadc724b8bc53` |
| **ID** | `20240049994` |
| **Inventores** | Lu Yin, Hazhir Teymourian, Joseph Wang, Juliane R. Sempionatto-Moreto, Jong-Min Moon |
| **Titular** | THE REGENTS OF THE UNIVERSITY OF CALIFORNIA |
| **Data** | 15.02.2024 |
| **Fonte** | Patentscope |
| **URL** | [20240049994](https://patentscope.wipo.int/search/en/detail.jsf?docId=US422369809&_cid=P10-MRXHSI-51243-1) |
| **Triagem** | exclude |
| **Rota** | screen_only |
| **Motivo da rota** | Patente excluída na triagem. |
| **Score de Triagem** | 3.5/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | Biossensores, Monitoramento Biomédico |
| **Cluster Temático** | Detecção e Análise de Analitos em Suor |
| **Papel do CO2** | co2_not_central |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | general_thermal_management |
| **Foco das Claims** | component_or_operation |
| **Categoria de Exclusão** | generic_tes |
| **Confiança** | 0.68 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> (EN)Methods, systems, and devices are disclosed for collecting and transferring naturally-produced sweat containing an analyte to a biosensor and/or biofuel cell to estimate a concentration of the analyte corresponding to the analyte's concentration in blood and/or for producing electricity. In some aspects, a device includes a substrate, a plurality of electrodes disposed on the substrate and operable to detect an analyte in naturally-produced sweat of an individual, and a sweat permeation layer including a hydrogel, wherein the sweat permeation layer is in contact with the plurality of electrodes and configured to transfer the sweat containing the analyte through the sweat permeation layer to reach the plurality of electrodes for detection and/or energy harvesting.

**Evidências citadas:**
> In some aspects, a device includes a substrate, a plurality of electrodes disposed on the substrate and operable to detect an analyte in naturally-produced sweat of an individual...
> ...sweat permeation layer including a hydrogel, wherein the sweat permeation layer is in contact with the plurality of electrodes...

---

### 18. ONE-TOUCH FINGERTIP SWEAT
SENSOR
AND PERSONALIZED DATA PROCESSING FOR RELIABLE PREDICTION OF BLOOD BIOMARKER CONCENTRATIONS
(FR)
CAPTEUR DE TRANSPIRATION DE BOUT DE DOIGT A TOUCHER UNIQUE ET TRAITEMENT DE DONNEES PERSONNALISEES POUR UNE PREDICTION FIABLE DE CONCENTRATIONS DE BIOMARQUEURS SANGUINS

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_8698c1280543` |
| **Family ID** | `family:ce553468cc09cc7eaa5ca311a4e0287f4bbb0d64` |
| **ID** | `3210742` |
| **Inventores** | LU YIN, HAZHIR TEYMOURIAN, JOSEPH WANG, JULIANE R. SEMPIONATTO-MORETO, JONG-MIN MOON |
| **Titular** | THE REGENTS OF THE UNIVERSITY OF CALIFORNIA |
| **Data** | 11.08.2022 |
| **Fonte** | Patentscope |
| **URL** | [3210742](https://patentscope.wipo.int/search/en/detail.jsf?docId=CA406582873&_cid=P10-MRXHSI-51243-1) |
| **Triagem** | exclude |
| **Rota** | screen_only |
| **Motivo da rota** | Patente excluída na triagem. |
| **Score de Triagem** | 3.5/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | Biossensores, Monitoramento Biomédico |
| **Cluster Temático** | Detecção de Biomarcadores em Suor |
| **Papel do CO2** | co2_not_central |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | general_thermal_management |
| **Foco das Claims** | component_or_operation |
| **Categoria de Exclusão** | generic_tes |
| **Confiança** | 0.68 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> (EN)Methods, systems, and devices are disclosed for collecting and transferring naturally-produced sweat containing an analyte to a biosensor and/or biofuel cell to estimate a concentration of the analyte corresponding to the analyte's concentration in blood and/or for producing electricity. In some aspects, a device includes a substrate, a plurality of electrodes disposed on the substrate and operable to detect an analyte in naturally-produced sweat of an individual, and a sweat permeation layer including a hydrogel, wherein the sweat permeation layer is in contact with the plurality of electrodes and configured to transfer the sweat containing the analyte through the sweat permeation layer to reach the plurality of electrodes for detection and/or energy harvesting.(FR)La divulgation concerne des procédés, des systèmes et des dispositifs permettant de collecter et de transférer de la transpiration produite naturellement contenant un analyte à un biocapteur et/ou à une pile à combustible en vue d'estimer une concentration de l'analyte correspondant à la concentration de l'analyte dans le sang et/ou de produire de l'électricité. Selon certains aspects, un dispositif comprenant un substrat, une pluralité d'électrodes disposées sur le substrat et pouvant être utilisées pour détecter un analyte dans la transpiration produite naturellement par un individu, ainsi qu'une couche de perméation à la transpiration comprenant un hydrogel, la couche de perméation à la transpiration étant en contact avec la pluralité d'électrodes et conçue pour transférer la transpiration contenant l'analyte à travers la couche de perméation à la transpiration pour atteindre la pluralité d'électrodes en vue de la détection et/ou de la collecte d'énergie.

**Evidências citadas:**
> In some aspects, a device includes a substrate, a plurality of electrodes disposed on the substrate and operable to detect an analyte in naturally-produced sweat of an individual...
> a sweat permeation layer including a hydrogel, wherein the sweat permeation layer is in contact with the plurality of electrodes and configured to transfer the sweat containing the analyte through the sweat permeation layer...

---

### 19. ONE-TOUCH FINGERTIP SWEAT
SENSOR
AND PERSONALIZED DATA PROCESSING FOR RELIABLE PREDICTION OF BLOOD BIOMARKER CONCENTRATIONS
(FR)
CAPTEUR DE TRANSPIRATION DE BOUT DE DOIGT À TOUCHER UNIQUE ET TRAITEMENT DE DONNÉES PERSONNALISÉES POUR UNE PRÉDICTION FIABLE DE CONCENTRATIONS DE BIOMARQUEURS SANGUINS

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_1f9d24476e0b` |
| **Family ID** | `family:5e2016c77cdc34d57f9ba1f2cd41f10abb14097c` |
| **ID** | `WO/2022/170361` |
| **Inventores** | YIN, Lu, TEYMOURIAN, Hazhir, WANG, Joseph, SEMPIONATTO-MORETO, Juliane R., MOON, Jong-Min |
| **Titular** | THE REGENTS OF THE UNIVERSITY OF CALIFORNIA
[US]/[US] |
| **Data** | 11.08.2022 |
| **Fonte** | Patentscope |
| **URL** | [WO/2022/170361](https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2022170361&_cid=P10-MRXHSI-51243-1) |
| **Triagem** | exclude |
| **Rota** | screen_only |
| **Motivo da rota** | Patente excluída na triagem. |
| **Score de Triagem** | 3.5/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | Biossensores e Bioenergia |
| **Cluster Temático** | Monitoramento Biomarcador via Transpiração |
| **Papel do CO2** | capture_process_stream |
| **Papel do Armazenamento** | implicit_or_support_storage |
| **Limite Sistêmico** | cycle_or_transfer_subsystem |
| **Tipo de Ciclo** | refrigeration_cycle |
| **Fonte/Sumidouro Térmico** | cooling_or_refrigeration |
| **Foco das Claims** | system_architecture |
| **Categoria de Exclusão** | cooling_only |
| **Confiança** | 0.68 |
| **Rerank Aplicado** | Sim |
| **Motivo do Rerank** | reranked:review->exclude |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> (EN)Methods, systems, and devices are disclosed for collecting and transferring naturally-produced sweat containing an analyte to a biosensor and/or biofuel cell to estimate a concentration of the analyte corresponding to the analyte's concentration in blood and/or for producing electricity. In some aspects, a device includes a substrate, a plurality of electrodes disposed on the substrate and operable to detect an analyte in naturally-produced sweat of an individual, and a sweat permeation layer including a hydrogel, wherein the sweat permeation layer is in contact with the plurality of electrodes and configured to transfer the sweat containing the analyte through the sweat permeation layer to reach the plurality of electrodes for detection and/or energy harvesting.(FR)La divulgation concerne des procédés, des systèmes et des dispositifs permettant de collecter et de transférer de la transpiration produite naturellement contenant un analyte à un biocapteur et/ou à une pile à combustible en vue d'estimer une concentration de l'analyte correspondant à la concentration de l'analyte dans le sang et/ou de produire de l'électricité. Selon certains aspects, un dispositif comprenant un substrat, une pluralité d'électrodes disposées sur le substrat et pouvant être utilisées pour détecter un analyte dans la transpiration produite naturellement par un individu, ainsi qu'une couche de perméation à la transpiration comprenant un hydrogel, la couche de perméation à la transpiration étant en contact avec la pluralité d'électrodes et conçue pour transférer la transpiration contenant l'analyte à travers la couche de perméation à la transpiration pour atteindre la pluralité d'électrodes en vue de la détection et/ou de la collecte d'énergie.

**Evidências citadas:**
> "Methods, systems, and devices are disclosed for collecting and transferring naturally-produced sweat..."
> The device includes a 'sweat permeation layer including a hydrogel, wherein the sweat permeation layer is in contact with the plurality of electrodes'

---

### 20. ONE-TOUCH FINGERTIP SWEAT
SENSOR
AND PERSONALIZED DATA PROCESSING FOR RELIABLE PREDICTION OF BLOOD BIOMARKER CONCENTRATIONS

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_f1b878a245ec` |
| **Family ID** | `family:33ec0a8c33555d4cb33d45a62f51383357ef88fa` |
| **ID** | `2022216341` |
| **Inventores** | MOON, Jong-Min, SEMPIONATTO-MORETO, Juliane R., TEYMOURIAN, Hazhir, WANG, Joseph, YIN, Lu |
| **Titular** | THE REGENTS OF THE UNIVERSITY OF CALIFORNIA |
| **Data** | 11.08.2022 |
| **Fonte** | Patentscope |
| **URL** | [2022216341](https://patentscope.wipo.int/search/en/detail.jsf?docId=AU406509324&_cid=P10-MRXHSI-51243-1) |
| **Triagem** | exclude |
| **Rota** | screen_only |
| **Motivo da rota** | Patente excluída na triagem. |
| **Score de Triagem** | 3.5/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | Biossensores, Monitoramento Biomédico |
| **Cluster Temático** | Detecção e análise de biomarcadores através de fluidos corporais |
| **Papel do CO2** | co2_not_central |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | general_thermal_management |
| **Foco das Claims** | component_or_operation |
| **Categoria de Exclusão** | generic_tes |
| **Confiança** | 0.68 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> (EN)Methods, systems, and devices are disclosed for collecting and transferring naturally-produced sweat containing an analyte to a biosensor and/or biofuel cell to estimate a concentration of the analyte corresponding to the analyte's concentration in blood and/or for producing electricity. In some aspects, a device includes a substrate, a plurality of electrodes disposed on the substrate and operable to detect an analyte in naturally-produced sweat of an individual, and a sweat permeation layer including a hydrogel, wherein the sweat permeation layer is in contact with the plurality of electrodes and configured to transfer the sweat containing the analyte through the sweat permeation layer to reach the plurality of electrodes for detection and/or energy harvesting.

**Evidências citadas:**
> "Methods, systems, and devices are disclosed for collecting and transferring naturally-produced sweat containing an analyte to a biosensor and/or biofuel cell..."
> A device includes a substrate, a plurality of electrodes disposed on the substrate and operable to detect an analyte in naturally-produced sweat

---

## 🧾 Fila de Revisão Manual

- rec_245e60bec916 (CN116448850A) | rota=manual_review | motivo=Triagem indicou revisão humana. | erro_llm=N/A
- rec_fde35625d301 (CN108872343A) | rota=manual_review | motivo=Triagem indicou revisão humana. | erro_llm=N/A
- rec_bc447a4191dd (CN1395094A) | rota=manual_review | motivo=Triagem indicou revisão humana. | erro_llm=N/A
- rec_d461537cff92 (CN105241868A) | rota=manual_review | motivo=Triagem indicou revisão humana. | erro_llm=N/A
- rec_2056c5d6639a (CN112578011A) | rota=manual_review | motivo=Triagem indicou revisão humana. | erro_llm=N/A
- rec_f7a5c817a31a (JP5390399B2) | rota=manual_review | motivo=Triagem indicou revisão humana. | erro_llm=N/A

---

## 🔬 Análise Comparativa

### 1. Panorama Geral

- O conjunto comparativo agrega 6 patente(s) e nao deve ser tratado como bloco homogeneo: ha um nucleo direto, fronteiras tecnicas em revisao e adjacencias uteis apenas para delimitar whitespace [IDs: CN105241868A, CN108872343A, CN112578011A, CN116448850A, CN1395094A, JP5390399B2]
- O subgrupo mais diretamente alinhado ao núcleo da query é CN105241868A, com foco em armazenamento de CO2, compressão/expansão e controle termodinâmico do meio armazenado [IDs: CN105241868A]
- CN105241868A, CN108872343A, CN112578011A, CN116448850A, CN1395094A, JP5390399B2 formam a fronteira tecnica: sao casos proximos do problema, mas ainda ambiguos quanto ao papel exato do CO2 no armazenamento ou na funcao arquitetural central [IDs: CN105241868A, CN108872343A, CN112578011A, CN116448850A, CN1395094A, JP5390399B2]

## Análise Comparativa de Patentes – “dopamine tears sensor”

### 2. Tendências Identificadas

*   **Eletroquímica como Técnica Predominante:** A grande maioria das patentes (CN105241868A, CN108872343A, CN112578011A, CN1395094A) utiliza a eletroquímica como método de detecção da dopamina, com foco em sensores eletrocrómicos e na otimização das membranas sensíveis. [IDs: CN105241868A, CN108872343A, CN112578011A, CN1395094A]
*   **Materiais Avançados:** Há uma tendência crescente no uso de nanomateriais (CN105241868A), grafeno dopado com nitrogênio (CN108872343A) e MXenes (CN112578011A) para melhorar as propriedades dos sensores. [IDs: CN105241868A, CN108872343A, CN112578011A]
*   **Integração de Termodinâmica:** Uma tendência emergente é a integração de elementos termodinâmicos e sistemas de armazenamento de calor para aumentar o potencial da detecção de dopamina. [IDs: CN116448850A, JP5390399B2]
*   **Foco em Líquidos Corporais:** A maioria das patentes se concentra na detecção de dopamina em lágrimas (CN108872343A, CN116448850A, JP5390399B2), refletindo o interesse em aplicações biomédicas específicas. [IDs: CN108872343A, CN116448850A, JP5390399B2]

### 3. Whitespaces e Oportunidades

- As patentes em review delimitam fronteiras tecnicas onde o papel do CO2 ainda esta ambiguo entre meio armazenado, fluido de trabalho e interface de troca termica; esse tipo de ambiguidade costuma ser um bom proxy para whitespace exploravel com recorte arquitetural mais especifico [IDs: CN105241868A, CN108872343A, CN112578011A, CN116448850A]

### 4. Recomendações

- Priorizar arquiteturas centradas em armazenamento explícito de CO2 e controle termodinâmico rigoroso [IDs: CN105241868A]

### 5. Ranking Final

1. **CN105241868A** — alinhamento técnico sustentado pelas evidências extraídas; score 6.5/10 [IDs: CN105241868A]
2. **CN108872343A** — alinhamento técnico sustentado pelas evidências extraídas; score 6.5/10 [IDs: CN108872343A]
3. **CN112578011A** — armazenamento termico explicito como parte central; score 6.5/10 [IDs: CN112578011A]
4. **CN116448850A** — CO2 aparece como meio termodinamico armazenado; armazenamento termico explicito como parte central; score 6.5/10 [IDs: CN116448850A]
5. **CN1395094A** — armazenamento termico explicito como parte central; score 6.5/10 [IDs: CN1395094A]
6. **JP5390399B2** — alinhamento técnico sustentado pelas evidências extraídas; score 6.2/10 [IDs: JP5390399B2]

### 6. Mapa de Evidências por ID

- **Desenvolvimento de sensores químicos para a detecção de neurotransmissores.** [IDs: CN108872343A]
- **Detecção Biomolecular Eletroquímica** [IDs: CN112578011A]
- **Detecção Biomolecular com Eletrônica e Termodinâmica** [IDs: CN116448850A]
- **Detecção Eletroquímica de Biomoléculas** [IDs: CN1395094A]
- **Detecção de Neurotransmissores em Líquidos Corporais** [IDs: JP5390399B2]
- **Detecção eletroluminescência de neurotransmissores** [IDs: CN105241868A]

### 7. Ranking por ID

1. **CN105241868A** — score 6.5/10 [IDs: CN105241868A]
2. **CN108872343A** — score 6.5/10 [IDs: CN108872343A]
3. **CN112578011A** — score 6.5/10 [IDs: CN112578011A]
4. **CN116448850A** — score 6.5/10 [IDs: CN116448850A]
5. **CN1395094A** — score 6.5/10 [IDs: CN1395094A]
6. **JP5390399B2** — score 6.2/10 [IDs: JP5390399B2]

---

## 🧭 Matriz de Whitespaces

- **Patentes selecionadas:** 6
- **Núcleo:** 0
- **Fronteira:** 6
- **Adjacência:** 0


---

## ℹ️ Informações do Sistema

- **Gerado por:** Agente de Web Scraping de Patentes
- **Modelo LLM:** gemma3:4b
- **Data de geração:** 23/07/2026 13:02:10
- **Query de busca:** `dopamine tears sensor`
- **Status da execução:** completed
- **Tempo total:** 1768.0s
- **LLM disponível:** sim
- **Fila de revisão manual:** 6 itens
- **Snapshot hash:** `4cd8a44d9f345026230bfb6941ecc1fa45d92ebd51614b6795fe2be86de24246`
- **Features habilitadas:** require_evidence, enable_thematic_clusters, enable_structural_roles, enable_screening_rerank, enable_prisma, enable_snapshot, enable_comparative_analysis, enable_whitespace_analysis, enable_manual_review_queue
- **Features desabilitadas:** nenhum
- **Versão do pipeline:** 1.1
- **Thresholds snapshot:** include=7.0, review=4.5
- **Cache LLM:** 0 hits, 34 misses, 159 entradas
- **Status do rascunho:** ready