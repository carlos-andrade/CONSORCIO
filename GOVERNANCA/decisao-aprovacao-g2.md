# Decisão formal — aprovação da baseline G2 do CONSORCIO

| Campo | Valor |
|---|---|
| **ID** | CONSORCIO-DEC-G2-001 |
| **Projeto** | CONSORCIO |
| **Repositório** | [carlos-andrade/CONSORCIO](https://github.com/carlos-andrade/CONSORCIO) |
| **Tipo documental** | DECISAO_FORMAL |
| **Fase** | G2 — Desenho |
| **Estado** | APROVADO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | e5652469991f44b58cb7738af217f50ff3e73398c9859975e31584fd5fc7a97f |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-16 |
| **Data de atualização** | 2026-10-16 |
| **Responsável** | Responsável pelo projeto CONSORCIO |
| **Aprovador** | Proprietário do projeto CONSORCIO — aprovação explícita nesta conversa |
| **Origem** | Declaração explícita “APROVO G2”, recebida em 2026-10-16 |
| **Autoridade superior** | [Política CONSORCIO](../GOVERNANCA.md) e [GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Estado

Decisão formal aprovada pelo proprietário para a baseline conservadora de requisitos e arquitetura descrita na revisão G2. A aprovação limita-se ao âmbito documental/analítico e não certifica controlos técnicos ainda não implementados.

## Decisão formal

Em 16 de outubro de 2026, o proprietário declarou **“APROVO G2”**, aprovando a baseline de requisitos e arquitetura apresentada para o projeto CONSORCIO, com as seguintes condições e limites:

1. Finalidade: estudar, comparar e documentar custos e condições de consórcios.
2. Utilizador inicial: proprietário/responsável pelo projeto.
3. Requisitos: REQ-001 a REQ-010 da revisão G2, com critérios de aceitação, rastreabilidade, separação de factos e hipóteses, cálculo de custo total, cenários, reprodutibilidade, minimização de dados, controlo de alterações, qualidade e aprovação humana.
4. Arquitetura lógica: fontes autorizadas → ingestão controlada → normalização → modelo analítico → motor de cálculo determinístico → relatórios → governação e auditoria.
5. Dados: fontes públicas ou autorizadas, agregados ou sintéticos; proveniência, datas, licença/uso permitido, unidades, moeda e hash devem ser registados quando aplicável.
6. Tecnologia: a escolha de framework, base de dados, cloud e microsserviços fica adiada até os casos de uso demonstrarem necessidade.
7. Privacidade e segurança: não recolher nem armazenar dados pessoais reais, documentos de identidade, dados bancários ou de crédito no âmbito inicial; não colocar segredos ou dados confidenciais no repositório.
8. Exclusões: sem contratação, execução de lances, pagamentos, movimentação de dinheiro, portal transacional, CRM, integrações financeiras ou decisões automáticas sobre pessoas.
9. Alterações de âmbito: qualquer expansão exige nova decisão formal, análise de riscos e privacidade, e revisão dos critérios de aceitação.

## Condições de aceitação e limites

- A decisão aprova a baseline para orientar a estrutura documental/analítica inicial.
- Cada análise deve identificar objetivo, fontes, datas, moeda/unidades, pressupostos, fórmulas, limitações e versão do modelo.
- Cálculos de negócio só podem ser usados para apoiar decisões após implementação e testes de referência/regressão.
- A aprovação não declara a aplicação construída, nem comprova implementação de controlos de segurança, privacidade, recuperação ou monitorização.
- G4, G5 e G6 mantêm os estados próprios e não são concluídos por esta decisão.
- Fontes concretas continuam sujeitas a validação de licença, disponibilidade e adequação.

## Evidências

- [Revisão técnica G2](revisao-requisitos-arquitetura-dados-privacidade-riscos.md)
- [Roadmap G0–G6](roadmap-adocao.md)
- [Política local de governação](../GOVERNANCA.md)
- [Repositório oficial](https://github.com/carlos-andrade/CONSORCIO)
- Declaração explícita do proprietário nesta conversa: “APROVO G2”.

## Validação

A decisão humana foi expressa pelo proprietário nesta conversa e registada neste documento. A auditoria automática pode verificar metadados e integridade documental, mas não substitui a aprovação humana nem valida a exatidão de futuras análises de negócio.

## Resultado

**G2 aprovado para a baseline documental/analítica definida nesta decisão.** A criação da estrutura inicial pode avançar dentro destes limites. Os gates operacionais e de lançamento continuam dependentes das suas próprias evidências.

## Próxima Ação

Atualizar a revisão técnica e o roadmap; executar a auditoria documental e os testes; verificar o commit e o resultado real do workflow antes de declarar a atualização validada.

## Histórico de alterações

| Versão | Data | Alteração | Evidência |
|---|---|---|---|
| 1.0.0 | 2026-10-16 | Registo da aprovação explícita da baseline G2 pelo proprietário | Declaração “APROVO G2” nesta conversa |
