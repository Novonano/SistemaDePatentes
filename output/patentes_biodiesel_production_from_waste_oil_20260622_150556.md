# 📋 Relatório de Análise de Patentes

**Data:** 22/06/2026 15:05:56
**Busca:** `biodiesel production from waste oil`
**Total de patentes encontradas:** 13
**Modelo de avaliação:** gemma3:27b

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

- **Total bruto coletado:** 13
- **Patentes únicas:** 13
- **Duplicatas removidas:** 0
- **Triadas:** 0
- **Incluídas:** 0
- **Em revisão manual:** 13
- **Excluídas:** 0
- **Extrações completas:** 0
- **Sem abstract/snippet:** 0
- **Sem ID:** 0
- **Identidade por conteúdo:** 0
- **Identidade fallback:** 0
- **Duplicatas por família removidas:** 0
- **Falhas de triagem LLM:** 13
- **Falhas totais LLM:** 0

## 🧭 Fluxo PRISMA-Like

- **Identificação:** 13 bruto(s), 13 único(s), 0 duplicata(s) removida(s)
- **Triagem:** 0 triado(s), 0 incluído(s), 13 em revisão, 0 excluído(s)
- **Elegibilidade:** 0 extração(ões) completa(s), 13 revisão(ões) manual(is), 0 adiada(s)
- **Cobertura:** 0 sem abstract/snippet, 0 sem ID
- **Síntese:** 0 registro(s) analisado(s)

## 🧠 Contexto Compartilhado

- **Top patentes no contexto:** 0
- **Clusters no contexto:** 0
- **Roteamento agregado:** 1 rota(s)
- **Slots ativos:** N/A

## ⏱️ Métricas por Etapa

| Etapa | Status | Duração | Itens | Detalhes |
|---|---|---:|---:|---|
| setup | degraded | 4.09s | 1 | Verificação do modelo Ollama |
| search | ok | 83.17s | 13 | 13 patentes únicas após dedupe |
| screening | skipped | 0.00s | 13 | LLM indisponível |
| comparative_analysis | skipped | 0.00s | 13 | LLM indisponível para síntese comparativa |
| whitespace_analysis | skipped | 0.00s | 0 | Whitespace analysis sem corpus elegível |
| reporting | ok | 0.01s | 13 | Relatórios Markdown e JSON |
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

## 🔎 Observabilidade Estruturada

### Rotas

- **unrouted**: total=13, include=0, review=13, exclude=0, llm_errors=13

### Fontes

- **EPO**: bruto=0, duração=0.00s, diagnósticos=config_missing=1
- **GooglePatents**: bruto=3, duração=10.79s, diagnósticos=nenhum
- **Patentscope**: bruto=10, duração=72.33s, diagnósticos=nenhum

### Falhas

- **Erros de execução:** 0
- **Registros com erro de LLM:** 13
- **Falhas totais do LLM:** 0
- **Scraper por tipo de sinal:** config_missing=1

## 📊 Resumo Executivo

**Score médio de relevância:** 0.0/10

