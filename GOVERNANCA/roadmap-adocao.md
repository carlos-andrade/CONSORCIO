# Roadmap de adoção da GOVERNANCA — CONSORCIO

| Campo | Valor |
|---|---|
| **ID** | CONSORCIO-PLAN-GOV-001 |
| **Projeto** | CONSORCIO |
| **Repositório** | [carlos-andrade/CONSORCIO](https://github.com/carlos-andrade/CONSORCIO) |
| **Tipo documental** | PLANO |
| **Fase** | G0–G6 |
| **Estado** | EM_CURSO |
| **Versão** | 1.0.8 |
| **SHA-256 (conteúdo canónico)** | 40ba80e72598046fcbe861bac3d6fcc095f6e895d5d52f7c78c5507f8b1771f0 |
| **Commit de referência (versão anterior)** | [5789d1bbad87432e77f3cad7a4a40c4797cb130f](https://github.com/carlos-andrade/CONSORCIO/commit/5789d1bbad87432e77f3cad7a4a40c4797cb130f) |
| **Data de criação** | 2026-10-16 |
| **Data de atualização** | 2026-10-16 |
| **Responsável** | Responsável pelo projeto CONSORCIO |
| **Aprovador** | Política local aprovada; aprovação global e restantes gates sujeitos a critérios e evidências |
| **Origem** | Adoção da fonte normativa GOVERNANCA |
| **Autoridade superior** | [GOVERNANCA.md](../GOVERNANCA.md) e [Constituição GOV-001 — proposta para revisão](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CONSTITUICAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Contexto Histórico

O projeto adotou a governação central através de documentação no repositório CONSORCIO e de um workflow diário em GitHub Actions.

## Estado

A política local de governação, `GOVERNANCA.md` versão 1.0.2, foi aprovada expressamente pelo proprietário em 16 de outubro de 2026 e a decisão encontra-se registada em [CONSORCIO-DEC-G0-001](aprovacao-politica-governanca.md). A versão 1.0.3 da política local regista a decisão e atualiza os metadados, preservando o conteúdo substantivo aprovado. A auditoria de integridade da atualização corre pelo workflow após o commit. Esta aprovação não equivale a aprovação global, não ratifica a Constituição central e não conclui automaticamente os demais gates.

## Estado atual

G0 tem agora aprovada a política local; o gate apenas pode ser marcado concluído após verificar também os restantes critérios de entrada: objetivo, beneficiário, proprietário, responsável e autoridade normativa devidamente identificados. G1 e G2 permanecem em revisão; as decisões DEC-001 a DEC-006 ainda não foram resolvidas ou formalmente classificadas como não aplicáveis. G4 permanece em revisão até existir evidência real de evento `schedule` bem-sucedido e de um ensaio controlado de recuperação. A aprovação condicional de lançamento consta em [CONSORCIO-DEC-G5-001](decisao-aprovacao-condicional-lancamento.md), mas não comprova prontidão nem publicação. G5 e G6 permanecem pendentes.

## Fases e critérios de saída

| Gate | Objetivo | Critério de saída | Estado |
|---|---|---|---|
| G0 — Entrada | Propósito, beneficiário, responsável e autoridade | Política aprovada e restantes elementos de entrada verificados | EM_REVISAO |
| G1 — Viabilidade e inventário | Enumerar documentos e dependências | Relatório inspecionado e desvios priorizados | EM_REVISAO |
| G2 — Desenho | Requisitos, arquitetura, dados, privacidade, riscos e testes | Revisão G2 validada, decisões bloqueadoras resolvidas e critérios aceites | EM_REVISAO |
| G3 — Construção validada | Normalizar documentação e rever alterações | Diferenças auditáveis, testes concluídos, hashes corretos e auditoria limpa | CONCLUIDO |
| G4 — Prontidão operacional | Observabilidade, recuperação, segurança e suporte | Execução agendada confirmada, evidências verificadas e recuperação ensaiada | EM_REVISAO |
| G5 — Lançamento | Autorização explícita e observação | Aprovação condicional registada; conclusão dos gates, prontidão operacional e evidência de publicação ainda obrigatórias | PENDENTE |
| G6 — Encerramento | Aceitação, arquivo, transferência e lições | Critérios finais cumpridos e encerramento registado | PENDENTE |

## Política de atualização diária

O workflow em [governanca-diaria.yml](../.github/workflows/governanca-diaria.yml) está configurado para consultar a branch main de GOVERNANCA diariamente às 06:25 UTC e validar localmente os documentos Markdown do projeto. Os relatórios e o manifesto JSON de execução são produzidos por execução e publicados como artefactos GitHub Actions com retenção de 90 dias. O workflow aplica limite de 15 minutos e tenta preservar evidências mesmo quando testes/auditoria falham.

O workflow não atualiza automaticamente todos os conteúdos, porque uma alteração cega pode alterar significado, inventar aprovação ou criar referências SHA circulares. As correções ocorrem em lotes pequenos, com revisão de diffs e nova validação. A automação atualiza a validação e os relatórios e deteta alterações no mestre normativo.

## Evidências

- [Política de governação aprovada](../GOVERNANCA.md)
- [Decisão formal de aprovação da política — G0](aprovacao-politica-governanca.md)
- [README do projeto](../README.md)
- [Revisão G2](revisao-requisitos-arquitetura-dados-privacidade-riscos.md)
- [Workflow de validação](../.github/workflows/governanca-diaria.yml)
- [Auditor estático](../automation/audit_repository_documents.py)
- [Execução #35 — deteção da divergência](https://github.com/carlos-andrade/CONSORCIO/actions/runs/38893569303)
- [Execução #36 — auditoria limpa após correção G2](https://github.com/carlos-andrade/CONSORCIO/actions/runs/38893652381)
- [Execução #40 — auditoria limpa após normalização documental](https://github.com/carlos-andrade/CONSORCIO/actions/runs/38893795182)
- [Execução #47 — manifesto JSON válido e artefacto de três ficheiros](https://github.com/carlos-andrade/CONSORCIO/actions/runs/38894368824)
- [Execução #48 — seis documentos PASS, zero avisos/falhas](https://github.com/carlos-andrade/CONSORCIO/actions/runs/38894424857)
- [Runbook de operação e recuperação](runbook-operacao-diaria-recuperacao.md)
- [Decisão formal — aprovação condicional de lançamento](decisao-aprovacao-condicional-lancamento.md)
- [Relatório de fecho — aceitação e evidências](relatorio-fecho-aceitacao-evidencias.md)
- [Execução #57 — validação após registo da decisão de lançamento](https://github.com/carlos-andrade/CONSORCIO/actions/runs/38896595277)
- [Execução #72 — auditoria limpa após correção dos avisos](https://github.com/carlos-andrade/CONSORCIO/actions/runs/38900452064)

## Validação

A auditoria usa UTF-8, normaliza finais de linha para LF e calcula o SHA-256 canónico excluindo apenas as duas linhas de controlo definidas pela norma mestre. Verifica cabeçalhos, campos obrigatórios, estados, versões, datas, IDs duplicados, hash declarado e secções de governação. Não altera documentos auditados. A execução [#72](https://github.com/carlos-andrade/CONSORCIO/actions/runs/38900452064) validou a correção dos dois avisos: 9 documentos PASS, 0 WARN, 0 FAIL, testes unitários aprovados e manifesto gerado. O artefacto `consorcio-governanca-72` está disponível com retenção até 2027-01-14.

## Resultado

A política de governação local foi formalmente aprovada e a decisão está registada. G0 fica EM_REVISAO enquanto se confirma o conjunto completo de critérios de entrada; não declarar o gate fechado apenas por causa da aprovação da política. G3 permanece concluído. G1/G2/G4 ainda carecem de revisão/evidência especificada. G5/G6 permanecem pendentes. A auditoria documental #72 passou com 9 PASS, 0 WARN e 0 FAIL; este resultado técnico não altera os estados dos gates.

## Próxima Ação

Confirmar objetivo, beneficiário, responsável e autoridade normativa para completar G0; resolver DEC-001 a DEC-006; comprovar uma execução schedule bem-sucedida; realizar e registar ensaio de recuperação operacional; validar publicação/arquivo e obter aceitação final antes de encerrar.

## Histórico de alterações

| Versão | Data | Alteração | Evidência |
|---|---|---|---|
| 1.0.0 | 2026-10-16 | Criação do roadmap de adoção da GOVERNANCA | Commit de criação no GitHub |
| 1.0.1 | 2026-10-16 | Atualização do estado dos gates e evidências da auditoria documental | Commit anterior identificado no cabeçalho |
| 1.0.2 | 2026-10-16 | Registo da revisão G2 e atualização dos estados, evidências e próximos passos | Commit anterior |
| 1.0.3 | 2026-10-16 | Atualização da auditoria, correção do hash G2 e progresso de normalização documental | Execuções #35 e #36 |
| 1.0.4 | 2026-10-16 | Registo da normalização final, revisão de diffs e conclusão de G3 | Execução #40 |
| 1.0.5 | 2026-10-16 | Reforço de evidências e runbook; G4 em validação operacional | Execuções #47 e #48 |
| 1.0.6 | 2026-10-16 | Registo da aprovação condicional de lançamento sem alterar os estados pendentes dos gates | Decisão CONSORCIO-DEC-G5-001 e execução #57 |
| 1.0.7 | 2026-10-16 | Registo da aprovação formal da política local e atualização honesta do estado de G0 | Decisão CONSORCIO-DEC-G0-001 |
| 1.0.8 | 2026-10-16 | Registo da correção dos dois avisos documentais e auditoria limpa | Execução #72: 9 PASS, 0 WARN, 0 FAIL |
