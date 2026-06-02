# Meta-prompt — Exercício 2.1 (Parte A)

## Contexto que anexo ao pedido

Estou mapeando os **atores da jornada** do serviço público **"Obter passaporte comum para brasileiro"**, prestado pela **Polícia Federal (PF)** em território nacional, conforme a ficha oficial no [gov.br](https://www.gov.br/pt-br/servicos/obter-passaporte-comum-para-brasileiro#etapas-para-a-realizacao-deste-servico).

A jornada tem **seis etapas** principais, com canais distintos:

1. **Preencher formulário** (web) — verificação prévia de documentação; gera protocolo; até ~10 min.
2. **Pagar taxa** (web: PagTesouro/PIX, cartão ou boleto) — taxa comum R$ 257,25; prazo de pagamento entre 24–72 h.
3. **Agendar atendimento** (web) — escolha de posto PF; entrega ocorre na **mesma unidade**; prazo máximo de retirada 90 dias.
4. **Comparecer presencialmente** (posto PF) — conferência documental, coleta biométrica (digitais + foto); prazo de produção ~6–10 dias úteis.
5. **Consultar andamento** (web).
6. **Retirar passaporte** (presencial, mesma unidade) — somente ao titular (regras específicas para menores).

Pontos que já observo e quero que a pesquisa explore:

- Serviço **100% digitalizado desde 2009** — sem fallback offline se o sistema cair.
- PF **não possui call center** para passaporte; dúvidas via FAQ/ouvidoria.
- Risco de **páginas falsas** e frustração quando pagamento não gera protocolo.
- **Failure demand** potencial: reagendamento, taxa adicional (urgência, passaporte extraviado), cancelamento por não retirada em 90 dias.
- Atores além da linha de frente: PagTesouro/Tesouro Nacional, fornecedores de TI/biometria, CGU/TCU, ouvidoria, conselhos de usuários (Lei 13.460/2017).

---

## Meta-prompt (texto a colar no Assistente 1)

Preciso de ajuda para **elaborar um prompt detalhado** que eu usarei em outra sessão de IA com **Deep Research** (pesquisa profunda com fontes).

**Meu problema:** Vou produzir um **mapa de atores** da jornada do serviço **"Obter passaporte comum para brasileiro"** (Polícia Federal, canal web + atendimento presencial em postos). Não quero ainda o mapa final — quero **material de pesquisa estruturado** que reduza lacunas de contexto antes de uma sessão de destilação posterior. Num contexto real eu entrevistaria stakeholders; como não tenho acesso a eles, preciso compensar com pesquisa rigorosa e fontes verificáveis.

**Objetivo da pesquisa:** Identificar e caracterizar **todos os atores** que participam, influenciam ou controlam essa jornada — não só o cidadão e o atendente PF. Incluir sistemas automatizados, gestores, órgãos normativos e de controle, fornecedores, intermediários (se houver), e vozes de controle social.

**Contexto que já tenho** (use como ponto de partida, mas valide e expanda):

- Jornada em 6 etapas: formulário web → pagamento (PagTesouro) → agendamento → atendimento presencial (biometria) → consulta de andamento → retirada.
- Taxa GRU via PagTesouro; posto de atendimento = posto de entrega; prazo de retirada 90 dias.
- Serviço digital-only; indisponibilidade do sistema não tem procedimento presencial alternativo.
- Normas: Decreto 1.983/1996, IN PF 173/2020, Lei 13.460/2017 (atendimento ao usuário).
- Avaliação no gov.br: nota ~4,8 (dezenas de milhares de avaliações) — sinal de maturidade digital com possíveis fricções residuais.

**O prompt que você elaborar deve instruir o pesquisador a:**

1. Descrever a **jornada atual** passo a passo, citando canais e sistemas envolvidos em cada etapa.
2. Listar **atores** em camadas: usuários diretos; operadores de linha de frente; gestores/decisores; órgãos de controle (CGU, TCU, MP se aplicável); fornecedores de TI e biometria; intermediários; normatizadores/judiciário.
3. Para cada ator relevante, indicar **papel na jornada**, **poder/interesse** (referência Mendelow) e **incentivos ou resistências** à simplificação do serviço.
4. Identificar **pontos de fricção** e **demanda falha** (failure demand) — recontatos, filas, reagendamentos, cancelamentos, judicialização, ouvidoria.
5. Diferenciar **fricção estrutural** (exigência legal/normativa) de **fricção de design** (UX, informação, exclusão digital).
6. Citar **fontes primárias ou secundárias confiáveis** (gov.br, PF, TCU/CGU, legislação, notícias jornalísticas verificáveis, estudos acadêmicos) — marcar claramente o que é inferência vs. evidência documentada.
7. Sinalizar **lacunas** onde não houver evidência pública (ex.: contratos de TI, organograma operacional interno da PF).
8. Incluir atores frequentemente **omitidos** em mapas ingênuos: PagTesouro, SERPRO ou fornecedores do sistema, ouvidoria PF, conselho de usuários, jornalismo de dados, entidades de controle social.

**Critério de sucesso:** O relatório deve permitir que eu, sem entrevistar ninguém, tome **decisões informadas** sobre quais 7+ atores incluir num mapa RACI ou diagrama de fluxo, com justificativa baseada em evidência — não lista genérica de "governo" e "cidadão".

**Formato pedido no prompt:** prosa estruturada com seções numeradas; tabela-resumo de atores ao final; bibliografia com URLs quando possível.

**Restrições:** foco em **passaporte comum no Brasil** (não passaporte no exterior, não diplomático/oficial); português do Brasil; não inventar dados operacionais internos — marcar como pendente se não houver fonte.

Por favor, **elabore o prompt completo** que eu copiarei e colarei no Deep Research. Não execute a pesquisa agora — apenas produza o prompt otimizado para isso.