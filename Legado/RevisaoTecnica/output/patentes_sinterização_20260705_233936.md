# 📋 Relatório de Análise de Patentes

**Data:** 05/07/2026 23:39:36
**Busca:** `sinterização`
**Total de patentes encontradas:** 4
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

- **Total bruto coletado:** 4
- **Patentes únicas:** 4
- **Duplicatas removidas:** 0
- **Triadas:** 4
- **Incluídas:** 0
- **Em revisão manual:** 0
- **Excluídas:** 4
- **Extrações completas:** 0
- **Sem abstract/snippet:** 0
- **Sem ID:** 2
- **Identidade por conteúdo:** 0
- **Identidade fallback:** 0
- **Duplicatas por família removidas:** 0
- **Falhas de triagem LLM:** 0
- **Falhas totais LLM:** 0

## 🧭 Fluxo PRISMA-Like

- **Identificação:** 4 bruto(s), 4 único(s), 0 duplicata(s) removida(s)
- **Triagem:** 4 triado(s), 0 incluído(s), 0 em revisão, 4 excluído(s)
- **Elegibilidade:** 0 extração(ões) completa(s), 0 revisão(ões) manual(is), 0 adiada(s)
- **Cobertura:** 0 sem abstract/snippet, 2 sem ID
- **Síntese:** 0 registro(s) analisado(s)

## 🧠 Contexto Compartilhado

- **Top patentes no contexto:** 0
- **Clusters no contexto:** 0
- **Roteamento agregado:** 1 rota(s)
- **Slots ativos:** N/A

## ⏱️ Métricas por Etapa

| Etapa | Status | Duração | Itens | Detalhes |
|---|---|---:|---:|---|
| setup | ok | 3.72s | 1 | Verificação do modelo Ollama |
| search | ok | 34.54s | 4 | 4 patentes únicas após dedupe |
| screening | ok | 153.28s | 4 | 0 incluídas, 0 revisão |
| comparative_analysis | skipped | 0.00s | 4 | Nenhuma patente elegível para síntese comparativa |
| whitespace_analysis | skipped | 0.00s | 0 | Whitespace analysis sem corpus elegível |
| reporting | ok | 0.00s | 4 | Relatórios Markdown e JSON |
| finalization | ok | 0.00s | 8 | Persistência de artefatos e estado |

## 🌐 Diagnósticos de Coleta

### GooglePatents

- Nenhum sinal relevante detectado.

### Patentscope

- **jsf_empty_results**: Nenhum resultado em result.jsf para query: sinterização
- **detail_session_expired**: Página de detalhe sem campos biblio — sessão/cid pode ter expirado.
- **detail_session_expired**: Página de detalhe sem campos biblio — sessão/cid pode ter expirado.
- **detail_session_expired**: Página de detalhe sem campos biblio — sessão/cid pode ter expirado.
- **detail_session_expired**: Página de detalhe sem campos biblio — sessão/cid pode ter expirado.

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
- **Latência média:** 3.72s
- **Latência máxima:** 3.72s

### screening

- **Chamadas:** 4
- **Sucessos:** 4
- **Falhas:** 0
- **Retries:** 0
- **Cache hits:** 0
- **Pulos por degradação:** 0
- **Latência média:** 38.321s
- **Latência máxima:** 43.043s

## 🔎 Observabilidade Estruturada

### Rotas

- **screen_only**: total=4, include=0, review=0, exclude=4, llm_errors=0

### Fontes

- **EPO**: bruto=0, duração=0.00s, diagnósticos=config_missing=1
- **GooglePatents**: bruto=4, duração=11.15s, diagnósticos=nenhum
- **Patentscope**: bruto=0, duração=23.38s, diagnósticos=detail_session_expired=4, jsf_empty_results=1

### Falhas

- **Erros de execução:** 0
- **Registros com erro de LLM:** 0
- **Falhas totais do LLM:** 0
- **LLM por operação:** healthcheck(falhas=0, retries=0, skips=0), screening(falhas=0, retries=0, skips=0)
- **Scraper por tipo de sinal:** config_missing=1, detail_session_expired=4, jsf_empty_results=1

## 📊 Resumo Executivo

