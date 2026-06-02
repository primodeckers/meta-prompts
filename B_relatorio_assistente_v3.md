# Relatório de Pesquisa Documental: Ecossistema de Atores, Sistemas e Jornada do Passaporte Comum no Brasil (v3)

## 1. Mapeamento e Análise Detalhada da Jornada

O serviço de emissão de passaporte comum para brasileiros, gerido pela Polícia Federal (PF), é estruturado sob uma lógica de dependência sequencial de etapas, atuando como um fluxo de validação de dados e segurança jurídica. O serviço engloba canais digitais e atendimento presencial. Sob a ótica de evidência documentada, o serviço possui um gargalo físico devido à necessidade de verificação biométrica e documental presencial. A análise detalhada das seis etapas operacionais e suas contingências técnicas revela o seguinte funcionamento sistêmico:

### Etapa 1: Preenchimento do Formulário Web (SINPA)

- **Canais e Sistemas de TI Envolvidos:** O canal de interação primário é o portal unificado Gov.br, que atua como interface de acesso e redireciona o cidadão para o Sistema Nacional de Passaportes (SINPA) da Polícia Federal.
- *FATO DOCUMENTADO:* O SINPA é o sistema oficial utilizado para a inserção de dados biográficos do requerente.
- *PENDENTE (Abordando audit_v2 — Falha 2 parcial):* Está classificado como pendente a demonstração formal, por meio de documentação de arquitetura de TI pública, do papel tecnológico exato do Gov.br na jornada e se ele atua ou não como barramento obrigatório de autenticação no SINPA ou se configura apenas um indexador unificado de serviços do Executivo Federal.
- *PENDENTE (Abordando audit_v2 — Falha 1):* Está em aberto e carece de validação em fontes públicas oficiais se o SINPA é classificado tecnicamente como software livre, bem como a confirmação de sua arquitetura de infraestrutura (como o uso de servidores JBoss, linguagem Java ou desenvolvimento exclusivo em parceria com o SERPRO).

**Contingência de Falha do Sistema Web:**

- *FATO DOCUMENTADO (Abordando audit_v2 — Falha 18 e 19):* A Instrução Normativa nº 173/2020-DG/PF prevê mecanismos de atuação da autoridade migratória, mas o formulário de solicitação inicial padrão permanece exclusivamente eletrônico via web. Em caso de indisponibilidade total dos servidores centrais, o cidadão fica impossibilitado de iniciar o requerimento.
- *INFERÊNCIA (Abordando audit_v2 — Nova Falha N3):* Deduz-se que a indisponibilidade do formulário web gera uma interrupção temporária na entrada da jornada, impedindo que novas solicitações sejam internalizadas até o restabelecimento da conectividade com o banco de dados da Polícia Federal.
- *PENDENTE (Abordando audit_v2 — Nova Falha N1 e N2):* Está classificado como pendente mapear se o SINPA realiza uma consulta automatizada em tempo real às bases da Receita Federal no momento do preenchimento do formulário web e se divergências ou irregularidades no CPF geram um bloqueio eletrônico impeditivo imediato nesta fase inicial.

### Etapa 2: Pagamento da Taxa Administrativa (PagTesouro / GRU)

- **Canais e Sistemas de TI Envolvidos:** A quitação da taxa de emissão (R$ 257,25 para o passaporte comum) é realizada por meio da Guia de Recolhimento da União (GRU).
- *FATO DOCUMENTADO (Abordando audit_v2 — Falha 3):* O PagTesouro é uma das plataformas integradas de pagamento (permitindo Pix e cartão de crédito), mas o recolhimento da GRU pode ocorrer por meio de toda a rede bancária conveniada, incluindo código de barras para pagamento em agências físicas, correspondentes bancários, lotéricas e internet banking. Os bancos arrecadadores atuam como agentes de recebimento e repasse desses valores à Conta Única do Tesouro Nacional.

**Contingência de Falha do Sistema Web:**

- *FATO DOCUMENTADO (Abordando audit_v2 — Falha 4):* A Polícia Federal orienta formalmente em seus canais de atendimento que o agendamento seja realizado somente após o processamento da compensação bancária. O prazo de compensação pode variar de algumas horas (para Pix/PagTesouro) até 24 a 48 horas úteis para boletos bancários tradicionais, a depender do tempo de transmissão do arquivo de retorno pelos bancos arrecadadores ao Sistema de Arrecadação (SIAR) da PF.
- *PENDENTE (Abordando audit_v2 — Nova Falha N6):* Fica mapeado como pendente de validação documental se os horários rígidos de fechamento bancário e as janelas de transmissão de arquivos de retorno de cada banco geram, de forma documentada, um impacto direto e mensurável na experiência de agendamento em tempo real do SINPA.

