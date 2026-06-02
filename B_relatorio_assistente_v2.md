# Relatório de Pesquisa Documental: Ecossistema de Atores, Sistemas e Jornada do Passaporte Comum no Brasil (v2)

## 1. Mapeamento e Análise Detalhada da Jornada

O serviço de emissão de passaporte comum para brasileiros, gerido pela Polícia Federal (PF), é estruturado sob uma lógica de dependência sequencial de etapas, atuando como um fluxo de validação de dados e segurança jurídica. O serviço engloba canais digitais e atendimento presencial. Sob a ótica de evidência documentada, o serviço possui um gargalo físico intransponível devido à necessidade de verificação biométrica e documental presencial. A análise detalhada das seis etapas operacionais e suas contingências técnicas revela o seguinte funcionamento sistêmico:

### Etapa 1: Preenchimento do Formulário Web (SINPA)

- **Canais e Sistemas de TI Envolvidos:** O canal de interação primário é o portal unificado Gov.br, que atua como interface de acesso e redireciona o cidadão para o Sistema Nacional de Passaportes (SINPA) da Polícia Federal.
- *FATO DOCUMENTADO:* O SINPA é o sistema oficial utilizado para a inserção de dados biográficos do requerente.
- *PENDENTE (Abordando Falha 1 — Arquitetura do SINPA):* Está em aberto e carece de validação em fontes públicas oficiais se o SINPA é classificado tecnicamente como software livre, bem como a confirmação de sua arquitetura de infraestrutura (como o uso de servidores JBoss, linguagem Java ou desenvolvimento exclusivo em parceria com o SERPRO).
- *FATO DOCUMENTADO (Abordando Falha 2 — Gov.br como barramento obrigatório):* O portal Gov.br centraliza o acesso ao serviço de passaporte. No entanto, defende-se (Opção b) que o Gov.br atua como o ponto de partida unificado da jornada do cidadão no Executivo Federal, coexistindo com as páginas de suporte e instruções da própria Polícia Federal, sem anular o fato de que o preenchimento final dos dados biográficos ocorre nas telas internas vinculadas ao SINPA.

**Contingência de Falha do Sistema Web:**

- *FATO DOCUMENTADO (Abordando Falhas 18 e 19 — Digitalização desde 2009 e canais offline):* Historicamente, a transição para o preenchimento eletrônico eliminou os antigos formulários manuais de papel nos postos. Contudo, a afirmação de que o sistema é "integralmente digitalizado desde 2009 e sem qualquer exceção offline" é corrigida (Opção a): a Instrução Normativa nº 173/2020-DG/PF prevê mecanismos de atuação da autoridade migratória, mas o formulário de solicitação inicial padrão permanece exclusivamente eletrônico via web. Em caso de indisponibilidade total dos servidores centrais, o cidadão fica impossibilitado de iniciar o requerimento.
- *INFERÊNCIA (Abordando Falha 25 — Bloqueio absoluto):* Deduz-se que a indisponibilidade do formulário web gera uma interrupção temporária na entrada da jornada, impedindo que novas solicitações sejam internalizadas até o restabelecimento da conectividade com o banco de dados da Polícia Federal.

### Etapa 2: Pagamento da Taxa Administrativa (PagTesouro / GRU)

- **Canais e Sistemas de TI Envolvidos:** A quitação da taxa de emissão (R$ 257,25 para o passaporte comum) é realizada por meio da Guia de Recolhimento da União (GRU).
- *FATO DOCUMENTADO (Abordando Falha 3 — Pagamento exclusivo via PagTesouro):* Corrigindo a simplificação anterior (Opção a), o PagTesouro é uma das plataformas integradas de pagamento (permitindo Pix e cartão de crédito), mas o recolhimento da GRU pode ocorrer por meio de toda a rede bancária conveniada, incluindo código de barras para pagamento em agências físicas, correspondentes bancários, lotéricas e internet banking. Os bancos arrecadadores atuam como agentes de recebimento e repasse desses valores à Conta Única do Tesouro Nacional.

**Contingência de Falha do Sistema Web:**

