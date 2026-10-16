# Relatório de fecho — aceitação e evidências CONSORCIO

| Campo | Valor |
|---|---|
| **ID** | CONSORCIO-CLOSEOUT-001 |
| **Projeto** | CONSORCIO |
| **Repositório** | [carlos-andrade/CONSORCIO](https://github.com/carlos-andrade/CONSORCIO) |
| **Tipo documental** | RELATORIO_DE_ENCERRAMENTO |
| **Fase** | G6 — Encerramento |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.1 |
| **SHA-256 (conteúdo canónico)** | 456db5cb3524a7dddf216772ece93999b055ac14e7ab37dd576baf15dd3dfe7f |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-16 |
| **Data de atualização** | 2026-10-16 |
| **Responsável** | Responsável pelo projeto CONSORCIO |
| **Aprovador** | Aprovação condicional de lançamento registada; aceitação final pendente |
| **Origem** | Pedido de encerramento com aceitação e evidências completas |
| **Autoridade superior** | [GOVERNANCA.md](../GOVERNANCA.md) e [GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## 1. Decisão de encerramento

**Resultado: aprovação condicional de lançamento registada; encerramento final não aprovado; G5 e G6 permanecem pendentes.**

O proprietário emitiu uma aprovação condicional de lançamento, registada em [CONSORCIO-DEC-G5-001](decisao-aprovacao-condicional-lancamento.md). Essa decisão autoriza o lançamento apenas depois da conclusão e validação dos gates aplicáveis e da confirmação da prontidão operacional. Não é uma aceitação final do resultado nem prova de que o lançamento ocorreu; as condições e a aceitação final permanecem pendentes.

O presente relatório consolida a evidência técnica disponível, identifica lacunas e define o conjunto mínimo necessário para uma decisão final auditável. É um relatório de fecho preparado, não um termo de aceitação concluído.

## 2. Resumo de evidências verificadas

| ID | Evidência | Resultado observado | Limite |
|---|---|---|---|
| EVD-001 | Workflow GitHub Actions — execução #56 | `success`, evento `push`, SHA `0d96753992ac6a08d55d92424a4afba0b9c5b5f3`, 16-10-2026 11:35:54 UTC | Valida apenas o commit/execução indicados; não prova aceitação humana nem prontidão operacional completa |
| EVD-002 | Auditoria da execução #56 | 6 PASS, 0 WARN, 0 FAIL; 2 testes unitários aprovados, conforme resumo de execução registado | Auditoria documental estática, não certificação integral do projeto |
| EVD-003 | Artefacto da execução #56 | `consorcio-governanca-56`, artefacto associado à execução #56 | Retenção configurada de 90 dias; arquivo de longo prazo não comprovado |
| EVD-004 | Workflow `.github/workflows/governanca-diaria.yml` | `schedule` definido para `25 6 * * *`, `workflow_dispatch` e `push` configurados | As últimas 56 execuções observadas foram acionadas por `push`; não foi localizada execução com evento `schedule` |
| EVD-005 | Roadmap de adoção v1.0.5 | G3 `CONCLUIDO`; G0 `EM_CURSO`; G1/G2/G4 `EM_REVISAO`; G5/G6 `PENDENTE` | Estados dos gates impedem encerramento global |
| EVD-006 | Revisão G2 v1.0.0 | Requisitos, arquitetura proposta, dados, privacidade e riscos documentados | DEC-001 a DEC-006 e critérios de aceitação G2 continuam dependentes de decisão/validação humana |
| EVD-007 | Runbook operacional v1.0.2 | Procedimento diário e recuperação documentados | G4 requer evidência de execução agendada e ensaio de recuperação controlado, além de revisão humana |
| EVD-008 | Política `GOVERNANCA.md` v1.0.2 | Define autoridade, gates, evidência e proibição de aprovação automática | Aprovação formal do proprietário permanece pendente |
| EVD-009 | Integridade documental | Hashes canónicos e auditorias de commits anteriores registados nos documentos de governação | Uma auditoria limpa não substitui aprovação formal, teste de recuperação ou aceitação do produto |

## 3. Estado dos gates para encerramento

| Gate | Estado atual | Evidência/lacuna | Condição para fecho |
|---|---|---|---|
| G0 — Entrada e governação | EM_CURSO | Política definida; aprovação formal pendente | Registar aprovação do proprietário e validar a autoridade normativa aplicável |
| G1 — Viabilidade e inventário | EM_REVISAO | Inventário e documentação existentes; revisão final não formalizada neste dossiê | Confirmar âmbito, alternativas, custos, dependências, riscos e valor esperado |
| G2 — Desenho | EM_REVISAO | Revisão técnica publicada; DEC-001 a DEC-006 por decidir | Resolver decisões bloqueadoras e aceitar formalmente requisitos, arquitetura, dados, privacidade e riscos |
| G3 — Construção validada | CONCLUIDO | Auditorias e testes documentais recentes com resultado limpo | Preservar o relatório e manifesto correspondentes como evidência do escopo verificado |
| G4 — Prontidão operacional | EM_REVISAO | Workflow e runbook presentes; execução agendada e ensaio de recuperação não comprovados | Capturar execução `schedule` bem-sucedida, verificar artefactos e executar recuperação controlada documentada |
| G5 — Lançamento | PENDENTE | Não há registo de aprovação formal de lançamento nem prova de publicação | Aprovação humana explícita e evidência verificável de publicação, após satisfazer os gates anteriores |
| G6 — Encerramento | PENDENTE | Não há termo de aceitação final concluído | Aceitação explícita do proprietário, arquivo de evidências, transferência de responsabilidades e lições aprendidas |

## 4. Critérios de aceitação final

O fecho só pode ser marcado `ACEITE` depois de cada item obrigatório ter evidência identificável:

- [ ] O proprietário confirma por escrito o âmbito e aceita expressamente o resultado final entregue.
- [ ] G0 e G1 têm decisão formal e evidência de revisão.
- [ ] DEC-001 a DEC-006 estão resolvidas ou têm decisão de não aplicabilidade aprovada e justificada.
- [ ] G3 mantém testes e auditoria válidos para o commit final.
- [ ] G4 tem execução `schedule` bem-sucedida e ensaio de recuperação controlado, com logs/relatórios e resultado revisto.
- [ ] G5 tem autorização humana explícita e evidência da publicação realmente realizada; não apenas configuração ou intenção.
- [ ] Artefactos e manifestos necessários foram preservados com referência ao run, commit, data, resultado e hash; arquivo de longo prazo foi confirmado.
- [ ] Responsável operacional, suporte, manutenção, riscos residuais e procedimento de rollback foram aceites.
- [ ] Lições aprendidas, limitações conhecidas e itens não entregues foram registados e aceites.
- [ ] A auditoria final do repositório passou após as alterações de fecho.

## 5. Pacote de evidências e referências

1. [Execução #56 — auditoria documental e testes](https://github.com/carlos-andrade/CONSORCIO/actions/runs/38894829559).
2. [Workflow de validação diária](../.github/workflows/governanca-diaria.yml).
3. [Roadmap de adoção G0–G6](roadmap-adocao.md).
4. [Revisão G2 — requisitos, arquitetura, dados, privacidade e riscos](revisao-requisitos-arquitetura-dados-privacidade-riscos.md).
5. [Runbook operacional e recuperação](runbook-operacao-diaria-recuperacao.md).
6. [Política de governação e autoridade](../GOVERNANCA.md).
7. [Fonte normativa central GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA).

O artefacto da execução #56 deve ser descarregado e preservado antes de expirar a retenção de 90 dias. Este relatório não afirma que o artefacto foi arquivado externamente.

## 6. Decisão formal do proprietário — lançamento condicional registado; aceitação final pendente

**Decisão de lançamento:** `APROVAÇÃO CONDICIONAL — REGISTADA`.

A decisão consta em [CONSORCIO-DEC-G5-001](decisao-aprovacao-condicional-lancamento.md) e não substitui o termo de aceitação final.

**Decisão de aceitação final:** `PENDENTE`.

**Declaração necessária para aceitação final:**

> Eu, proprietário do projeto CONSORCIO, aceito formalmente o resultado final descrito neste relatório, após verificar as evidências e confirmar que os critérios de aceitação aplicáveis foram cumpridos. Reconheço os riscos residuais e as limitações expressamente registados, e aprovo o encerramento do projeto.

**Nome/identificação do aprovador:** Pendente de registo  
**Data e hora da decisão:** Pendente de confirmação  
**Referência da decisão/assinatura:** Pendente de registo

Esta declaração não deve ser preenchida ou atribuída automaticamente. Se os gates obrigatórios continuarem abertos, o proprietário deve escolher entre manter o projeto aberto ou aprovar explicitamente uma aceitação parcial com as exceções, riscos residuais, responsáveis e prazos identificados. A aceitação parcial não autoriza declarar G5 ou G6 concluídos nem contornar obrigações legais ou controlos obrigatórios.

## 7. Próximas ações obrigatórias

1. Obter a decisão formal do proprietário sobre âmbito e aceitação.
2. Resolver G0/G1/G2 e registar as decisões pendentes.
3. Confirmar uma execução `schedule` real e realizar o ensaio de recuperação G4.
4. Obter aprovação explícita de lançamento e guardar evidência verificável de publicação para G5, se o lançamento fizer parte do âmbito.
5. Preservar os artefactos e manifestos, realizar auditoria final e só então atualizar G6.

## Resultado

O pacote de evidências disponível está consolidado neste relatório. O estado correto é **APROVAÇÃO CONDICIONAL DE LANÇAMENTO REGISTADA — GATES E ACEITAÇÃO FINAL PENDENTES**. A execução #60 terminou com 6 PASS, 2 WARN e 0 FAIL na auditoria documental; os avisos não equivalem a aprovação global. Não marcar o CONSORCIO como lançado ou encerrado até que as condições aplicáveis estejam satisfeitas e comprovadas.

## Histórico de alterações

| Versão | Data | Alteração | Evidência |
|---|---|---|---|
| 1.0.0 | 2026-10-16 | Consolidação inicial do estado de fecho, evidências e critérios de aceitação | Execução #56 e documentos de governação do repositório |
| 1.0.1 | 2026-10-16 | Atualização após registo da aprovação condicional de lançamento; aceitação final continua pendente | Decisão CONSORCIO-DEC-G5-001 e execução #60 |