### Etapa 3: Agendamento Eletrônico de Atendimento

- **Canais e Sistemas de TI Envolvidos:** O agendamento ocorre no ambiente do SINPA após a validação do pagamento da GRU no sistema interno da Polícia Federal, cruzando os dados biográficos do requerente com a confirmação do recolhimento financeiro.

**Contingência de Falha do Sistema Web:**

- *FATO DOCUMENTADO (Abordando audit_v2 — Falha 5):* Com base na Instrução Normativa nº 173/2020-DG/PF, as situações de urgência emergencial devem ser comprovadas documentalmente pelo requerente diretamente ao Chefe do Posto ou da Unidade de Emissão (NUMIG/DELEX), que possui a discricionariedade legal para autorizar o encaixe imediato e a emissão do passaporte de emergência ou adiantamento do passaporte comum.
- *PENDENTE (Abordando audit_v2 — Falha 20 parcial):* Está classificado como pendente identificar de forma documental e com base em normativos internos os canais formais alternativos e de contingência mantidos pela Polícia Federal (como e-mails institucionais, Ouvidoria ou balcões físicos de triagem) para sanar falhas exclusivas de agendamento digital ou exclusão digital de cidadãos que não conseguem acessar o calendário unificado.

### Etapa 4: Atendimento Presencial e Coleta Biométrica

- **Canais e Sistemas de TI Envolvidos:** Realizado nas delegacias e postos de atendimento da PF. Envolve a captura de impressões digitais, fotografia facial e conferência de documentos originais.
- *PENDENTE (Abordando audit_v2 — Falha 6 parcial e C.2):* Está classificado como em aberto e pendente de validação documental interna os papéis operacionais e a arquitetura sistêmica exata do STI-MAR (Sistema de Tráfego Internacional) durante a fase de triagem presencial do passaporte. É pendente confirmar formalmente se o STI-MAR é consultado ou alimenta barramentos de segurança para verificação de impedimentos judiciais na emissão, ou se sua atuação é exclusiva para o controle migratório de fronteiras, portos e aeroportos.
- *PENDENTE (Abordando audit_v2 — Falha 14):* Está classificado como pendente a identificação formal e a comprovação contratual das empresas privadas desenvolvedoras ou licenciadoras do algoritmo da Solução Automatizada de Identificação Biométrica (ABIS) ativa na PF.

**Contingência de Falha do Sistema Web:**

- *PENDENTE (Abordando audit_v2 — Falha 7 e Falha 22):* Está classificada como em aberto a verificação do protocolo operacional interno de contingência escrita aplicável caso os barramentos centrais de biometria fiquem offline.
- *INFERÊNCIA:* Presume-se que, devido aos rigorosos critérios de segurança de identificação civil e controle de fraudes, a impossibilidade de pesquisar restrições criminais e de validar a unicidade biométrica restringe a emissão final do documento, gerando retenção ou reagendamento do atendimento físico.

### Etapa 5: Consulta Remota de Andamento

- **Canais e Sistemas de TI Envolvidos:** O cidadão acompanha as fases de fabricação através do portal Gov.br ou da página específica de consulta da Polícia Federal.

**Contingência de Falha do Sistema Web:**

- *INFERÊNCIA:* Deduz-se que a centralização da consulta em meios eletrônicos gera demandas de suporte presencial ou consultas junto a intermediários por parte de cidadãos que carecem de facilidade no manuseio de interfaces digitais.

### Etapa 6: Retirada Física e Entrega do Documento

- **Canais e Sistemas de TI Envolvidos:** Ocorre presencialmente no mesmo posto de atendimento. O operador realiza a conferência documental e uma nova verificação biométrica digital do titular para confirmar a identidade antes da entrega da caderneta.
- *PENDENTE (Abordando audit_v2 — Falha 8, 9 e 23):* Está listada como pendente e em aberto a confirmação técnica e normativa de que ocorre um procedimento de "ativação eletrônica do chip" por meio de terminal local na entrega e se isso inviabiliza de forma absoluta a entrega do documento em cenários de queda localizada de rede (offline).

