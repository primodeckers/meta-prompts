# Transcript — Sessão `/grill-me` (Parte C)

**Serviço:** Obter passaporte comum para brasileiro (Polícia Federal)  
**Participante:** Rene Estevam Deckers  
**Contexto:** `B_relatorio_assistente_v3.md`, metodologia `aula02.pdf` (Passos 0–5)  
**Ferramenta:** Claude Code — skill `/grill-me` (sessão conduzida com apoio do assistente; Claude CLI indisponível no ambiente local)

---

## Rodada 1 — Propósito do mapa (Passo 0)

**Claude:** Qual risco ou problema concreto este mapa de atores deve endereçar? Não aceito "mapear o passaporte" — preciso do *porquê*.

**Rene:** O mapa endereça **demanda falha (failure demand)** na jornada digital do passaporte: (1) cidadãos que tentam agendar antes da compensação da GRU e recontatam canais de suporte; (2) exclusão digital no preenchimento web, empurrando o cidadão a despachantes; (3) cancelamento automático após 90 dias sem retirada, gerando reinício completo da jornada com nova taxa. O propósito é orientar um redesenho que reduza recontatos evitáveis e perdas de taxa por fricção de design — não por exigência legal de biometria presencial.

---

## Rodada 2 — Escopo de atores (Passo 1)

**Claude:** Você listou dezenas de atores na v3. Para um mapa acionável, quantos incluir e qual critério de corte?

**Rene:** Incluo **10 atores** que (a) aparecem em etapa distinta da jornada ou (b) explicam failure demand documentada na v3. Critério de corte: excluo MJSP, MGI, SERPRO e ICAO como atores separados neste mapa — ICAO e normas internacionais entram como **fricção estrutural** citada na decisão sobre biometria, não como nó operacional diário. SERPRO fica implícito na sustentação do SINPA. Foco na **linha cidadão → sistemas → posto → fabricação → controle**.

---

## Rodada 3 — Cidadão e exclusão digital

**Claude:** "Cidadão requerente" é um só ator ou você separa perfis (primeira viagem, renovação, analfabeto digital)?

**Rene:** **Um ator** — "Cidadão requerente" — porque o mapa é operacional, não persona. Registro na decisão que a failure demand de exclusão digital afeta sobretudo quem não domina o SINPA/PagTesouro; despachantes capturam esse subgrupo. Não subdivido em personas no RACI para não inflar a matriz.

---

## Rodada 4 — Sistemas: SINPA vs Gov.br

**Claude:** Gov.br e SINPA entram separados ou fundidos?

**Rene:** **Só SINPA** como sistema no mapa. Gov.br é portal de entrada; na v3 está pendente se é barramento ou indexador. Para o mapa operacional, o gargalo digital está no **SINPA** (formulário, validação de GRU, agendamento, consulta). Gov.br menciono no transcript como canal, não como linha do RACI.

---

## Rodada 5 — Pagamento e compensação bancária

**Claude:** PagTesouro, SIAR, bancos arrecadadores — quantos atores?

**Rene:** Agrupo em **"Rede de arrecadação (PagTesouro / Bancos arrecadadores / SIAR-PF)"** como um ator-sistema. Motivo: a failure demand da rodada 1 nasce do **intervalo entre pagamento e liberação do agendamento**; tecnicamente envolve PagTesouro, boleto bancário e arquivo de retorno ao SIAR — separar bancos individuais não muda a ação de redesenho (status de compensação visível ao cidadão). Decisão explícita da rodada 1.

---

## Rodada 6 — Linha de frente

**Claude:** Atendente terceirizado e policial federal — mesmo ator ou dois?

**Rene:** **"Operador de posto PF (policial + apoio terceirizado)"** como um ator de linha de frente. Ambos executam triagem, biometria e entrega; a v3 mostra que terceirizados absorvem descontentamento por falhas dos sistemas centrais. Para RACI, quem **executa** presencialmente é essa célula de posto, reportando à DPas.