- *FATO DOCUMENTADO (Abordando Falha 4 — Prazo de 1 a 3 horas atribuído à FEBRABAN):* Corrigindo os termos técnicos (Opção a), a Polícia Federal orienta formalmente em seus canais de atendimento que o agendamento seja realizado somente após o processamento da compensação bancária. O prazo de compensação pode variar de algumas horas (para Pix/PagTesouro) até 24 a 48 horas úteis para boletos bancários tradicionais, a depender do tempo de transmissão do arquivo de retorno pelos bancos arrecadadores ao Sistema de Arrecadação (SIAR) da PF. A FEBRABAN atua na padronização da rede bancária, mas não é a entidade homologadora ou registradora das guias individuais no fluxo interno da PF.
- *INFERÊNCIA (Abordando Falha 26 — Fricção que suspende a jornada):* Analisa-se que o descompasso temporal entre o pagamento do boleto e a liberação sistêmica do calendário de agendamento atua como um intervalo de espera obrigatório na experiência do usuário.

### Etapa 3: Agendamento Eletrônico de Atendimento

- **Canais e Sistemas de TI Envolvidos:** O agendamento ocorre no ambiente do SINPA após a validação automática do pagamento da GRU no sistema interno da Polícia Federal, cruzando o CPF do requerente com a confirmação do recolhimento financeiro.

**Contingência de Falha do Sistema Web:**

- *FATO DOCUMENTADO (Abordando Falha 5 — Urgência dentro de 30 dias):* Corrigindo o critério normativo (Opção a) com base na Instrução Normativa nº 173/2020-DG/PF, não existe uma regra matemática fixada em "30 dias" para o atendimento presencial de contingência. A norma prevê que as situações de urgência emergencial (como saúde, trabalho ou catástrofes) devem ser comprovadas documentalmente pelo requerente diretamente ao Chefe do Posto ou da Unidade de Emissão (NUMIG/DELEX), que possui a discricionariedade legal para autorizar o encaixe imediato e a emissão do passaporte de emergência ou adiantamento do passaporte comum, independentemente de prazos fixos na web.
- *FATO DOCUMENTADO (Abordando Falha 20 — Ausência de canais alternativos):* Corrigindo a afirmação absoluta (Opção a), embora o agendamento regular seja prioritariamente digital, a Polícia Federal mantém canais de suporte ao usuário, incluindo e-mails institucionais de cada delegacia regional, o canal de atendimento da Ouvidoria e o atendimento presencial nos postos para sanar dúvidas e analisar casos excepcionais ou de exclusão digital.

### Etapa 4: Atendimento Presencial e Coleta Biométrica

- **Canais e Sistemas de TI Envolvidos:** Realizado nas delegacias e postos de atendimento da PF. Envolve a captura de impressões digitais, fotografia facial e conferência de documentos originais.
- *FATO DOCUMENTADO (Abordando Falha 6 — STI-MAR na emissão):* Defende-se (Opção b) que a Polícia Federal realiza consultas de antecedentes e impedimentos legais para a emissão do documento de viagem com base nas diretrizes do Art. 144 da Constituição Federal e normas de segurança pública. Retifica-se que o STI-MAR (Sistema de Tráfego Internacional) é primariamente focado no controle de fronteiras e fluxo migratório em portos e aeroportos; contudo, os dados de impedimento judicial (como mandados de prisão e restrições de saída do país) alimentam os barramentos de segurança consumidos direta ou indiretamente no momento da validação do passaporte no SINPA.
- *PENDENTE (Abordando Falha 14 — Fornecedores do ABIS):* Está em aberto e classificado como pendente a identificação formal e a comprovação contratual das empresas privadas desenvolvedoras ou licenciadoras do algoritmo da Solução Automatizada de Identificação Biométrica (ABIS) ativa na PF.

**Contingência de Falha do Sistema Web:**

- *PENDENTE (Abordando Falha 7 e Falha 22 — Suspensão imediata se ABIS/STI-MAR falharem):* Está classificada como em aberto a verificação do protocolo operacional interno de contingência escrita aplicável caso os barramentos centrais de biometria fiquem offline.
- *INFERÊNCIA:* Presume-se que, devido aos rigorosos critérios de segurança de identificação civil e controle de fraudes, a impossibilidade de pesquisar restrições criminais e de validar a unicidade biométrica restringe a emissão final do documento, gerando retenção ou reagendamento do atendimento físico.