| # | Patente | Score | Inovação | Domínio |
|---|---------|-------|----------|---------|
| 1 | [WO2021204610A1](https://patents.google.com/patent/WO2021204610A1/en) — Energy efficient biodiesel production from natural or indust... | 🔴 0.0 (review) | N/A | N/A |
| 2 | [US10654789B2](https://patents.google.com/patent/US10654789B2/en) — Catalyst and method for biodiesel production from unrefined ... | 🔴 0.0 (review) | N/A | N/A |
| 3 | [US20100166620A1](https://patents.google.com/patent/US20100166620A1/en) — System and process of biodiesel production | 🔴 0.0 (review) | N/A | N/A |
| 4 | [20080250700](https://patentscope.wipo.int/search/en/detail.jsf?docId=US42660468&_cid=P11-MQPIZB-03010-1) — Apparatus and method for bio-fuel
production | 🔴 0.0 (review) | N/A | N/A |
| 5 | [20160257908](https://patentscope.wipo.int/search/en/detail.jsf?docId=US177602065&_cid=P11-MQPIZB-03010-1) — Acidic methanol stripping process that reduces sulfur conten... | 🔴 0.0 (review) | N/A | N/A |
| 6 | [WO/2009/089802](https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2009089802&_cid=P11-MQPIZB-03010-1) — METHOD FOR
BIODIESEL
PRODUCTION
FROM
THE FATS AND
OILS
(FR)
... | 🔴 0.0 (review) | N/A | N/A |
| 7 | [20100166620](https://patentscope.wipo.int/search/en/detail.jsf?docId=US43774737&_cid=P11-MQPIZB-03010-1) — System and process of
biodiesel
production | 🔴 0.0 (review) | N/A | N/A |
| 8 | [2703599](https://patentscope.wipo.int/search/en/detail.jsf?docId=CA94496673&_cid=P11-MQPIZB-03010-1) — SYSTEM AND PROCESS OF
BIODIESEL
PRODUCTION
(FR)
INSTALLATION... | 🔴 0.0 (review) | N/A | N/A |
| 9 | [WO/2017/192029](https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2017192029&_cid=P11-MQPIZB-03010-1) — A METHOD OF PRODUCING
BIODIESEL
(FR)
PROCÉDÉ DE PRÉPARATION ... | 🔴 0.0 (review) | N/A | N/A |
| 10 | [WO/2006/089429](https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2006089429&_cid=P11-MQPIZB-03010-1) — APPARATUS AND METHOD FOR BIO-FUEL
PRODUCTION
(FR)
APPAREIL E... | 🔴 0.0 (review) | N/A | N/A |
| 11 | [2599499](https://patentscope.wipo.int/search/en/detail.jsf?docId=CA94292010&_cid=P11-MQPIZB-03010-1) — APPARATUS AND METHOD FOR BIO-FUEL
PRODUCTION
(FR)
APPAREIL E... | 🔴 0.0 (review) | N/A | N/A |
| 12 | [2724970](https://patentscope.wipo.int/search/en/detail.jsf?docId=CA94503297&_cid=P11-MQPIZB-03010-1) — METHODS AND CATALYSTS FOR MAKING
BIODIESEL
FROM
THE TRANSEST... | 🔴 0.0 (review) | N/A | N/A |
| 13 | [WO/2009/143159](https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2009143159&_cid=P11-MQPIZB-03010-1) — METHODS AND CATALYSTS FOR MAKING
BIODIESEL
FROM
THE TRANSEST... | 🔴 0.0 (review) | N/A | N/A |

---

## 🔍 Análise Detalhada das Patentes

### 1. Energy efficient biodiesel production from natural or industrial waste oil

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_843a5e5b5bcc` |
| **Family ID** | `family:9f7f63e8c4766cc7d8a5ba72da6b2ded7840a624` |
| **ID** | `WO2021204610A1` |
| **Inventores** | Paul Klingelhoefer, Michael Schier |
| **Titular** | BASF SE |
| **Data** | 2021-10-14 |
| **Fonte** | Google Patents |
| **URL** | [WO2021204610A1](https://patents.google.com/patent/WO2021204610A1/en) |
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
> AbstractA method of producing fatty acid alkyl ester from an organic oil source containing at least one free fatty acid, wherein the vegetable and/or animal waste oil has an acid number of at least 30 mg KOH/g and wherein the method comprises the steps of a) reacting the oil source with glycerol at a temperature, which is at least 110Â°C and does not exceed 180Â°C during the reaction, in the presence of a catalyst comprising at least methane sulfonic acid or the homo anhydride thereof; and b) acidic transesterification at a temperature, which is at least 110Â°C and does not exceed 160Â°C during the reaction of the reaction product from step a) with an alkanol; and c) isolating the fatty acid alkyl ester from the reaction product of step b).

---

### 2. Catalyst and method for biodiesel production from unrefined low-grade oil and crude aqueous alcohols

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_d9d249fb229f` |
| **Family ID** | `family:9c80bced7734dac8b56806b672c704d27ef1ccd5` |
| **ID** | `US10654789B2` |
| **Inventores** | Ka-fu YUNG, Wing-Tak Wong, Tsz-lung KWONG, Pak-chung LAU |
| **Titular** | Shenzhen Research Institute HKPU |
| **Data** | 2020-05-19 |
| **Fonte** | Google Patents |
| **URL** | [US10654789B2](https://patents.google.com/patent/US10654789B2/en) |
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
> AbstractA catalyst for catalyzing transesterification of esters or esterification of fatty acids, the catalyst is selected from the group consisting of manganese (II) glycerolate, cobalt (II) glycerolate, iron (II) glycerolate, and any combination thereof. A method for transesterification reaction, includes: a) providing a catalyst, wherein the catalyst is selected from the group consisting of manganese (II) glycerolate, cobalt (II) glycerolate, iron (II) glycerolate, and any combination thereof; b) adding the catalyst, one or more alcohols, and a composition comprising one or more esters to a reactor to form a reaction mixture; and c) stirring while heating the reaction mixture for reaction to form transesterification products.

---

### 3. System and process of biodiesel production

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_2353676b5091` |
| **Family ID** | `family:fb0bd6fa2a96e966affb0f917cd5a309e0c2500d` |
| **ID** | `US20100166620A1` |
| **Inventores** | Stephanie Marie Gurski, Anam Kazim, Hoi Ki Cheung, Amani Obeid |
| **Titular** | Individual |
| **Data** | 2010-07-01 |
| **Fonte** | Google Patents |
| **URL** | [US20100166620A1](https://patents.google.com/patent/US20100166620A1/en) |
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
> AbstractA system and process for continuous production of fatty acid methyl esters (FAME) from the fatty acid triglycerides of waste oil via transesterification in the presence of a reusable sugar-based catalyst. The system and process incorporates re-cycling and re-use of waste bi-product streams to result in a near-zero emissions, with a 97% product yield mix consisting of almost pure biodiesel and a very small percentage of impurities including glycerol.

---

### 4. Apparatus and method for bio-fuel
production

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_144c9b1aab19` |
| **Family ID** | `family:f33b9e37239c92f79f70cdabd765c47fc4ba1e9f` |
| **ID** | `20080250700` |
| **Inventores** | Tremblay André Yves, Dubé Marc Arnold |
| **Titular** | The University of Ottawa |
| **Data** | 16.10.2008 |
| **Fonte** | Patentscope |
| **URL** | [20080250700](https://patentscope.wipo.int/search/en/detail.jsf?docId=US42660468&_cid=P11-MQPIZB-03010-1) |
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
> (EN)An apparatus for theproductionof a bio-fuel or a bio-fuel additivefromplant-derivedoils, animal fats or a mixture thereof, suitable for use in a diesel engine is disclosed. The apparatus comprises a porous membrane for separating a reaction mixturefroma permeate, the reaction mixture comprising an alcohol, a feedstock comprising plant-derivedoils, animal fats or mixture thereof, and a catalyst for converting said feedstock to a bio-fuel or a bio-fuel additive, wherein said porous membrane is substantially impermeable to the feedstock and substantially permeable to said bio-fuel or bio-fuel additive. A method using said porous membrane in theproductionof a bio-fuel or a bio-fuel additive is also disclosed.

---

### 5. Acidic methanol stripping process that reduces sulfur content of
biodiesel
from
waste
greases

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_dc8508d79339` |
| **Family ID** | `family:8384d9b0795bc70e5855cb25c3727c3f34b05f55` |
| **ID** | `20160257908` |
| **Inventores** | Richard Allan Cairncross, Megan Elizabeth Hums, Colin James Stacy |
| **Titular** | Drexel University
Environmental Fuel Research, LLC |
| **Data** | 08.09.2016 |
| **Fonte** | Patentscope |
| **URL** | [20160257908](https://patentscope.wipo.int/search/en/detail.jsf?docId=US177602065&_cid=P11-MQPIZB-03010-1) |
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
> (EN)The present invention provides a method of producing fatty acid alkyl estersfroma lipid, comprising steps of introducing a gas comprising vapor of an alcohol selectedfrommethanol, ethanol, 1-propanol, iso-propanol and butanols, into the lipid in a form of bubbles to enable the bubbles to pass through the lipid and be dischargedfromthe lipid. Theproductmay then be subjected to a transesterification process catalyzed by a base catalyst. The present invention is robust with low quality feedstocks thus significantly reduceproductioncost forbiodiesel.

---

### 6. METHOD FOR
BIODIESEL
PRODUCTION
FROM
THE FATS AND
OILS
(FR)
PROCÉDÉ DE PRODUCTION DE BIODIESEL À PARTIR DE MATIÈRES GRASSES

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_4f75f5840fbe` |
| **Family ID** | `family:f2cf49060a6d9fec68e2264d35720f2f7f0ab82e` |
| **ID** | `WO/2009/089802` |
| **Inventores** | KOLOMAZNÍK, Karel, KLEIN, Karel, VASEK, Vladimír, JANÁCOVÁ, Dagmar, JELÍNEK, Milos, UHLÍROVÁ, Michaela, MYNARÍK, Alois |
| **Titular** | TOMAS BATA UNIVERSITY IN ZLÍN
[CZ]/[CZ]
(AllExceptUS)
KOLOMAZNÍK, Karel
[CZ]/[CZ](UsOnly)
KLEIN, Karel
[CZ]/[CZ](UsOnly)
VASEK, Vladimír
[CZ]/[CZ](UsOnly)
JANÁCOVÁ, Dagmar
[CZ]/[CZ](UsOnly)
JELÍNEK, Milos
[CZ]/[CZ](UsOnly)
UHLÍROVÁ, Michaela
[CZ]/[CZ](UsOnly)
MYNARÍK, Alois
[CZ]/[CZ](UsOnly) |
| **Data** | 23.07.2009 |
| **Fonte** | Patentscope |
| **URL** | [WO/2009/089802](https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2009089802&_cid=P11-MQPIZB-03010-1) |
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
> (EN)The method lies in reesterification of fats andoilsunder alkali conditions and subsequent separation of thebiodieselphasefromthe glycerin phase. An organic base or a mixture of organic bases is used for the creation of alkali conditions and as catalysts for alcoholysis. A suitable organic base, or bases, is an amine with boiling point at normal pressure up to 200°C, or a mixture of such amines with tetramethylammonium hydroxide. It particularly concerns aminesfromthe group containing isopropylamine, diisopropylamine, diethylamine, n-butylamine and cyclohexylamine. Inwasteoilsand fats containing free fatty acids, especially when the content of free fatty acids exceeds the limit value of acid number, esterification of these acids can be applied with the use of an organic base or a mixture of organic bases.(FR)Le procédé de l'invention se rapporte à la réestérification de matières grasses dans des conditions alcalines, et à la séparation subséquente de la phase biodiesel de la phase glycérine. Une base organique, ou un mélange de bases organiques, est utilisé pour la création de conditions alcalines et comme catalyseur d'alcoolyse. Une base (ou des bases) organique appropriée est une amine dont le point d'ébullition à pression normale peut atteindre 200°C, ou un mélange de telles amines avec un hydroxyde de tétraméthylammonium. L’invention concerne particulièrement des amines du groupe constitué par isopropylamine, diisopropylamine, diéthylamine, n-butylamine et cyclohexylamine. Dans des matières grasses contenant des acides gras libres, en particulier lorsque la teneur en acides gras libres dépasse la valeur limite de l'indice d'acidité, l'estérification de ces acides peut être réalisée par l'utilisation d'une base organique ou d'un mélange de bases organiques.

---

### 7. System and process of
biodiesel
production

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_0175c5309d24` |
| **Family ID** | `family:d94fce9ee371be199037a86835cb57b9d636bfbe` |
| **ID** | `20100166620` |
| **Inventores** | Gurski Stephanie Marie, Kazim Anam, Cheung Hoi Ki, Obeid Amani |
| **Titular** | Gurski Stephanie Marie
Kazim Anam
Cheung Hoi Ki
Obeid Amani |
| **Data** | 01.07.2010 |
| **Fonte** | Patentscope |
| **URL** | [20100166620](https://patentscope.wipo.int/search/en/detail.jsf?docId=US43774737&_cid=P11-MQPIZB-03010-1) |
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
> (EN)A system and process for continuousproductionof fatty acid methyl esters (FAME)fromthe fatty acid triglycerides ofwasteoilvia transesterification in the presence of a reusable sugar-based catalyst. The system and process incorporates re-cycling and re-use ofwasteby-productstreams to result in a near-zero emissions, with a 97%productyield mix consisting of almost purebiodieseland a very small percentage of impurities including glycerol.

---

### 8. SYSTEM AND PROCESS OF
BIODIESEL
PRODUCTION
(FR)
INSTALLATION ET PROCEDE DE PRODUCTION DE BIODIESEL

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_ff8144cbafdf` |
| **Family ID** | `family:5cfc1988b763afd697e5baad812761abf34668fe` |
| **ID** | `2703599` |
| **Inventores** | N/A |
| **Titular** | GURSKI, STEPHANIE MARIE
KAZIM, ANAM
CHEUNG, HOI KI
OBEID, AMANI |
| **Data** | 18.05.2011 |
| **Fonte** | Patentscope |
| **URL** | [2703599](https://patentscope.wipo.int/search/en/detail.jsf?docId=CA94496673&_cid=P11-MQPIZB-03010-1) |
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
> (EN)A system and process for continuousproductionof fatty acid methyl esters(FAME)fromthe fatty acid triglycerides ofwasteoilvia transesterificationin thepresence of a reusable sugar-based catalyst. The system and processincorporatesre-cycling and re-use ofwastebi-productstreams to result in a near-zeroemissions, witha 97%productyield mix consisting of almost purebiodieseland a very smallpercentage of impurities including glycerol.

---

### 9. A METHOD OF PRODUCING
BIODIESEL
(FR)
PROCÉDÉ DE PRÉPARATION DE BIODIESEL

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_3279aa5dd01e` |
| **Family ID** | `family:69434200c71201f2f71cc08f5ab86a40d13c538a` |
| **ID** | `WO/2017/192029` |
| **Inventores** | BIN KU HAMID, Ku Halim |
| **Titular** | UNIVERSITI TEKNOLOGI MARA
[MY]/[MY] |
| **Data** | 09.11.2017 |
| **Fonte** | Patentscope |
| **URL** | [WO/2017/192029](https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2017192029&_cid=P11-MQPIZB-03010-1) |
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
> (EN)The present invention relates a method forbiodieselproductionfromwasteoilcomprising the steps of mixingwasteoiland alcohol; and performing transesterification in a reactor comprising a combination of a high speed mixer operating at 1000 to 5000 rpm and a sonic mixer operating at 1.5 to 2.4 MHz wherein the mixture is passed through a plurality of reactors connected in series.(FR)La présente invention concerne un procédé de production de biodiesel à partir d'huile usée comprenant les étapes consistant à mélanger de l'huile usée et de l'alcool; et à effectuer une transestérification dans un réacteur comprenant une combinaison d'un mélangeur à grande vitesse fonctionnant à 1000 à 5000 tr/min et d'un mélangeur sonique fonctionnant à 1,5 à 2,4 MHz, le mélange étant passé à travers une pluralité de réacteurs reliés en série.

---

### 10. APPARATUS AND METHOD FOR BIO-FUEL
PRODUCTION
(FR)
APPAREIL ET PROCEDE POUR LA PRODUCTION DE BIOCOMBUSTIBLE

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_33a6eb761b0a` |
| **Family ID** | `family:26e396f5f517903eafd6c9627138c1fa90a29f00` |
| **ID** | `WO/2006/089429` |
| **Inventores** | TREMBLAY, André Yves, DUBÉ, Marc Arnold |
| **Titular** | UNIVERSITY OF OTTAWA
[CA]/[CA]
(AllExceptUS)
TREMBLAY, André Yves
[CA]/[CA](UsOnly)
DUBÉ, Marc Arnold
[CA]/[CA](UsOnly) |
| **Data** | 31.08.2006 |
| **Fonte** | Patentscope |
| **URL** | [WO/2006/089429](https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2006089429&_cid=P11-MQPIZB-03010-1) |
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
> (EN)An apparatus for theproductionof a bio-fuel or a bio-fuel additivefromplant-derivedoils, animal fats or a mixture thereof, suitable for use in a diesel engine is disclosed. The apparatus comprises a porous membrane for separating a reaction mixturefroma permeate, the reaction mixture comprising an alcohol, a feedstock comprising plant-derivedoils, animal fats or mixture thereof, and a catalyst for converting said feedstock to a bio-fuel or a bio-fuel additive, wherein said porous membrane is substantially impermeable to the feedstock and substantially permeable to said bio-fuel or bio-fuel additive. A method using said porous membrane in theproductionof a bio-fuel or a bio-fuel additive is also disclosed(FR)L'invention concerne un appareil pour la production d'un biocombustible ou d'un adjuvant de biocombustible issu d'huiles végétales, de graisses animales ou de leurs mélanges, approprié pour être utilisé dans un moteur diesel. L'appareil comprend une membrane poreuse destinée à séparer un mélange réactionnel d'un perméat, le mélange réactionnel comprenant un alcool, une charge comprenant des huiles végétales, des graisses animales ou leurs mélanges et un catalyseur pour convertir ladite charge en un biocombustible ou un adjuvant de biocombustible, ladite membrane poreuse étant sensiblement imperméable à la charge et sensiblement perméable audit biocombustible ou adjuvant de biocombustible. L'invention concerne également un procédé utilisant ladite membrane poreuse pour la production d'un biocombustible ou d'un adjuvant de biocombustible.

---

### 11. APPARATUS AND METHOD FOR BIO-FUEL
PRODUCTION
(FR)
APPAREIL ET PROCEDE POUR LA PRODUCTION DE BIOCOMBUSTIBLE

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_f3efddf0f846` |
| **Family ID** | `family:49d70c138922be24511357b8b151bb6b4b881437` |
| **ID** | `2599499` |
| **Inventores** | N/A |
| **Titular** | UNIVERSITY OF OTTAWA |
| **Data** | 31.08.2006 |
| **Fonte** | Patentscope |
| **URL** | [2599499](https://patentscope.wipo.int/search/en/detail.jsf?docId=CA94292010&_cid=P11-MQPIZB-03010-1) |
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
> (EN)An apparatus for theproductionof a bio-fuel or a bio-fuel additivefromplant-derivedoils, animal fats or a mixture thereof, suitable for use in adiesel engine is disclosed. The apparatus comprises a porous membrane forseparating a reaction mixturefroma permeate, the reaction mixture comprisingan alcohol, a feedstock comprising plant-derivedoils, animal fats or mixturethereof, and a catalyst for converting said feedstock to a bio-fuel or a bio-fuel additive, wherein said porous membrane is substantially impermeable tothe feedstock and substantially permeable to said bio-fuel or bio-fueladditive. A method using said porous membrane in theproductionof a bio-fuelor a bio-fuel additive is also disclosed

---

### 12. METHODS AND CATALYSTS FOR MAKING
BIODIESEL
FROM
THE TRANSESTERIFICATION AND ESTERIFICATION OF UNREFINED
OILS
(FR)
PROCEDES ET CATALYSEURS POUR FABRIQUER UN BIODIESEL, PAR TRANSESTERIFICATION ET ESTERIFICATION D'HUILES NON RAFFINEES

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_698403409d1d` |
| **Family ID** | `family:1314563b37c124086c37827a918f204596aceb70` |
| **ID** | `2724970` |
| **Inventores** | YAN, SHULI, SALLEY, STEVEN O., NG, K. Y. SIMON |
| **Titular** | WAYNE STATE UNIVERSITY |
| **Data** | 26.11.2009 |
| **Fonte** | Patentscope |
| **URL** | [2724970](https://patentscope.wipo.int/search/en/detail.jsf?docId=CA94503297&_cid=P11-MQPIZB-03010-1) |
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
> (EN)A method of forming abiodieselproductand a heterogeneous catalyst system  used to form saidproductthat has a high tolerance  for the presence of water and free fatty  acids (FFA) in theoilfeedstock is disclosed.  This catalyst system may simultaneously catalyze    both the esterification of FAA and the  transesterification of triglycerides present in theoilfeedstock. The catalyst system according to  one aspect of the present disclosure represents a  class of zinc and lanthanum oxide heterogeneous  catalysts that include different ratios of zinc oxide  to lanthanum oxides (Zn:La ratio) rangingfromabout 10:0 to 0:10. The Zn:La ratio in the  catalyst is believed to have an effect on the number  and reactivity of Lewis acid and base sites, as  well as the transesterification of glycehdes, the  esterification of fatty acids, and the hydrolysis of  glycehdes andbiodiesel.

---

### 13. METHODS AND CATALYSTS FOR MAKING
BIODIESEL
FROM
THE TRANSESTERIFICATION AND ESTERIFICATION OF UNREFINED
OILS
(FR)
PROCÉDÉS ET CATALYSEURS POUR FABRIQUER UN BIODIESEL, PAR TRANSESTÉRIFICATION ET ESTÉRIFICATION D'HUILES NON RAFFINÉES

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_8e80f3d89661` |
| **Family ID** | `family:cb8f0aacd7fe7c0eec8aefb4a757cd37492633c4` |
| **ID** | `WO/2009/143159` |
| **Inventores** | YAN, Shuli, SALLEY, Steven, O., NG, K.Y., Simon |
| **Titular** | WAYNE STATE UNIVERSITY
[US]/[US]
(AllExceptUS)
YAN, Shuli
[CN]/[US](UsOnly)
SALLEY, Steven, O.
[US]/[US](UsOnly)
NG, K.Y., Simon
[US]/[US](UsOnly) |
| **Data** | 26.11.2009 |
| **Fonte** | Patentscope |
| **URL** | [WO/2009/143159](https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2009143159&_cid=P11-MQPIZB-03010-1) |
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
> (EN)A method of forming abiodieselproductand a heterogeneous catalyst system used to form saidproductthat has a high tolerance for the presence of water and free fatty acids (FFA) in theoilfeedstock is disclosed. This catalyst system may simultaneously catalyze both the esterification of FAA and the transesterification of triglycerides present in theoilfeedstock. The catalyst system according to one aspect of the present disclosure represents a class of zinc and lanthanum oxide heterogeneous catalysts that include different ratios of zinc oxide to lanthanum oxides (Zn:La ratio) rangingfromabout 10:0 to 0:10. The Zn:La ratio in the catalyst is believed to have an effect on the number and reactivity of Lewis acid and base sites, as well as the transesterification of glycehdes, the esterification of fatty acids, and the hydrolysis of glycehdes andbiodiesel.(FR)L'invention porte sur un procédé de formation d'un produit biodiesel et sur un système catalyseur hétérogène utilisé pour former ledit produit, qui a une grande tolérance à la présence d'eau et d'acides gras libres (FFA) dans l'huile de charge. Le système catalyseur peut simultanément catalyser tant l'estérification des FFA que la transestérification des triglycérides présents dans l'huile de charge. Le système catalyseur selon un aspect de la présente invention représente une classe de catalyseurs hétérogènes à l'oxyde de zinc et de lanthane, qui présentent différents rapports de l'oxyde de zinc aux oxydes de lanthane (rapport Zn:La), compris entre environ 10:0 et 0:10. On pense que le rapport Zn:La du catalyseur a un effet sur le nombre et la réactivité des sites d'acides et de bases de Lewis, ainsi que sur la transestérification des glycérides, l'estérification des acides gras et l'hydrolyse des glycérides et du biodiesel.

---

## 🧾 Fila de Revisão Manual

- rec_3279aa5dd01e (WO/2017/192029) | rota= | motivo=LLM indisponível. | erro_llm=LLM indisponível.
- rec_33a6eb761b0a (WO/2006/089429) | rota= | motivo=LLM indisponível. | erro_llm=LLM indisponível.
- rec_f3efddf0f846 (2599499) | rota= | motivo=LLM indisponível. | erro_llm=LLM indisponível.
- rec_dc8508d79339 (20160257908) | rota= | motivo=LLM indisponível. | erro_llm=LLM indisponível.
- rec_144c9b1aab19 (20080250700) | rota= | motivo=LLM indisponível. | erro_llm=LLM indisponível.
- rec_d9d249fb229f (US10654789B2) | rota= | motivo=LLM indisponível. | erro_llm=LLM indisponível.
- rec_843a5e5b5bcc (WO2021204610A1) | rota= | motivo=LLM indisponível. | erro_llm=LLM indisponível.
- rec_4f75f5840fbe (WO/2009/089802) | rota= | motivo=LLM indisponível. | erro_llm=LLM indisponível.
- rec_698403409d1d (2724970) | rota= | motivo=LLM indisponível. | erro_llm=LLM indisponível.
- rec_8e80f3d89661 (WO/2009/143159) | rota= | motivo=LLM indisponível. | erro_llm=LLM indisponível.
- rec_ff8144cbafdf (2703599) | rota= | motivo=LLM indisponível. | erro_llm=LLM indisponível.
- rec_0175c5309d24 (20100166620) | rota= | motivo=LLM indisponível. | erro_llm=LLM indisponível.
- rec_2353676b5091 (US20100166620A1) | rota= | motivo=LLM indisponível. | erro_llm=LLM indisponível.

---

## ℹ️ Informações do Sistema

- **Gerado por:** Agente de Web Scraping de Patentes
- **Modelo LLM:** gemma3:27b
- **Data de geração:** 22/06/2026 15:05:56
- **Query de busca:** `biodiesel production from waste oil`
- **Status da execução:** completed
- **Tempo total:** 87.3s
- **LLM disponível:** não
- **Fila de revisão manual:** 13 itens
- **Snapshot hash:** `9ac57d29ee662d5da0298e19811ad1b5acea6324a7c29163bc42875c8f23b43b`
- **Features habilitadas:** require_evidence, enable_thematic_clusters, enable_structural_roles, enable_screening_rerank, enable_prisma, enable_snapshot, enable_comparative_analysis, enable_whitespace_analysis, enable_manual_review_queue
- **Features desabilitadas:** nenhum
- **Versão do pipeline:** 1.1
- **Thresholds snapshot:** include=7.0, review=4.5
- **Cache LLM:** 0 hits, 0 misses, 0 entradas
- **Status do rascunho:** blocked
- **Avisos do rascunho:** 1