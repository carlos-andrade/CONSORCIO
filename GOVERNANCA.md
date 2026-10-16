# Governação do projeto CONSORCIO

| Campo | Valor |
|---|---|
| **ID** | CONSORCIO-POL-001 |
| **Projeto** | CONSORCIO |
| **Repositório** | [carlos-andrade/CONSORCIO](https://github.com/carlos-andrade/CONSORCIO) |
| **Tipo documental** | POLITICA |
| **Fase** | G0 — Governação e entrada |
| **Estado** | EM_CURSO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | A calcular na normalização inicial — ver issue #1 |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-16 |
| **Data de atualização** | 2026-10-16 |
| **Responsável** | Responsável pelo projeto CONSORCIO |
| **Aprovador** | Pendente de registo formal |
| **Origem** | Instrução de adoção e [repositório GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Autoridade superior** | [GOVERNANCA/CONSTITUICAO.md](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CONSTITUICAO.md) e normas aprovadas em GOVERNANCA |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |
| **Rastreabilidade** | Workflow diário em `.github/workflows/governanca-diaria.yml` |
| **Escopo** | Documentação, requisitos, código, testes, alterações e evidências deste repositório |
| **Objetivo** | Aplicar as regras mestres de governação ao CONSORCIO e manter verificações documentais diárias |
| **Dependências** | GOVERNANCA, GitHub Actions e permissões do repositório |

## Contexto Histórico

O repositório CONSORCIO adota o repositório [GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) como fonte normativa central. As regras são consultadas na branch principal do repositório mestre; não devem ser copiadas de forma a criar uma segunda fonte normativa divergente.

A Constituição da GOVERNANCA encontra-se identificada no repositório mestre como **proposta para revisão**. A norma de cabeçalho documental v1.0.3 está identificada como **aprovada**. A adoção respeita o estado de cada artefacto de origem e não transforma propostas em normas ratificadas.

## Estado

A política de adoção e o workflow foram adicionados como base operacional. A conformidade global do projeto só poderá ser declarada depois de inventário e auditoria individual de todos os documentos e outros artefactos aplicáveis.

## Evidências

- [Primeiro relatório de auditoria automatizada](https://github.com/carlos-andrade/CONSORCIO/actions/runs/38888136512).
- [Registo de remediação — issue #1](https://github.com/carlos-andrade/CONSORCIO/issues/1).

## Regras obrigatórias de execução

1. A lei aplicável, contratos vinculativos e políticas formalmente aprovadas têm precedência sobre padrões, procedimentos, recomendações e exemplos.
2. Cada documento Markdown deve começar com título de nível 1 e tabela Markdown de metadados conforme a norma aprovada de cabeçalho.
3. Quando aplicável, os metadados devem incluir ID único, projeto, repositório, tipo, fase, estado, versão, SHA-256 canónico, commit anterior, datas, responsável, aprovador, origem, autoridade superior, cadeia de autoridade e rastreabilidade.
4. Não inventar aprovações, resultados, evidências, testes ou estados. O estado deve representar o que foi comprovado.
5. O SHA-256 canónico não é o Git blob SHA. O cálculo segue a norma mestre: UTF-8, finais de linha LF, BOM removido e exclusão apenas das linhas dos campos SHA-256 canónico e commit de referência.
6. O commit de referência deve apontar para um commit anterior real, quando disponível. Não criar referência circular para o commit que contém a própria alteração.
7. Preservar conteúdo substantivo e histórico. A automação diária identifica desvios e publica um relatório; não reescreve automaticamente o conteúdo de todos os documentos.
8. Controlos usam os estados PASS, WARN, FAIL e UNKNOWN. Ausência de evidência ou execução nunca equivale a PASS.
9. Registar exceções com regra, motivo, risco, controlos compensatórios, aprovador, validade, responsável e condição de revogação. Exceções não dispensam obrigações legais ou contratuais.
10. Aplicar os gates G0–G6 de forma proporcional ao risco e manter evidência de aceitação, revisão e lançamento.
11. As alterações automatizadas devem ser idempotentes, auditáveis, de escopo mínimo e reversíveis. O workflow diário tem permissões de leitura e não faz commit nem aprovação automática.
12. A atualização automática verifica as regras publicadas em GOVERNANCA na execução diária. Alterações normativas materiais exigem avaliação de impacto humana antes de serem consideradas conformes.

## Validação

A primeira execução da auditoria estática foi concluída operacionalmente. O relatório identificou quatro avisos não bloqueantes, relacionados com hashes canónicos em falta e algumas secções documentais. A auditoria não prova conformidade integral. A pendência está registada em [issue #1](https://github.com/carlos-andrade/CONSORCIO/issues/1).

## Evidências e validação

- Fonte normativa: [repositório GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA).
- Norma de cabeçalho: [NORMA-CABECALHO-PADRAO.md](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md).
- Constituição do sistema: [CONSTITUICAO.md](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CONSTITUICAO.md).
- Automação: [governanca-diaria.yml](.github/workflows/governanca-diaria.yml).
- Relatório gerado: [relatorio-diario.md](GOVERNANCA/relatorio-diario.md).

## Resultado

A regra de autoridade central está documentada e o controlo diário é preparado como validação, deteção de desvios e relatório. A existência da política e do workflow, por si só, não prova que todos os documentos já estejam normalizados nem que a primeira execução diária tenha passado.

## Próxima Ação

Executar o workflow manualmente em GitHub Actions, rever o relatório de conformidade, corrigir os desvios por lotes pequenos e voltar a validar. A publicação de estado APROVADO exige evidência apropriada.

## Histórico de alterações

| Versão | Data | Alteração | Responsável | Evidência |
|---|---|---|---|---|
| 1.0.0 | 2026-10-16 | Criação da política de adoção da governação central | Responsável pelo projeto | Commit de criação no GitHub |
