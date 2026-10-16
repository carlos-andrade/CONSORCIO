# Inventário técnico e priorização de desvios — CONSORCIO

| Campo | Valor |
|---|---|
| **ID** | CONSORCIO-INV-G1-001 |
| **Projeto** | CONSORCIO |
| **Repositório** | [carlos-andrade/CONSORCIO](https://github.com/carlos-andrade/CONSORCIO) |
| **Tipo documental** | INVENTARIO |
| **Fase** | G1 — Viabilidade e inventário |
| **Estado** | CONCLUIDO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | HASH_PENDENTE |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-16 |
| **Data de atualização** | 2026-10-16 |
| **Responsável** | Responsável pelo projeto CONSORCIO |
| **Aprovador** | Revisão técnica do inventário; aceitação final global continua sujeita aos gates G5/G6 |
| **Origem** | Inspeção da árvore GitHub e dos documentos do projeto |
| **Autoridade superior** | [GOVERNANCA.md](../GOVERNANCA.md) e [GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Estado

Inventário concluído com base na árvore main observada em 2026-10-16. O repositório contém documentação de governação, auditoria estática Python, testes unitários e um workflow GitHub Actions. Não foi identificada aplicação transacional, base de dados de negócio, integração financeira ou publicação do produto.

## Inventário de artefactos

| Área | Artefactos | Estado observado | Lacuna |
|---|---|---|---|
| Entrada e contexto | README.md, GOVERNANCA.md | Propósito e política local documentados; política aprovada pelo proprietário | Manter âmbito explícito e não confundir aprovação local com ratificação da Constituição central |
| Governação | GOVERNANCA/README.md, GOVERNANCA/aprovacao-politica-governanca.md | Estrutura e decisão G0 registadas | Nenhuma lacuna documental crítica identificada para o âmbito atual |
| Planeamento | GOVERNANCA/roadmap-adocao.md | Gates G0–G6 e critérios definidos | Atualizar estados após cada evidência real |
| Desenho | GOVERNANCA/revisao-requisitos-arquitetura-dados-privacidade-riscos.md | Linha de base conservadora e decisões DEC-001–006 registadas | Validação formal da baseline; reabrir se houver expansão de âmbito |
| Operação | GOVERNANCA/runbook-operacao-diaria-recuperacao.md, .github/workflows/governanca-diaria.yml | Agendamento diário, dispatch manual, auditoria, manifesto e artefactos configurados | Falta execução com evento schedule e ensaio controlado de recuperação operacional |
| Auditoria | automation/audit_repository_documents.py, tests/test_audit_repository_documents.py | Auditor estático e testes unitários presentes; run #76 limpo | Revalidar após alterações documentais |
| Decisão de lançamento | GOVERNANCA/decisao-aprovacao-condicional-lancamento.md | Aprovação condicional registada | Não prova lançamento nem dispensa gates |
| Encerramento | GOVERNANCA/relatorio-fecho-aceitacao-evidencias.md | Critérios e pacote de evidências documentados | Aceitação final, arquivo duradouro e publicação não demonstrados |
| Licença | LICENSE | MIT no repositório | Confirmar que a licença escolhida cobre o conteúdo e as dependências futuras; não reutilizar fontes sem licença verificada |

## Desvios priorizados

| Prioridade | Desvio | Ação | Condição de fecho |
|---|---|---|---|
| P0 | Execução agendada não comprovada | Observar a primeira execução real com evento schedule e verificar resultado/artefactos | Run com event=schedule, success, testes e auditoria aprovados |
| P0 | Ensaio formal de recuperação ausente | Executar ensaio controlado sem expor segredos nem alterar dados de negócio | Registo do cenário, logs, resultado, recuperação e revisão |
| P0 | G2 precisa de validação formal da linha de base | Manter âmbito documental/analítico, sem dados pessoais ou transações | Decisão formal associada à revisão G2 |
| P1 | Arquivo de evidências limitado a 90 dias | Preservar artefactos finais e manifesto em arquivo aprovado | Local de arquivo, hash e acesso documentados |
| P1 | Fonte normativa central continua proposta | Aplicar apenas normas com estado normativo apropriado; registar divergências | Revisão de impacto após alteração formal da fonte |
| P2 | Produto operacional não existe no âmbito atual | Não criar stack, base de dados, orçamento ou SLA sem mudança de âmbito | Reabrir G2/G4 antes de desenvolver serviço |

## Evidências

- [Repositório oficial e árvore main](https://github.com/carlos-andrade/CONSORCIO).
- [Política local aprovada](../GOVERNANCA.md).
- [Revisão G2 e decisões](revisao-requisitos-arquitetura-dados-privacidade-riscos.md).
- [Workflow diário](../.github/workflows/governanca-diaria.yml).
- [Execução #76 — auditoria documental limpa](https://github.com/carlos-andrade/CONSORCIO/actions/runs/38900656563).

## Validação

A árvore do repositório e os artefactos indicados foram inspecionados. A execução #76 confirmou a auditoria estática limpa no commit f27455d813a64d387f3cd3ae1c43f3a21c92074d, com 9 PASS, 0 WARN e 0 FAIL. O histórico consultado contém 76 execuções, todas acionadas por push; não foi encontrada execução schedule. A validação do inventário não equivale a teste de aplicação, recuperação operacional, publicação ou aceitação final.

## Resultado

G1 concluído para o inventário documental/técnico e priorização de desvios do âmbito atual. Os bloqueios operacionais P0 permanecem atribuídos a G4 e impedem declarar o projeto pronto para lançamento/encerramento.

## Próxima Ação

Executar e preservar a evidência da primeira execução schedule; realizar ensaio controlado de recuperação; validar formalmente a baseline G2 e preservar evidências finais antes de avaliar G5/G6.

## Histórico de alterações

| Versão | Data | Alteração | Evidência |
|---|---|---|---|
| 1.0.0 | 2026-10-16 | Inventário técnico, lacunas e prioridades de remediação | Inspeção da árvore main e auditoria #76 |
