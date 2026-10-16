# Roadmap de adoção da GOVERNANCA — CONSORCIO

| Campo | Valor |
|---|---|
| **ID** | CONSORCIO-PLAN-GOV-001 |
| **Projeto** | CONSORCIO |
| **Repositório** | [carlos-andrade/CONSORCIO](https://github.com/carlos-andrade/CONSORCIO) |
| **Tipo documental** | PLANO |
| **Fase** | G0–G6 |
| **Estado** | EM_CURSO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | e67d77640e511c582cbd7c0c642709add18e1a2d368e663cffde403bcdc6f682 |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
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

A automação está instalada; a conformidade documental continua parcial até à correção dos avisos e à aceitação dos resultados.

## Estado atual

A integração inicial foi criada. A auditoria completa e a conformidade documental ficam dependentes da primeira execução, da inspeção dos relatórios e da remediação dos resultados FAIL/WARN.

## Fases e critérios de saída

| Gate | Objetivo | Critério de saída | Estado |
|---|---|---|---|
| G0 — Entrada | Propósito, beneficiário, responsável e autoridade | Política e fonte normativa identificadas | EM_CURSO |
| G1 — Viabilidade e inventário | Enumerar documentos e dependências | Relatório inicial inspecionado e desvios priorizados | PENDENTE |
| G2 — Desenho | Requisitos, arquitetura, dados, riscos e testes | Requisitos e critérios de aceitação registados | PENDENTE |
| G3 — Construção validada | Normalizar documentação e rever alterações | Diferenças auditáveis, testes concluídos, hashes corretos | PENDENTE |
| G4 — Prontidão operacional | Observabilidade, recuperação, segurança e suporte | Execução diária confirmada e falhas tratadas | PENDENTE |
| G5 — Lançamento | Autorização explícita e observação | Aprovação humana e evidência de publicação | PENDENTE |
| G6 — Encerramento | Aceitação, arquivo, transferência e lições | Critérios finais cumpridos e encerramento registado | PENDENTE |

## Política de atualização diária

O workflow em [governanca-diaria.yml](../.github/workflows/governanca-diaria.yml) consulta a branch `main` de GOVERNANCA diariamente às 06:25 UTC e valida localmente os documentos Markdown do projeto. Os relatórios são produzidos por execução e publicados como artefactos de GitHub Actions.

O workflow não atualiza automaticamente todos os conteúdos, porque uma alteração cega pode alterar significado, inventar aprovação ou criar referências SHA circulares. As correções devem ocorrer em lotes pequenos, com revisão de diffs e nova validação. A atualização automática neste estágio significa atualização diária da validação e dos relatórios, e deteção de alterações no mestre normativo.

## Evidências

- [Política de governação](../GOVERNANCA.md)
- [README do projeto](../README.md)
- [Workflow de validação](../.github/workflows/governanca-diaria.yml)
- [Auditor estático](../automation/audit_repository_documents.py)

## Validação

A auditoria usa UTF-8, normaliza finais de linha para LF e calcula o SHA-256 canónico excluindo apenas as duas linhas de controlo definidas pela norma mestre. Verifica cabeçalhos, campos obrigatórios, estados, versões, datas, IDs duplicados, hash declarado e secções de governação. Não altera documentos auditados.

## Resultado

A estrutura inicial de adoção e a automação de verificação foram criadas. Ainda não se declara conformidade integral, nem se afirma que a rotina diária já executou com sucesso.

## Próxima Ação

Executar o workflow manualmente; ler os artefactos de relatório; corrigir desvios prioritários; confirmar o cron diário e os resultados da primeira execução; só então rever a progressão dos gates.

## Histórico de alterações

| Versão | Data | Alteração | Evidência |
|---|---|---|---|
| 1.0.0 | 2026-10-16 | Criação do roadmap de adoção da GOVERNANCA | Commit de criação no GitHub |
