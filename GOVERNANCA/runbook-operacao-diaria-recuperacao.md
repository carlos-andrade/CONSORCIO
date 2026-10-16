# Runbook operacional — validação diária e recuperação CONSORCIO

| Campo | Valor |
|---|---|
| **ID** | CONSORCIO-RUNBOOK-OPS-001 |
| **Projeto** | CONSORCIO |
| **Repositório** | [carlos-andrade/CONSORCIO](https://github.com/carlos-andrade/CONSORCIO) |
| **Tipo documental** | RUNBOOK |
| **Fase** | G4 — Prontidão operacional |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 012424ec2ebed8ea26cc77f2546a5f414afd5aaac573db38b589c7d87532a4a7 |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-16 |
| **Data de atualização** | 2026-10-16 |
| **Responsável** | Responsável pelo projeto CONSORCIO |
| **Aprovador** | Pendente de registo formal |
| **Origem** | Validação operacional do workflow de governação |
| **Autoridade superior** | [GOVERNANCA.md](../GOVERNANCA.md) e [GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Estado

Este runbook define verificação diária, recolha de evidências e recuperação. A configuração e os testes acionados por `push` não substituem a confirmação de pelo menos uma execução `schedule`. A prontidão G4 permanece EM_REVISAO até existir evidência de execução agendada e revisão humana do procedimento.

## Objetivo e âmbito

Validar a operação do workflow `.github/workflows/governanca-diaria.yml`, preservar evidências de cada execução e definir passos reproduzíveis para falhas de auditoria, falhas de infraestrutura ou ausência de execução agendada.

## Operação diária

1. Abrir [GitHub Actions — validação documental diária](https://github.com/carlos-andrade/CONSORCIO/actions/workflows/governanca-diaria.yml).
2. Confirmar que a execução diária mais recente tem evento `schedule`, data/hora esperada e estado final `success`.
3. Abrir a execução e verificar que os testes unitários terminaram com sucesso e que o resumo é `PASS > 0`, `WARN = 0`, `FAIL = 0`.
4. Confirmar a presença do artefacto `consorcio-governanca-<run_number>`, contendo relatório Markdown, JSON de auditoria e manifesto JSON da execução.
5. Guardar fora do prazo de retenção os artefactos necessários ao arquivo de auditoria, de acordo com a política aprovada. A retenção automática atual é de 90 dias.
6. Registar falhas, avisos, ausência de execução e ações corretivas no histórico de incidentes/decisões; não declarar PASS quando a evidência está ausente.

## Evidências exigidas

- ID/número da execução, evento, commit SHA, tentativa, data UTC e estado dos passos.
- Relatório `GOVERNANCA/relatorio-diario.md`.
- Dados por ficheiro em `GOVERNANCA/relatorio-diario.json`.
- Manifesto `GOVERNANCA/evidencia-execucao.json`, com evento, commit, ator, ID, tentativa e resultado dos testes/auditoria.
- URL permanente da execução do GitHub Actions e registo de incidentes quando aplicável.

O manifesto e os relatórios são artefactos da execução e não substituem o log de execução. Os artefactos expiram após 90 dias, salvo arquivo manual aprovado. Não colocar segredos, tokens, credenciais ou dados pessoais desnecessários nos relatórios.

## Recuperação

### A. Falha dos testes ou da auditoria

1. Abrir a execução com falha e identificar o primeiro passo falhado.
2. Transferir o artefacto da execução e examinar o relatório/JSON e o manifesto, se disponíveis.
3. Classificar a causa: teste, integridade documental, fonte normativa indisponível, dependência externa ou runner.
4. Corrigir em commit pequeno e rever o diff antes de publicar.
5. Reexecutar o workflow pela opção **Re-run jobs** na execução original ou aguardar a validação do novo commit.
6. Confirmar execução concluída, testes verdes e resumo sem WARN/FAIL. Manter a execução falhada como evidência histórica; não a apagar nem a substituir no relatório de incidente.

### B. Execução diária ausente

1. Verificar o histórico do workflow e confirmar se existe evento `schedule` para o dia esperado.
2. Se não existir, abrir o workflow e selecionar **Run workflow** na branch `main` (evento `workflow_dispatch`).
3. Registar a ausência da execução agendada como incidente operacional; uma execução manual recupera a validação, mas não prova que o agendamento funcionou.
4. Confirmar a execução manual e artefactos; continuar a verificar o próximo ciclo agendado.

### C. Artefacto ausente ou expirado

1. Consultar os logs da execução e verificar a etapa de upload.
2. Se ainda estiver dentro da retenção, descarregar o artefacto pela página da execução.
3. Se expirou, executar novamente a auditoria e guardar o novo resultado com referência explícita ao commit atualmente validado. Não apresentar o resultado refeito como se fosse o artefacto histórico original.

### D. Falha persistente de runner ou serviço externo

1. Não alterar a norma mestre nem ignorar falhas para obter um resultado verde.
2. Reexecutar uma vez após verificar indisponibilidade transitória; se persistir, registar incidente com run ID, hora UTC, commit SHA e logs relevantes.
3. Escalar conforme a política de governação e só encerrar o incidente após uma execução verificável.

## Limitações e critérios de aceitação

- O workflow valida Markdown e a cadeia documental; não é monitorização permanente da infraestrutura do projeto nem garantia de disponibilidade do GitHub.
- A execução manual ou por `push` não substitui a prova de execução agendada.
- O manifesto regista resultados dos passos; não atesta por si só a conclusão global do workflow.
- G4 só pode ser promovida após uma execução `schedule` bem-sucedida, verificação dos três ficheiros de evidência, ensaio documentado de recuperação e revisão formal do responsável.

## Evidências

- [Workflow operacional](../.github/workflows/governanca-diaria.yml)
- [Histórico de execuções](https://github.com/carlos-andrade/CONSORCIO/actions/workflows/governanca-diaria.yml)
- [Roadmap de adoção](roadmap-adocao.md)

## Validação

O workflow define execução diária às 06:25 UTC, execução manual, concorrência sem cancelamento, limite de 15 minutos e upload do relatório e manifesto mesmo quando os passos de teste/auditoria falham. A validação de uma execução real com esta versão e a confirmação do evento `schedule` são obrigatórias antes de declarar G4 concluída.

## Resultado

Procedimento de operação e recuperação documentado. Estado provisório EM_REVISAO até à validação pós-commit, evidência de execução agendada e ensaio de recuperação.

## Próxima Ação

Validar a nova execução do workflow, confirmar o artefacto com três ficheiros e observar uma execução `schedule`; depois executar e registar um ensaio de recuperação sem adulterar a evidência original.