**Contingência de Falha do Sistema Web:**

- *FATO DOCUMENTADO (Abordando audit_v2 — Falha 17 e 21):* De acordo com a Instrução Normativa nº 173/2020-DG/PF (Art. 93), o passaporte não retirado pelo cidadão no prazo de 90 dias, contados a partir da data de sua fabricação, será cancelado no sistema. A norma oficial determina o cancelamento no sistema e a consequente inutilização física do documento.

---

## 2. Mapeamento de Atores em Camadas

O ecossistema do serviço de emissão de passaporte comum brasileiro integra as seguintes entidades estruturantes categorizadas em camadas:

### Camada de Usuários Diretos

- **Cidadão Comum (Primeira Viagem):** Requerente que necessita de orientações básicas sobre o fluxo de identificação e documentação.
- **Cidadão em Renovação (Emissão de Novo Passaporte):**
  - *FATO DOCUMENTADO (Abordando audit_v2 — Falha 10 parcial):* O Decreto nº 5.978/2006 estabelece que o requerente que deixar de apresentar o passaporte anterior (válido) ficará sujeito ao pagamento da taxa majorada (atualmente correspondente ao dobro do valor da taxa comum). O Boletim de Ocorrência (BO) é exigido formalmente para fins de registro e segurança em casos de roubo, furto ou extravio, visando ao cancelamento do documento anterior no sistema de segurança para evitar fraudes de identidade. Retira-se a afirmação sobre hipóteses genéricas de isenção por calamidade pública por ausência de fonte normativa expressa mapeada nesta pesquisa documental.
- **Menores de Idade e Responsáveis Legais:**
  - *FATO DOCUMENTADO (Abordando audit_v2 — Falha 11):* A Instrução Normativa nº 173/2020-DG/PF e as orientações oficiais demonstram que a autorização para emissão de passaporte de menor exige o consentimento de ambos os pais. Contudo, a presença física simultânea dos dois genitores no posto da PF **não** é obrigatória em todos os casos: o fluxo permite que um dos pais compareça portando o formulário de autorização assinado pelo outro genitor com firma reconhecida por autenticidade em cartório, ou mediante procuração pública específica.
  - *PENDENTE (Abordando audit_v2 — Nova Falha N4):* Permanece pendente de documentação e comprovação formal o fluxo técnico e a vigência nacional da Autorização Eletrônica de Viagem (AEV) operada via cartórios como substituto integrado eletronicamente ao formulário físico da PF na jornada de emissão do passaporte.
- **Pessoas com Deficiência (PCD) e Analfabetos Digitais:** Requerentes que demandam acessibilidade física e apoio no preenchimento dos fluxos governamentais.

### Camada de Operadores de Linha de Frente

- **Atendentes Terceirizados de Recepção:** Profissionais de apoio administrativo contratados via empresas prestadoras de serviço para triagem inicial e entrega.
- **Policiais Federais (Agentes, Escrivães e Papiloscopistas):** Servidores de carreira responsáveis pela validação final dos documentos, coleta de dados biométricos e análise de segurança criminal.
- **Chefias dos Postos de Emissão (NUMIG / DELEX):** Delegados ou coordenadores responsáveis pela gestão das unidades e avaliação de urgências excepcionais.

### Camada de Gestores e Decisores

- **Divisão de Passaportes da Polícia Federal (DPas) [PENDENTE — Abordando audit_v2 — Falha 45 e C.3]:** Classifica-se como institucionalmente plausível, porém pendente de confirmação por meio de portarias de regimento interno ou organogramas formais publicados da Polícia Federal, o papel exato da DPas como a unidade central técnica exclusiva e direta responsável por centralizar o planejamento, normatização e fiscalização das atividades de expedição de documentos de viagem.
- **Direção-Geral da Polícia Federal (DG/PF) e Ministério da Justiça e Segurança Pública (MJSP):** Instâncias de deliberação máxima, fixação de instruções normativas e articulação orçamentária federal.
- **Ministério da Gestão e da Inovação em Serviços Públicos (MGI):** Gestor das diretrizes transversais da plataforma unificada Gov.br.

### Camada de Órgãos de Controle, Padronização e Articulação Institucional

