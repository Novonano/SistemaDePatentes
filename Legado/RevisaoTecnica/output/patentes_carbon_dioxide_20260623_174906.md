# 📋 Relatório de Análise de Patentes

**Data:** 23/06/2026 17:49:06
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
- **Incluídas:** 10
- **Em revisão manual:** 3
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
- **Triagem:** 20 triado(s), 10 incluído(s), 3 em revisão, 7 excluído(s)
- **Elegibilidade:** 13 extração(ões) completa(s), 3 revisão(ões) manual(is), 0 adiada(s)
- **Cobertura:** 1 sem abstract/snippet, 0 sem ID
- **Síntese:** 13 registro(s) analisado(s)

## 🧩 Síntese Temática

### Engenharia Química / Materiais

- **Patentes:** 1
- **Score médio:** 8.20/10
- **Confiança média:** 0.90
- **Evidências citadas:** 2
- **IDs:** US12202743B2

### Química, Engenharia Química, Materiais

- **Patentes:** 1
- **Score médio:** 8.10/10
- **Confiança média:** 0.95
- **Evidências citadas:** 2
- **IDs:** US12391556B1

### Engenharia Química / Tecnologias de Captura de Carbono

- **Patentes:** 1
- **Score médio:** 8.10/10
- **Confiança média:** 0.95
- **Evidências citadas:** 2
- **IDs:** WO2021239747A1

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

### Química, Catálise, Engenharia Química

- **Patentes:** 1
- **Score médio:** 8.10/10
- **Confiança média:** 0.95
- **Evidências citadas:** 2
- **IDs:** US20240059978A1

### Química Industrial

- **Patentes:** 1
- **Score médio:** 8.00/10
- **Confiança média:** 0.95
- **Evidências citadas:** 2
- **IDs:** US20240343563A1

### Engenharia Química / Processamento de Gases

- **Patentes:** 1
- **Score médio:** 8.00/10
- **Confiança média:** 0.95
- **Evidências citadas:** 1
- **IDs:** US20230191322A1

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
- **Clusters no contexto:** 10
- **Roteamento agregado:** 3 rota(s)
- **Slots ativos:** N/A

## ⏱️ Métricas por Etapa

| Etapa | Status | Duração | Itens | Detalhes |
|---|---|---:|---:|---|
| setup | ok | 0.97s | 1 | Verificação do modelo Ollama |
| search | ok | 99.93s | 20 | 20 patentes únicas após dedupe |
| screening | ok | 184.77s | 20 | 10 incluídas, 3 revisão |
| comparative_analysis | ok | 52.45s | 20 | Síntese comparativa gerada |
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
- **Latência média:** 0.969s
- **Latência máxima:** 0.969s

### screening

- **Chamadas:** 20
- **Sucessos:** 20
- **Falhas:** 0
- **Retries:** 0
- **Cache hits:** 18
- **Pulos por degradação:** 0
- **Latência média:** 2.999s
- **Latência máxima:** 30.604s

### rerank

- **Chamadas:** 3
- **Sucessos:** 3
- **Falhas:** 0
- **Retries:** 0
- **Cache hits:** 3
- **Pulos por degradação:** 0
- **Latência média:** 0.0s
- **Latência máxima:** 0.0s

### evaluation

- **Chamadas:** 13
- **Sucessos:** 13
- **Falhas:** 0
- **Retries:** 0
- **Cache hits:** 11
- **Pulos por degradação:** 0
- **Latência média:** 9.598s
- **Latência máxima:** 63.756s

### comparative

- **Chamadas:** 1
- **Sucessos:** 1
- **Falhas:** 0
- **Retries:** 0
- **Cache hits:** 0
- **Pulos por degradação:** 0
- **Latência média:** 52.442s
- **Latência máxima:** 52.442s

## 🔎 Observabilidade Estruturada

### Rotas

