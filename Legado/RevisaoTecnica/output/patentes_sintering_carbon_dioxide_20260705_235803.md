# 📋 Relatório de Análise de Patentes

**Data:** 05/07/2026 23:58:03
**Busca:** `sintering carbon dioxide`
**Total de patentes encontradas:** 8
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

- **Total bruto coletado:** 8
- **Patentes únicas:** 8
- **Duplicatas removidas:** 0
- **Triadas:** 8
- **Incluídas:** 0
- **Em revisão manual:** 5
- **Excluídas:** 3
- **Extrações completas:** 5
- **Sem abstract/snippet:** 0
- **Sem ID:** 0
- **Identidade por conteúdo:** 0
- **Identidade fallback:** 0
- **Duplicatas por família removidas:** 0
- **Falhas de triagem LLM:** 1
- **Falhas totais LLM:** 0

## 🧭 Fluxo PRISMA-Like

- **Identificação:** 8 bruto(s), 8 único(s), 0 duplicata(s) removida(s)
- **Triagem:** 8 triado(s), 0 incluído(s), 5 em revisão, 3 excluído(s)
- **Elegibilidade:** 5 extração(ões) completa(s), 5 revisão(ões) manual(is), 0 adiada(s)
- **Cobertura:** 0 sem abstract/snippet, 0 sem ID
- **Síntese:** 5 registro(s) analisado(s)

## 🧠 Contexto Compartilhado

- **Top patentes no contexto:** 0
- **Clusters no contexto:** 0
- **Roteamento agregado:** 2 rota(s)
- **Slots ativos:** N/A

## ⏱️ Métricas por Etapa

| Etapa | Status | Duração | Itens | Detalhes |
|---|---|---:|---:|---|
| setup | ok | 0.86s | 1 | Verificação do modelo Ollama |
| search | ok | 41.20s | 8 | 8 patentes únicas após dedupe |
| screening | degraded | 741.51s | 8 | 0 incluídas, 5 revisão |
| comparative_analysis | ok | 140.98s | 8 | Síntese comparativa gerada |
| whitespace_analysis | ok | 0.00s | 4 | Whitespace analysis estruturada gerada |
| reporting | ok | 0.00s | 8 | Relatórios Markdown e JSON |
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
- **Latência média:** 0.863s
- **Latência máxima:** 0.863s

### screening

- **Chamadas:** 8
- **Sucessos:** 8
- **Falhas:** 0
- **Retries:** 0
- **Cache hits:** 0
- **Pulos por degradação:** 0
- **Latência média:** 37.329s
- **Latência máxima:** 54.33s

### rerank

- **Chamadas:** 4
- **Sucessos:** 4
- **Falhas:** 0
- **Retries:** 0
- **Cache hits:** 0
- **Pulos por degradação:** 0
- **Latência média:** 36.788s
- **Latência máxima:** 47.617s

### evaluation

- **Chamadas:** 4
- **Sucessos:** 4
- **Falhas:** 0
- **Retries:** 0
- **Cache hits:** 0
- **Pulos por degradação:** 0
- **Latência média:** 73.93s
- **Latência máxima:** 89.669s

### comparative

- **Chamadas:** 1
- **Sucessos:** 1
- **Falhas:** 0
- **Retries:** 0
- **Cache hits:** 0
- **Pulos por degradação:** 0
- **Latência média:** 140.979s
- **Latência máxima:** 140.979s

## 🔎 Observabilidade Estruturada

### Rotas

- **manual_review**: total=5, include=0, review=5, exclude=0, llm_errors=1
- **screen_only**: total=3, include=0, review=0, exclude=3, llm_errors=0

### Fontes

- **EPO**: bruto=0, duração=0.00s, diagnósticos=config_missing=1
- **GooglePatents**: bruto=4, duração=11.98s, diagnósticos=nenhum
- **Patentscope**: bruto=4, duração=29.21s, diagnósticos=nenhum

### Falhas

- **Erros de execução:** 0
- **Registros com erro de LLM:** 1
- **Falhas totais do LLM:** 0
- **LLM por operação:** comparative(falhas=0, retries=0, skips=0), evaluation(falhas=0, retries=0, skips=0), healthcheck(falhas=0, retries=0, skips=0), rerank(falhas=0, retries=0, skips=0), screening(falhas=0, retries=0, skips=0)
- **Scraper por tipo de sinal:** config_missing=1

## 📊 Resumo Executivo

**Score médio de relevância:** 0.0/10

