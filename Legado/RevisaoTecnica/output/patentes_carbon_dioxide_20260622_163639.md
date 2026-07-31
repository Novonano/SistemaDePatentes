# 📋 Relatório de Análise de Patentes

**Data:** 22/06/2026 16:36:39
**Busca:** `carbon dioxide`
**Total de patentes encontradas:** 20
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

- **Total bruto coletado:** 20
- **Patentes únicas:** 20
- **Duplicatas removidas:** 0
- **Triadas:** 20
- **Incluídas:** 6
- **Em revisão manual:** 7
- **Excluídas:** 7
- **Extrações completas:** 13
- **Sem abstract/snippet:** 1
- **Sem ID:** 0
- **Identidade por conteúdo:** 0
- **Identidade fallback:** 0
- **Duplicatas por família removidas:** 0
- **Falhas de triagem LLM:** 0
- **Falhas totais LLM:** 0

## 🧭 Fluxo PRISMA-Like

- **Identificação:** 20 bruto(s), 20 único(s), 0 duplicata(s) removida(s)
- **Triagem:** 20 triado(s), 6 incluído(s), 7 em revisão, 7 excluído(s)
- **Elegibilidade:** 13 extração(ões) completa(s), 7 revisão(ões) manual(is), 0 adiada(s)
- **Cobertura:** 1 sem abstract/snippet, 0 sem ID
- **Síntese:** 13 registro(s) analisado(s)

## 🧩 Síntese Temática

### Engenharia Química / Materiais

- **Patentes:** 1
- **Score médio:** 8.40/10
- **Confiança média:** 0.95
- **Evidências citadas:** 1
- **IDs:** US7132090B2

### Química, Engenharia Química, Materiais

- **Patentes:** 1
- **Score médio:** 8.10/10
- **Confiança média:** 0.95
- **Evidências citadas:** 2
- **IDs:** US12391556B1

### Economic Optimization

- **Patentes:** 1
- **Score médio:** 8.10/10
- **Confiança média:** 0.95
- **Evidências citadas:** 2
- **IDs:** US20220072471A1

### Engenharia Química, Engenharia Ambiental

- **Patentes:** 1
- **Score médio:** 8.10/10
- **Confiança média:** 0.95
- **Evidências citadas:** 2
- **IDs:** US20230302393A1

### Eletroquímica, Captura de Carbono, DAC (Direct Air Capture)

- **Patentes:** 1
- **Score médio:** 8.00/10
- **Confiança média:** 0.95
- **Evidências citadas:** 2
- **IDs:** US20240252980A1

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
| setup | ok | 3.83s | 1 | Verificação do modelo Ollama |
| search | ok | 103.31s | 20 | 20 patentes únicas após dedupe |
| screening | ok | 1705.74s | 20 | 6 incluídas, 7 revisão |
| comparative_analysis | ok | 52.26s | 20 | Síntese comparativa gerada |
| whitespace_analysis | ok | 0.00s | 13 | Whitespace analysis estruturada gerada |
| reporting | ok | 0.01s | 20 | Relatórios Markdown e JSON |
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
- **Latência média:** 3.83s
- **Latência máxima:** 3.83s

### screening

- **Chamadas:** 20
- **Sucessos:** 20
- **Falhas:** 0
- **Retries:** 0
- **Cache hits:** 0
- **Pulos por degradação:** 0
- **Latência média:** 32.659s
- **Latência máxima:** 40.168s

### rerank

- **Chamadas:** 7
- **Sucessos:** 7
- **Falhas:** 0
- **Retries:** 0
- **Cache hits:** 0
- **Pulos por degradação:** 0
- **Latência média:** 31.37s
- **Latência máxima:** 39.413s

### evaluation

- **Chamadas:** 13
- **Sucessos:** 13
- **Falhas:** 0
- **Retries:** 0
- **Cache hits:** 0
- **Pulos por degradação:** 0
- **Latência média:** 64.073s
- **Latência máxima:** 76.434s

### comparative

- **Chamadas:** 1
- **Sucessos:** 1
- **Falhas:** 0
- **Retries:** 0
- **Cache hits:** 0
- **Pulos por degradação:** 0
- **Latência média:** 52.256s
- **Latência máxima:** 52.256s

## 🔎 Observabilidade Estruturada

### Rotas

- **manual_review**: total=7, include=0, review=7, exclude=0, llm_errors=0
- **screen_only**: total=7, include=0, review=0, exclude=7, llm_errors=0
- **deep_extraction**: total=6, include=6, review=0, exclude=0, llm_errors=0

### Fontes

- **EPO**: bruto=0, duração=0.00s, diagnósticos=config_missing=1
- **GooglePatents**: bruto=10, duração=33.55s, diagnósticos=nenhum
- **Patentscope**: bruto=10, duração=69.75s, diagnósticos=nenhum

### Falhas

- **Erros de execução:** 0
- **Registros com erro de LLM:** 0
- **Falhas totais do LLM:** 0
- **LLM por operação:** comparative(falhas=0, retries=0, skips=0), evaluation(falhas=0, retries=0, skips=0), healthcheck(falhas=0, retries=0, skips=0), rerank(falhas=0, retries=0, skips=0), screening(falhas=0, retries=0, skips=0)
- **Scraper por tipo de sinal:** config_missing=1

## 📊 Resumo Executivo

**Score médio de relevância:** 8.1/10