- **Conselho Nacional de Justiça (CNJ):** Ator normativo responsável pela edição de resoluções (como a Resolução CNJ nº 131) que regulamentam a concessão de autorizações de viagem de menores.
- **Controladoria-Geral da União (CGU) e Tribunal de Contas da União (TCU) [FATO DOCUMENTADO — Abordando audit_v2 — Falha 44 parcial]:** O TCU atua no âmbito de suas competências constitucionais na fiscalização e controle externo da legalidade, legitimidade e economicidade dos contratos administrativos e repasses orçamentários firmados pela Polícia Federal para sustentação do serviço. Fica marcado como pendente por ausência de fonte pública qualquer detalhamento ou afirmação sobre fiscalização específica do TCU sobre o licenciamento ou contratação da tecnologia do sistema ABIS.
- **International Civil Aviation Organization (ICAO):** Organização internacional da aviação civil responsável por ditar os padrões globais de segurança e interoperabilidade de documentos de viagem eletrônicos (especificações do Doc 9303), os quais o Brasil adota na fabricação das cadernetas.

### Camada de Parceiros e Infraestrutura Pública

- **Receita Federal do Brasil (RFB) [PENDENTE — Abordando audit_v2 — C.1, N1]:** Fica classificado como pendente detalhar de forma documental e com fontes normativas explícitas a distinção operacional entre a checagem do CPF cadastral (dados biográficos de identificação) versus a situação de regularidade fiscal do cidadão perante a Secretaria da Receita Federal como critério elegível ou impeditivo na emissão de passaportes.
- **Cartórios de Registro Civil de Pessoas Naturais e Tabelionatos de Notas (Notários):** Instituições fundamentais na cadeia de identificação civil nacional, responsáveis pela emissão e averbação de certidões de nascimento, casamento e óbito, bem como pelo reconhecimento de firmas por autenticidade em formulários de autorização.
- **Bancos Arrecadadores:** Instituições financeiras integrantes da rede bancária nacional responsáveis pelo acolhimento do pagamento da GRU e repasse dos valores à Conta Única do Tesouro Nacional.
- **Casa da Moeda do Brasil (CMB):** Responsável exclusiva pela fabricação material das cadernetas, inserção dos elementos de segurança física e gravação a laser dos dados biográficos combinados ao chip eletrônico.
- *PENDENTE (Abordando audit_v2 — Nova Falha N5):* É classificado como pendente de comprovação via relatórios comerciais oficiais ou demonstrações financeiras se as oscilações cambiais na importação de insumos físicos de segurança atuam como barreiras e resistências materiais diretas na cadeia de fornecimento de cadernetas junto à Polícia Federal.

### Camada de Fornecedores de TI e Intermediários

- **SERPRO:** Empresa pública contratada para fornecer suporte tecnológico e sustentação a sistemas de governo.
- *PENDENTE (Abordando audit_v2 — Falha 12, 42 e 43):* Está classificado como pendente e em aberto comprovar documentalmente via portaria ou contrato se a Dataprev participa ativamente do barramento cadastral específico do passaporte e se o SERPRO é a empresa responsável pela hospedagem direta dos bancos de dados do sistema de controle migratório associado ou do STI-MAR.
- **Despachantes, Assessorias e Agências de Turismo:** Intermediários privados que atuam no suporte logístico e comercial de preenchimento e agendamento para terceiros.

---

## 3. Matriz de Mendelow e Drivers Operacionais

A governança do serviço de passaportes é avaliada a seguir por meio da análise de poder e interesse de seus atores constituintes, correlacionada a seus respectivos drivers motivacionais.

### Tabela 1: Matriz de Mendelow Ampliada

> **NOTA METODOLÓGICA (Abordando audit_v2 — C.6):** As classificações de quadrantes, papéis e barreiras atribuídas na tabela abaixo constituem exclusivamente uma **ANÁLISE DO AUTOR** deste relatório, baseada em deduções lógicas e inferências sobre a estrutura de governança pública, não se configurando como fatos documentados extraídos diretamente de fontes governamentais ou atos normativos explícitos.