| # | Patente | Score | Inovação | Domínio |
|---|---------|-------|----------|---------|
| 1 | [JP6833123B1](https://patents.google.com/patent/JP6833123B1/en) — Manufacturing method of carbon dioxide adsorption sintered b... | 🟡 6.5 (review) | Incremental | Ciência dos Materiais, Engenharia Química |
| 2 | [CN113941247A](https://patents.google.com/patent/CN113941247A/en) — System and method for capturing carbon dioxide in steel sint... | 🟡 6.5 (review) | Incremental | Engenharia de Processos Industriais, Engenharia Metalúrgica, Captura e Utilização de Carbono |
| 3 | [US3930787A](https://patents.google.com/patent/US3930787A/en) — Sintering furnace with hydrogen carbon dioxide atmosphere | 🟡 6.2 (review) | Incremental | Materials Science, Thermal Processing |
| 4 | [910517](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB134822149&_cid=P21-MR8FS7-09117-1) — Improvements in or relating to the production of
sintered
ur... | 🟡 5.9 (review) | Incremental | Ceramic Materials & Nuclear Fuel Production |
| 5 | [WO2024117144A1](https://patents.google.com/patent/WO2024117144A1/en) — Sintered ore production method | 🔴 0.0 (exclude) | N/A | Metalurgia, Sinterização |
| 6 | [1171698](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135354895&_cid=P21-MR8FS7-09117-1) — Dispensing Device | 🔴 0.0 (exclude) | N/A | Engenharia de Fluidos, Dispositivos Dispensadores |
| 7 | [1174314](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135357801&_cid=P21-MR8FS7-09117-1) — A Dispensing Device for Gases Under Pressure. | 🔴 0.0 (review) | N/A | N/A |
| 8 | [153069](https://patentscope.wipo.int/search/en/detail.jsf?docId=NZ178918854&_cid=P21-MR8FS7-09117-1) — NOZZLE FOR PRESSURISING AND DISPENSING LIQUID FROM CAN | 🔴 0.0 (exclude) | N/A | Engenharia Mecânica / Processamento de Materiais |

---

## 🔍 Análise Detalhada das Patentes

### 1. Manufacturing method of carbon dioxide adsorption sintered body

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_8d21878ddc6f` |
| **Family ID** | `family:4cb528251905b42103c4bf03a86ce94516df5f97` |
| **ID** | `JP6833123B1` |
| **Inventores** | å¥äº ä¸­æ¬, æ­å¹³ å±±ç°, ä½³å¥å­ å¼æ«, ç°ä¸­ãç­, ç­ ç°ä¸­, å°æ¨¹ å¤§æ¬, äº¬ä¸é æ¨«æ, è¤äºãéå¸, éå¸ è¤äº |
| **Titular** | Chugoku Electric Power Co Inc |
| **Data** | 2021-02-24 |
| **Fonte** | Google Patents |
| **URL** | [JP6833123B1](https://patents.google.com/patent/JP6833123B1/en) |
| **Triagem** | review |
| **Rota** | manual_review |
| **Motivo da rota** | Triagem indicou revisão humana. |
| **Score de Triagem** | 7.2/10 |
| **Score de Relevância** | 6.5/10 |
| **Nível de Inovação** | Incremental |
| **Domínio Técnico** | Ciência dos Materiais, Engenharia Química |
| **Cluster Temático** | Sinterização e Adsorção de Dióxido de Carbono |
| **Papel do CO2** | capture_process_stream |
| **Papel do Armazenamento** | Suporte/Armazenamento Implícito |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | Não Claro (Implica um ciclo de adsorção-desorção) |
| **Fonte/Sumidouro Térmico** | Combustão, Gás de Escape |
| **Foco das Claims** | Método de Fabricação e Composição do Corpo de Adsorção Sinterizado |
| **Categoria de Exclusão** | industrial_heat_adjacent |
| **Confiança** | 0.85 |
| **Rerank Aplicado** | Sim |
| **Motivo do Rerank** | reranked:decision_confirmed |
| **Revisão Manual** | Sim |
| **Erro LLM** | N/A |

**Abstract:**
> AbstractTranslated fromJapaneseãèª²é¡ãè£½é æã«ãäºé¸åç­ç´ ãçºçããããã¨ããªããã¾ããçç¼æã¬ã¹ä¸­ã®äºé¸åç­ç´ ãä½æ¸ãããã¨ãå¯è½ãªäºé¸åç­ç´ å¸çç¼çµä½ã®è£½é æ¹æ³ãæä¾ããããè§£æ±ºææ®µãç³ç­ç°ã®ã¤ã°ã­ã¹éãèª¿æ´ããã¤ã°ã­ã¹éèª¿æ´å·¥ç¨ã¨ãç³ç­ç°ã«æ··åããï¼£ï½æºï¼ã³ã³ã¯ãªã¼ãç´ãéé¼ã¹ã©ã°ï¼ã®æ··åéãèª¿æ´ããï¼£ï½æºèª¿æ´å·¥ç¨ã¨ãã¤ã°ã­ã¹éèª¿æ´å·¥ç¨ã«ãã£ã¦ã¤ã°ã­ã¹éãèª¿æ´ãããç³ç­ç°åã³åè¨ã«ã«ã·ã¦ã æºèª¿æ´å·¥ç¨ã«ãã£ã¦æ··åéãèª¿æ´ãããã«ã«ã·ã¦ã æºãæ··åãããæ··åå·¥ç¨ã¨ãæ··åå·¥ç¨ã«ãã£ã¦æ··åãããæ··åç©ã«ãã¤ã¯ã­æ³¢ãç§å°ãã¦åè¨æ··åç©ãç¼çµæ¸©åº¦ä»¥ä¸ã«ææ¸©ããã¦ç¼çµãããææ¸©å·¥ç¨ã¨ãææ¸©å·¥ç¨ã«ãã£ã¦å¾ãããåè¨æ··åç©ã®ç¼çµä½ãéæ¸©ãããéç¨ã«ããã¦ãç¼çµä½ã«çç¼æã¬ã¹ãå¹ãè¾¼ãéæ¸©å·¥ç¨ã¨ããæããããé¸æå³ã å³ï¼PROBLEM TO BE SOLVED: To provide a method for producing a carbon dioxide adsorption sintered body which does not generate carbon dioxide during production and can reduce carbon dioxide in combustion exhaust gas. SOLUTION: An igross amount adjusting step for adjusting the igros amount of coal ash, a Ca source adjusting step for adjusting the mixing amount of a Ca source (concrete powder, steel slag) to be mixed with the coal ash, and an igros amount adjusting step A mixing step of mixing coal ash whose amount has been adjusted and a calcium source whose mixing amount has been adjusted by the calcium source adjusting step, and a mixing step where the mixed mixture is irradiated with microwaves to sinter the mixture above the sintering temperature. In the process of lowering the temperature of the sintered body of the mixture obtained by the raising temperature step, the temperature lowering step of blowing the combustion exhaust gas into the sintered body is included. [Selection diagram] Fig. 1

**Avaliação do LLM:**
Esta patente descreve um método para fabricar um corpo de adsorção de dióxido de carbono sinterizado, utilizando irradiação por micro-ondas e gás de escape de combustão, com ajustes na quantidade de cinzas de carvão e fonte de cálcio. O processo envolve a mistura desses componentes, seguido pela sinterização por micro-ondas e posterior resfriamento com gás de escape para reduzir as emissões de CO2.

**Extração Estruturada:**
- **Problema:** O problema abordado é a produção de corpos de adsorção de dióxido de carbono que minimizem a geração de CO2 durante o processo de sinterização, aproveitando o gás de escape de combustão.
- **Solução:** A solução proposta consiste em ajustar as quantidades de cinzas de carvão e fonte de cálcio na mistura, seguida pela sinterização por micro-ondas e resfriamento com gás de escape para controlar a temperatura e reduzir as emissões de CO2.
- **Maturidade:** Inicial

**Achados-chave:**
- Ajuste da quantidade de cinzas de carvão e fonte de cálcio para otimizar o processo de sinterização.
- Utilização da irradiação por micro-ondas como método de sinterização.
- Incorporação do gás de escape de combustão para resfriamento e redução de emissões de CO2.

**Vantagens alegadas:**
- Redução das emissões de dióxido de carbono durante o processo de fabricação.
- Utilização eficiente de gás de escape de combustão.
- Melhora nas propriedades do corpo de adsorção de dióxido de carbono sinterizado.

**Limitações:**
- A patente não detalha especificamente as condições de irradiação por micro-ondas ou a composição exata do gás de escape de combustão.
- A eficácia da redução de emissões pode depender das características específicas do gás de escape e do material de suporte.

**Aplicações potenciais:**
- Adsorção e armazenamento de dióxido de carbono em processos industriais.
- Remoção de CO2 de fluxos de combustão.
- Produção de materiais de adsorção de CO2 para aplicações ambientais.

**Evidências citadas:**
> "To provide a method for producing a carbon dioxide adsorption sintered body..."
> "blowing the combustion exhaust gas into the sintered body"

---

### 2. System and method for capturing carbon dioxide in steel sintering flue gas

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_72a65e6eb3eb` |
| **Family ID** | `family:41d760291c97b96c9594304c94533e2eb27dbd34` |
| **ID** | `CN113941247A` |
| **Inventores** | è¡é¿é, æ±ç¹, çå»ºå, é±æè±, å´å²©, å¼ èºå³°, ä»»ä¹, å²å, å¾ç»§æ³ |
| **Titular** | Capital Engineering & Research Inc Ltd |
| **Data** | 2022-01-18 |
| **Fonte** | Google Patents |
| **URL** | [CN113941247A](https://patents.google.com/patent/CN113941247A/en) |
| **Triagem** | review |
| **Rota** | manual_review |
| **Motivo da rota** | Triagem indicou revisão humana. |
| **Score de Triagem** | 7.7/10 |
| **Score de Relevância** | 6.5/10 |
| **Nível de Inovação** | Incremental |
| **Domínio Técnico** | Engenharia de Processos Industriais, Engenharia Metalúrgica, Captura e Utilização de Carbono |
| **Cluster Temático** | Captura de CO2 de Fontes Industriais |
| **Papel do CO2** | capture_process_stream |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | sintering_process |
| **Foco das Claims** | system_architecture |
| **Categoria de Exclusão** | capture_process |
| **Confiança** | 0.80 |
| **Rerank Aplicado** | Sim |
| **Motivo do Rerank** | reranked:decision_confirmed |
| **Revisão Manual** | Sim |
| **Erro LLM** | N/A |

**Abstract:**
> AbstractThe invention discloses a system and a method for capturing carbon dioxide in steel sintering flue gas. The system comprises: the device comprises a metallurgical production wastewater incoming pipeline, a sintering dedusting ash incoming pipeline, a slurry preparation unit, a flue gas absorption unit, a flue gas incoming pipeline, an emptying pipeline, a precipitation unit and a supernatant return pipeline; the flue gas absorption unit is provided with an evacuation port, a liquid inlet, a gas inlet and a liquid outlet; the metallurgical production wastewater input pipeline and the sintering dedusting ash incoming pipeline are respectively connected with the slurry preparation unit; an outlet of the slurry preparation unit is connected with a liquid inlet of the flue gas absorption unit, a liquid outlet of the flue gas absorption unit is connected with an inlet of the precipitation unit, an emptying port of the flue gas absorption unit is connected with the emptying pipeline, and a flue gas incoming pipeline is connected with a gas inlet of the flue gas absorption unit; the upper part of the settling unit is connected to the slurry preparation unit through the supernatant return line.

**Avaliação do LLM:**
Esta patente descreve um sistema para capturar dióxido de carbono (CO2) dos gases de exaustão da sinterização do aço, utilizando uma combinação de água e resíduos de produção de metalurgia. O sistema inclui unidades para preparação de suspensão, absorção de gás e precipitação, visando a recuperação eficiente do CO2. A integração com o tratamento de águas residuais da produção de metalurgia é um aspecto chave.

**Extração Estruturada:**
- **Problema:** A sinterização do aço gera gases de exaustão contendo CO2 que representam um desperdício de recurso e um potencial emissor de gases de efeito estufa. A patente busca uma solução para capturar esse CO2 de forma eficiente.
- **Solução:** O sistema proposto utiliza um processo de absorção de gás com água, combinando-o com etapas de separação por precipitação para maximizar a captura e recuperação do CO2 dos gases de exaustão da sinterização.
- **Maturidade:** Inicial

**Achados-chave:**
- O sistema integra o tratamento de águas residuais da produção de metalurgia com a captura de CO2, promovendo a utilização de recursos.
- A arquitetura do sistema inclui unidades específicas para preparação de suspensão, absorção de gás e precipitação, otimizando a eficiência do processo.
- O uso de uma linha de retorno de supernatant permite o controle da concentração do produto final.

**Vantagens alegadas:**
- Captura eficiente de CO2 dos gases de exaustão da sinterização.
- Integração com o tratamento de águas residuais, promovendo a sustentabilidade.
- Potencial para reduzir as emissões de gases de efeito estufa.

**Limitações:**
- O documento não detalha a escala ou otimização do sistema para diferentes taxas de sinterização.
- A eficiência da captura pode depender das características específicas dos gases de exaustão (composição, temperatura).
- A patente foca na integração e arquitetura do sistema, sem fornecer detalhes sobre o desempenho operacional.

**Aplicações potenciais:**
- Siderúrgicas e fundições que utilizam processos de sinterização.
- Plantas de produção de aço com foco em sustentabilidade.
- Tecnologias de captura e utilização de carbono em outros processos industriais.

**Evidências citadas:**
> The system comprises a flue gas absorption unit…
> the upper part of the settling unit is connected to the slurry preparation unit

---

### 3. Sintering furnace with hydrogen carbon dioxide atmosphere

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_c324f3020aef` |
| **Family ID** | `family:aeab2d9ac8bbbf180ceb1dfc388fec8bd15cb8b5` |
| **ID** | `US3930787A` |
| **Inventores** | William R. DeHollander, Yogesh Nivas |
| **Titular** | General Electric Co |
| **Data** | 1976-01-06 |
| **Fonte** | Google Patents |
| **URL** | [US3930787A](https://patents.google.com/patent/US3930787A/en) |
| **Triagem** | review |
| **Rota** | manual_review |
| **Motivo da rota** | Triagem indicou revisão humana. |
| **Score de Triagem** | 6.2/10 |
| **Score de Relevância** | 6.2/10 |
| **Nível de Inovação** | Incremental |
| **Domínio Técnico** | Materials Science, Thermal Processing |
| **Cluster Temático** | Atmospheric Sintering of Oxides |
| **Papel do CO2** | componente_da_atmosfera |
| **Papel do Armazenamento** | implicit_or_support_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | forno (calor da reação) |
| **Foco das Claims** | utilização de atmosfera reativa para sinterização |
| **Categoria de Exclusão** | industrial_heat_adjacent |
| **Confiança** | 0.75 |
| **Rerank Aplicado** | Sim |
| **Motivo do Rerank** | reranked:decision_confirmed |
| **Revisão Manual** | Sim |
| **Erro LLM** | N/A |

**Abstract:**
> AbstractA heated furnace for sintering structures of uranium oxide containing composition being introduced to the furnace. The furnace receives an atmosphere comprising a mixture of hydrogen and carbon dioxide as initially introduced to the furnace, and this mixture reacts in the furnace to give the presence of water vapor and carbon monoxide.

**Avaliação do LLM:**
Esta patente descreve um forno para sinterização de óxido de urânio utilizando uma atmosfera de hidrogênio e dióxido de carbono, que produz água e monóxido de carbono como subprodutos. A principal questão é a utilização do CO2 como meio termodinâmico ou fluido de trabalho para o processo de sinterização, mas o papel exato do CO2 não é claramente definido.

**Extração Estruturada:**
- **Problema:** O problema abordado é a necessidade de um método para sinterizar estruturas de óxido de urânio em um forno, buscando otimizar as condições de atmosfera.
- **Solução:** A solução proposta envolve o uso de uma atmosfera contendo hidrogênio e dióxido de carbono dentro do forno, com a reação gerando água e monóxido de carbono. O CO2 atua como um componente da atmosfera.
- **Maturidade:** Intermediária

**Achados-chave:**
- O CO2 é introduzido na atmosfera do forno em conjunto com o hidrogênio.
- A reação da mistura resulta na produção de água vapor e monóxido de carbono.

**Vantagens alegadas:**
- Utilização de uma atmosfera reativa para a sinterização.
- Produção de subprodutos (água, monóxido de carbono) durante o processo.

**Limitações:**
- O papel do CO2 como meio termodinâmico não é explicitamente definido.
- A patente foca na reação da atmosfera e não no controle preciso das condições de sinterização.

**Aplicações potenciais:**
- Sinterização de materiais cerâmicos em ambientes controlados.
- Processos de tratamento térmico onde a remoção de subprodutos é desejada.

**Evidências citadas:**
> "A heated furnace for sintering structures of uranium oxide containing composition being introduced to the furnace."

---

### 4. Sintered ore production method

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_37bf32607be4` |
| **Family ID** | `family:a5200c7aa20ea6a27d8f045dea7533c16940024b` |
| **ID** | `WO2024117144A1` |
| **Inventores** | å æ¾æ, ä¸æ­ çå±±, æ·³æ²» é·ç°, äº«å¤ª åé |
| **Titular** | Nippon Steel Corp |
| **Data** | 2024-06-06 |
| **Fonte** | Google Patents |
| **URL** | [WO2024117144A1](https://patents.google.com/patent/WO2024117144A1/en) |
| **Triagem** | exclude |
| **Rota** | screen_only |
| **Motivo da rota** | Patente excluída na triagem. |
| **Score de Triagem** | 3.5/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | Metalurgia, Sinterização |
| **Cluster Temático** | Processos de Fabricação de Materiais |
| **Papel do CO2** | co2_not_central |
| **Papel do Armazenamento** | explicit_thermal_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | not_clear |
| **Fonte/Sumidouro Térmico** | industrial_heat |
| **Foco das Claims** | process_integration |
| **Categoria de Exclusão** | low_alignment |
| **Confiança** | 0.64 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> AbstractThis sintered ore production method is for producing sintered ore using a Dwight-Lloyd type sintering machine that progresses sintering through downward suction and that includes an ignition furnace that performs initial ignition and a reignition furnace that performs reignition and that is located apart from the ignition furnace by a predetermined interval on the downstream side thereof. In the method, as a coagulation agent for raw materials to be blended, a low-combustion carbon material having a combustion start temperature of higher than 550Â°C and a high-combustion carbon material having a combustion start temperature of not higher than 550Â°C are used, and, in the high-combustion carbon material, the proportion of particles having a size of 2.8 mm or greater is 30-80 mass%.

**Evidências citadas:**
> AbstractThis sintered ore production method is for producing sintered ore using a Dwight-Lloyd type sintering machine that progresses sintering through downward suction...
> a low-combustion carbon material having a combustion start temperature of higher than 550Â°C and a high-combustion carbon material having a combustion start temperature of not higher than 550Â°C

---

### 5. Dispensing Device

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
| **URL** | [1171698](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135354895&_cid=P21-MR8FS7-09117-1) |
| **Triagem** | exclude |
| **Rota** | screen_only |
| **Motivo da rota** | Patente excluída na triagem. |
| **Score de Triagem** | 3.3/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | Engenharia de Fluidos, Dispositivos Dispensadores |
| **Cluster Temático** | Dispensação de fluidos com gases comprimidos |
| **Papel do CO2** | working_fluid |
| **Papel do Armazenamento** | implicit_or_support_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | refrigeration_cycle |
| **Fonte/Sumidouro Térmico** | cooling_or_refrigeration |
| **Foco das Claims** | component_or_operation |
| **Categoria de Exclusão** | generic_tes |
| **Confiança** | 0.52 |
| **Rerank Aplicado** | Não |
| **Motivo do Rerank** | N/A |
| **Revisão Manual** | Não |
| **Erro LLM** | N/A |

**Abstract:**
> (EN)1, 171, 698. Dispensing liquids by gaseous pressure. DISTILLERS CO. (CARBONDIOXIDE) Ltd. April 11, 1968 (April 11, 1967], No.16511/67. Heading F1R. A dispenser of liquids from a container comprises a body provided with means for attaching the dispenser to the container, a sharp tube capable of piercing a hole in the lid of the container, a seal on the underside of the body surrounding the tube which when the dispenser is attached to the container forms a substantially gas-tight chamber around the tube, the chamber being in communication with the interior of the container via the hole in the lid, a supply ofcarbondioxideunder pressure with which the chamber is in communication via a non-return valve, and a delivery tube housed within the sharp tube which communicates with a dispensing tube projecting from the body of the device. After removal of a dip tube 8, a sharp tube 1 is forced into the lid of a beer can to form a hole. The dip tube 8 is then refitted and a screw thread 3 is screwed into the hole in the lid until a seal 43, which may be of silicone rubber, is in sealing engagement with the lid. A capsule 21 of high-pressurecarbondioxideis placed in a holder 20 and a cap 22 is screwed on, a pin 23 on the cap piercing the capsule. High-pressurecarbondioxidepasses through a pressure reducing valve, asinteredmetal filter 34, and a capillary tube 29 to a low-pressure chamber 25. The pressure reducing valve is formed by the engagement of the end of the capillary tube 29 with a polyurethane pad 30, the capillary tube being pressed against the pad by a piston 26 subjected to the pressure in the low-pressure chamber 25 and the opposing force of a spring 27. From the low-pressure chamber 25, the low-pressurecarbondioxidepasses via a duct 39, a duct (38) and a non-return valve (44) into the space between the seal 43 and the sharp tube 1 and thence into the beer can. On depression of a button 5 to the position shown, a bore 11 is brought adjacent a port 12 to allow beer, urged by thecarbondioxideto be delivered via the dip tube 8, bores 10, 11, port 12 and a dispensing tube 13. A relief valve (45) vents excessive pressure to atmosphere. Castellations 55 cooperate with pins (56) depending from the button 5 so that by rotating the button the dispenser can be locked into a non-dispensing state. Instead of a screw thread 3, spring members hooking over the rim of the can may be used. Alternatively, a bayonet-type joint may be used with cans provided with the necessary fitment. The pin 23 can be provided at the other end of the holder 20, projecting from the pad 30. Provision may be made for holding twocarbondioxidecapsules with interchangeable connections to the interior of the can. Thecarbondioxidesupply may be a large cylinder of liquidcarbondioxideunder pressure.

**Evidências citadas:**
> High-pressurecarbondioxidepasses through a pressure reducing valve, asinteredmetal filter 34...
> After removal of a dip tube 8, a sharp tube 1 is forced into the lid...

---

### 6. A Dispensing Device for Gases Under Pressure.

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
| **URL** | [1174314](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB135357801&_cid=P21-MR8FS7-09117-1) |
| **Triagem** | review |
| **Rota** | manual_review |
| **Motivo da rota** | Falha do LLM; revisão humana necessária. |
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
| **Erro LLM** | Resposta inválida ou não estruturada do modelo na triagem. |

**Abstract:**
> (EN)1,174,314. Valves. DISTILLERS CO. (CARBONDIOXIDE) Ltd. 22 May, 1968 [25 May, 1967], No. 24270/67. Heading F2V. Universal dispensing device for supplyingcarbondioxideat suitable reduced pressures to various appliances such as, soda syphones, fire extinguishers, dinghies, life-rafts and tyre inflators from a container comprises a reducing valve 12, 14 operated by a diaphragm 13 exposed to pressure in an outlet chamber 13. A loading spring 17 for the diaphragm is adjustable by a screwed retainer 16 connected through a rack and pinion device to pins 31 slidable in an outlet connection 28 and adapted to form a bayonet connection with the appliance. The appliances are arranged so that connection can only be made when the device is adjusted to supply the gas at the required pressure. A trigger operated valve 25 is in series with the reducing valve. The latter comprises a capillary tube 12 connected to the diaphragm and passing through an 0-ring seal to engage a seat 14 carried in a porous plug 10. A piercing member 6 opens the container as the device is coupled. The setting is indicated on a plate 5. A relief valve 19 is included.

**Evidências citadas:**
> (EN)1,174,314. Valves. DISTILLERS CO. (CARBONDIOXIDE) Ltd. 22 May, 1968 [25 May, 1967], No. 24270/67. Heading F2V. Universal dispensing device for supplyingcarbondioxideat suitable reduced pressures to various appliances such as, soda sypho

---

### 7. NOZZLE FOR PRESSURISING AND DISPENSING LIQUID FROM CAN

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_e9a9df09739a` |
| **Family ID** | `family:08f7bea9e7ba9897b7973352892807cd494fc3f7` |
| **ID** | `153069` |
| **Inventores** | W E Mole |
| **Titular** | The Distillers Co. (
Carbon
Dioxide
) Ltd. |
| **Data** | 16.04.1970 |
| **Fonte** | Patentscope |
| **URL** | [153069](https://patentscope.wipo.int/search/en/detail.jsf?docId=NZ178918854&_cid=P21-MR8FS7-09117-1) |
| **Triagem** | exclude |
| **Rota** | screen_only |
| **Motivo da rota** | Patente excluída na triagem. |
| **Score de Triagem** | 3.5/10 |
| **Score de Relevância** | 0.0/10 |
| **Nível de Inovação** | N/A |
| **Domínio Técnico** | Engenharia Mecânica / Processamento de Materiais |
| **Cluster Temático** | Dispositivos de Dispensação e Sinterização de Gases |
| **Papel do CO2** | stored_thermodynamic_medium |
| **Papel do Armazenamento** | implicit_or_support_storage |
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
> (EN)The dispensing device fitted to a sealed can of liquid has a cutting tube 1 with threads 3 through which passes a dispensing tube 8 along which liquid passes to outlet tube 13. Acarbondioxidecontainer 21 is contained in an outer casing 22 and when punctured by sharp device 23 the gas passes out through asinteredmetal filter 34 and tube 39 to a low pressure chamber 25. When the button 5 is depressed liquid passes out of the tubes and is replaced in the can bycarbondioxidethe pressure of which assists in the passage of liquid up and out of the tube.

**Evidências citadas:**
> “Acarbondioxidecontainer 21 is contained in an outer casing 22 and when punctured by sharp device 23 the gas passes out through asinteredmetal filter 34…”

---

### 8. Improvements in or relating to the production of
sintered
uranium
dioxide

| Campo | Valor |
|-------|-------|
| **Record ID** | `rec_bbd3a7e262bb` |
| **Family ID** | `family:65272d16dba3149592d4866a190bc57eed8641c7` |
| **ID** | `910517` |
| **Inventores** | RUSSELL LEWIS ERIC, HARRISON JOHN DAVID LAWRENCE, BRETT NORMAN HARRY |
| **Titular** | ATOMIC ENERGY AUTHORITY UK |
| **Data** | 14.11.1962 |
| **Fonte** | Patentscope |
| **URL** | [910517](https://patentscope.wipo.int/search/en/detail.jsf?docId=GB134822149&_cid=P21-MR8FS7-09117-1) |
| **Triagem** | review |
| **Rota** | manual_review |
| **Motivo da rota** | Triagem indicou revisão humana. |
| **Score de Triagem** | 6.4/10 |
| **Score de Relevância** | 5.9/10 |
| **Nível de Inovação** | Incremental |
| **Domínio Técnico** | Ceramic Materials & Nuclear Fuel Production |
| **Cluster Temático** | Sinterization of Oxide Fuels |
| **Papel do CO2** | stored_thermodynamic_medium |
| **Papel do Armazenamento** | implicit_or_support_storage |
| **Limite Sistêmico** | process_integration |
| **Tipo de Ciclo** | não_claro |
| **Fonte/Sumidouro Térmico** | CO2 atmosphere |
| **Foco das Claims** | component_or_operation |
| **Categoria de Exclusão** | industrial_heat_adjacent |
| **Confiança** | 0.71 |
| **Rerank Aplicado** | Sim |
| **Motivo do Rerank** | reranked:decision_confirmed |
| **Revisão Manual** | Sim |
| **Erro LLM** | N/A |

**Abstract:**
> (EN)Asinteredbody of high density containing uraniumdioxideore as mixture thereof with, preferably 10-30% plutoniumdioxide, for use as a fuel element in a fast neutron reactor, is obtained by heating a compressed body of uraniumdioxide, or mixture thereof with plutoniumdioxide, to at least 1300 DEG C. in an atmosphere consisting ofcarbondioxide, or a mixture thereof withcarbonmonoxide.  If CO2 alone is used the maximumsinteringtemperature is 1550 DEG C.  The CO/CO2 volumetric ratio may range from 1:100 to 100:1.  The preferred range for a 10% PuO2, 90% UO2 being 1:100 to 1:10 and for a 30% PuO2 70% UO2 from 1:20 to 1:1, duringsinteringat 1400 DEG -1600 DEG C. Asinteredbody having a metal / oxygen atomic ratio 1,98 to 2.02:1 is produced by cooling in a reducing atmosphere, preferably a CO/CO2 atmosphere of volumetric composition range 1:10 to 100:1 although hydrogen or hydrogen containing water vapour may be used.  The density of thesinteredproduct, depends uponsinteringtime and attains a maximum value and diminishes thereafter.  Optimum times, determined by experiment, are between 3-6 hours.  Thus in Example 1 a mixture of 10% plutoniumdioxide90% uraniumdioxidewere ball milled and polybutyl methacrylate in toluene were added as a binder.  After drying the granules were double pressed into pellets, which were heated at 400 DEG C. then to 1500 DEG C. in a CO2 atmosphere, and maintained at 1500 DEG C. for 4 hours.  The resulting pellets had a theoretical density of 96% and had an oxygen/metal ratio of 2,14/1. Other examples refer to the use of CO/CO2 mixtures duringsinteringand H2 or H2 and water vapour during cooling.  Specification 881,883 is referred to.

**Avaliação do LLM:**
Esta patente descreve um processo de sinterização para produzir corpos de óxido de urânio misturado com plutônio, utilizando uma atmosfera de dióxido de carbono (CO2) como meio termodinâmico. A temperatura de sinterização é ajustada dependendo da proporção de CO2 e monóxido de carbono, visando obter alta densidade e controlar a relação oxigênio/metal no produto final. O processo envolve etapas de aquecimento em CO2 seguido por resfriamento em atmosfera redutora com CO2 ou hidrogênio.

**Extração Estruturada:**
- **Problema:** O problema técnico abordado é a necessidade de produzir corpos de óxido de urânio e plutônio sinterizados com densidade e composição desejadas para uso como combustível em reatores rápidos, otimizando o processo de sinterização.
- **Solução:** A solução proposta consiste em aquecer uma mistura de óxidos de urânio e plutônio sob uma atmosfera de CO2 (ou misturas de CO/CO2) a temperaturas entre 1300°C e 1600°C, ajustando as proporções para influenciar a densidade e a composição do produto sinterizado. O resfriamento subsequente é realizado em uma atmosfera redutora com CO2 ou hidrogênio.
- **Maturidade:** Intermediária

**Achados-chave:**
- A sinterização ocorre com sucesso em atmosferas de CO2, com a temperatura máxima dependendo da proporção de CO/CO2 utilizada (1:100 a 100:1).
- O controle da relação oxigênio/metal no produto final é alcançado através da manipulação das condições de sinterização e resfriamento, utilizando atmosferas de CO/CO2 ou H2/H2O.

**Vantagens alegadas:**
- Produção de corpos de óxido de urânio e plutônio com alta densidade e composição controlada.
- Utilização do CO2 como meio termodinâmico para o processo de sinterização.

**Limitações:**
- A temperatura máxima de sinterização é limitada pela presença de CO2, necessitando de misturas de CO/CO2 para atingir temperaturas mais elevadas.
- O controle preciso da relação oxigênio/metal depende da otimização das condições experimentais.

**Aplicações potenciais:**
- Produção de combustível para reatores rápidos de nêutrons rápidos.
- Desenvolvimento de novos materiais cerâmicos com propriedades específicas.

**Evidências citadas:**
> "Asinteredbody of high density containing uraniumdioxideore as mixture thereof..."
> The CO/CO2 volumetric ratio may range from 1:100 to 100:1.

---

## 🧾 Fila de Revisão Manual

- rec_56073152026b (1174314) | rota=manual_review | motivo=Falha do LLM; revisão humana necessária. | erro_llm=Resposta inválida ou não estruturada do modelo na triagem.
- rec_72a65e6eb3eb (CN113941247A) | rota=manual_review | motivo=Triagem indicou revisão humana. | erro_llm=N/A
- rec_8d21878ddc6f (JP6833123B1) | rota=manual_review | motivo=Triagem indicou revisão humana. | erro_llm=N/A
- rec_bbd3a7e262bb (910517) | rota=manual_review | motivo=Triagem indicou revisão humana. | erro_llm=N/A
- rec_c324f3020aef (US3930787A) | rota=manual_review | motivo=Triagem indicou revisão humana. | erro_llm=N/A

---

## 🔬 Análise Comparativa

### 1. Panorama Geral

- O conjunto comparativo agrega 4 patente(s) e nao deve ser tratado como bloco homogeneo: ha um nucleo direto, fronteiras tecnicas em revisao e adjacencias uteis apenas para delimitar whitespace [IDs: CN113941247A, JP6833123B1, US3930787A, 910517]
- O subgrupo mais diretamente alinhado ao núcleo da query é CN113941247A, com foco em armazenamento de CO2, compressão/expansão e controle termodinâmico do meio armazenado [IDs: CN113941247A]
- CN113941247A, JP6833123B1, US3930787A, 910517 formam a fronteira tecnica: sao casos proximos do problema, mas ainda ambiguos quanto ao papel exato do CO2 no armazenamento ou na funcao arquitetural central [IDs: CN113941247A, JP6833123B1, US3930787A, 910517]
- 910517 entram como adjacencia exploratoria: tratam CO2 principalmente como fluido de trabalho em transferencia termica ou distribuicao de energia, de modo que ajudam a delimitar combinacoes pouco cobertas sem virar evidencia de cobertura consolidada [IDs: 910517]

## Análise Comparativa de Patentes: "Sintering Carbon Dioxide"

### 2. Tendências Identificadas

As principais tendências tecnológicas observadas são:

*   **Utilização do CO2 como Meio Termodinâmico:** A predominância da utilização do CO2 como um meio termodinâmico para controlar a temperatura e promover as reações de sinterização é uma tendência central [IDs: CN113941247A, JP6833123B1, US3930787A, 910517].
*   **Integração com Outros Gases:** A combinação do CO2 com outros gases como hidrogênio para otimizar as condições de sinterização é uma área explorada [IDs: JP6833123B1, CN113941247A].
*   **Controle da Atmosfera e Composição:** A manipulação precisa da composição da atmosfera (proporções de gases, adição de aditivos) para influenciar a cinética da sinterização é uma preocupação constante [IDs: JP6833123B1, CN113941247A, 910517].
*   **Aplicação em Materiais Específicos:** A aplicação do método de sinterização com CO2 se concentra principalmente na produção de óxidos metálicos, especialmente para aplicações nucleares [IDs: CN113941247A, 910517].

### 3. Whitespaces e Oportunidades

- Gestao termica transiente, subresfriamento e acoplamentos com captura/reatores aparecem de forma lateral; isso sugere oportunidade em claims de controle, operacao multi-regime e integracao de processo ainda pouco amarradas ao armazenamento central [IDs: 910517, CN113941247A, JP6833123B1, US3930787A]
- As patentes em review delimitam fronteiras tecnicas onde o papel do CO2 ainda esta ambiguo entre meio armazenado, fluido de trabalho e interface de troca termica; esse tipo de ambiguidade costuma ser um bom proxy para whitespace exploravel com recorte arquitetural mais especifico [IDs: CN113941247A, JP6833123B1, US3930787A, 910517]

### 4. Recomendações

- Priorizar arquiteturas centradas em armazenamento explícito de CO2 e controle termodinâmico rigoroso [IDs: CN113941247A]

### 5. Ranking Final

1. **CN113941247A** — armazenamento termico explicito como parte central; score 6.5/10 [IDs: CN113941247A]
2. **JP6833123B1** — alinhamento técnico sustentado pelas evidências extraídas; score 6.5/10 [IDs: JP6833123B1]
3. **US3930787A** — armazenamento aparece mais como subsistema de apoio; score 6.2/10 [IDs: US3930787A]
4. **910517** — CO2 aparece como meio termodinamico armazenado; armazenamento aparece mais como subsistema de apoio; score 5.9/10 [IDs: 910517]

### 6. Mapa de Evidências por ID

- **Atmospheric Sintering of Oxides** [IDs: US3930787A]
- **Captura de CO2 de Fontes Industriais** [IDs: CN113941247A]
- **Sinterization of Oxide Fuels** [IDs: 910517]
- **Sinterização e Adsorção de Dióxido de Carbono** [IDs: JP6833123B1]

### 7. Ranking por ID

1. **CN113941247A** — score 6.5/10 [IDs: CN113941247A]
2. **JP6833123B1** — score 6.5/10 [IDs: JP6833123B1]
3. **US3930787A** — score 6.2/10 [IDs: US3930787A]
4. **910517** — score 5.9/10 [IDs: 910517]

---

## 🧭 Matriz de Whitespaces

- **Patentes selecionadas:** 4
- **Núcleo:** 0
- **Fronteira:** 4
- **Adjacência:** 0


---

## ℹ️ Informações do Sistema

- **Gerado por:** Agente de Web Scraping de Patentes
- **Modelo LLM:** gemma3:4b
- **Data de geração:** 05/07/2026 23:58:03
- **Query de busca:** `sintering carbon dioxide`
- **Status da execução:** completed
- **Tempo total:** 924.6s
- **LLM disponível:** sim
- **Fila de revisão manual:** 5 itens
- **Snapshot hash:** `c61e1cdb0eaad0ae3121308b91efcc099f8cfbb30c6b8aba104af02497c3630c`
- **Features habilitadas:** require_evidence, enable_thematic_clusters, enable_structural_roles, enable_screening_rerank, enable_prisma, enable_snapshot, enable_comparative_analysis, enable_whitespace_analysis, enable_manual_review_queue
- **Features desabilitadas:** nenhum
- **Versão do pipeline:** 1.1
- **Thresholds snapshot:** include=7.0, review=4.5
- **Cache LLM:** 0 hits, 17 misses, 125 entradas
- **Status do rascunho:** ready