| # | Patente | Score | Inovação | Domínio |
|---|---------|-------|----------|---------|
| 1 | [US7132090B2](https://patents.google.com/patent/US7132090B2/en) — Sequestration of carbon dioxide | 🟢 8.4 (include) | Incremental | Engenharia Química / Materiais |
| 2 | [US12391556B1](https://patents.google.com/patent/US12391556B1/en) — Carbon dioxide capture using activated carbon derived from s... | 🟢 8.1 (include) | Incremental | Química, Engenharia Química, Materiais |
| 3 | [US20220072471A1](https://patents.google.com/patent/US20220072471A1/en) — Direct carbon dioxide capture from air | 🟢 8.1 (include) | Incremental | Engenharia Química / Engenharia Ambiental |
| 4 | [US20230302393A1](https://patents.google.com/patent/US20230302393A1/en) — System and method for direct air capture of carbon dioxide u... | 🟢 8.1 (include) | Incremental | Engenharia Química, Engenharia Ambiental |
| 5 | [US20240252980A1](https://patents.google.com/patent/US20240252980A1/en) — Direct air capture reactor systems and related methods of tr... | 🟢 8.0 (include) | Significativa | Eletroquímica, Captura de Carbono, DAC (Direct Air Capture) |
| 6 | [WO2024208966A1](https://patents.google.com/patent/WO2024208966A1/en) — Plant and method for capturing carbon dioxide | 🟢 7.7 (include) | Significativa | Engenharia Química / Engenharia Ambiental |
| 7 | [US20070231244A1](https://patents.google.com/patent/US20070231244A1/en) — Carbon dioxide purification method | 🟡 6.5 (review) | Incremental | Refrigeração Industrial |
| 8 | [US8500855B2](https://patents.google.com/patent/US8500855B2/en) — System and method for carbon dioxide capture and sequestrati... | 🟡 6.5 (review) | Incremental | Chemical Engineering |
| 9 | [WO2025230882A1](https://patents.google.com/patent/WO2025230882A1/en) — Capture and release of carbon dioxide using electrogenerated... | 🟡 6.5 (review) | Incremental | Electrochemistry, Chemical Engineering |
| 10 | [US8119091B2](https://patents.google.com/patent/US8119091B2/en) — Carbon dioxide capture | 🟡 6.5 (review) | Incremental | Chemical Engineering, Environmental Technology |
| 11 | [1429678](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135599119&_cid=P22-MQPEQU-91691-1) — APPARATUS FOR SUPPLYING LIQUID
CARBON
DIOXIDE | 🟡 6.5 (review) | Significativa | Controle de Processos, Termodinâmica, Sistemas de Refrigeração |
| 12 | [2047588](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135860928&_cid=P22-MQPEQU-91691-1) — Reclamation of foundry sand | 🟡 6.5 (review) | Incremental | Materiais de Fundição e Processos Recuperativos |
| 13 | [1125505](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135308953&_cid=P22-MQPEQU-91691-1) — Production of
carbon
dioxide
and argon | 🟡 6.5 (review) | Incremental | Chemical Engineering |
| 14 | [1171698](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135354895&_cid=P22-MQPEQU-91691-1) — Dispensing Device | 🔴 0.0 (exclude) | N/A | Dispositivos de Dispensação de Líquidos |
| 15 | [1557123](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135726881&_cid=P22-MQPEQU-91691-1) — METHOD AND APPARATUS FOR REPARING EXTRACTS OF HOPS AND OTHER... | 🔴 0.0 (exclude) | N/A | Processamento de bebidas alcoólicas |
| 16 | [1426573](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135595668&_cid=P22-MQPEQU-91691-1) — WEIGHING MACHINES | 🔴 0.0 (exclude) | N/A | Engenharia de Processos |
| 17 | [1174314](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135357801&_cid=P22-MQPEQU-91691-1) — A Dispensing Device for Gases Under Pressure. | 🔴 0.0 (exclude) | N/A | Engenharia de Fluidos, Instrumentação |
| 18 | [1253973](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135438798&_cid=P22-MQPEQU-91691-1) — LIQUID MOVING SYSTEMS | 🔴 0.0 (exclude) | N/A | Process Control & Instrumentation |
| 19 | [1329637](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135513929&_cid=P22-MQPEQU-91691-1) — TEMPORARY FREEZING OF SOFT OR FLEXIBLE ARTICLES | 🔴 0.0 (exclude) | N/A | Engenharia de Materiais, Refrigeração |
| 20 | [1236064](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135420945&_cid=P22-MQPEQU-91691-1) — IMPROVEMENTS IN OR RELATING TO FIRE EXTINGUISHING COMPOSITIO... | 🔴 0.0 (exclude) | N/A | Extinção de Incêndio |

---

## 🔍 Análise Detalhada das Patentes

### 1. Carbon dioxide capture using activated carbon derived from spent coffee grounds

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_4dc0a7b145e4` |
| **Family ID** | `family:4039807f1b6106aa7a26b2238f896e1491b2584d` |
| **ID** | `US12391556B1` |
| **Inventores** | Haif Aljomard, Abrar Inayat, Rafik Kalfat, Chaouki GHENAI |
| **Titular** | University of Sharjah |
| **Data** | 2025-08-19 |
| **Fonte** | Google Patents |
| **URL** | [US12391556B1](https://patents.google.com/patent/US12391556B1/en) |
| **Triagem** | include |
| **Rota** | deep_extraction |
| **Motivo da rota** | Há evidência suficiente para extração detalhada. |
| **Score de Triagem** | 9.2/10 |
| **Score de Relevância** | 8.1/10 |
| **Nível de Inovação** | Incremental |
| **Domínio Técnico** | Química, Engenharia Química, Materiais |
| **Cluster Temático** | Química, Engenharia Química, Materiais |
| **Papel do CO2** | capture_process_stream |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | não especificado no abstract |
| **Foco das Claims** | Síntese e utilização de carvão ativado para adsorção de CO2. |
| **Categoria de Exclusão** | N/A |
| **Confiança** | 0.95 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> AbstractA method of capturing carbon dioxide comprising synthesising activated carbon using spent coffee grounds (SCG), polyethylene terephthalate (PET), and potassium hydroxide (KOH). The mixture is co-pyrolyzed at a temperature of less than 500 degrees Celsius activated at a temperature of less than 700 degrees Celsius. Carbon dioxide is adsorbed onto a surface of the synthesized activated carbon at a rate of greater than 8 mmol/g at 0 degrees Celsius and at 1 bar absolute pressure. There is also provided an activated carbon product, wherein the activated carbon product has a carbon dioxide adsorption rate of greater than 8 mmol/g at 0 degrees Celsius and at 1 bar absolute pressure.

**Avaliação do LLM:**
Esta patente descreve um método para capturar dióxido de carbono utilizando carvão ativado produzido a partir de resíduos de café, PET e KOH. O processo envolve a co-pirólise da mistura em temperaturas controladas, resultando em carvão ativado com alta capacidade de adsorção de CO2. A patente foca na otimização da taxa de adsorção do CO2 neste material.

**Extração Estruturada:**
- **Problema:** A necessidade de métodos eficientes e sustentáveis para a captura de dióxido de carbono, utilizando resíduos como matéria-prima.
- **Solução:** A solução proposta é a síntese de carvão ativado a partir de resíduos de café, PET e KOH através da co-pirólise, criando um material com alta capacidade de adsorção para CO2.
- **Maturidade:** Inicial

**Achados-chave:**
- A taxa de adsorção de CO2 no carvão ativado sintetizado é superior a 8 mmol/g em 0°C e 1 bar.
- O processo utiliza uma temperatura de co-pirólise inferior a 500°C, minimizando o consumo de energia.

**Vantagens alegadas:**
- Utilização de resíduos como matéria-prima (spent coffee grounds, PET, KOH).
- Alta taxa de adsorção de CO2 no material produzido.

**Limitações:**
- A patente não detalha a escala do processo ou a durabilidade do carvão ativado.
- O desempenho pode variar dependendo das condições operacionais específicas (temperatura, pressão).

**Aplicações potenciais:**
- Captura de CO2 em fontes industriais (e.g., usinas de energia).
- Remoção de CO2 da atmosfera.
- Utilização do carvão ativado em outras aplicações de adsorção.

**Evidências citadas:**
> AbstractA method of capturing carbon dioxide comprising synthesising activated carbon using spent coffee grounds (SCG), polyethylene terephthalate (PET), and potassium hydroxide (KOH).
> Carbon dioxide is adsorbed onto a surface of the synthesized activated carbon...

---

### 2. Direct carbon dioxide capture from air

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_bf9199489578` |
| **Family ID** | `family:450006d06fd5358f368f1f6d3359139d138f6a20` |
| **ID** | `US20220072471A1` |
| **Inventores** | Hans De Neve, Wilhelmus Jozef SOPPE, Johannis Alouisius Zacharias Pieterse, Gerard Douwe Elzinga, Cornelis Hendrikus Frijters, Catharina Henriette Maria Van Der Werf |
| **Titular** | Nederlandse Organisatie voor Toegepast Natuurwetenschappelijk Onderzoek TNO |
| **Data** | 2022-03-10 |
| **Fonte** | Google Patents |
| **URL** | [US20220072471A1](https://patents.google.com/patent/US20220072471A1/en) |
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
> AbstractThe present invention concerns a device and process for capturing CO2 from air. The device comprises (a) a membrane at least partly permeable for air comprising a solid state CO2 sorbent; (b) at least one sorption chamber; (c) at least one regeneration chamber; (d) means for transporting the membrane from the sorption chamber to the regeneration chamber and back; (e) an inlet for receiving air located on one end of the membrane and an outlet for discharging air depleted in CO2 located on the other end of the membrane in the sorption chamber, wherein the device is configured to allow air to flow from the inlet to the outlet through the membrane; (f) means for flowing stripping gas through the membrane into the regeneration chamber; (g) at least one outlet for discharging CO2, located in the regeneration chamber; and (h) heating means for heating the regeneration chamber. The device according to the invention provides an efficient and low-cost solution for capturing CO2 directly from air.

**Avaliação do LLM:**
Esta patente descreve um dispositivo para captura direta de CO2 da atmosfera utilizando um sorvente sólido e um processo de regeneração, envolvendo membranas permeáveis, câmaras de absorção e regeneração, e aquecimento. O objetivo é fornecer uma solução eficiente e de baixo custo para a captura de CO2 do ar.

**Extração Estruturada:**
- **Problema:** A necessidade de métodos eficientes e econômicos para capturar CO2 diretamente da atmosfera, um passo crucial para mitigar as mudanças climáticas.
- **Solução:** O dispositivo utiliza uma membrana com sorvente sólido para absorver o CO2 do ar, seguido por um processo de regeneração através de aquecimento para liberar o CO2 concentrado. A patente foca na integração de componentes para otimizar a captura e regeneração.
- **Maturidade:** Inicial

**Achados-chave:**
- O dispositivo incorpora uma membrana permeável com um sorvente sólido para capturar CO2 da atmosfera.
- Um processo de regeneração é utilizado para liberar o CO2 concentrado, envolvendo aquecimento da câmara de regeneração.

**Vantagens alegadas:**
- Eficiência na captura de CO2 diretamente do ar.
- Custo reduzido no processo de captura.

**Limitações:**
- A patente não detalha especificamente a composição do sorvente sólido ou as condições operacionais otimizadas para o processo de regeneração.
- O impacto da escala e da integração com outras tecnologias de armazenamento ainda não é abordado.

**Aplicações potenciais:**
- Redução de emissões de gases de efeito estufa em fontes industriais.
- Captura direta de CO2 para uso em processos químicos ou armazenamento geológico.

**Evidências citadas:**
> The device comprises (a) a membrane at least partly permeable for air comprising a solid state CO2 sorbent;
> The device according to the invention provides an efficient and low-cost solution for capturing CO2 directly from air.

---

### 3. Direct air capture reactor systems and related methods of transporting carbon dioxide

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_bad1378c89ef` |
| **Family ID** | `family:4c59dcf7ccee98a5050ed42358c17ffa2281af1a` |
| **ID** | `US20240252980A1` |
| **Inventores** | Dong Ding, Lucun WANG, Wei Wu |
| **Titular** | Battelle Energy Alliance LLC |
| **Data** | 2024-08-01 |
| **Fonte** | Google Patents |
| **URL** | [US20240252980A1](https://patents.google.com/patent/US20240252980A1/en) |
| **Triagem** | include |
| **Rota** | deep_extraction |
| **Motivo da rota** | Há evidência suficiente para extração detalhada. |
| **Score de Triagem** | 9.2/10 |
| **Score de Relevância** | 8.0/10 |
| **Nível de Inovação** | Significativa |
| **Domínio Técnico** | Eletroquímica, Captura de Carbono, DAC (Direct Air Capture) |
| **Cluster Temático** | Eletroquímica, Captura de Carbono, DAC (Direct Air Capture) |
| **Papel do CO2** | capture_process_stream |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | dedicated_storage_system |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | electrical |
| **Foco das Claims** | system_architecture |
| **Categoria de Exclusão** | N/A |
| **Confiança** | 0.95 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> AbstractA direct air capture (DAC) reactor system is disclosed and comprises electrochemical cells. One or more of the electrochemical cells comprises a cathode, an anode, and an electrolyte membrane between the cathode and the anode. The electrolyte membrane is configured to transport carbonate ions and oxygenate ions from the cathode to the anode. Additional DAC reactor systems and methods of capturing carbon dioxide from a feedstream using the reactor systems are also disclosed.

**Avaliação do LLM:**
Esta patente descreve um sistema de captura direta de ar (DAC) que utiliza células eletroquímicas para capturar dióxido de carbono do ar. O sistema emprega uma membrana iônica para transportar íons carbonato e oxigênio, permitindo a conversão do CO2 em produtos químicos. A tecnologia visa abordar o desafio da captura de CO2 de fontes não concentradas.

**Extração Estruturada:**
- **Problema:** A patente aborda o problema da captura eficiente de dióxido de carbono (CO2) diretamente da atmosfera, onde as concentrações são baixas e dispersas, dificultando a coleta em comparação com fontes industriais.
- **Solução:** A solução proposta é um sistema DAC baseado em células eletroquímicas que utiliza uma membrana iônica para facilitar o transporte de íons e a conversão do CO2 em produtos químicos. O sistema permite a captura contínua de CO2 do ar ambiente.
- **Maturidade:** Inicial

**Achados-chave:**
- O sistema emprega células eletroquímicas com um cátodo, ânodo e uma membrana iônica para transportar íons carbonato e oxigênio.
- A membrana iônica é crucial para o transporte eficiente dos íons, otimizando a captura de CO2.

**Vantagens alegadas:**
- Captura direta de CO2 do ar ambiente.
- Utilização de células eletroquímicas para conversão do CO2.

**Limitações:**
- A patente não detalha a eficiência da captura em diferentes condições ambientais (temperatura, umidade).
- O sistema depende da disponibilidade de energia elétrica para alimentar as células eletroquímicas.

**Aplicações potenciais:**
- Mitigação das mudanças climáticas através da remoção de CO2 da atmosfera.
- Produção de produtos químicos a partir do CO2 capturado.

**Evidências citadas:**
> AbstractA direct air capture (DAC) reactor system is disclosed and comprises electrochemical cells.
> One or more of the electrochemical cells comprises a cathode, an anode, and an electrolyte membrane between the cathode and the anode.

---

### 4. Carbon dioxide purification method

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_d7e147125c55` |
| **Family ID** | `family:c839876d2b43557c6642033bd6ddf08e10fd8535` |
| **ID** | `US20070231244A1` |
| **Inventores** | Minish Shah, Henry Howard |
| **Titular** | Praxair Technology Inc |
| **Data** | 2007-10-04 |
| **Fonte** | Google Patents |
| **URL** | [US20070231244A1](https://patents.google.com/patent/US20070231244A1/en) |
| **Triagem** | review |
| **Rota** | manual_review |
| **Motivo da rota** | Triagem indicou revisão humana. |
| **Score de Triagem** | 7.2/10 |
| **Score de Relevância** | 6.5/10 |
| **Nível de Inovação** | Incremental |
| **Domínio Técnico** | Refrigeração Industrial |
| **Cluster Temático** | Ciclos Termodinâmicos com CO2 para Refrigeração e Purificação |
| **Papel do CO2** | working_fluid |
| **Papel do Armazenamento** | implicit_or_support_storage |
| **Limite Sistêmico** | cycle_or_transfer_subsystem |
| **Tipo de Ciclo** | supercritical_or_transcritical_co2 |
| **Fonte/Sumidouro Térmico** | CO2 vapor/líquido |
| **Foco das Claims** | cycle_integration |
| **Categoria de Exclusão** | cooling_only |
| **Confiança** | 0.80 |
| **Rerank Aplicado** | Sim |
| **Motivo do Rerank** | reranked:decision_confirmed |
| **Revisão Manual** | Sim |
| **Erro LLM** | N/A |

**Abstract:**
> AbstractMethod of purifying a feed stream containing carbon dioxide wherein the feed stream after having been compressed and dried is partly cooled and then used to reboil a stripping column. Thereafter, the feed stream is further cooled and expanded to a lower operational temperature of the stripping column. A carbon dioxide product stream composed of the liquid column bottoms of the stripping column is expanded at one or more pressures to generate refrigeration, then fully vaporized within the main heat exchanger and compressed by a compressor to produce a compressed carbon dioxide product. Refrigeration is recovered in the main heat exchanger from a column overhead stream extracted from the stripping column within the main heat exchanger either directly or indirectly by auxiliary processing in which carbon dioxide is further separated and optionally recycled back to the main compressor used in compressing the feed stream.

**Avaliação do LLM:**
Esta patente descreve um método de purificação de CO2 que utiliza um ciclo termodinâmico para gerar refrigeração a partir do vaporização e condensação do CO2. O sistema envolve a compressão, resfriamento e expansão do CO2, com recuperação de refrigeração em várias etapas. A patente foca na purificação do CO2 e no uso da refrigeração gerada.

**Extração Estruturada:**
- **Problema:** O problema abordado é a necessidade de um método eficiente para purificar o CO2 e gerar refrigeração simultaneamente, utilizando um ciclo termodinâmico.
- **Solução:** A solução proposta envolve um ciclo termodinâmico que utiliza um stripping column para purificação do CO2, seguido por expansão para geração de refrigeração e compressão para recuperação do produto. A refrigeração é recuperada em várias etapas dentro do ciclo.
- **Maturidade:** Intermediária

**Achados-chave:**
- O método utiliza um stripping column para a purificação do CO2, com o feed stream sendo parcialmente resfriado e usado para reboar a coluna.
- A expansão do produto da coluna de stripping gera refrigeração que é posteriormente recuperada e utilizada no processo de compressão.

**Vantagens alegadas:**
- Geração simultânea de CO2 purificado e refrigeração.
- Recuperação de refrigeração em várias etapas do ciclo termodinâmico.

**Limitações:**
- A patente não detalha a complexidade do ciclo termodinâmico ou a otimização para diferentes condições operacionais.
- O foco principal é na purificação e geração de refrigeração, sem uma análise profunda da integração com outros processos.

**Aplicações potenciais:**
- Sistemas de refrigeração industrial que utilizam CO2 como fluido de trabalho.
- Processos industriais onde a purificação do CO2 e a geração de refrigeração são requisitos simultâneos.

**Evidências citadas:**
> "partly cooled and then used to reboil a stripping column"

---

### 5. System and method for carbon dioxide capture and sequestration

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_1d2f62aad7c7` |
| **Family ID** | `family:247714a45dc0120aa1b837271fa4aee30a08c2c0` |
| **ID** | `US8500855B2` |
| **Inventores** | Peter Eisenberger |
| **Titular** | Individual |
| **Data** | 2013-08-06 |
| **Fonte** | Google Patents |
| **URL** | [US8500855B2](https://patents.google.com/patent/US8500855B2/en) |
| **Triagem** | review |
| **Rota** | manual_review |
| **Motivo da rota** | Triagem indicou revisão humana. |
| **Score de Triagem** | 7.2/10 |
| **Score de Relevância** | 6.5/10 |
| **Nível de Inovação** | Incremental |
| **Domínio Técnico** | Chemical Engineering |
| **Cluster Temático** | Carbon Dioxide Capture and Sequestration Technologies |
| **Papel do CO2** | capture_process_stream |
| **Papel do Armazenamento** | implicit_or_support_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | não_claro |
| **Fonte/Sumidouro Térmico** | calor co-gerado, vapor saturado |
| **Foco das Claims** | system_architecture |
| **Categoria de Exclusão** | industrial_heat_adjacent |
| **Confiança** | 0.80 |
| **Rerank Aplicado** | Sim |
| **Motivo do Rerank** | reranked:decision_confirmed |
| **Revisão Manual** | Sim |
| **Erro LLM** | N/A |

**Abstract:**
> AbstractA method and a system to remove relatively pure carbon dioxide directly from ambient air. The method comprises generating process heat, to co-generate substantially saturated steam; alternately and repeatedly exposing a sorbent to a flow of ambient air, at substantially ambient conditions, to sorb, and therefore remove, carbon dioxide from said ambient air, and exposing the CO2-laden sorbent to a flow of the co-generated steam, at a temperature in the range of not greater than about 130Â° C, to release the carbon dioxide, thereby regenerating the sorbent, and capturing relatively pure carbon dioxide. To render this process more efficient, admix with the air a minor amount of a pre-treated effluent gas containing a higher concentration of carbon dioxide than in the atmosphere. The captured carbon dioxide can be stored for further use, or sequestered permanently. The purified carbon dioxide is useful for agriculture or chemical processes.

**Avaliação do LLM:**
Esta patente descreve um sistema para capturar CO2 diretamente do ar, utilizando calor gerado para co-gerar vapor saturado e um material absorvente. O processo envolve a exposição do ar à sorbente, seguida pela regeneração com vapor aquecido. A patente foca na captura e armazenamento de CO2.

**Extração Estruturada:**
- **Problema:** A necessidade de capturar CO2 de fontes atmosféricas para armazenamento ou utilização em processos.
- **Solução:** A solução proposta é um sistema que utiliza calor co-gerado para aquecer uma sorbente, permitindo a remoção e posterior liberação do CO2 da corrente de ar ambiente. O vapor gerado auxilia na regeneração da sorbente.
- **Maturidade:** Intermediária

**Achados-chave:**
- Utilização de calor co-gerado para otimizar o processo de captura de CO2.
- A temperatura máxima de operação do vapor é limitada a 130°C.
- Admissão de um gás residual pré-tratado com maior concentração de CO2 para aumentar a eficiência da captura.

**Vantagens alegadas:**
- Captura de CO2 relativamente puro diretamente do ar.
- Utilização eficiente de calor co-gerado.
- Possibilidade de armazenamento ou utilização do CO2 capturado.

**Limitações:**
- A temperatura máxima de 130°C pode limitar a eficiência da regeneração da sorbente em algumas condições.
- Dependência da geração de calor co-gerado, que pode ser um fator limitante em certos cenários.

**Aplicações potenciais:**
- Agricultura (utilização do CO2 capturado como fertilizante)
- Processos químicos (utilização do CO2 capturado como matéria-prima)

**Evidências citadas:**
> 'The captured carbon dioxide can be stored for further use, or sequestered permanently.'
> ‘alternately and repeatedly exposing a sorbent to a flow of ambient air’

---

### 6. Sequestration of carbon dioxide

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_654cb5b98f3f` |
| **Family ID** | `family:d8d73f30d3b0b6095a48f49ad10e337bea609922` |
| **ID** | `US7132090B2` |
| **Inventores** | Daniel Dziedzic, Kenneth B Gross, Robert A Gorski, John T Johnson |
| **Titular** | General Motors Corp |
| **Data** | 2006-11-07 |
| **Fonte** | Google Patents |
| **URL** | [US7132090B2](https://patents.google.com/patent/US7132090B2/en) |
| **Triagem** | include |
| **Rota** | deep_extraction |
| **Motivo da rota** | Há evidência suficiente para extração detalhada. |
| **Score de Triagem** | 9.2/10 |
| **Score de Relevância** | 8.4/10 |
| **Nível de Inovação** | Incremental |
| **Domínio Técnico** | Engenharia Química / Materiais |
| **Cluster Temático** | Engenharia Química / Materiais |
| **Papel do CO2** | capture_process_stream |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | dedicated_storage_system |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | não especificado no resumo |
| **Foco das Claims** | system_architecture |
| **Categoria de Exclusão** | N/A |
| **Confiança** | 0.95 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> AbstractA process for selectively removing carbon dioxide from a gaseous stream by converting the carbon dioxide to a solid, stable form is provided. In a sequestration process, carbon dioxide enriched air is passed through a gas diffusion membrane to transfer the carbon dioxide to a fluid medium. The carbon dioxide rich fluid is then passed through a matrix containing a catalyst specific for carbon dioxide, which accelerates the conversion of the carbon dioxide to carbonic acid. In the final step, a mineral ion is added to the reaction so that a precipitate of carbonate salt is formed. This solid mineral precipitate can be safely stored for extended periods of time, such as by burying the precipitate in the ground or depositing the precipitate into storage sites either on land or into a body of water. An apparatus for removing carbon dioxide from a gaseous stream is also provided.

**Avaliação do LLM:**
Esta patente descreve um processo para capturar dióxido de carbono de um fluxo gasoso convertendo-o em um precipitado sólido através da utilização de um catalisador e íons minerais. O sistema envolve a transferência do CO2 para um meio fluido seguido pela formação de um sal de carbonato, que pode ser armazenado de forma segura. A patente foca na conversão e armazenamento do CO2 como um produto sólido.

**Extração Estruturada:**
- **Problema:** O problema abordado é a remoção eficiente e o armazenamento seguro de dióxido de carbono (CO2) de fluxos gasosos, buscando uma alternativa ao armazenamento térmico tradicional.
- **Solução:** A solução proposta envolve a conversão do CO2 em um precipitado sólido através da reação catalítica com íons minerais, permitindo o armazenamento a longo prazo do CO2 como um sal de carbonato.
- **Maturidade:** Inicial

**Achados-chave:**
- O processo utiliza um gas diffusion membrane para transferir o CO2 para um meio fluido.
- A adição de íons minerais acelera a conversão do CO2 em carbonic acid, levando à formação de um precipitado de carbonato.

**Vantagens alegadas:**
- Armazenamento seguro e de longo prazo do CO2 como um sal de carbonato.
- Processo seletivo para remoção de CO2 de fluxos gasosos.

**Limitações:**
- A patente não detalha a eficiência do catalisador ou a otimização das condições de reação.
- O método de armazenamento proposto (entulho ou corpos d'água) pode ter implicações ambientais que precisam ser consideradas.

**Aplicações potenciais:**
- Redução de emissões de gases de efeito estufa em processos industriais.
- Captura e sequestro de carbono em escala industrial.

**Evidências citadas:**
> AbstractA process for selectively removing carbon dioxide from a gaseous stream by converting the carbon dioxide to a solid, stable form…

---

### 7. System and method for direct air capture of carbon dioxide utilizing a microwave desorption technique

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_034c1bffb6ea` |
| **Family ID** | `family:8a1e28dde14e4a55d28aed40bb6c63bef7dc9488` |
| **ID** | `US20230302393A1` |
| **Inventores** | Xiwang Qi |
| **Titular** | Individual |
| **Data** | 2023-09-28 |
| **Fonte** | Google Patents |
| **URL** | [US20230302393A1](https://patents.google.com/patent/US20230302393A1/en) |
| **Triagem** | include |
| **Rota** | deep_extraction |
| **Motivo da rota** | Há evidência suficiente para extração detalhada. |
| **Score de Triagem** | 9.2/10 |
| **Score de Relevância** | 8.1/10 |
| **Nível de Inovação** | Incremental |
| **Domínio Técnico** | Engenharia Química, Engenharia Ambiental |
| **Cluster Temático** | Engenharia Química, Engenharia Ambiental |
| **Papel do CO2** | capture_process_stream |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | dedicated_storage_system |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | general_thermal_management |
| **Foco das Claims** | system_architecture |
| **Categoria de Exclusão** | N/A |
| **Confiança** | 0.95 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> AbstractA direct air capture of CO2 system and method including a chamber defining a microwave cavity, a microwave heating unit coupled to the chamber in electromagnetic communication, and a sorbent structure carried within the chamber. The sorbent structure includes one or more porous support structures each having a plurality of pores and channels formed therethrough providing a large area of surfaces coated by nanoparticles of CO2 adsorbent material. A motor fan creates an air flow through the chamber and the sorbent structure carried therein. CO2 in the air is adsorbed by the CO2 adsorbent material. The microwave heating unit heats the CO2 adsorbent material to desorb the CO2 for further sequestration or value-added utilization.

**Avaliação do LLM:**
Esta patente descreve um sistema para captura direta de CO2 da atmosfera que utiliza aquecimento por micro-ondas e uma estrutura de sorbimento. O sistema incorpora um cavidade de micro-ondas para aquecer o adsorvente de CO2, promovendo a desorção do gás. A patente foca na eficiência da captura e sequestro do CO2.

**Extração Estruturada:**
- **Problema:** A necessidade de métodos eficientes para capturar CO2 diretamente da atmosfera, especialmente em aplicações de baixo nível de concentração.
- **Solução:** A solução proposta é um sistema que utiliza aquecimento por micro-ondas para ativar um adsorvente de CO2, permitindo a desorção e posterior sequestro ou utilização do CO2.
- **Maturidade:** Inicial

**Achados-chave:**
- Utilização de aquecimento por micro-ondas para promover a desorção do CO2 do adsorvente.
- Incorporação de uma estrutura de sorbimento com alta área superficial e nanopartículas de material adsorvente de CO2.
- Um fluxo de ar criado por um ventilador impulsiona o ar através da estrutura de sorbimento, maximizando a captura de CO2.

**Vantagens alegadas:**
- Eficiência na captura de CO2 da atmosfera
- Utilização de aquecimento por micro-ondas para otimizar a desorção do CO2
- Potencial para valorização do CO2 capturado

**Limitações:**
- A patente não especifica detalhes sobre a eficiência energética do processo de aquecimento por micro-ondas.
- O sistema depende da disponibilidade de energia elétrica para o funcionamento do aquecedor.

**Aplicações potenciais:**
- Captura direta de CO2 em fontes point source (e.g., usinas de energia)
- Remediação de ar atmosférico
- Produção de combustíveis sintéticos a partir de CO2 capturado

**Evidências citadas:**
> A direct air capture of CO2 system and method including a chamber defining a microwave cavity...
> The sorbent structure includes one or more porous support structures each having a plurality of pores and channels formed therethrough providing a large area of surfaces coated by nanoparticles of CO2 adsorbent material.

---

### 8. Capture and release of carbon dioxide using electrogenerated acids and bases

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_42a3a58fa795` |
| **Family ID** | `family:65f05e58692d724dbc3cdc7c4eac16fbfed6302c` |
| **ID** | `WO2025230882A1` |
| **Inventores** | Ian Robinson, David KOSHY, Sahag Voskian, Kyle Weldon SELF |
| **Titular** | Eleryc Inc |
| **Data** | 2025-11-06 |
| **Fonte** | Google Patents |
| **URL** | [WO2025230882A1](https://patents.google.com/patent/WO2025230882A1/en) |
| **Triagem** | review |
| **Rota** | manual_review |
| **Motivo da rota** | Triagem indicou revisão humana. |
| **Score de Triagem** | 7.2/10 |
| **Score de Relevância** | 6.5/10 |
| **Nível de Inovação** | Incremental |
| **Domínio Técnico** | Electrochemistry, Chemical Engineering |
| **Cluster Temático** | CO2 Capture and Release Technologies – Electrochemical Approaches |
| **Papel do CO2** | capture_process_stream |
| **Papel do Armazenamento** | implicit_or_support_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | não especificado no abstract |
| **Foco das Claims** | process_integration |
| **Categoria de Exclusão** | industrial_heat_adjacent |
| **Confiança** | 0.80 |
| **Rerank Aplicado** | Sim |
| **Motivo do Rerank** | reranked:decision_confirmed |
| **Revisão Manual** | Sim |
| **Erro LLM** | N/A |

**Abstract:**
> AbstractSystems and methods for capturing and releasing carbon dioxide at least in part via the electrochemical production of acids and/or bases are generally described. An aqueous input stream that includes a dissolved salt such as sodium chloride may be input into an electrolysis assembly to produce acidic and/or basic species. The basic species may promote capture of carbon dioxide (e.g., via direct air capture or from a point source). The acidic species may promote subsequent release of the carbon dioxide to form a carbon dioxide-rich stream. In some instances, at least some streams are concentrated and/or recycled, thereby improving overall system performance and/or efficiency.

**Avaliação do LLM:**
Esta patente descreve um sistema para captura e liberação de CO2 utilizando a produção eletroquímica de ácidos e bases. O processo envolve a eletrólise de uma solução salina para gerar espécies ácidas e básicas que promovem o sequestro e a posterior liberação do CO2, respectivamente. A patente foca na integração de processos com ciclos de concentração e reciclagem.

**Extração Estruturada:**
- **Problema:** Capturar e liberar CO2 de forma eficiente, especialmente em aplicações como captura direta do ar ou de fontes pontuais, requer sistemas que possam controlar tanto a absorção quanto a liberação do gás.
- **Solução:** A patente propõe um sistema eletroquímico que utiliza a produção in situ de ácidos e bases para facilitar o ciclo de captura e liberação de CO2. A base promove a captura, enquanto o ácido facilita a liberação, com potencial para concentração e reciclagem dos fluxos.
- **Maturidade:** Inicial

**Achados-chave:**
- O sistema emprega eletrólise para gerar ácidos e bases a partir de uma solução salina (ex: NaCl).
- As espécies básicas são utilizadas para promover a captura do CO2, enquanto as ácidas facilitam sua liberação.

**Vantagens alegadas:**
- Melhora no desempenho e eficiência do sistema através da concentração e reciclagem de fluxos.
- Utilização de processos eletroquímicos para uma abordagem potencialmente mais sustentável em comparação com métodos tradicionais.

**Limitações:**
- A patente não detalha a escala ou o tipo específico de eletrólise utilizado.
- A eficiência da captura e liberação do CO2 pode depender das condições operacionais (ex: concentração, temperatura) e da composição da solução salina.

**Aplicações potenciais:**
- Captura direta do ar (DAC)
- Captura de CO2 de fontes industriais pontuais
- Processos químicos que requerem um fluxo de CO2 purificado

**Evidências citadas:**
> ‘An aqueous input stream that includes a dissolved salt such as sodium chloride may be input into an electrolysis assembly’
> ‘The basic species may promote capture of carbon dioxide (e.g., via direct air capture or from a point source)’

---

### 9. Carbon dioxide capture

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

### 10. Plant and method for capturing carbon dioxide

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

### 11. APPARATUS FOR SUPPLYING LIQUID
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
| **URL** | [1429678](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135599119&_cid=P22-MQPEQU-91691-1) |
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

### 12. Dispensing Device

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
| **URL** | [1171698](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135354895&_cid=P22-MQPEQU-91691-1) |
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

### 13. METHOD AND APPARATUS FOR REPARING EXTRACTS OF HOPS AND OTHER MATERIALS

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
| **URL** | [1557123](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135726881&_cid=P22-MQPEQU-91691-1) |
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

### 14. Reclamation of foundry sand

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
| **URL** | [2047588](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135860928&_cid=P22-MQPEQU-91691-1) |
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

### 15. WEIGHING MACHINES

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
| **URL** | [1426573](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135595668&_cid=P22-MQPEQU-91691-1) |
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

### 16. A Dispensing Device for Gases Under Pressure.

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
| **URL** | [1174314](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135357801&_cid=P22-MQPEQU-91691-1) |
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

### 17. LIQUID MOVING SYSTEMS

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
| **URL** | [1253973](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135438798&_cid=P22-MQPEQU-91691-1) |
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

### 18. TEMPORARY FREEZING OF SOFT OR FLEXIBLE ARTICLES

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
| **URL** | [1329637](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135513929&_cid=P22-MQPEQU-91691-1) |
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

### 19. Production of
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
| **URL** | [1125505](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135308953&_cid=P22-MQPEQU-91691-1) |
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

### 20. IMPROVEMENTS IN OR RELATING TO FIRE EXTINGUISHING COMPOSITIONS

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
| **URL** | [1236064](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135420945&_cid=P22-MQPEQU-91691-1) |
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
- rec_42a3a58fa795 (WO2025230882A1) | rota=manual_review | motivo=Triagem indicou revisão humana. | erro_llm=N/A
- rec_bb7ef455d20e (US8119091B2) | rota=manual_review | motivo=Triagem indicou revisão humana. | erro_llm=N/A
- rec_d7e147125c55 (US20070231244A1) | rota=manual_review | motivo=Triagem indicou revisão humana. | erro_llm=N/A
- rec_a058d6ba7b0a (1125505) | rota=manual_review | motivo=Triagem indicou revisão humana. | erro_llm=N/A
- rec_1d2f62aad7c7 (US8500855B2) | rota=manual_review | motivo=Triagem indicou revisão humana. | erro_llm=N/A
- rec_ca73a4e50a56 (2047588) | rota=manual_review | motivo=Triagem indicou revisão humana. | erro_llm=N/A

---

## 🔬 Análise Comparativa

### 1. Panorama Geral

- O conjunto comparativo agrega 13 patente(s) e nao deve ser tratado como bloco homogeneo: ha um nucleo direto, fronteiras tecnicas em revisao e adjacencias uteis apenas para delimitar whitespace [IDs: US7132090B2, US12391556B1, US20220072471A1, US20230302393A1, US20240252980A1, WO2024208966A1, 1125505, 1429678, 2047588, US20070231244A1, US8119091B2, US8500855B2, WO2025230882A1]
- O subgrupo mais diretamente alinhado ao núcleo da query é US7132090B2, com foco em armazenamento de CO2, compressão/expansão e controle termodinâmico do meio armazenado [IDs: US7132090B2]
- 1125505, 1429678, 2047588, US20070231244A1, US8119091B2, US8500855B2, WO2025230882A1 formam a fronteira tecnica: sao casos proximos do problema, mas ainda ambiguos quanto ao papel exato do CO2 no armazenamento ou na funcao arquitetural central [IDs: 1125505, 1429678, 2047588, US20070231244A1, US8119091B2, US8500855B2, WO2025230882A1]
- 1125505, US20070231244A1 entram como adjacencia exploratoria: tratam CO2 principalmente como fluido de trabalho em transferencia termica ou distribuicao de energia, de modo que ajudam a delimitar combinacoes pouco cobertas sem virar evidencia de cobertura consolidada [IDs: 1125505, US20070231244A1]

##

### 3. Whitespaces e Oportunidades

- O whitespace mais promissor esta na combinacao entre arquiteturas de ciclo/transferencia termica com CO2 e armazenamento explicito do inventario termico, porque esses elementos ainda aparecem fragmentados entre nucleo, fronteira e adjacencia [IDs: US7132090B2, US12391556B1, US20220072471A1, US20230302393A1]
- Gestao termica transiente, subresfriamento e acoplamentos com captura/reatores aparecem de forma lateral; isso sugere oportunidade em claims de controle, operacao multi-regime e integracao de processo ainda pouco amarradas ao armazenamento central [IDs: 1125505, US20070231244A1, US12391556B1, US20220072471A1]
- As patentes em review delimitam fronteiras tecnicas onde o papel do CO2 ainda esta ambiguo entre meio armazenado, fluido de trabalho e interface de troca termica; esse tipo de ambiguidade costuma ser um bom proxy para whitespace exploravel com recorte arquitetural mais especifico [IDs: 1125505, 1429678, 2047588, US20070231244A1]

### 4. Recomendações

- Priorizar arquiteturas centradas em armazenamento explícito de CO2 e controle termodinâmico rigoroso [IDs: US7132090B2]

### 5. Ranking Final

1. **US7132090B2** — armazenamento termico explicito como parte central; score 8.4/10 [IDs: US7132090B2]
2. **US12391556B1** — armazenamento termico explicito como parte central; score 8.1/10 [IDs: US12391556B1]
3. **US20220072471A1** — armazenamento termico explicito como parte central; score 8.1/10 [IDs: US20220072471A1]
4. **US20230302393A1** — armazenamento termico explicito como parte central; score 8.1/10 [IDs: US20230302393A1]
5. **US20240252980A1** — armazenamento termico explicito como parte central; score 8.0/10 [IDs: US20240252980A1]
6. **WO2024208966A1** — armazenamento termico explicito como parte central; score 7.7/10 [IDs: WO2024208966A1]
7. **1125505** — armazenamento termico explicito como parte central; ênfase em refrigeração/sub-resfriamento, mais adjacente ao núcleo da query; score 6.5/10 [IDs: 1125505]
8. **1429678** — CO2 aparece principalmente como fluido de trabalho; armazenamento termico explicito como parte central; score 6.5/10 [IDs: 1429678]
9. **2047588** — armazenamento termico explicito como parte central; score 6.5/10 [IDs: 2047588]
10. **US20070231244A1** — CO2 aparece principalmente como fluido de trabalho; armazenamento aparece mais como subsistema de apoio; score 6.5/10 [IDs: US20070231244A1]
11. **US8119091B2** — armazenamento aparece mais como subsistema de apoio; score 6.5/10 [IDs: US8119091B2]
12. **US8500855B2** — armazenamento aparece mais como subsistema de apoio; score 6.5/10 [IDs: US8500855B2]
13. **WO2025230882A1** — armazenamento aparece mais como subsistema de apoio; score 6.5/10 [IDs: WO2025230882A1]

### 6. Mapa de Evidências por ID

- **CO2 Capture and Release Technologies – Electrochemical Approaches** [IDs: WO2025230882A1]
- **CO2 Capture and Utilization - Aqueous Solutions** [IDs: US8119091B2]
- **Carbon Dioxide Capture and Sequestration Technologies** [IDs: US8500855B2]
- **Ciclos Termodinâmicos com CO2 para Refrigeração e Purificação** [IDs: US20070231244A1]
- **Economic Optimization** [IDs: US20220072471A1]
- **Eletroquímica, Captura de Carbono, DAC (Direct Air Capture)** [IDs: US20240252980A1]
- **Engenharia Química / Engenharia Ambiental** [IDs: WO2024208966A1]
- **Engenharia Química / Materiais** [IDs: US7132090B2]
- **Engenharia Química, Engenharia Ambiental** [IDs: US20230302393A1]
- **Química, Engenharia Química, Materiais** [IDs: US12391556B1]
- **Reciclagem de Materiais para Fundição com Utilização de CO2** [IDs: 2047588]
- **Separação de Gases, Combustão** [IDs: 1125505]
- **Sistemas de Controle Automatizado para Manipulação de Fluidos Refrigerados** [IDs: 1429678]

### 7. Ranking por ID

1. **US7132090B2** — score 8.4/10 [IDs: US7132090B2]
2. **US12391556B1** — score 8.1/10 [IDs: US12391556B1]
3. **US20220072471A1** — score 8.1/10 [IDs: US20220072471A1]
4. **US20230302393A1** — score 8.1/10 [IDs: US20230302393A1]
5. **US20240252980A1** — score 8.0/10 [IDs: US20240252980A1]
6. **WO2024208966A1** — score 7.7/10 [IDs: WO2024208966A1]
7. **1125505** — score 6.5/10 [IDs: 1125505]
8. **1429678** — score 6.5/10 [IDs: 1429678]
9. **2047588** — score 6.5/10 [IDs: 2047588]
10. **US20070231244A1** — score 6.5/10 [IDs: US20070231244A1]
11. **US8119091B2** — score 6.5/10 [IDs: US8119091B2]
12. **US8500855B2** — score 6.5/10 [IDs: US8500855B2]
13. **WO2025230882A1** — score 6.5/10 [IDs: WO2025230882A1]

---

## 🧭 Matriz de Whitespaces

- **Patentes selecionadas:** 13
- **Núcleo:** 6
- **Fronteira:** 7
- **Adjacência:** 0

- **hybrid_cycle_storage_architecture**: Combinar ciclos/transferencia com CO2 e armazenamento termico explicitamente reivindicado ainda aparece fragmentado entre nucleo e borda tecnica. [core=US7132090B2, US12391556B1, US20220072471A1 | frontier=1125505, 1429678, 2047588 | adjacent=N/A]
- **control_and_operability_claims**: Ha espaco para claims de controle, operacao transiente e integracao de processo onde o papel do CO2 e do armazenamento ainda esta ambiguo. [core=US7132090B2, US12391556B1, US20220072471A1 | frontier=1429678 | adjacent=N/A]

---

## ℹ️ Informações do Sistema

- **Gerado por:** Agente de Web Scraping de Patentes
- **Modelo LLM:** gemma3:4b
- **Data de geração:** 22/06/2026 16:36:39
- **Query de busca:** `carbon dioxide`
- **Status da execução:** completed
- **Tempo total:** 1865.2s
- **LLM disponível:** sim
- **Fila de revisão manual:** 7 itens
- **Snapshot hash:** `37db1fce7a450ee534df688570bf9fa48a8d869d69d75da2c85fe05193b7b2b7`
- **Features habilitadas:** require_evidence, enable_thematic_clusters, enable_structural_roles, enable_screening_rerank, enable_prisma, enable_snapshot, enable_comparative_analysis, enable_whitespace_analysis, enable_manual_review_queue
- **Features desabilitadas:** nenhum
- **Versão do pipeline:** 1.1
- **Thresholds snapshot:** include=0.0, review=0.0
- **Cache LLM:** 0 hits, 41 misses, 41 entradas
- **Status do rascunho:** ready