| Ator / Grupo de Atores | Quadrante de Mendelow (ANÁLISE DO AUTOR) | Papel Exato na Jornada (ANÁLISE DO AUTOR) | Incentivo para Melhorar o Serviço (ANÁLISE DO AUTOR) | Principais Resistências ou Barreiras (ANÁLISE DO AUTOR) |
| --- | --- | --- | --- | --- |
| **Divisão de Passaportes (DPas/PF)** | Alto Poder / Alto Interesse (Key Player) | Normatização nacional, gestão e controle de qualidade procedimental do serviço. | Redução de filas, elevação dos índices de eficiência e prevenção a fraudes de identidade. | Limitações decorrentes de contingenciamentos e adequação aos rígidos padrões internacionais. |
| **Casa da Moeda do Brasil (CMB)** | Alto Poder / Alto Interesse (Key Player) | Confecção material das cadernetas e montagem física do chip eletrônico seguro. | Cumprimento das metas de fornecimento e faturamento de contratos de suprimentos oficiais. | Oscilações cambiais na importação de insumos físicos de segurança e componentes eletrônicos. |
| **Receita Federal (RFB)** | Alto Poder / Baixo Interesse (Latente) | Fornecimento da base cadastral e validação da regularidade fiscal/cadastral do CPF. | Integridade e saneamento dos dados biográficos do cadastro civil nacional. | Foco operacional voltado à fiscalização tributária primária, e não à usabilidade de sistemas parceiros. |
| **Cartórios e Notários** | Alto Poder / Baixo Interesse (Latente) | Emissão de certidões base e atos notariais de autorização/AEV de menores. | Modernização e captação de emolumentos via serviços digitais integrados (e-Notariado). | Heterogeneidade de sistemas informatizados entre diferentes comarcas e estados do país. |
| **Bancos Arrecadadores** | Médio Poder / Baixo Interesse (Latente) | Processamento da arrecadação e envio de arquivos de compensação de taxas. | Eficiência no processamento de transações financeiras e tarifas de arrecadação de serviços públicos. | Horários rígidos de fechamento bancário e janelas de transmissão de arquivos de retorno. |
| **ICAO** | Alto Poder / Baixo Interesse (Latente) | Estabelecimento de diretrizes internacionais de segurança aérea e de documentos (Doc 9303). | Padronização global de segurança cibernética e biometria para facilitação de viagens seguras. | Distanciamento das particularidades operacionais e de infraestrutura de TI de cada país membro. |
| **Cidadão Requerente** | Baixo Poder / Alto Interesse (Sujeito) | Fornecimento de dados biográficos, pagamento de taxas e comparecimento presencial. | Obtenção do documento no menor prazo, menor custo e sem complexidade burocrática. | Barreiras de letramento digital, restrições orçamentárias e custos de deslocamento físico. |
| **SERPRO** | Alto Poder / Alto Interesse (Key Player) | Sustentação tecnológica e desenvolvimento evolutivo de sistemas de TI governamentais. | Cumprimento de metas de SLA estabelecidas contratualmente com a Administração Pública. | Gerenciamento de débitos tecnológicos e arquitetura de sistemas legados de alta complexidade. |

### Análise Sistêmica dos Drivers Orçamentários e de Controle

- *FATO DOCUMENTADO (Abordando audit_v2 — Falha 30, 31, 32, 33):* O fluxo operacional do serviço de passaporte sofre impactos diretos da disponibilidade orçamentária federal. Os valores históricos de contingenciamento orçamentário que geraram suspensões temporárias na confecção de passaportes (como as crises orçamentárias de 2017 e 2022 acompanhadas pelos órgãos de controle) decorreram do esgotamento do teto de empenho das dotações orçamentárias destinadas à Polícia Federal para a contratação da Casa da Moeda. Os valores exatos de aditivos vigentes e empenhos financeiros detalhados para o ano corrente flutuam anualmente e necessitam de verificação periódica direta no Portal da Transparência.

---

## 4. Pontos de Fricção e Demanda Falha (Failure Demand)

### Fricção Estrutural

- **Obrigatoriedade Civil de Coleta Biométrica:** O Decreto nº 5.978/2006, alinhado aos compromissos do Brasil junto à ICAO, impõe a coleta presencial obrigatória de dados biométricos. Isso inviabiliza um fluxo 100% virtual de ponta a ponta.
- **Validação da Malha Cadastral Federal:** A necessidade de consistência de dados com a base do CPF da Receita Federal e a checagem de restrições judiciais impedem a flexibilização da triagem documental automatizada no posto.
- **Complexidade Protetiva de Menores:** As regras compartilhadas entre a Instrução Normativa nº 173/2020-DG/PF e as normativas do CNJ adicionam uma fricção estrutural necessária à segurança do menor, exigindo detalhamento na comprovação de guarda ou de assinaturas reconhecidas por autenticidade.