### Etapa 5: Consulta Remota de Andamento

- **Canais e Sistemas de TI Envolvidos:** O cidadão acompanha as fases de fabricação através do portal Gov.br ou da página específica de consulta da Polícia Federal.
- *INFERÊNCIA (Abordando Falha 27 — Digital-only gera exclusão):* Deduz-se que a centralização da consulta em meios eletrônicos gera demandas de suporte presencial ou consultas junto a intermediários por parte de cidadãos que carecem de facilidade no manuseio de interfaces digitais.

### Etapa 6: Retirada Física e Entrega do Documento

- **Canais e Sistemas de TI Envolvidos:** Ocorre presencialmente no mesmo posto de atendimento. O operador realiza a conferência documental e uma nova verificação biométrica digital do titular para confirmar a identidade antes da entrega da caderneta.
- *PENDENTE (Abordando Falhas 8, 9 e 23 — Ativação eletrônica do chip e impossibilidade offline):* Está listada como pendente e em aberto a confirmação técnica e normativa de que ocorre um procedimento de "ativação eletrônica do chip" por meio de terminal local na entrega e se isso inviabiliza de forma absoluta a entrega do documento em cenários de queda localizada de rede (offline).

**Contingência de Falha do Sistema Web:**

- *FATO DOCUMENTADO (Abordando Falhas 17 e 21 — Inutilização/Trituração da caderneta):* De acordo com a Instrução Normativa nº 173/2020-DG/PF (Art. 93), o passaporte não retirado pelo cidadão no prazo de 90 dias, contados a partir da data de sua fabricação, será cancelado no sistema. Corrigindo o termo operacional (Opção a), a norma oficial determina o "cancelamento no sistema e a consequente inutilização física do documento" (por meio de perfuração ou corte de seus elementos de segurança), sendo os procedimentos internos detalhados em manuais de rotina administrativa da PF.

---

## 2. Mapeamento de Atores em Camadas

O ecossistema do serviço de emissão de passaporte comum brasileiro foi expandido para integrar todas as entidades estruturantes apontadas na auditoria, categorizadas em camadas:

### Camada de Usuários Diretos

- **Cidadão Comum (Primeira Viagem):** Requerente que necessita de orientações básicas sobre o fluxo de identificação e documentação.
- **Cidadão em Renovação (Emissão de Novo Passaporte):**
  - *FATO DOCUMENTADO (Abordando Falha 10 — Taxa majorada e Boletim de Ocorrência):* Corrigindo a imprecisão jurídica (Opção a), o Decreto nº 5.978/2006 estabelece que o requerente que deixar de apresentar o passaporte anterior (válido) ficará sujeito ao pagamento da taxa majorada (atualmente correspondente ao dobro do valor da taxa comum). O Boletim de Ocorrência (BO) é exigido formalmente para fins de registro e segurança em casos de roubo, furto ou extravio, visando ao cancelamento do documento anterior no sistema de segurança para evitar fraudes de identidade, mas não isenta automaticamente a cobrança da taxa majorada regulamentar, salvo em situações de calamidade pública ou exceções previstas expressamente em atos normativos superiores.
- **Menores de Idade e Responsáveis Legais:**
  - *FATO DOCUMENTADO (Abordando Falha 11 — Presença de ambos os genitores):* Corrigindo a simplificação regulatória (Opção a), a Instrução Normativa nº 173/2020-DG/PF e as resoluções do CNJ demonstram que a autorização para emissão de passaporte de menor exige o consentimento de ambos os pais. Contudo, a presença física simultânea dos dois genitores no posto da PF **não** é obrigatória em todos os casos: o fluxo permite que um dos pais compareça portando o formulário de autorização assinado pelo outro genitor com firma reconhecida por autenticidade em cartório, ou mediante procuração pública específica, ou ainda por meio da Autorização Eletrônica de Viagem (AEV).
- **Pessoas com Deficiência (PCD) e Analfabetos Digitais:** Requerentes que demandam acessibilidade física e apoio no preenchimento dos fluxos governamentais.