**Score médio de relevância:** 0.0/10

| # | Patente | Score | Inovação | Domínio |
|---|---------|-------|----------|---------|
| 1 | [rec_cf7740d73e52](https://patents.google.com/patent/BRPI0306141B1/pt) — mÃ©todo de granulaÃ§Ã£o de material de sinterizaÃ§Ã£o para a... | 🔴 0.0 (exclude) | N/A | Metalurgia, Processamento de Materiais |
| 2 | [rec_0b3f39205925](https://patents.google.com/patent/BRPI0520278A2/en) — Method for pretreatment of sintering material | 🔴 0.0 (exclude) | N/A | Metalurgia |
| 3 | [BR112015015064B1](https://patents.google.com/patent/BR112015015064B1/pt) — MÃ©todo e sistema para controlar a quantidade de ar da caixa... | 🔴 0.0 (exclude) | N/A | Processamento de Minérios / Sinterização |
| 4 | [WO2023035050A1](https://patents.google.com/patent/WO2023035050A1/pt) — QUEIMADOR DE BAIXA EMISSÃO DE NOx E MÃTODO OPERACIONAL PAR... | 🔴 0.0 (exclude) | N/A | Metalurgia / Processamento de Materiais |

---

## 🔍 Análise Detalhada das Patentes

### 1. mÃ©todo de granulaÃ§Ã£o de material de sinterizaÃ§Ã£o para a fabricaÃ§Ã£o de ferro

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_cf7740d73e52` |
| **Family ID** | `family:80da79de91b6e207ea53445aac6a77dcaee25fd3` |
| **ID** | `` |
| **Inventores** | Katsuyuki Kono, Kazuyuki Shinagawa, Keiichi Nakamoto, Satoru Miura, Takehiko Sato, Tsutomu Okada, Yohzoh Hosotani |
| **Titular** | Nippon Steel & Sumitomo Metal Corp |
| **Data** | 2015-10-20 |
| **Fonte** | Google Patents |
| **URL** | [rec_cf7740d73e52](https://patents.google.com/patent/BRPI0306141B1/pt) |
| **Triagem** | exclude |
| **Rota** | screen_only |
| **Motivo da rota** | Patente excluída na triagem. |
| **Score de Triagem** | 3.5/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | Metalurgia, Processamento de Materiais |
| **Cluster Temático** | Processos de Fabricação de Materiais Sólidos |
| **Papel do CO2** | co2_not_central |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | industrial_heat |
| **Foco das Claims** | component_or_operation |
| **Categoria de Exclusão** | generic_tes |
| **Confiança** | 0.59 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> Abstract"mÃ©todo de granulaÃ§Ã£o de material de sinterizaÃ§Ã£o para fabricar ferro". Ã© um objeto da presente invenÃ§Ã£o fornecer um mÃ©todo de granulaÃ§Ã£o de matÃ©ria-prima para sinterizar, para a fabricaÃ§Ã£o de ferro, o qual Ã© eficazmente usado para granular matÃ©ria-prima para sinterizar, para a fabricaÃ§Ã£o de ferro, tal como finos de minÃ©rios de ferro, na fabricaÃ§Ã£o de minÃ©rio sinterizado que forma as matÃ©rias-primas para uma carga de alto-forno em um processo de produzir ferro gusa, e tornar possÃ­vel melhorar suficientemente a produtividade de uma mÃ¡quina de sinterizaÃ§Ã£o. a presente invenÃ§Ã£o Ã© dirigida a um mÃ©todo de granulaÃ§Ã£o de um material de sinterizaÃ§Ã£o para fabricar ferro contendo minÃ©rio de ferro em pÃ³, compreendendo um processo para realizar a granulaÃ§Ã£o por diluiÃ§Ã£o preliminar das partÃ­culas finas tendo um tamanho mÃ©dio de partÃ­cula de nÃ£o mais do que 200 <109>m em uma porÃ§Ã£o de um solvente ou um material de sinterizaÃ§Ã£o, e adiÃ§Ã£o do material resultante ao restante do material de sinterizaÃ§Ã£o, em que referida granulaÃ§Ã£o Ã© pelo menos um processo selecionado do grupo consistindo dos seguintes (1), (2) e (3): (1) um processo para realizar a granulaÃ§Ã£o, o qual compreende misturar referidas partÃ­culas finas com Ã¡gua, de modo a formar uma lama tendo uma viscosidade de 0,005 a 10 pa.s, e depois adicionar a lama ao material de sinterizaÃ§Ã£o, (2) um processo para realizar a granulaÃ§Ã£o, o qual compreende granular preliminarmente referidas partÃ­culas finas com 13 a 60 % em quantidade de massa de um material de sinterizaÃ§Ã£o compreendendo minÃ©rio de ferro como um componente essencial medido no estado seco, e depois adicionar referido produto granulado ao restante do material de sinterizaÃ§Ã£o, e (3) um processo para realizar a granulaÃ§Ã£o, o qual compreende misturar preliminarmente referidas partÃ­culas finas com 0,3 a 10 % em quantidade de massa do material de sinterizaÃ§Ã£o, medido no estado seco.

**Evidências citadas:**
> "mÃ©todo de granulaÃ§Ã£o de material de sinterizaÃ§Ã£o para fabricar ferro"
> âprocesso para realizar a granulaÃ§ão, o qual compreende misturar referidas partÃ­culas finas com Ãgua...â

---

### 2. Method for pretreatment of sintering material

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_0b3f39205925` |
| **Family ID** | `family:cb54e04215eecec64625d892cce5e4bca28cdcec` |
| **ID** | `` |
| **Inventores** | Kenichi Yakashiro, Takeshi Imai, Akira Gushima, Tsuneo Ikeda |
| **Titular** | Nippon Steel Corp |
| **Data** | 2009-04-28 |
| **Fonte** | Google Patents |
| **URL** | [rec_0b3f39205925](https://patents.google.com/patent/BRPI0520278A2/en) |
| **Triagem** | exclude |
| **Rota** | screen_only |
| **Motivo da rota** | Patente excluída na triagem. |
| **Score de Triagem** | 3.5/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | Metalurgia |
| **Cluster Temático** | Processamento de Materiais |
| **Papel do CO2** | co2_not_central |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | industrial_heat |
| **Foco das Claims** | process_integration |
| **Categoria de Exclusão** | generic_tes |
| **Confiança** | 0.56 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> AbstractTranslated fromPortugueseMÃTODO PARA PRÃ-TRATAMENTO DE MATERIAL DE SINTERIZAÃÃ§O. A presente invenÃ§Ã£o refere-se a um mÃ©todo para prÃ©-tratamento de um material de sinterizaÃ§Ã£o usando como material pelo menos dois tipos de minÃ©rio de ferro contendo grÃ£os brutos e pÃ³ fino, usando-se um primeiro peletizador para fazer o pÃ³ fino aglutinar-se aos grÃ£os brutos formando grÃ£os de nÃºcleo de modo a produzir pelotas do tipo S, e usando-se um segundo peletizador para peletizar apenas pÃ³ fino ou principalmente pÃ³ fino para produzir pelotas do tipo P, cujo mÃ©todo de produÃ§Ã£o de pelotas do tipo S pelo ajuste da quantidade de pÃ³ fino fornecido ao mencionado primeiro peletizador de forma que a espessura mÃ©dia do aglomerado de pÃ³ fino para os grÃ£os de nÃºcleo se tornem 50 a 300 p~m e fornecendo-se o pÃ³ fino remanescente nÃ£o fornecido ao mencionado primeiro peletizador para o segundo peletizador.METHOD FOR PRETREATMENT OF SYNTERIZATION MATERIAL. The present invention relates to a method for pretreatment of a sintering material using as material at least two types of raw grain-containing iron ore and fine powder, using a first pelletizer to agglutinate the fine powder. to the raw grains forming core grains to produce type S pellets, and using a second pelletizer to pellet only fine powder or mainly fine powder to produce type P pellets, whose method of producing type S pellets by adjusting of the amount of fine powder supplied to said first pelletizer such that the average thickness of the fine grain agglomerate for the core grains becomes 50 to 300 m 2 and the remaining fine powder not supplied to said first pelletizer is provided. pelletizer.

**Evidências citadas:**
> MÃTODO PARA PRÃ-TRATAMENTO DE UM MATERIAL DE SINTERIZAÃÇO...
> usando como material pelo menos dois tipos de minÃ©rio de ferro...

---

### 3. MÃ©todo e sistema para controlar a quantidade de ar da caixa-de-ar do carrinho de sinterizaÃ§Ã£o.

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_f967a6d0dd68` |
| **Family ID** | `family:ac89d7389daa7a05624cdabcace413298e091cde` |
| **ID** | `BR112015015064B1` |
| **Inventores** | Lixin Yuan, Chao Sun, Yangquan Lu, Weijie SHEN, Pengshuang Gao |
| **Titular** | Zhongye Changtian International Engineering Co., Ltd. |
| **Data** | 2019-07-09 |
| **Fonte** | Google Patents |
| **URL** | [BR112015015064B1](https://patents.google.com/patent/BR112015015064B1/pt) |
| **Triagem** | exclude |
| **Rota** | screen_only |
| **Motivo da rota** | Patente excluída na triagem. |
| **Score de Triagem** | 3.5/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | Processamento de Minérios / Sinterização |
| **Cluster Temático** | Controle de Processos em Sinterização |
| **Papel do CO2** | co2_not_central |
| **Papel do Armazenamento** | implicit_or_support_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | industrial_heat |
| **Foco das Claims** | component_or_operation |
| **Categoria de Exclusão** | generic_tes |
| **Confiança** | 0.59 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> Abstract"mÃ©todo e sistema para controlar a quantidade de ar da caixa-de-ar do carrinho de sinterizaÃ§Ã£o". mÃ©todo e um sistema para controlar a quantidade de ar de uma caixa-de-ar de um carrinho de sinterizaÃ§Ã£o. Ã© disposta uma vÃ¡lvula em cada caixa-de-ar do carrinho de sinterizaÃ§Ã£o. o mÃ©todo compreende: adquirir dados da quantidade de ar de uma caixa-de-ar especificada do carrinho de sinterizaÃ§Ã£o; ajustar um grau de abertura da vÃ¡lvula de outra caixa-de-ar de acordo com os dados da quantidade de ar da caixa-de-ar especificada e uma relaÃ§Ã£o entre a quantidade de ar de cada caixa-de-ar em uma base de dados e o grau de abertura de uma vÃ¡lvula correspondente, de modo a permitir que a quantidade de ar de outra caixa-de-ar seja consistente com a quantidade de ar da primeira caixa-de-ar especificada. pelo facto de a quantidade atual de ar na caixa-de-ar ser o mais consistente possÃ­vel com a quantidade de ar exigida e, por conseguinte, ser evitada a situaÃ§Ã£o de a proporÃ§Ã£o do ar efetivo na caixade-ar ser gradualmente reduzida, diminui-se fortemente o desperdÃ­cio de ar e obtÃªm-se fontes de poupanÃ§a de energia mais eficazes. graÃ§as ao mÃ©todo, a velocidade de sinterizaÃ§Ã£o vertical nÃ£o Ã© excessivamente alta e a quantidade invÃ¡lida de ar Ã© diminuÃ­da quando Ã© garantida a qualidade do minÃ©rio de sinterizaÃ§Ã£o.

**Evidências citadas:**
> mÃ©todo e um sistema para controlar a quantidade de ar de uma caixa-de-ar...
> graças ao mÃ©todo, a velocidade de sinterizaÃ§Ã£o vertical nÃ£© excessivamente alta...

---

### 4. QUEIMADOR DE BAIXA EMISSÃO DE NOx E MÃTODO OPERACIONAL PARA REDUÃÃO DE FORMAÃÃO DE NOx APLICADO EM PROCESSO DE SINTERIZAÃÃO E/OU ENDURECIMENTO DE PELOTAS DE MINÃRIO DE FERRO

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_c4b2c01f455e` |
| **Family ID** | `family:e49cddec852a1d3ba69aa1e26830a8a8c5fbb7ad` |
| **ID** | `WO2023035050A1` |
| **Inventores** | David James Retallack |
| **Titular** | Fct Holdings Pty Ltd |
| **Data** | 2023-03-16 |
| **Fonte** | Google Patents |
| **URL** | [WO2023035050A1](https://patents.google.com/patent/WO2023035050A1/pt) |
| **Triagem** | exclude |
| **Rota** | screen_only |
| **Motivo da rota** | Patente excluída na triagem. |
| **Score de Triagem** | 3.5/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | Metalurgia / Processamento de Materiais |
| **Cluster Temático** | Processos de Sinterização com Combustão Controlada |
| **Papel do CO2** | co2_not_central |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | power_or_work_cycle |
| **Fonte/Sumidouro Térmico** | industrial_heat |
| **Foco das Claims** | system_architecture |
| **Categoria de Exclusão** | low_alignment |
| **Confiança** | 0.66 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> AbstractQueimador (12) que utiliza o oxigÃªnio presente no fluxo descendente (18) de gases, composto por mistura de ar com produtos de combustÃ£o que circula atravÃ©s das zonas do forno de pelotizaÃ§Ã£o de minÃ©rio de ferro. O conjunto do queimador (12) inclui anel coletor (24) de combustÃ­vel equipado com aletas (26) montadas na parte interna do coletor, e tambÃ©m conta com uma pluralidade de aberturas (30) para descarga de gÃ¡s combustÃ­vel. Essas aberturas (30) compÃµem uma sequÃªncia de grupos (32) alinhado com cada aleta (26). O conjunto do queimador (12) Ã© inserido atravÃ©s da janela especial (16) e instalado onde o fluxo descendente (18) precisa ser aquecido, por exemplo, de partir de 850 a 1350Â°C. As aletas (26) defletem parte do fluxo descendente (18) e criam o efeito de rotaÃ§Ã£o nos gases no "downcomer" do forno. Os jatos de gÃ¡s combustÃ­vel descarregados a partir do anel de coletor (24) sÃ£o misturados com o fluxo de gases e queimam na corrente do fluxo descendente em redemoinho. A distribuiÃ§Ã£o uniforme do gÃ¡s combustÃ­vel em torno do perÃ­metro da passagem descendente junto com o efeito de redemoinho do fluxo descendente permite a mistura rÃ¡pida do gÃ¡s combustÃ­vel com o oxigÃªnio do fluxo descendente e por isso reduz, significativamente, a formaÃ§Ã£o de NOx na zona de combustÃ£o.

**Evidências citadas:**
> O conjunto do queimador (12) é inserido atravÃ©s da janela especial (16) e instalado onde o fluxo descendente (18) precisa ser aquecido...
> A distribuiÃ§Ã£o uniforme do gÃ¡s combustÃ­vel em torno do perÃ­metro da passagem descendente junto com o efeito de redemoinho do fluxo descendente permite a mistura rÃ¡pida do gÃ¡s combustÃ­vel com o oxigÃªnio do fluxo descendente e por isso reduz, significativamente, a formaÃ§Ã£o de NOx na zona de combustÃ£o.

---

## 🔬 Análise Comparativa

⚠️ Nenhuma patente elegível para síntese comparativa e whitespace após a triagem.

---

## ℹ️ Informações do Sistema

- **Gerado por:** Agente de Web Scraping de Patentes
- **Modelo LLM:** gemma3:4b
- **Data de geração:** 05/07/2026 23:39:36
- **Query de busca:** `sinterização`
- **Status da execução:** completed
- **Tempo total:** 191.6s
- **LLM disponível:** sim
- **Snapshot hash:** `ff1b944a48525ae9e01dd2bb903dac54a72ec3e55d57daf28e755817b5371212`
- **Features habilitadas:** require_evidence, enable_thematic_clusters, enable_structural_roles, enable_screening_rerank, enable_prisma, enable_snapshot, enable_comparative_analysis, enable_whitespace_analysis, enable_manual_review_queue
- **Features desabilitadas:** nenhum
- **Versão do pipeline:** 1.1
- **Thresholds snapshot:** include=7.0, review=4.5
- **Cache LLM:** 0 hits, 4 misses, 108 entradas
- **Status do rascunho:** blocked
- **Avisos do rascunho:** 1