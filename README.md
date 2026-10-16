# CONSORCIO

| Campo | Valor |
|---|---|
| **ID** | CONSORCIO-README-001 |
| **Projeto** | CONSORCIO |
| **Repositório** | [carlos-andrade/CONSORCIO](https://github.com/carlos-andrade/CONSORCIO) |
| **Tipo documental** | README |
| **Fase** | G3 — Construção controlada |
| **Estado** | EM_CURSO |
| **Versão** | 1.0.7 |
| **SHA-256 (conteúdo canónico)** | dff3500304ed6eb91068e4a2f1bc60947902e7421919e98bcf6cc22458bdec02 |
| **Commit de referência (versão anterior)** | [e5e2875e63e1594c461487227150d1f1832cbf3b](https://github.com/carlos-andrade/CONSORCIO/commit/e5e2875e63e1594c461487227150d1f1832cbf3b) |
| **Data de criação** | 2026-10-16 |
| **Data de atualização** | 2026-10-16 |
| **Responsável** | Responsável pelo projeto CONSORCIO |
| **Aprovador** | Proprietário do projeto — decisão G2 registada em 2026-10-16 |
| **Origem** | Documento inicial e instrução de adoção do projeto |
| **Autoridade superior** | [GOVERNANCA.md](GOVERNANCA.md) e [repositório GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |
| **Rastreabilidade** | [.github/workflows/governanca-diaria.yml](.github/workflows/governanca-diaria.yml) |
| **Objetivo** | Documentar o propósito do projeto e a forma de execução da governação |
| **Dependências** | Repositório GOVERNANCA e GitHub Actions |

## Estado

O projeto está na fase de adoção controlada da governação. A auditoria documental automatizada está instalada e a decisão CONSORCIO-DEC-G2-001 aprovou formalmente a baseline documental/analítica. A estrutura inicial do projeto está descrita em [ESTRUTURA.md](ESTRUTURA.md), com diretórios separados para governação, dados, modelos, análises, relatórios e testes. Os módulos de negócio ainda não estão implementados. G4 continua a exigir evidência de execução agendada bem-sucedida e ensaio controlado de recuperação; não existe declaração de conformidade integral.

## Estrutura inicial

Consultar [ESTRUTURA.md](ESTRUTURA.md) para o mapa de diretórios, respetivos objetivos, limites de segurança e critérios de aceitação.

## Objetivo do projeto

O consórcio no Brasil é uma modalidade de compra baseada na união de pessoas físicas ou jurídicas em grupo para aquisição de bens ou serviços, com contribuições periódicas e regras contratuais próprias. Embora não tenha juros remuneratórios como um empréstimo tradicional, o consórcio pode incluir taxa de administração, fundo de reserva, seguros e outros encargos previstos no contrato. A análise económica deve considerar todos os custos e condições de contemplação.

O projeto CONSORCIO destina-se a estudar, documentar e avaliar estruturas, custos, riscos, estratégias e decisões relacionadas com consórcios, com base em fontes verificáveis e pressupostos explícitos.

## Governação obrigatória

Toda a governação do projeto é gerida pela fonte normativa central:

- [Repositório GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA)
- [Constituição do Sistema de Governança](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CONSTITUICAO.md)
- [Norma de cabeçalho documental padrão](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md)
- [Política de governação do CONSORCIO](GOVERNANCA.md)

As regras devem ser interpretadas segundo o estado registado de cada artefacto mestre. A Constituição da GOVERNANCA está identificada como proposta para revisão, enquanto a norma de cabeçalho v1.0.3 está identificada como aprovada. A adoção desta governação não equivale a uma declaração de conformidade integral do projeto.

## Atualização e validação automáticas

O workflow [GOVERNANCA — validação documental diária](.github/workflows/governanca-diaria.yml) está configurado para:

1. Executar diariamente às 06:25 UTC e também em execução manual ou após alterações relevantes na branch `main`.
2. Consultar a versão corrente da branch `main` de GOVERNANCA, sem copiar as normas para criar uma fonte paralela.
3. Inventariar ficheiros documentais e validar cabeçalhos, estados, metadados, integridade SHA-256, identificadores e referências.
4. Gerar relatório Markdown e JSON com resultados PASS, WARN, FAIL e UNKNOWN.
5. Guardar relatórios como artefactos da execução e falhar quando forem identificados erros de conformidade.

A automação é de validação e deteção: **não reescreve automaticamente o conteúdo substantivo de todos os documentos, não inventa aprovações e não faz commits automáticos**. A correção é efetuada de forma controlada, preservando conteúdo e histórico. Para forçar uma validação, abrir o separador Actions e executar o workflow manualmente.

## Estado de implementação

- Adoção explícita da governação central: documentada.
- Cabeçalho e hash canónico do README: normalizados e validados na execução #40.
- Workflow diário: configurado no repositório.
- Auditoria documental: execução #48 confirmou 6 documentos PASS, 0 WARN e 0 FAIL; 2 testes unitários passaram.
- Aprovação formal da conformidade global: pendente de evidência e revisão humana.
- G0 e G1: concluídos para o âmbito documental/analítico.
- G2: baseline conservadora registada; validação formal pendente.
- G4: execução schedule e ensaio de recuperação ainda não comprovados.

## Operação e recuperação

- Workflow: [validação documental diária](.github/workflows/governanca-diaria.yml).
- Runbook: [operação diária, evidências e recuperação](GOVERNANCA/runbook-operacao-diaria-recuperacao.md).
- Evidências recentes: [execução #47 — manifesto válido](https://github.com/carlos-andrade/CONSORCIO/actions/runs/38894368824) e [execução #48 — auditoria limpa](https://github.com/carlos-andrade/CONSORCIO/actions/runs/38894424857).
- A auditoria #94 foi limpa. O teste temporário de scheduler em #95/#96 foi inconclusivo, a configuração foi corrigida e o cron diário original foi restaurado; ainda não há evento schedule nem ensaio formal de recuperação comprovados. G4 não está concluída.

## Roadmap

| Fase | Atividade | Estado |
|---|---|---|
| G0 | Definir propósito, autoridade e âmbito | CONCLUIDO |
| G1 | Inventariar documentos, código e dados | CONCLUIDO |
| G2 | Rever requisitos, arquitetura, dados, privacidade e riscos | EM_REVISAO |
| G3 | Normalizar documentos e validar alterações | CONCLUIDO |
| G4 | Verificar execução diária, relatórios e recuperação | EM_REVISAO |
| G5 | Aceitação e autorização explícitas | PENDENTE |
| G6 | Encerramento documentado quando os critérios forem cumpridos | PENDENTE |

## Evidências

- [Inventário G1](GOVERNANCA/inventario-g1.md).
- [Revisão G2 e decisões DEC-001–006](GOVERNANCA/revisao-requisitos-arquitetura-dados-privacidade-riscos.md).
- Governação central: [GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA).
- Política de adoção: [GOVERNANCA.md](GOVERNANCA.md).
- Workflow diário: [governanca-diaria.yml](.github/workflows/governanca-diaria.yml).
- Primeira auditoria executada: [GitHub Actions run 6](https://github.com/carlos-andrade/CONSORCIO/actions/runs/38888136512).
- Pendência de remediação documental: [issue #1](https://github.com/carlos-andrade/CONSORCIO/issues/1).

## Validação

A validação automatizada é estática e de leitura. A última execução confirmada analisou quatro documentos, com 0 falhas bloqueantes e 4 avisos: os quatro documentos ainda precisam de valores SHA-256 canónicos válidos, e há secções de governação opcionais por completar em alguns ficheiros. Este resultado não representa conformidade total.

## Resultado

A governação central está referenciada, e o workflow diário foi executado com sucesso operacional. A conformidade documental permanece pendente até a resolução dos avisos e uma nova execução sem pendências ou com exceções justificadas.

## Próxima Ação

Resolver a [issue #1](https://github.com/carlos-andrade/CONSORCIO/issues/1), calcular os hashes canónicos conforme a norma GOVERNANCA e repetir a auditoria.

## Histórico de alterações

| Versão | Data | Alteração | Evidência |
|---|---|---|---|
| 1.0.0 | 2026-10-16 | Cabeçalho normalizado, referência normativa e mecanismo de validação descritos | Commit de atualização no GitHub |