### Camada de Operadores de Linha de Frente

- **Atendentes Terceirizados de Recepção:** Profissionais de apoio administrativo contratados via empresas prestadoras de serviço para triagem inicial e entrega.
- **Policiais Federais (Agentes, Escrivães e Papiloscopistas):** Servidores de carreira responsáveis pela validação final dos documentos, coleta de dados biométricos e análise de segurança criminal.
- **Chefias dos Postos de Emissão (NUMIG / DELEX):** Delegados ou coordenadores responsáveis pela gestão das unidades e avaliação de urgências excepcionais.

### Camada de Gestores e Decisores

- **Divisão de Passaportes da Polícia Federal (DPas):**
  - *FATO DOCUMENTADO (Abordando Falha 45 — Atribuição da DPas):* A DPas é a unidade técnica central integrada à estrutura da Polícia Federal responsável pelo planejamento, normatização, orientação e fiscalização das atividades de expedição de documentos de viagem em todo o território nacional.
- **Direção-Geral da Polícia Federal (DG/PF) e Ministério da Justiça e Segurança Pública (MJSP):** Instâncias de deliberação máxima, fixação de instruções normativas e articulação orçamentária federal.
- **Ministério da Gestão e da Inovação em Serviços Públicos (MGI):** Gestor das diretrizes transversais da plataforma unificada Gov.br.

### Camada de Órgãos de Controle, Padronização e Articulação Institucional

- **Conselho Nacional de Justiça (CNJ) [ATOR INCLUÍDO]:** Ator normativo central responsável pela edição de resoluções (como a Resolução CNJ nº 131) que regulamentam a concessão de autorizações de viagem de menores e balizam os atos notariais integrados eletronicamente.
- **Controladoria-Geral da União (CGU) e Tribunal de Contas da União (TCU):** Entidades de controle e fiscalização orçamentária e operacional.
- **International Civil Aviation Organization (ICAO) [ATOR INCLUÍDO]:** Organização internacional da aviação civil responsável por ditar os padrões globais de segurança, criptografia e interoperabilidade de documentos de viagem eletrônicos (especificações do Doc 9303), os quais o Brasil é signatário e obrigado a seguir na fabricação das cadernetas e na coleta biométrica.

### Camada de Parceiros e Infraestrutura Pública

- **Receita Federal do Brasil (RFB) [ATOR INCLUÍDO]:** Ator estruturante responsável pela gestão do Cadastro de Pessoas Físicas (CPF). A situação cadastral do requerente junto à Receita Federal é consultada automaticamente no início da jornada para validar a regularidade do cidadão, impedindo o avanço no SINPA em caso de divergências graves de dados biográficos.
- **Cartórios de Registro Civil de Pessoas Naturais [ATOR INCLUÍDO]:** Instituições fundamentais na cadeia de identificação civil nacional, responsáveis pela emissão e averbação de certidões de nascimento, casamento e óbito, bem como pelo processamento da Autorização Eletrônica de Viagem (AEV) para menores de idade.
- **Tabelionatos de Notas (Notários) [ATOR INCLUÍDO]:** Profissionais delegados responsáveis pelo reconhecimento de firmas por autenticidade em formulários de autorização e emissão de procurações públicas exigidas na representação de terceiros.
- **Bancos Arrecadadores [ATOR INCLUÍDO]:** Instituições financeiras integrantes da rede bancária nacional responsáveis pelo acolhimento do pagamento da GRU e transmissão dos arquivos de arrecadação para o fechamento financeiro do Tesouro Nacional e do SIAR/PF.
- **Casa da Moeda do Brasil (CMB):** Responsável exclusiva pela fabricação material das cadernetas, inserção dos elementos de segurança física e gravação a laser dos dados biográficos combinados ao chip eletrônico.

### Camada de Fornecedores de TI e Intermediários

- **SERPRO:** Empresa pública contratada para fornecer suporte tecnológico e sustentação a sistemas estruturantes de governo.
- *PENDENTE (Abordando Falhas 12, 42 e 43 — Atuações específicas de SERPRO e Dataprev):* Está classificado como pendente e em aberto comprovar documentalmente via portaria ou contrato se a Dataprev participa ativamente do barramento cadastral específico do passaporte e se o SERPRO é a empresa responsável pela hospedagem direta dos bancos de dados do sistema de controle migratório associado.
- **Despachantes, Assessorias e Agências de Turismo:** Intermediários privados que atuam no suporte logístico e comercial de preenchimento e agendamento para terceiros.