### Fricção de Design

- **Rigidez de UX e Formulários "Digital-Only" [INFERÊNCIA — Abordando audit_v2 — Nova Falha N7]:** Deduz-se analiticamente que a ausência de mecanismos de auxílio interativo em tempo real ou ferramentas integradas de checagem ortográfica preditiva automática para mitigar erros de digitação de nomes complexos (como transições de nome por divórcio ou casamento) induz ao preenchimento incorreto pelo próprio cidadão.
- **Limitação do Fluxo de Agendamento:** A ausência de um sistema dinâmico de lista de espera ativa força o usuário a realizar consultas repetidas no SINPA para identificar vagas geradas por cancelamentos.

### Análise de Demanda Falha (Failure Demand)

A demanda falha caracteriza-se pelo retrabalho e novos contatos gerados por falhas na concepção original do serviço:

- **Atraso no Registro de Cobrança:** O intervalo entre a emissão da GRU e a efetiva transmissão do arquivo de compensação bancária gera tentativas frustradas de agendamento no SINPA, acarretando chamados adicionais de suporte.
- *FATO DOCUMENTADO (Abordando audit_v2 — Falha 16):* Se um erro de preenchimento biográfico for detectado apenas na triagem presencial, a praxe administrativa indica que erros simples de digitação de nomes podem ser saneados pelo próprio policial/atendente no guichê de atendimento presencial através do terminal local do SINPA, aproveitando a mesma taxa paga. Contudo, se houver divergência estrutural de titularidade do CPF ou impossibilidade de vinculação dos dados base da GRU, o atendimento não prossegue, gerando retrabalho no agendamento.
- *PENDENTE (Abordando audit_v2 — Falha 35 e C.4):* Fica classificado como pendente a extração e a citação documental, com data de referência específica, do painel oficial de monitoramento do Gov.br que aponte a nota de avaliação média histórica atribuída pelos usuários ao serviço de emissão de passaporte (como a nota de 4,8 estrelas anteriormente citada).
- *INFERÊNCIA (Abordando audit_v2 — Falha 28 e 29):* Diante da falta de relatórios públicos de auditoria de usabilidade transversais, infere-se que os indicadores de satisfação baseados exclusivamente em avaliações pós-conclusão podem apresentar um viés de sobrevivência, omitindo a fricção e as barreiras daqueles usuários que abandonaram a jornada ou enfrentaram gargalos graves de compensação e triagem documental nas fases preliminares.

---

## 5. Lacunas de Evidência (Gap Analysis)

Por se tratar de uma pesquisa baseada em fontes abertas, determinadas informações operacionais específicas não estão disponíveis ao público e permanecem mapeadas sob rigoroso isolamento analítico:

### Tabela 2: Matriz de Lacunas de Evidência Técnica

| Área da Jornada | Informação Ausente ou Indisponível em Fontes Abertas | Impacto Técnico no Mapeamento de Atores |
| --- | --- | --- |
| **Operação e Dimensionamento** | Número exato e distribuição geográfica de funcionários terceirizados alocados na triagem física e entrega por unidade federativa da PF. | Dificulta a modelagem de capacidade de atendimento e dimensionamento de filas presenciais. |
| **Custos Unitários CMB** | Custo unitário de fabricação isolado de cada caderneta física de passaporte eletrônico cobrado pela CMB da União. | Impede o cálculo exato do impacto financeiro do desperdício material decorrente de cancelamentos. |
| **Métricas de Cancelamento** | O volume absoluto anual de cadernetas de passaporte comum inutilizadas por decurso do prazo regulamentar de 90 dias de guarda. | Oculta a dimensão real do desperdício operacional gerado pelo não comparecimento para retirada. |
| **Performance Biométrica** | Taxas de erro (falsos positivos e falsos negativos) do algoritmo biométrico do sistema ABIS em operações de rotina de emissão. | Impede a avaliação independente da eficiência técnica da solução em relação aos padrões internacionais. |
| **Indicadores de Indisponibilidade** | Relatórios de "downtime" consolidados das APIs de comunicação do SINPA com a Receita Federal e redes bancárias. | Limita a compreensão exata da origem sistêmica das falhas de agendamento registradas pelos cidadãos. |

