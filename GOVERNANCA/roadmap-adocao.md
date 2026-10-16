# Roadmap de adoção da GOVERNANCA — CONSORCIO

| Campo | Valor |
|---|---|
| **ID** | CONSORCIO-PLAN-GOV-001 |
| **Projeto** | CONSORCIO |
| **Repositório** | [carlos-andrade/CONSORCIO](https://github.com/carlos-andrade/CONSORCIO) |
| **Tipo documental** | PLANO |
| **Fase** | G0–G6 |
| **Estado** | EM_CURSO |
| **Versão** | 1.0.3 |
| **SHA-256 (conteúdo canónico)** | c25f1f705e1ebfd4c931801a2f9096f947ecde291c28d5c10949465055b9f6fd |
| **Commit de referência (versão anterior)** | [5789d1bbad87432e77f3cad7a4a40c4797cb130f](https://github.com/carlos-andrade/CONSORCIO/commit/5789d1bbad87432e77f3cad7a4a40c4797cb130f) |
| **Data de criação** | 2026-10-16 |
| **Data de atualização** | 2026-10-16 |
| **Responsável** | Responsável pelo projeto CONSORCIO |
| **Aprovador** | Pendente de registo formal |
| **Origem** | Adoção da fonte normativa GOVERNANCA |
| **Autoridade superior** | [GOVERNANCA.md](../GOVERNANCA.md) e [CONSTITUICAO.md](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CONSTITUICAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Contexto Histórico

O projeto adotou a governação central através de documentação no repositório CONSORCIO e de um workflow diário em GitHub Actions.

## Estado

A validação documental está automatizada. A execução #36 confirmou 5 documentos PASS, 0 WARN e 0 FAIL e 2 testes unitários aprovados. A normalização do README e deste roadmap foi feita depois dessa execução e requer nova validação pós-commit. A aprovação global e os gates permanecem sujeitos a revisão humana.

## Estado atual

A execução [#35](https://github.com/carlos-andrade/CONSORCIO/actions/runs/38893569303) detetou divergência no hash canónico da revisão G2; foi corrigida a secção obrigatória `## Estado` e recalculado o hash. A execução [#36](https://github.com/carlos-andrade/CONSORCIO/actions/runs/38893652381) validou 5 documentos com PASS=5, WARN=0, FAIL=0 e 2 testes unitários aprovados. A normalização subsequente do README e deste roadmap ainda exige validação após o commit correspondente. G2 permanece EM_REVISAO: os requisitos são uma linha de base proposta e DEC-001 a DEC-006 dependem de decisão/validação humana. G0 continua dependente da aprovação formal do proprietário.

## Fases e critérios de saída

| Gate | Objetivo | Critério de saída | Estado |
|---|---|---|---|
| G0 — Entrada | Propósito, beneficiário, responsável e autoridade | Política e fonte normativa identificadas e aprovadas formalmente | EM_CURSO |
| G1 — Viabilidade e inventário | Enumerar documentos e dependências | Relatório inspecionado e desvios priorizados | EM_REVISAO |
| G2 — Desenho | Requisitos, arquitetura, dados, privacidade, riscos e testes | Revisão G2 validada, decisões bloqueadoras resolvidas e critérios aceites | EM_REVISAO |
| G3 — Construção validada | Normalizar documentação e rever alterações | Diferenças auditáveis, testes concluídos, hashes corretos e auditoria limpa | EM_REVISAO |
| G4 — Prontidão operacional | Observabilidade, recuperação, segurança e suporte | Execução diária confirmada e falhas tratadas | PENDENTE |
| G5 — Lançamento | Autorização explícita e observação | Aprovação humana e evidência de publicação | PENDENTE |
| G6 — Encerramento | Aceitação, arquivo, transferência e lições | Critérios finais cumpridos e encerramento registado | PENDENTE |

## Política de atualização diária

O workflow em [governanca-diaria.yml](../.github/workflows/governanca-diaria.yml) consulta a branch main de GOVERNANCA diariamente às 06:25 UTC e valida localmente os documentos Markdown do projeto. Os relatórios são produzidos por execução e publicados como artefactos de GitHub Actions.

O workflow não atualiza automaticamente todos os conteúdos, porque uma alteração cega pode alterar significado, inventar aprovação ou criar referências SHA circulares. As correções ocorrem em lotes pequenos, com revisão de diffs e nova validação. A automação atualiza a validação e os relatórios e deteta alterações no mestre normativo.

## Evidências

- [Política de governação](../GOVERNANCA.md)
- [README do projeto](../README.md)
- [Revisão G2](revisao-requisitos-arquitetura-dados-privacidade-riscos.md)
- [Workflow de validação](../.github/workflows/governanca-diaria.yml)
- [Auditor estático](../automation/audit_repository_documents.py)
- [Execução #35 — deteção da divergência](https://github.com/carlos-andrade/CONSORCIO/actions/runs/38893569303)
- [Execução #36 — auditoria limpa após correção G2](https://github.com/carlos-andrade/CONSORCIO/actions/runs/38893652381)

## Validação

A auditoria usa UTF-8, normaliza finais de linha para LF e calcula o SHA-256 canónico excluindo apenas as duas linhas de controlo definidas pela norma mestre. Verifica cabeçalhos, campos obrigatórios, estados, versões, datas, IDs duplicados, hash declarado e secções de governação. Não altera documentos auditados. A execução #36 confirmou a revisão G2; o README e este roadmap foram alterados depois dela e requerem nova execução.

## Resultado

A base documental e a auditoria automatizada estão instaladas. A divergência de hash e a secção obrigatória ausente na revisão G2 foram corrigidas e a execução #36 ficou limpa (5 PASS, 0 WARN, 0 FAIL). As alterações mais recentes ao README e ao roadmap aguardam validação pós-commit. Não se declara conformidade integral nem aprovação humana dos gates.

## Próxima Ação

Executar e inspecionar a auditoria após a normalização do README e do roadmap; corrigir qualquer desvio; rever o diff final e resolver DEC-001 a DEC-006 com o proprietário antes de promover G2.

## Histórico de alterações

| Versão | Data | Alteração | Evidência |
|---|---|---|---|
| 1.0.0 | 2026-10-16 | Criação do roadmap de adoção da GOVERNANCA | Commit de criação no GitHub |
| 1.0.1 | 2026-10-16 | Atualização do estado dos gates e evidências da auditoria documental | Commit anterior identificado no cabeçalho |
| 1.0.2 | 2026-10-16 | Registo da revisão G2 e atualização dos estados, evidências e próximos passos | Commit anterior |
| 1.0.3 | 2026-10-16 | Atualização da auditoria, correção do hash G2 e progresso de normalização documental | Execuções #35 e #36 |