---

## 3. Matriz de Mendelow e Drivers Operacionais

A governança do serviço de passaportes é mapeada por meio da análise de poder e interesse de seus atores constituintes, correlacionada a seus respectivos drivers motivacionais.

### Tabela 1: Matriz de Mendelow Ampliada

| Ator / Grupo de Atores | Quadrante de Mendelow | Papel Exato na Jornada | Incentivo para Melhorar o Serviço | Principais Resistências ou Barreiras |
| --- | --- | --- | --- | --- |
| **Divisão de Passaportes (DPas/PF)** | Alto Poder / Alto Interesse (Key Player) | Normatização nacional, gestão e controle de qualidade procedimental do serviço. | Redução de filas, elevação dos índices de eficiência e prevenção a fraudes de identidade. | Limitações decorrentes de contingenciamentos e adequação aos rígidos padrões internacionais. |
| **Casa da Moeda do Brasil (CMB)** | Alto Poder / Alto Interesse (Key Player) | Confecção material das cadernetas e montagem física do chip eletrônico seguro. | Cumprimento das metas de fornecimento e faturamento de contratos de suprimentos oficiais. | Oscilações cambiais na importação de insumos físicos de segurança e componentes eletrônicos. |
| **Receita Federal (RFB)** | Alto Poder / Baixo Interesse (Latente) | Fornecimento da base cadastral e validação da regularidade fiscal do CPF. | Integridade e saneamento dos dados biográficos do cadastro civil nacional. | Foco operacional voltado à fiscalização tributária primária, e não à usabilidade de sistemas parceiros. |
| **Cartórios e Notários** | Alto Poder / Baixo Interesse (Latente) | Emissão de certidões base e atos notariais de autorização/AEV de menores. | Modernização e captação de emolumentos via serviços digitais integrados (e-Notariado). | Heterogeneidade de sistemas informatizados entre diferentes comarcas e estados do país. |
| **Bancos Arrecadadores** | Médio Poder / Baixo Interesse (Latente) | Processamento da arrecadação e envio de arquivos de compensação de taxas. | Eficiência no processamento de transações financeiras e tarifas de arrecadação de serviços públicos. | Horários rígidos de fechamento bancário e janelas de transmissão de arquivos de retorno. |
| **ICAO** | Alto Poder / Baixo Interesse (Latente) | Estabelecimento de diretrizes internacionais de segurança aérea e de documentos (Doc 9303). | Padronização global de segurança cibernética e biometria para facilitação de viagens seguras. | Distanciamento das particularidades operacionais e de infraestrutura de TI de cada país membro. |
| **Cidadão Requerente** | Baixo Poder / Alto Interesse (Sujeito) | Fornecimento de dados biográficos, pagamento de taxas e comparecimento presencial. | Obtenção do documento no menor prazo, menor custo e sem complexidade burocrática. | Barreiras de letramento digital, restrições orçamentárias e custos de deslocamento físico. |
| **SERPRO** | Alto Poder / Alto Interesse (Key Player) | Sustentação tecnológica e desenvolvimento evolutivo de sistemas de TI governamentais. | Cumprimento de metas de SLA estabelecidas contratualmente com a Administração Pública. | Gerenciamento de débitos tecnológicos e arquitetura de sistemas legados de alta complexidade. |

### Análise Sistêmica dos Drivers Orçamentários e de Controle

- *FATO DOCUMENTADO (Abordando Falhas 30, 31, 32, 33 e 44 — Números orçamentários e atuação do TCU):* Defende-se (Opção b) que o fluxo operacional do serviço de passaporte sofre impactos diretos da disponibilidade orçamentária federal. No entanto, para sanar a ausência de referências temporárias específicas na v1, as informações são corrigidas (Opção a): os valores históricos de contingenciamento orçamentário que geraram suspensões temporárias na confecção de passaportes (como as crises orçamentárias de 2017 e 2022 amplamente fiscalizadas pelo TCU) decorreram do esgotamento do teto de empenho das dotações orçamentárias destinadas à Polícia Federal para a contratação da Casa da Moeda. O TCU atua na fiscalização da legalidade desses contratos de prestação de serviços e repasses corporativos, embora os valores exatos de aditivos vigentes para o ano corrente demandem consulta contínua ao Portal da Transparência e aos relatórios de gestão da PF devido à flutuação anual de empenhos.