- **deep_extraction**: total=10, include=10, review=0, exclude=0, llm_errors=0
- **screen_only**: total=7, include=0, review=0, exclude=7, llm_errors=0
- **manual_review**: total=3, include=0, review=3, exclude=0, llm_errors=0

### Fontes

- **EPO**: bruto=0, duração=0.00s, diagnósticos=config_missing=1
- **GooglePatents**: bruto=10, duração=31.42s, diagnósticos=nenhum
- **Patentscope**: bruto=10, duração=68.50s, diagnósticos=nenhum

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
| 2 | [US12391556B1](https://patents.google.com/patent/US12391556B1/en) — Carbon dioxide capture using activated carbon derived from s... | 🟢 8.1 (include) | Incremental | Química, Engenharia Química, Materiais |
| 3 | [WO2021239747A1](https://patents.google.com/patent/WO2021239747A1/en) — Method for capture of carbon dioxide from ambient air and co... | 🟢 8.1 (include) | Significativa | Engenharia Química / Tecnologias de Captura de Carbono |
| 4 | [US20220072471A1](https://patents.google.com/patent/US20220072471A1/en) — Direct carbon dioxide capture from air | 🟢 8.1 (include) | Incremental | Engenharia Química / Engenharia Ambiental |
| 5 | [US20230302393A1](https://patents.google.com/patent/US20230302393A1/en) — System and method for direct air capture of carbon dioxide u... | 🟢 8.1 (include) | Incremental | Engenharia Química, Engenharia Ambiental |
| 6 | [US20240059978A1](https://patents.google.com/patent/US20240059978A1/en) — One-step process for the production of hydrocarbons from car... | 🟢 8.1 (include) | Significativa | Química, Catálise, Engenharia Química |
| 7 | [US20240343563A1](https://patents.google.com/patent/US20240343563A1/en) — Methods of Utilizing Captured Carbon Dioxide to Generate Hyd... | 🟢 8.0 (include) | Incremental | Química Industrial |
| 8 | [US20230191322A1](https://patents.google.com/patent/US20230191322A1/en) — Systems and methods for direct air carbon dioxide capture | 🟢 8.0 (include) | Significativa | Engenharia Química / Processamento de Gases |
| 9 | [US20240252980A1](https://patents.google.com/patent/US20240252980A1/en) — Direct air capture reactor systems and related methods of tr... | 🟢 8.0 (include) | Significativa | Eletroquímica, Captura de Carbono, DAC (Direct Air Capture) |
| 10 | [WO2024208966A1](https://patents.google.com/patent/WO2024208966A1/en) — Plant and method for capturing carbon dioxide | 🟢 7.7 (include) | Significativa | Engenharia Química / Engenharia Ambiental |
| 11 | [1429678](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135599119&_cid=P12-MQQXOI-01618-1) — APPARATUS FOR SUPPLYING LIQUID
CARBON
DIOXIDE | 🟡 6.5 (review) | Significativa | Controle de Processos, Termodinâmica, Sistemas de Refrigeração |
| 12 | [2047588](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135860928&_cid=P12-MQQXOI-01618-1) — Reclamation of foundry sand | 🟡 6.5 (review) | Incremental | Materiais de Fundição e Processos Recuperativos |
| 13 | [1125505](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135308953&_cid=P12-MQQXOI-01618-1) — Production of
carbon
dioxide
and argon | 🟡 6.5 (review) | Incremental | Chemical Engineering |
| 14 | [1171698](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135354895&_cid=P12-MQQXOI-01618-1) — Dispensing Device | 🔴 0.0 (exclude) | N/A | Dispositivos de Dispensação de Líquidos |
| 15 | [1557123](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135726881&_cid=P12-MQQXOI-01618-1) — METHOD AND APPARATUS FOR REPARING EXTRACTS OF HOPS AND OTHER... | 🔴 0.0 (exclude) | N/A | Processamento de bebidas alcoólicas |
| 16 | [1174314](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135357801&_cid=P12-MQQXOI-01618-1) — A Dispensing Device for Gases Under Pressure. | 🔴 0.0 (exclude) | N/A | Engenharia de Fluidos, Instrumentação |
| 17 | [1426573](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135595668&_cid=P12-MQQXOI-01618-1) — WEIGHING MACHINES | 🔴 0.0 (exclude) | N/A | Engenharia de Processos |
| 18 | [1253973](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135438798&_cid=P12-MQQXOI-01618-1) — LIQUID MOVING SYSTEMS | 🔴 0.0 (exclude) | N/A | Process Control & Instrumentation |
| 19 | [1329637](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135513929&_cid=P12-MQQXOI-01618-1) — TEMPORARY FREEZING OF SOFT OR FLEXIBLE ARTICLES | 🔴 0.0 (exclude) | N/A | Engenharia de Materiais, Refrigeração |
| 20 | [1236064](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135420945&_cid=P12-MQQXOI-01618-1) — IMPROVEMENTS IN OR RELATING TO FIRE EXTINGUISHING COMPOSITIO... | 🔴 0.0 (exclude) | N/A | Extinção de Incêndio |

---

## 🔍 Análise Detalhada das Patentes

### 1. Direct removal of carbon dioxide from oceanwater based on a composite membrane

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

### 2. Methods of Utilizing Captured Carbon Dioxide to Generate Hydrogen for Powering Oilfield Equipment

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_3c4b6de26011` |
| **Family ID** | `family:4ee4b376bd6ade85c71d439749b66ddedc85cee1` |
| **ID** | `US20240343563A1` |
| **Inventores** | Philip D. Nguyen, Ronald Glen Dusterhoft, Stanley Vernon Stephenson, I Wayan Rakananda Saputra |
| **Titular** | Halliburton Energy Services Inc |
| **Data** | 2024-10-17 |
| **Fonte** | Google Patents |
| **URL** | [US20240343563A1](https://patents.google.com/patent/US20240343563A1/en) |
| **Triagem** | include |
| **Rota** | deep_extraction |
| **Motivo da rota** | Há evidência suficiente para extração detalhada. |
| **Score de Triagem** | 9.2/10 |
| **Score de Relevância** | 8.0/10 |
| **Nível de Inovação** | Incremental |
| **Domínio Técnico** | Química Industrial |
| **Cluster Temático** | Química Industrial |
| **Papel do CO2** | capture_process_stream |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | power_or_work_cycle |
| **Fonte/Sumidouro Térmico** | CO2 (entrada), Hidrogênio (saída) |
| **Foco das Claims** | process_integration |
| **Categoria de Exclusão** | N/A |
| **Confiança** | 0.95 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> AbstractA system comprising a first reactor, a second reactor fluidly connected with the first reactor, and a liquid-solid separator fluidly connected with the second reactor. The first reactor is operable to produce an aqueous bicarbonate solution from captured carbon dioxide (CO2), and an aqueous alkaline solution. The second reactor is configured to produce hydrogen gas and a mixture comprising metal carbonate agglomerates by contacting the aqueous bicarbonate solution from the first reactor with zero-valent metal particulates. The metal carbonate agglomerates comprise a carbonate of the metal on a surface of the zero-valent metal particulates, and the zero-valent metal particulates comprise a zero-valent metal. The liquid-solid separator is configured to receive the mixture from the second reactor and separate the metal carbonate agglomerates from a recovered aqueous alkaline solution.

**Avaliação do LLM:**
Esta patente descreve um sistema para a geração de hidrogênio utilizando dióxido de carbono (CO2) capturado, empregando reatores e um separador de sólidos. O processo envolve a conversão do CO2 em soluções aquosas e a subsequente produção de hidrogênio através da reação com partículas de metal zero-valent. A patente foca na integração de processos para aplicações em equipamentos de poços de petróleo.

**Extração Estruturada:**
- **Problema:** A necessidade de métodos eficientes para utilizar dióxido de carbono capturado, transformando-o em produtos de valor agregado como hidrogênio.
- **Solução:** A solução proposta consiste em um sistema que utiliza reatores para produzir soluções aquosas a partir do CO2 e um segundo reator para gerar hidrogênio através da reação com partículas de metal zero-valent, seguido por separação dos sólidos.
- **Maturidade:** Inicial

**Achados-chave:**
- O sistema utiliza um primeiro reator para produzir uma solução aquosa de bicarbonato e uma solução alcalina a partir do CO2 capturado.
- A conversão do CO2 em hidrogênio é realizada através da reação com partículas de metal zero-valent, resultando na formação de metal carbonato agglomerados.

**Vantagens alegadas:**
- Geração de hidrogênio a partir de CO2 capturado.
- Integração de processos para otimização do uso de recursos.

**Limitações:**
- A patente não detalha especificamente as condições operacionais dos reatores ou o tipo de metal zero-valent utilizado.
- A eficiência da conversão do CO2 em hidrogênio pode ser influenciada por fatores como a concentração e a temperatura das soluções.

**Aplicações potenciais:**
- Geração de energia em poços de petróleo
- Produção de hidrogênio para aplicações industriais

**Evidências citadas:**
> AbstractA system comprising a first reactor, a second reactor fluidly connected with the first reactor, and a liquid-solid separator fluidly connected with the second reactor.
> The first reactor is operable to produce an aqueous bicarbonate solution from captured carbon dioxide (CO2), and an aqueous alkaline solution.

---

### 3. Carbon dioxide capture using activated carbon derived from spent coffee grounds

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

### 4. Systems and methods for direct air carbon dioxide capture

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

### 6. Direct air capture reactor systems and related methods of transporting carbon dioxide

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

### 7. Direct carbon dioxide capture from air

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

### 8. System and method for direct air capture of carbon dioxide utilizing a microwave desorption technique

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

### 10. One-step process for the production of hydrocarbons from carbon dioxide

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
| **URL** | [1429678](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135599119&_cid=P12-MQQXOI-01618-1) |
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
| **URL** | [1171698](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135354895&_cid=P12-MQQXOI-01618-1) |
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
| **URL** | [1557123](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135726881&_cid=P12-MQQXOI-01618-1) |
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
| **URL** | [2047588](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135860928&_cid=P12-MQQXOI-01618-1) |
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
| **URL** | [1174314](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135357801&_cid=P12-MQQXOI-01618-1) |
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

### 16. WEIGHING MACHINES

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
| **URL** | [1426573](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135595668&_cid=P12-MQQXOI-01618-1) |
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
| **URL** | [1253973](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135438798&_cid=P12-MQQXOI-01618-1) |
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
| **URL** | [1329637](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135513929&_cid=P12-MQQXOI-01618-1) |
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
| **URL** | [1125505](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135308953&_cid=P12-MQQXOI-01618-1) |
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
| **URL** | [1236064](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135420945&_cid=P12-MQQXOI-01618-1) |
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
- rec_a058d6ba7b0a (1125505) | rota=manual_review | motivo=Triagem indicou revisão humana. | erro_llm=N/A
- rec_ca73a4e50a56 (2047588) | rota=manual_review | motivo=Triagem indicou revisão humana. | erro_llm=N/A

---

## 🔬 Análise Comparativa

### 1. Panorama Geral

- O conjunto comparativo agrega 13 patente(s) e nao deve ser tratado como bloco homogeneo: ha um nucleo direto, fronteiras tecnicas em revisao e adjacencias uteis apenas para delimitar whitespace [IDs: US12202743B2, US12391556B1, US20220072471A1, US20230302393A1, US20240059978A1, WO2021239747A1, US20230191322A1, US20240252980A1, US20240343563A1, WO2024208966A1, 1125505, 1429678, 2047588]
- O subgrupo mais diretamente alinhado ao núcleo da query é US12202743B2, com foco em armazenamento de CO2, compressão/expansão e controle termodinâmico do meio armazenado [IDs: US12202743B2]
- 1125505, 1429678, 2047588 formam a fronteira tecnica: sao casos proximos do problema, mas ainda ambiguos quanto ao papel exato do CO2 no armazenamento ou na funcao arquitetural central [IDs: 1125505, 1429678, 2047588]
- 1125505 entram como adjacencia exploratoria: tratam CO2 principalmente como fluido de trabalho em transferencia termica ou distribuicao de energia, de modo que ajudam a delimitar combinacoes pouco cobertas sem virar evidencia de cobertura consolidada [IDs: 1125505]

##

### 3. Whitespaces e Oportunidades

- O whitespace mais promissor esta na combinacao entre arquiteturas de ciclo/transferencia termica com CO2 e armazenamento explicito do inventario termico, porque esses elementos ainda aparecem fragmentados entre nucleo, fronteira e adjacencia [IDs: US12202743B2, US12391556B1, US20220072471A1, US20230302393A1]
- Gestao termica transiente, subresfriamento e acoplamentos com captura/reatores aparecem de forma lateral; isso sugere oportunidade em claims de controle, operacao multi-regime e integracao de processo ainda pouco amarradas ao armazenamento central [IDs: 1125505, US12391556B1, US20220072471A1, US20230302393A1]
- As patentes em review delimitam fronteiras tecnicas onde o papel do CO2 ainda esta ambiguo entre meio armazenado, fluido de trabalho e interface de troca termica; esse tipo de ambiguidade costuma ser um bom proxy para whitespace exploravel com recorte arquitetural mais especifico [IDs: 1125505, 1429678, 2047588, US12202743B2]

### 4. Recomendações

- Priorizar arquiteturas centradas em armazenamento explícito de CO2 e controle termodinâmico rigoroso [IDs: US12202743B2]

### 5. Ranking Final

1. **US12202743B2** — armazenamento termico explicito como parte central; score 8.2/10 [IDs: US12202743B2]
2. **US12391556B1** — armazenamento termico explicito como parte central; score 8.1/10 [IDs: US12391556B1]
3. **US20220072471A1** — armazenamento termico explicito como parte central; score 8.1/10 [IDs: US20220072471A1]
4. **US20230302393A1** — armazenamento termico explicito como parte central; score 8.1/10 [IDs: US20230302393A1]
5. **US20240059978A1** — armazenamento termico explicito como parte central; score 8.1/10 [IDs: US20240059978A1]
6. **WO2021239747A1** — armazenamento termico explicito como parte central; score 8.1/10 [IDs: WO2021239747A1]
7. **US20230191322A1** — armazenamento termico explicito como parte central; score 8.0/10 [IDs: US20230191322A1]
8. **US20240252980A1** — armazenamento termico explicito como parte central; score 8.0/10 [IDs: US20240252980A1]
9. **US20240343563A1** — armazenamento termico explicito como parte central; score 8.0/10 [IDs: US20240343563A1]
10. **WO2024208966A1** — armazenamento termico explicito como parte central; score 7.7/10 [IDs: WO2024208966A1]
11. **1125505** — armazenamento termico explicito como parte central; ênfase em refrigeração/sub-resfriamento, mais adjacente ao núcleo da query; score 6.5/10 [IDs: 1125505]
12. **1429678** — CO2 aparece principalmente como fluido de trabalho; armazenamento termico explicito como parte central; score 6.5/10 [IDs: 1429678]
13. **2047588** — armazenamento termico explicito como parte central; score 6.5/10 [IDs: 2047588]

### 6. Mapa de Evidências por ID

- **Economic Optimization** [IDs: US20220072471A1]
- **Eletroquímica, Captura de Carbono, DAC (Direct Air Capture)** [IDs: US20240252980A1]
- **Engenharia Química / Engenharia Ambiental** [IDs: WO2024208966A1]
- **Engenharia Química / Materiais** [IDs: US12202743B2]
- **Engenharia Química / Processamento de Gases** [IDs: US20230191322A1]
- **Engenharia Química / Tecnologias de Captura de Carbono** [IDs: WO2021239747A1]
- **Engenharia Química, Engenharia Ambiental** [IDs: US20230302393A1]
- **Química Industrial** [IDs: US20240343563A1]
- **Química, Catálise, Engenharia Química** [IDs: US20240059978A1]
- **Química, Engenharia Química, Materiais** [IDs: US12391556B1]
- **Reciclagem de Materiais para Fundição com Utilização de CO2** [IDs: 2047588]
- **Separação de Gases, Combustão** [IDs: 1125505]
- **Sistemas de Controle Automatizado para Manipulação de Fluidos Refrigerados** [IDs: 1429678]

### 7. Ranking por ID

1. **US12202743B2** — score 8.2/10 [IDs: US12202743B2]
2. **US12391556B1** — score 8.1/10 [IDs: US12391556B1]
3. **US20220072471A1** — score 8.1/10 [IDs: US20220072471A1]
4. **US20230302393A1** — score 8.1/10 [IDs: US20230302393A1]
5. **US20240059978A1** — score 8.1/10 [IDs: US20240059978A1]
6. **WO2021239747A1** — score 8.1/10 [IDs: WO2021239747A1]
7. **US20230191322A1** — score 8.0/10 [IDs: US20230191322A1]
8. **US20240252980A1** — score 8.0/10 [IDs: US20240252980A1]
9. **US20240343563A1** — score 8.0/10 [IDs: US20240343563A1]
10. **WO2024208966A1** — score 7.7/10 [IDs: WO2024208966A1]
11. **1125505** — score 6.5/10 [IDs: 1125505]
12. **1429678** — score 6.5/10 [IDs: 1429678]
13. **2047588** — score 6.5/10 [IDs: 2047588]

---

## 🧭 Matriz de Whitespaces

- **Patentes selecionadas:** 13
- **Núcleo:** 10
- **Fronteira:** 3
- **Adjacência:** 0

- **hybrid_cycle_storage_architecture**: Combinar ciclos/transferencia com CO2 e armazenamento termico explicitamente reivindicado ainda aparece fragmentado entre nucleo e borda tecnica. [core=US12202743B2, US12391556B1, US20220072471A1 | frontier=1125505, 1429678, 2047588 | adjacent=N/A]
- **control_and_operability_claims**: Ha espaco para claims de controle, operacao transiente e integracao de processo onde o papel do CO2 e do armazenamento ainda esta ambiguo. [core=US12202743B2, US12391556B1, US20220072471A1 | frontier=1429678 | adjacent=N/A]

---

## ℹ️ Informações do Sistema

- **Gerado por:** Agente de Web Scraping de Patentes
- **Modelo LLM:** gemma3:4b
- **Data de geração:** 23/06/2026 17:49:06
- **Query de busca:** `carbon dioxide`
- **Status da execução:** completed
- **Tempo total:** 338.1s
- **LLM disponível:** sim
- **Fila de revisão manual:** 3 itens
- **Snapshot hash:** `83c94060d3114fed7a65727357f51f76f9a900012613b9c511e1e38b4d1d3bf0`
- **Features habilitadas:** require_evidence, enable_thematic_clusters, enable_structural_roles, enable_screening_rerank, enable_prisma, enable_snapshot, enable_comparative_analysis, enable_whitespace_analysis, enable_manual_review_queue
- **Features desabilitadas:** nenhum
- **Versão do pipeline:** 1.1
- **Thresholds snapshot:** include=0.0, review=0.0
- **Cache LLM:** 32 hits, 5 misses, 90 entradas
- **Status do rascunho:** ready