---

## Rodada 7 — Fabricação e normatização

**Claude:** Casa da Moeda entra? Ela interage com o cidadão?

**Rene:** Sim, **Casa da Moeda do Brasil (CMB)** entra. Não fala com o cidadão, mas é ator crítico entre coleta biométrica e retirada: atraso ou ruptura de empenho gera failure demand indireta (consultas de andamento, reagendamentos). Incluo porque o cancelamento por 90 dias (IN 173/2020) desperdiça caderneta fabricada — liga fricção regulatória a ator de supply chain.

---

## Rodada 8 — Intermediários e controle social

**Claude:** Despachantes são ator legítimo ou ruído?

**Rene:** **Despachantes e assessorias de passaporte** entram como ator de **intermediário** (Mendelow: monitorar). Não são parte do governo, mas a v3 documenta que exploram assimetria informacional do digital-only — failure demand paga duas vezes (taxa GRU + serviço privado). O mapa precisa deles para explicar por que simplificar UX no SINPA é alavanca de política pública.

**Claude:** E ouvidoria / CGU?

**Rene:** Incluo **Ouvidoria da Polícia Federal** como ator de controle social operacional — canal onde convergem reclamações de compensação GRU, agendamento e conduta em postos (v3, demanda falha). CGU/TCU ficam fora deste mapa operacional; fiscalização orçamentária não entra no RACI da jornada do cidadão.

---

## Rodada 9 — Receita Federal e cartórios

**Claude:** Receita Federal — bloqueia ou só consulta CPF?

**Rene:** Decisão conservadora alinhada à audit_v2: incluo **Receita Federal (base CPF)** como ator, papel **Consultado (C)** na validação cadastral. **Não** afirmo bloqueio automático no SINPA — na v3 isso está pendente. No mapa, RFB entra na etapa de preenchimento/triagem por consistência de dados biográficos.

**Claude:** Cartórios para menores?

**Rene:** Incluo **Cartórios e notários (Registro Civil / Tabelionato)** como ator único de **cadeia documental**: certidões, firma reconhecida, autorização de genitor ausente. Fricção estrutural em menores (IN 173 + CNJ) gera failure demand quando documentação cartorial está incompleta no dia do posto.

---

## Rodada 10 — Gestor e formatos do artefato

**Claude:** DPas entra como aprovador de quê?

**Rene:** **Divisão de Passaportes (DPas/PF)** entra como **Aprovador (A)** de regras procedimentais e gestor do serviço — normatiza fluxo, responde por metas e interface com orçamento para postos e CMB. Plausível na v3, pendente de portaria — aceito no mapa como decisão institucional do grill.

**Claude:** RACI ou mermaid?

**Rene:** **Tabela RACI** com colunas de entrada/saída na jornada — mais claro para 10 atores e rubrica do exercício. Diagrama mermaid opcional no mesmo arquivo como visão de fluxo.

**Claude:** Algum ator-chave faltando?

**Rene:** **Sistema ABIS (biometria PF)** não entro como linha separada — está subordinado ao operador de posto e à fricção estrutural ICAO/biometria presencial. **CNJ** absorvido dentro de "Cartórios e notários" para autorização de menores. Lista fechada em 10 atores; mapa em `C_mapa_atores.md`.

---

## Síntese das decisões (para consistência transcript ↔ mapa)

| Decisão | Escolha |
| --- | --- |
| Propósito | Failure demand: GRU, exclusão digital, 90 dias |
| Formato | RACI + mermaid auxiliar |
| Atores no mapa (10) | Cidadão requerente; SINPA; Rede de arrecadação; Operador de posto PF; Casa da Moeda; Despachantes; Ouvidoria PF; Receita Federal; Cartórios/notários; DPas/PF |
| Fora do mapa | Gov.br (canal), SERPRO, ICAO, CGU/TCU, ABIS (subordinado ao posto) |