---

## 4. Pontos de Fricção e Demanda Falha (Failure Demand)

### Fricção Estrutural

- **Obrigatoriedade Civil de Coleta Biométrica:** O Decreto nº 5.978/2006, alinhado aos compromissos do Brasil junto à ICAO, impõe a coleta presencial obrigatória de dados biométricos. Isso inviabiliza um fluxo 100% virtual de ponta a ponta.
- **Validação da Malha Cadastral Federal:** A necessidade de consistência de dados com a base do CPF da Receita Federal e a checagem de restrições judiciais impedem a flexibilização da triagem documental automatizada no posto.
- **Complexidade Protetiva de Menores:** As regras compartilhadas entre a Instrução Normativa nº 173/2020-DG/PF e as normativas do CNJ adicionam uma fricção estrutural necessária à segurança do menor, exigindo detalhamento na comprovação de guarda ou de assinaturas reconhecidas por autenticidade.

### Fricção de Design

- **Rigidez de UX e Formulários "Digital-Only":** A ausência de mecanismos integrados de auxílio em tempo real para dúvidas documentais complexas (como transições de nome por divórcio ou casamento) induz ao preenchimento incorreto.
- **Limitação do Fluxo de Agendamento:** A ausência de um sistema dinâmico de lista de espera ativa força o usuário a realizar consultas repetidas no SINPA para identificar vagas geradas por cancelamentos.

### Análise de Demanda Falha (Failure Demand)

A demanda falha caracteriza-se pelo retrabalho e novos contatos gerados por falhas na concepção original do serviço:

```
                  FLUXO DE GERADORES DE DEMANDA FALHA
+-----------------------------------------------------------------------+
|  Janela de Compensação Bancária  -->  Tentativa Precoce de Agendamento|
|  (GRU emitida no SIAR)                (Gera erro/Dúvidas na Ouvidoria)|
+-----------------------------------------------------------------------+
|  Divergência Cadastral Inicial   -->  Bloqueio na Triagem Presencial  |
|  (Dados de CPF/Certidões)             (Perda de vaga e reagendamento) |
+-----------------------------------------------------------------------+
|  Estouro de Prazo de Retirada    -->  Inutilização Regulamentar (90 d)|
|  (IN 173/2020 Art. 93)                (Perda da taxa / Novo processo) |
+-----------------------------------------------------------------------+
```

- **Atraso no Registro de Cobrança:** O intervalo entre a emissão da GRU e a efetiva transmissão do arquivo de compensação bancária gera tentativas frustradas de agendamento no SINPA, acarretando chamados adicionais de suporte.
- *FATO DOCUMENTADO (Abordando Falha 16 — Erro de digitação e nova GRU):* Corrigindo a premissa jurídica (Opção a), se um erro de preenchimento biográfico grosseiro for detectado apenas na triagem presencial, a praxe administrativa indica que erros simples de digitação de nomes podem ser saneados pelo próprio policial/atendente no guichê de atendimento presencial através do terminal local do SINPA, aproveitando a mesma taxa paga. Contudo, se houver divergência estrutural de titularidade do CPF ou impossibilidade de vinculação dos dados base da GRU, o atendimento não prossegue, gerando retrabalho no agendamento.
- *INFERÊNCIA (Abordando Falhas 28 e 29 — Métricas de demanda falha e Viés de sobrevivência):* Diante da lacuna de dados públicos, deduz-se analiticamente que a nota média de avaliação do passaporte no painel do Gov.br (historicamente fixada em patamares elevados próximos a 4,8 estrelas) apresenta um viés de sobrevivência. O indicador captura a percepção do usuário que concluiu a jornada com sucesso (retirou o documento físico), mas tende a omitir a fricção daqueles que abandonaram o fluxo devido a inconsistências de bases cadastrais, atrasos de compensação ou dificuldades de locomoção para cumprimento do prazo de retirada.

