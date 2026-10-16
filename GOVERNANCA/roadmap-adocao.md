# Roadmap de adoção da GOVERNANCA — CONSORCIO

| Campo | Valor |
|---|---|
| **ID** | CONSORCIO-PLAN-GOV-001 |
| **Projeto** | CONSORCIO |
| **Repositório** | [carlos-andrade/CONSORCIO](https://github.com/carlos-andrade/CONSORCIO) |
| **Tipo documental** | PLANO |
| **Fase** | G0–G6 |
| **Estado** | EM_CURSO |
| **Versão** | 1.0.6 |
| **SHA-256 (conteúdo canónico)** | c59ce375fe322d35bd851963cdf185f1aff51427e2c40ad416774092e7f86801 |
| **Commit de referência (versão anterior)** | [5789d1bbad87432e77f3cad7a4a40c4797cb130f](https://github.com/carlos-andrade/CONSORCIO/commit/5789d1bbad87432e77f3cad7a4a40c4797cb130f) |
| **Data de criação** | 2026-10-16 |
| **Data de atualização** | 2026-10-16 |
| **Responsável** | Responsável pelo projeto CONSORCIO |
| **Aprovador** | Aprovação condicional de lançamento registada; aprovação dos gates pendente |
| **Origem** | Adoção da fonte normativa GOVERNANCA |
| **Autoridade superior** | [GOVERNANCA.md](../GOVERNANCA.md) e [CONSTITUICAO.md](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CONSTITUICAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Contexto Histórico

O projeto adotou a governação central através de documentação no repositório CONSORCIO e de um workflow diário em GitHub Actions.

## Estado

A validação documental está automatizada. A execução [#40](https://github.com/carlos-andrade/CONSORCIO/actions/runs/38893795182) confirmou 5 documentos PASS, 0 WARN e 0 FAIL e 2 testes unitários aprovados após a normalização do README e deste roadmap. Foi registada a aprovação condicional de lançamento do proprietário; a aprovação global e a conclusão dos gates permanecem sujeitas a evidências e revisão humana.

## Estado atual

A execução [#35](https://github.com/carlos-andrade/CONSORCIO/actions/runs/38893569303) detetou divergência no hash canónico da revisão G2; foi corrigida a secção obrigatória `## Estado` e recalculado o hash. A execução [#36](https://github.com/carlos-andrade/CONSORCIO/actions/runs/38893652381) validou a revisão G2. A execução [#40](https://github.com/carlos-andrade/CONSORCIO/actions/runs/38893795182) confirmou a normalização do README e do roadmap: 5 PASS, 0 WARN, 0 FAIL e 2 testes unitários aprovados. G2 permanece EM_REVISAO: os requisitos são uma linha de base proposta e DEC-001 a DEC-006 dependem de decisão/validação humana. A aprovação condicional de lançamento foi registada em [CONSORCIO-DEC-G5-001](decisao-aprovacao-condicional-lancamento.md). G0 continua dependente da aprovação formal da política de governação; a decisão condicional não encerra gates.

## Fases e critérios de saída

| Gate | Objetivo | Critério de saída | Estado |
|---|---|---|---|
| G0 — Entrada | Propósito, beneficiário, responsável e autoridade | Política e fonte normativa identificadas e aprovadas formalmente | EM_CURSO |
| G1 — Viabilidade e inventário | Enumerar documentos e dependências | Relatório inspecionado e desvios priorizados | EM_REVISAO |
| G2 — Desenho | Requisitos, arquitetura, dados, privacidade, riscos e testes | Revisão G2 validada, decisões bloqueadoras resolvidas e critérios aceites | EM_REVISAO |
| G3 — Construção validada | Normalizar documentação e rever alterações | Diferenças auditáveis, testes concluídos, hashes corretos e auditoria limpa | CONCLUIDO |
| G4 — Prontidão operacional | Observabilidade, recuperação, segurança e suporte | Execução agendada confirmada, evidências verificadas e recuperação ensaiada | EM_REVISAO |
| G5 — Lançamento | Autorização explícita e observação | Aprovação condicional registada; conclusão dos gates, prontidão operacional e evidência de publicação ainda obrigatórias | PENDENTE |
| G6 — Encerramento | Aceitação, arquivo, transferência e lições | Critérios finais cumpridos e encerramento registado | PENDENTE |

## Política de atualização diária

O workflow em [governanca-diaria.yml](../.github/workflows/governanca-diaria.yml) consulta a branch main de GOVERNANCA diariamente às 06:25 UTC e valida localmente os documentos Markdown do projeto. Os relatórios e o manifesto JSON de execução são produzidos por execução e publicados como artefactos de GitHub Actions com retenção de 90 dias. O workflow aplica limite de 15 minutos e tenta preservar evidências mesmo quando testes/auditoria falham.

O workflow não atualiza automaticamente todos os conteúdos, porque uma alteração cega pode alterar significado, inventar aprovação ou criar referências SHA circulares. As correções ocorrem em lotes pequenos, com revisão de diffs e nova validação. A automação atualiza a validação e os relatórios e deteta alterações no mestre normativo.

## Evidências

- [Política de governação](../GOVERNANCA.md)
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
- [Execução #57 — validação após registo da decisão](https://github.com/carlos-andrade/CONSORCIO/actions/runs/38896595277)

## Validação

A auditoria usa UTF-8, normaliza finais de linha para LF e calcula o SHA-256 canónico excluindo apenas as duas linhas de controlo definidas pela norma mestre. Verifica cabeçalhos, campos obrigatórios, estados, versões, datas, IDs duplicados, hash declarado e secções de governação. Não altera documentos auditados. A execução #40 validou os cinco documentos e os hashes após a normalização.

## Resultado

G3 está concluída. A execução #57 terminou com sucesso nos testes e na auditoria documental, com manifesto e artefacto registados. Foi recebida e registada a aprovação condicional de lançamento em [CONSORCIO-DEC-G5-001](decisao-aprovacao-condicional-lancamento.md). A decisão não comprova cumprimento das condições: as execuções observadas continuam sem evento schedule comprovado, não há ensaio formal de recuperação registado, e G0/G1/G2/G4 permanecem por fechar. G5 e G6 continuam PENDENTES.

## Próxima Ação

Resolver DEC-001 a DEC-006 e obter as aprovações G0/G1/G2; observar e registar uma execução schedule bem-sucedida; executar um ensaio de recuperação documentado; verificar artefactos e retenção; concluir a revisão G4. Só depois avaliar o cumprimento das condições de G5 e a aceitação final G6.

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
