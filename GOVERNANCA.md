# Política de governação e autoridade — CONSORCIO

| Campo | Valor |
|---|---|
| **ID** | CONSORCIO-POL-001 |
| **Projeto** | CONSORCIO |
| **Repositório** | [carlos-andrade/CONSORCIO](https://github.com/carlos-andrade/CONSORCIO) |
| **Tipo documental** | POLITICA |
| **Fase** | G0 — Governação e entrada |
| **Estado** | EM_CURSO |
| **Versão** | 1.0.1 |
| **SHA-256 (conteúdo canónico)** | A calcular na normalização inicial — ver issue #1 |
| **Commit de referência (versão anterior)** | [6fc6e6accfa675f4b76c122e3471b5c290e4bfbc](https://github.com/carlos-andrade/CONSORCIO/commit/6fc6e6accfa675f4b76c122e3471b5c290e4bfbc) |
| **Data de criação** | 2026-10-16 |
| **Data de atualização** | 2026-10-16 |
| **Responsável** | Responsável pelo projeto CONSORCIO |
| **Aprovador** | Pendente de aprovação formal pelo proprietário do projeto |
| **Origem** | Decisão de adoção da governação central e repositório GOVERNANCA |
| **Autoridade superior** | Lei aplicável, contratos vinculativos e normas aprovadas em [GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## 1. Objetivo e âmbito

Esta política define a autoridade, a hierarquia de decisões e os controlos mínimos do repositório CONSORCIO. Aplica-se a documentação, requisitos, arquitetura, código, dados, testes, workflows, releases, incidentes e artefactos produzidos no projeto.

## 2. Fonte normativa central

O repositório [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) é a fonte central das regras de governação adotadas pelo CONSORCIO. A branch `main` é consultada pelo workflow de validação. Não se devem criar cópias locais concorrentes das normas mestres.

**Limite de autoridade:** a Constituição `GOV-001` da GOVERNANCA está identificada como `PROPOSTA PARA REVISÃO`, e a aprovação formal está pendente. Por isso, é referencial orientador, não uma norma ratificada. A norma de cabeçalho só é obrigatória na extensão em que o seu estado aprovado e o seu âmbito sejam confirmados na fonte mestre. Nenhum documento deste repositório pode elevar unilateralmente uma proposta a norma aprovada.

## 3. Hierarquia de precedência

Em caso de conflito, aplicar a seguinte ordem:

1. Lei e regulamentação aplicáveis.
2. Contratos e obrigações vinculativas.
3. Políticas e normas formalmente aprovadas pela autoridade competente.
4. Procedimentos e padrões técnicos aprovados dentro do respetivo mandato.
5. Recomendações, exemplos e rascunhos.

Conflitos devem ser registados com referências concretas, impacto, responsável e decisão de resolução. Não se deve escolher silenciosamente uma regra conveniente.

## 4. Papéis e direitos de decisão

| Papel | Responsabilidade e autoridade | Limites |
|---|---|---|
| Proprietário / patrocinador do projeto | Define finalidade, beneficiários, prioridades, recursos e aceita o resultado de negócio | Não pode dispensar obrigações legais ou falsificar evidência técnica |
| Responsável pelo projeto | Mantém roadmap, dependências, riscos, decisões e estado dos gates | Não aprova sozinho controlos críticos que tenha implementado |
| Responsável técnico | Decide arquitetura e implementação dentro do escopo aprovado; garante testes e documentação | Deve registar desvios, riscos e limitações |
| Responsável por dados/processo | Define origem, semântica, qualidade, acesso, retenção e uso permitido dos dados | Não autoriza usos fora da base legal ou mandato |
| Segurança/privacidade/conformidade | Avalia controlos especializados e pode bloquear uma mudança dentro do mandato aplicável | Deve registar fundamento e condições de desbloqueio |
| Operações | Avalia observabilidade, suporte, recuperação, continuidade e rollback | Não declara conformidade de controlos que não foram verificados |
| Revisor independente | Revê alterações de risco elevado e evidência de aceitação | Deve ser independente da implementação sempre que proporcional ao risco |

Quando uma pessoa acumula papéis, essa acumulação deve ser registada. Em alterações de alto impacto, exigir revisão independente ou controlo compensatório documentado.

## 5. Política de alteração e publicação

1. Alterações devem ser pequenas, rastreáveis, reversíveis e acompanhadas por evidência.
2. Não apagar nem substituir histórico sem autorização e justificação explícitas.
3. Não inventar aprovações, hashes, resultados, commits, testes ou responsáveis.
4. Alterações automáticas de conteúdo substantivo, permissões, dados ou produção exigem autorização explícita e revisão adequada ao risco.
5. A automação diária pode validar e reportar. Não pode aprovar a própria execução, promover estados a `APROVADO` nem reescrever conteúdo substantivo por defeito.
6. Segredos, tokens e dados pessoais desnecessários não devem ser gravados em documentos, logs ou artefactos.
7. Toda a publicação deve ter critérios de aceitação e plano de reversão proporcionais ao impacto.

## 6. Gates de governação

| Gate | Condição mínima de saída |
|---|---|
| G0 — Entrada | Objetivo, beneficiário, proprietário, responsável e autoridade normativa identificados |
| G1 — Viabilidade | Alternativas, custos, riscos, dependências e valor esperado registados |
| G2 — Desenho | Requisitos, arquitetura, dados, privacidade, ameaças e testes definidos |
| G3 — Construção validada | Revisão de alterações, testes, documentação e integridade verificadas |
| G4 — Prontidão operacional | Observabilidade, segurança, recuperação, suporte e rollback avaliados |
| G5 — Lançamento | Aprovação humana explícita e evidências de prontidão registadas |
| G6 — Encerramento | Aceitação final, arquivo, responsabilidades e lições registadas |

Gate não concluído permanece pendente ou bloqueado. Uma execução de CI bem-sucedida não equivale, por si só, a aprovação do gate.

## 7. Estados e evidência

- `PASS`: critério verificado com evidência identificável.
- `WARN`: desvio ou limitação não bloqueante que exige decisão ou remediação.
- `FAIL`: critério obrigatório não cumprido.
- `UNKNOWN`: evidência insuficiente ou verificação não executada.
- `APROVADO`: estado documental que exige aprovador autorizado e evidência explícita.

Não usar ausência de falha detetada como prova de conformidade total. Relatórios devem indicar escopo, timestamp, fonte normativa, versão de ferramentas, limitações e artefactos.

## 8. Exceções

Cada exceção deve registar a regra afetada, motivo, risco residual, controlos compensatórios, responsável, aprovador autorizado, data de expiração e condição de revogação. Exceções não dispensam obrigações legais ou contratuais. Uma exceção sem prazo ou aprovação válida não fecha a pendência.

## 9. Governação da própria norma

Alterações à fonte normativa central são governadas no repositório GOVERNANCA, não neste repositório. Quando a norma mestre muda, o CONSORCIO deve avaliar impacto, registar a versão/commit consultado, atualizar os controlos aplicáveis e executar novamente a validação. Se a fonte mestre estiver indisponível ou ambígua, o estado é `UNKNOWN`, não `PASS`.

## 10. Evidências e rastreabilidade

- [Fonte normativa GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA).
- [Constituição GOV-001 — proposta para revisão](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CONSTITUICAO.md).
- [Workflow diário](.github/workflows/governanca-diaria.yml).
- [Auditor documental](automation/audit_repository_documents.py).
- [Issue de remediação documental #1](https://github.com/carlos-andrade/CONSORCIO/issues/1).

## Estado

G0 foi definido documentalmente: fonte normativa, hierarquia de precedência, papéis, limites de autoridade, gates e evidência estão explicitados. A aprovação formal pelo proprietário do projeto permanece pendente; por isso, este documento não é declarado `APROVADO`.

## Validação

A política é coerente com a distinção entre norma aprovada e proposta para revisão na fonte central. A implementação operacional é validada pelo workflow; a validação documental integral e os hashes canónicos continuam sujeitos à issue #1.

## Resultado

Política de autoridade e governação definida e registada no repositório. O gate G0 só pode ser considerado formalmente encerrado após a aprovação humana registada e a verificação das evidências exigidas.

## Próxima Ação

Solicitar ao proprietário do projeto a aprovação explícita desta política; depois, calcular e preencher o SHA-256 canónico conforme a norma mestre e reexecutar a auditoria.

## Histórico de alterações

| Versão | Data | Alteração | Evidência |
|---|---|---|---|
| 1.0.0 | 2026-10-16 | Política inicial de adoção | Commit anterior identificado no cabeçalho |
| 1.0.1 | 2026-10-16 | Clarificação de autoridade, papéis, gates e limites da automação | Commit desta atualização |