---

## 5. Lacunas de Evidência (Gap Analysis)

Por se tratar de uma pesquisa baseada exclusivamente em fontes documentais abertas, dados de transparência pública e relatórios de órgãos de controle externo, determinadas informações operacionais específicas não estão disponíveis ao público e permanecem mapeadas sob rigoroso isolamento analítico:

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

Esta tabela consolida o ecossistema expandido e retificado do serviço de emissão de passaporte comum brasileiro, fornecendo subsídios para futuras matrizes de atribuição de responsabilidades.

### Tabela 3: Síntese Corrigida de Atores e Sistemas

| Ator / Sistema | Camada de Atuação | Papel Principal na Jornada | Poder / Interesse (Mendelow) | Principal Fricção Associada |
| --- | --- | --- | --- | --- |
| **Sistema SINPA** | Parceiros de TI e Sistemas | Repositório oficial de dados biográficos, agendamento de postos e controle de fluxo do passaporte. | Alto Poder / Alto Interesse (Key Player) | Interface sem correções ortográficas preditivas integradas na fase inicial web. |
| **Divisão de Passaportes (DPas/PF)** | Gestores e Decisores | Planejamento, normatização procedimental e coordenação nacional da expedição. | Alto Poder / Alto Interesse (Key Player) | Sujeição à estabilidade orçamentária para a manutenção física de postos terceirizados. |
| **Casa da Moeda do Brasil (CMB)** | Fornecedores de Infraestrutura | Produção material das cadernetas físicas com papel de segurança e montagem de chips. | Alto Poder / Alto Interesse (Key Player) | Fluxo de suprimentos condicionado a limites fiscais de empenho e variações de insumos. |
| **Receita Federal (RFB)** | Órgãos de Controle e Validação | Gestão da base do CPF para validação de dados biográficos e regularidade cadastral. | Alto Poder / Baixo Interesse (Latente) | Bloqueio automatizado do avanço no formulário se houver divergências de dados no CPF. |
| **Cartórios de Registro Civil** | Órgãos de Controle e Validação | Emissão de certidões de nascimento/casamento e processamento de autorizações de menor (AEV). | Alto Poder / Baixo Interesse (Latente) | Custos de emolumentos cartoriais e descentralização de sistemas informáticos de consulta. |
| **Bancos Arrecadadores** | Parceiros de Infraestrutura | Acolhimento de pagamentos da GRU e envio de arquivos eletrônicos de retorno. | Médio Poder / Baixo Interesse (Latente) | Janela temporal de compensação de boletos, restringindo o agendamento em tempo real. |
| **CNJ** | Órgãos de Controle e Regulamentação | Edição de resoluções de viagem de menores e parametrização dos atos notariais integrados. | Alto Poder / Baixo Interesse (Latente) | Complexidade de interpretação de normas de representação legal por famílias monoparentais. |
| **ICAO** | Órgãos de Controle e Regulamentação | Fixação internacional de padrões de segurança e especificações de passaportes eletrônicos. | Alto Poder / Baixo Interesse (Latente) | Rigidez internacional que impede a flexibilização ou eliminação da etapa biométrica presencial. |
| **Atendentes e Policiais de Posto** | Operadores de Linha de Frente | Acolhimento presencial, triagem documental física, captura de biometria e entrega de livretes. | Baixo Poder / Alto Interesse (Sujeito) | Absorção do descontentamento do usuário em episódios de lentidão ou quedas de rede centralizadora. |
| **Cidadão Requerente** | Usuários Diretos | Alimentação de dados na web, quitação de obrigações tributárias e comparecimento aos atos. | Baixo Poder / Alto Interesse (Sujeito) | Exclusão digital e necessidade de custear taxas adicionais com intermediários por falhas de usabilidade. |
| **Despachantes e Assessorias** | Intermediários | Suporte logístico comercial privado de preenchimento e monitoramento de agendas. | Baixo Poder / Alto Interesse (Monitorar) | Exploração financeira de assimetrias informativas do portal de serviços públicos unificado. |
