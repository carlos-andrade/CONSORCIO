# Roadmap de adoção da GOVERNANCA — CONSORCIO

| Campo | Valor |
|---|---|
| **ID** | CONSORCIO-PLAN-GOV-001 |
| **Projeto** | CONSORCIO |
| **Repositório** | [carlos-andrade/CONSORCIO](https://github.com/carlos-andrade/CONSORCIO) |
| **Tipo documental** | PLANO |
| **Fase** | G0–G6 |
| **Estado** | EM_CURSO |
| **Versão** | 1.1.4 |
| **SHA-256 (conteúdo canónico)** | 0d09316d9bfb110cb12e37912a7885fe45ee296bcab501c7accbe00e1635caec |
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

G0 foi concluído no âmbito atual: propósito documental/analítico, beneficiário/utilizador-alvo, proprietário, papéis funcionais e política local aprovada estão documentados. G1 foi concluído com inventário e priorização em [CONSORCIO-INV-G1-001](inventario-g1.md). G2 foi aprovado formalmente em 2026-10-16 para a baseline documental/analítica, através da decisão [CONSORCIO-DEC-G2-001](decisao-aprovacao-g2.md) e revisão técnica v1.0.2. A estrutura inicial foi criada e documentada em [ESTRUTURA.md](../ESTRUTURA.md); a validação pós-alteração ainda está em curso. A aprovação não conclui G4, G5 ou G6. G4 permanece em revisão até existir evidência real de evento `schedule` bem-sucedido e de um ensaio controlado de recuperação. A aprovação condicional de lançamento consta em [CONSORCIO-DEC-G5-001](decisao-aprovacao-condicional-lancamento.md), mas não comprova prontidão nem publicação. G5 e G6 permanecem pendentes.

## Fases e critérios de saída

| Gate | Objetivo | Critério de saída | Estado |
|---|---|---|---|
| G0 — Entrada | Propósito, beneficiário, responsável e autoridade | Política local aprovada; âmbito, beneficiário, proprietário e papéis documentados | CONCLUIDO |
| G1 — Viabilidade e inventário | Enumerar documentos e dependências | [Inventário técnico](inventario-g1.md) concluído e desvios priorizados | CONCLUIDO |
| G2 — Desenho | Requisitos, arquitetura, dados, privacidade, riscos e testes | Baseline conservadora aprovada e decisão formal registada; execução de testes de negócio continua condicionada à implementação | CONCLUIDO |
| G3 — Construção validada | Criar a estrutura inicial e validar os artefactos resultantes | Estrutura remota verificada, hashes corretos, testes e auditoria limpa após alterações | EM_CURSO |
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
- [Inventário G1 e desvios priorizados](inventario-g1.md)
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
- [Execução #88 — auditoria limpa após atualização do inventário, G2, roadmap, README, runbook e relatório de fecho](https://github.com/carlos-andrade/CONSORCIO/actions/runs/38901648930)
- [Execução #94 — auditoria limpa da revisão seguinte](https://github.com/carlos-andrade/CONSORCIO/actions/runs/38901886731)
- [Execuções #95/#96 — teste de scheduler inconclusivo e recuperação da configuração](https://github.com/carlos-andrade/CONSORCIO/actions/runs/38901961328)

## Validação

A auditoria usa UTF-8, normaliza finais de linha para LF e calcula o SHA-256 canónico excluindo apenas as duas linhas de controlo definidas pela norma mestre. Verifica cabeçalhos, campos obrigatórios, estados, versões, datas, IDs duplicados, hash declarado e secções de governação. Não altera documentos auditados. A execução [#94](https://github.com/carlos-andrade/CONSORCIO/actions/runs/38901886731) validou o commit `fd8d77ece952d4679c5e595ee059e51ff1841326`: 10 documentos PASS, 0 WARN, 0 FAIL, testes unitários aprovados e manifesto gerado. O teste temporário de scheduler em #95/#96 foi inconclusivo e o cron diário original foi restaurado. O histórico consultado não contém evento `schedule`; G4/G5/G6 continuam dependentes de evidência operacional, publicação e aceitação.

## Resultado

A política local está aprovada; G0 e G1 foram concluídos para o âmbito documental/analítico. G2 foi formalmente aprovado pela decisão CONSORCIO-DEC-G2-001. G3 está em curso para criação e validação da estrutura inicial. G4 depende de execução `schedule` e ensaio controlado de recuperação. G5/G6 permanecem pendentes. A auditoria pós-estrutura [#117](https://github.com/carlos-andrade/CONSORCIO/actions/runs/38906302112) terminou com 12 PASS, 0 WARN e 0 FAIL; os hashes canónicos dos documentos Markdown foram reconciliados e a árvore remota foi verificada. O teste #95/#96 foi inconclusivo e o cron diário original está restaurado.

## Próxima Ação

Subfase de criação da estrutura inicial validada pela auditoria #117 e verificação remota. Continuar G3 com requisitos específicos, modelos e casos de teste incrementais; não declarar módulos de negócio implementados. Em paralelo, comprovar uma execução schedule bem-sucedida e realizar/registar ensaio de recuperação antes de avaliar G5/G6.

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
| 1.0.9 | 2026-10-16 | Fecho documental de G0/G1, baseline conservadora G2 e atualização dos bloqueios operacionais | Inventário G1 e revisão G2 v1.0.1 |
| 1.1.0 | 2026-10-16 | Atualização da evidência para a auditoria limpa #88; estados G0/G1 e bloqueios G2/G4/G5/G6 consolidados | Execução #88: 10 PASS, 0 WARN, 0 FAIL |
| 1.1.1 | 2026-10-16 | Registo da auditoria #94 e do teste de scheduler inconclusivo, com cron restaurado | Execuções #94–#96 |
| 1.1.2 | 2026-10-16 | Registo da aprovação formal de G2 e preservação dos bloqueios G4–G6 | CONSORCIO-DEC-G2-001 |
| 1.1.3 | 2026-10-16 | Registo da criação da estrutura inicial e reabertura controlada de G3 até auditoria pós-alteração | ESTRUTURA.md e commits de estrutura |
| 1.1.4 | 2026-10-16 | Auditoria pós-estrutura limpa e hashes reconciliados; subfase estrutural validada | Execução #117: 12 PASS, 0 WARN, 0 FAIL |