---

## 6. Tabela-Resumo de Atores do Ecossistema

Esta tabela consolida o ecossistema do serviço de emissão de passaporte comum brasileiro, fornecendo subsídios para futuras matrizes de atribuição de responsabilidades.

### Tabela 3: Síntese de Atores e Sistemas

> **NOTA METODOLÓGICA (Abordando audit_v2 — C.6):** As classificações de poder, interesse e identificação de fricções associadas nesta tabela resumida constituem exclusivamente uma **ANÁLISE DO AUTOR** deste relatório, baseada em deduções e inferências sobre a estrutura de governança pública, não se configurando como fatos documentados extraídos diretamente de fontes governamentais ou atos normativos explícitos.

| Ator / Sistema | Camada de Atuação | Papel Principal na Jornada (ANÁLISE DO AUTOR) | Poder / Interesse (Mendelow — ANÁLISE DO AUTOR) | Principal Fricção Associada (ANÁLISE DO AUTOR) |
| --- | --- | --- | --- | --- |
| **Sistema SINPA** | Parceiros de TI e Sistemas | Repositório oficial de dados biográficos, agendamento de postos e controle de fluxo do passaporte. | Alto Poder / Alto Interesse (Key Player) | Interface sem correções ortográficas preditivas integradas na fase inicial web. |
| **Divisão de Passaportes (DPas/PF)** | Gestores e Decisores | Papel atribuído de planejamento e coordenação nacional (pendente de fonte primária). | Alto Poder / Alto Interesse (Key Player) | Sujeição à estabilidade orçamentária para a manutenção física de postos terceirizados. |
| **Casa da Moeda do Brasil (CMB)** | Fornecedores de Infraestrutura | Produção material das cadernetas físicas com papel de segurança e montagem de chips. | Alto Poder / Alto Interesse (Key Player) | Fluxo de suprimentos condicionado a limites fiscais de empenho e variações de insumos. |
| **Receita Federal (RFB)** | Órgãos de Controle e Validação | Gestão da base do CPF para validação de dados biográficos e cadastrais. | Alto Poder / Baixo Interesse (Latente) | Mapeamento pendente se gera bloqueio automatizado do avanço no formulário web. |
| **Cartórios de Registro Civil** | Órgãos de Controle e Validação | Emissão de certidões de nascimento/casamento (fluxo de AEV de menor classificado como pendente). | Alto Poder / Baixo Interesse (Latente) | Custos de emolumentos cartoriais e descentralização de sistemas informáticos de consulta. |
| **Bancos Arrecadadores** | Parceiros de Infraestrutura | Acolhimento de pagamentos da GRU e envio de arquivos eletrônicos de retorno. | Médio Poder / Baixo Interesse (Latente) | Janela temporal de compensação de boletos, restringindo o agendamento em tempo real. |
| **CNJ** | Órgãos de Controle e Regulamentação | Edição de resoluções de viagem de menores e parametrização dos atos notariais. | Alto Poder / Baixo Interesse (Latente) | Complexidade de interpretação de normas de representação legal por famílias monoparentais. |
| **ICAO** | Órgãos de Controle e Regulamentação | Fixação internacional de padrões de segurança e especificações de passaportes eletrônicos. | Alto Poder / Baixo Interesse (Latente) | Rigidez internacional que impede a flexibilização ou eliminação da etapa biométrica presencial. |
| **Atendentes e Policiais de Posto** | Operadores de Linha de Frente | Acolhimento presencial, triagem documental física, captura de biometria e entrega de livretes. | Baixo Poder / Alto Interesse (Sujeito) | Absorção do descontentamento do usuário em episódios de lentidão ou quedas de rede centralizadora. |
| **Cidadão Requerente** | Usuários Diretos | Alimentação de dados na web, quitação de obrigações tributárias e comparecimento aos atos. | Baixo Poder / Alto Interesse (Sujeito) | Exclusão digital e necessidade de custear taxas adicionais com intermediários por falhas de usabilidade. |
| **Despachantes e Assessorias** | Intermediários | Suporte logístico comercial privado de preenchimento e monitoramento de agendas. | Baixo Poder / Alto Interesse (Monitorar) | Exploração financeira de assimetrias informativas do portal de serviços públicos unificado. |
