# Revisão G2 — Requisitos, arquitetura, dados, privacidade e riscos

| Campo | Valor |
|---|---|
| **ID** | CONSORCIO-REV-G2-001 |
| **Projeto** | CONSORCIO |
| **Repositório** | [carlos-andrade/CONSORCIO](https://github.com/carlos-andrade/CONSORCIO) |
| **Tipo documental** | REVISAO_TECNICA |
| **Fase** | G2 — Desenho |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.1 |
| **SHA-256 (conteúdo canónico)** | HASH_PENDENTE |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-16 |
| **Data de atualização** | 2026-10-16 |
| **Responsável** | Responsável pelo projeto CONSORCIO |
| **Aprovador** | Pendente de validação formal pelo proprietário |
| **Origem** | Revisão G2 do roadmap de adoção da governação |
| **Autoridade superior** | [Política CONSORCIO](../GOVERNANCA.md) e [GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Estado

Documento de revisão técnica em estado `EM_REVISAO`. A linha de base é proposta; a aprovação formal depende da resolução das decisões bloqueadoras e dos critérios de aceitação definidos neste documento.

## 1. Resumo executivo

Esta revisão estabelece uma linha de base inicial para requisitos, arquitetura, dados, privacidade e riscos. O âmbito declarado do CONSORCIO é estudar, documentar e avaliar custos, condições, estratégias e decisões relativas a consórcios com fontes verificáveis e pressupostos explícitos.

**Conclusão:** o repositório demonstra documentação e automação de governação, não uma aplicação transacional. Não aprovar arquitetura de aplicação, integrações financeiras ou tratamento de dados pessoais reais sem confirmação do proprietário. Manter o âmbito documental/analítico até essa decisão.

## 2. Âmbito e exclusões

Incluído: comparação de custos e condições contratuais; cenários para carta de crédito, prazo, taxa de administração, fundo de reserva, seguros, reajustes, parcelas, lance e contemplação; rastreabilidade de fontes; análises reproduzíveis.

Fora do âmbito até aprovação expressa: contratação, lances ou movimentação de dinheiro; aplicação transacional, portal, CRM ou pagamentos; integrações bancárias/administradoras; recolha de documentos de identidade, dados bancários ou de crédito; decisões automáticas sobre pessoas. Resultados não são garantias nem substituem aconselhamento profissional.

## 3. Requisitos de base

Esta é uma proposta de requisitos, não uma especificação de negócio aprovada.

| ID | Requisito | Critério de aceitação | Prioridade |
|---|---|---|---|
| REQ-001 | Definir finalidade, utilizador e decisão suportada | Cada estudo declara objetivo, público, decisão e limites | P0 |
| REQ-002 | Rastrear entradas | Cada valor tem fonte, data, unidade, moeda e método | P0 |
| REQ-003 | Separar factos de hipóteses | Relatórios identificam observações, pressupostos e estimativas | P0 |
| REQ-004 | Calcular custo total | Encargos documentados incluídos sem duplicação | P0 |
| REQ-005 | Modelar incerteza | Cenários e sensibilidades; nenhuma contemplação ou valorização garantida | P0 |
| REQ-006 | Reproduzir cálculos | Fórmulas, entradas e versão do modelo identificadas; testes de regressão | P0 |
| REQ-007 | Minimizar dados | Padrão usa dados públicos, agregados ou sintéticos | P0 |
| REQ-008 | Controlar alterações | Mudanças materiais têm revisão, evidência e rollback proporcional | P0 |
| REQ-009 | Validar qualidade | Completude, validade, consistência, unicidade, atualidade e proveniência | P1 |
| REQ-010 | Aprovação humana | Nenhum resultado inicia transação ou contratação automaticamente | P0 |

## 4. Arquitetura proposta

### Estado observado

Há documentação, auditoria estática Markdown, testes unitários e workflow GitHub Actions. Não há evidência inspecionada de aplicação de negócio, base de dados transacional, autenticação ou integração financeira.

### Arquitetura lógica recomendada

1. **Fontes:** documentos autorizados e fontes públicas verificáveis.
2. **Ingestão controlada:** origem, data, licença, versão e hash; rejeitar segredos e dados desnecessários.
3. **Normalização:** unidades, moeda, periodicidade e distinção entre valor nominal e reajustado.
4. **Domínio analítico:** contrato/plano, administradora, encargo, parcela, lance, contemplação, cenário, fonte e resultado.
5. **Motor de cálculo:** funções determinísticas, entradas versionadas, validações e testes.
6. **Relatórios:** resultados, hipóteses, sensibilidades, data de corte e limitações.
7. **Governação:** GitHub para documentos, decisões e testes; artefactos de CI sem dados confidenciais.
8. **Controlos:** menor privilégio, revisão, monitorização, resposta a incidentes e recuperação conforme risco.

Não escolher framework, base de dados, cloud ou microsserviços antes de confirmar os casos de uso. Se houver implementação, separar domínio/cálculos, ingestão, apresentação e infraestrutura. Qualquer persistência exige classificação, acesso, retenção, backup, recuperação e eliminação definidos.

## 5. Dados e qualidade

| Entidade conceptual | Campos mínimos | Controlo |
|---|---|---|
| Fonte | referência, emissor, data de publicação/observação, licença | Proveniência |
| Plano/contrato | prazo, carta, regras de reajuste e condições | Distinguir cláusula de hipótese |
| Encargo/parcela | tipo, base, valor, moeda, periodicidade e vigência | Não duplicar custos |
| Lance/contemplação | tipo, montante, condições e cenário | Não tratar incerteza como certeza |
| Cenário/resultado | parâmetros, versão, data, fórmulas e limitações | Reprodutibilidade |
| Decisão | alternativas, critérios, risco, decisão e aprovador | Evidência humana |

Não criar campos pessoais antecipadamente. CPF, morada, rendimento individual, extratos, credenciais e dados de crédito ficam fora do modelo inicial. Valores ausentes não são zero por defeito. Registar datas distintas de publicação, captura e período de referência; validar intervalos, duplicados e consistência; marcar estimativas e usar UNKNOWN quando não há evidência.

## 6. Privacidade e segurança

Avaliação preliminar de desenho, não parecer jurídico. A aplicabilidade do RGPD e/ou da legislação brasileira depende das pessoas, operações e responsáveis envolvidos e deve ser confirmada por pessoa competente.

- Privacidade por defeito: dados públicos, agregados ou sintéticos.
- Antes de dados pessoais, documentar finalidade, fundamento legal, titulares, destinatários, retenção e responsáveis.
- Minimização: não colocar dados pessoais, contratos confidenciais ou segredos em repositório público, issues, logs ou artefactos.
- Acesso mínimo, contas individuais, MFA administrativo e revisão periódica de permissões.
- Segredos em armazenamento próprio, nunca em código; rotação e privilégios mínimos.
- Avaliar terceiros, transferências, retenção, direitos dos titulares e resposta a incidentes.
- Avaliar formalmente a necessidade de DPIA/avaliação de impacto para operações de risco elevado.

**Gate:** não autorizar ingestão de dados pessoais reais até haver finalidade, inventário, base legal, retenção, acesso e responsáveis definidos.

## 7. Registo inicial de riscos

| ID | Risco | Probabilidade | Impacto | Mitigação | Estado residual |
|---|---|---|---|---|---|
| RSK-001 | Requisitos incompletos | Alta | Alto | Charter e aceitação aprovados antes de desenvolver | Aberto |
| RSK-002 | Custos contratuais omitidos | Média | Alto | Fontes primárias, checklist e revisão de fórmulas | Aberto |
| RSK-003 | Reajuste/contemplação tratados como garantidos | Média | Alto | Cenários, sensibilidades e ressalvas explícitas | Aberto |
| RSK-004 | Dados desatualizados | Alta | Médio/alto | Data de corte, proveniência e UNKNOWN | Aberto |
| RSK-005 | Exposição de dados pessoais/financeiros | Média | Alto | Proibição por defeito, minimização e processo de incidente | Mitigação proposta; não verificada |
| RSK-006 | Segredos em código/logs | Média | Alto | Secret scanning, permissões mínimas e rotação | Mitigação proposta; não verificada |
| RSK-007 | Mudança da norma central não detetada | Média | Médio | Registar versão/commit normativo e reauditar | Parcial |
| RSK-008 | Falha do workflow sem alerta externo | Média | Alto | Heartbeat externo e teste de escalonamento | Aberto |
| RSK-009 | Actions/runtime obsoletos | Média | Médio | Atualizar ações, acompanhar runtime e fixar SHA quando apropriado | Aberto |
| RSK-010 | Cálculos não reproduzíveis | Média | Alto | Entradas versionadas e testes de referência/regressão | Aberto |
| RSK-011 | Aprovação declarada sem autoridade | Média | Alto | Separar CI de aprovação humana e guardar evidência | Parcial |
| RSK-012 | Expansão para transações sem controlos | Média | Alto | Gate de mudança e nova revisão de risco/privacidade | Aberto |

Risco residual só pode ser reduzido depois de existir evidência de implementação e teste.

## 8. Critérios de aceitação G2

- [ ] Proprietário confirma objetivo, utilizadores, decisões e exclusões.
- [ ] Requisitos P0 têm critérios, responsáveis e evidência.
- [ ] Arquitetura é revista; decisões tecnológicas pendentes estão justificadas.
- [ ] Dados têm origem, sensibilidade, qualidade, uso permitido e retenção definidos.
- [ ] Gate impede dados pessoais reais antes dos controlos de privacidade.
- [ ] Riscos têm dono, mitigação, prazo e risco residual.
- [ ] Cálculos têm casos de referência e testes antes de suportar decisões.
- [ ] Operação, incidentes, recuperação e rollback estão definidos proporcionalmente.
- [ ] Limitações e decisões em aberto permanecem explícitas.

## 9. Decisões bloqueadoras

| ID | Decisão | Estado |
|---|---|---|
| DEC-001 | Âmbito: estudo documental/analítico e apoio à decisão; sem aplicação transacional neste ciclo | Resolvida para o âmbito atual; expansão exige nova decisão de âmbito |
| DEC-002 | Utilizador-alvo: proprietário/responsável do projeto; decisões suportadas: comparar custos, encargos, prazos, regras contratuais e cenários de consórcio | Resolvida para o âmbito atual; requisitos adicionais passam por controlo de alterações |
| DEC-003 | Fontes: primárias/oficiais e documentos autorizados; registar emissor, URL/referência, licença/uso permitido, data de publicação/captura, período de referência e hash. Atualização por estudo/relatório; não assumir ingestão automática | Resolvida como política-base; cada fonte concreta ainda requer validação de licença e disponibilidade |
| DEC-004 | Não recolher nem armazenar dados pessoais reais, documentos de identidade, dados bancários ou de crédito; usar dados públicos, agregados ou sintéticos | Resolvida como exclusão de âmbito; alteração exige revisão de privacidade e segurança |
| DEC-005 | Proprietário: decisões de âmbito/aceitação; responsável do projeto: documentação, roadmap e evidências; responsável técnico: automação/testes; revisão especializada de privacidade/jurídica antes de qualquer expansão para dados pessoais ou operação. Papéis definidos por função, sem inventar nomeações individuais | Resolvida por atribuição funcional mínima para o âmbito documental; nomeações nominais obrigatórias se houver operação/produto |
| DEC-006 | Ambiente operacional, orçamento, SLA e recuperação de produto: não aplicável enquanto o âmbito permanecer documental/analítico e não existir serviço de negócio publicado | Não aplicável ao âmbito atual; reabrir antes de aprovar qualquer produto operacional |

## 10. Conclusão e estado do gate

A revisão inicial cobre requisitos, arquitetura, dados, privacidade e riscos. A recomendação é manter o âmbito documental/analítico e não iniciar transações nem tratar dados pessoais reais sem decisões e controlos prévios.

**G2: EM_REVISAO — não aprovado.** A revisão documental não substitui decisões de negócio ou avaliação jurídica. DEC-001 a DEC-006 e os critérios de aceitação impedem declarar G2 concluído até existirem evidências.

## Evidências

- [Política CONSORCIO](../GOVERNANCA.md)
- [Roadmap de adoção](roadmap-adocao.md)
- [Repositório oficial](https://github.com/carlos-andrade/CONSORCIO)
- [Fonte normativa GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA)
- [Workflow de validação](../.github/workflows/governanca-diaria.yml)
- [Auditor documental](../automation/audit_repository_documents.py)

## Validação

Revisão baseada no âmbito declarado no README e na hierarquia local. Entidades, requisitos e riscos são uma proposta a confirmar pelo proprietário. Não foram testadas funcionalidades de negócio porque não foi identificada aplicação no repositório. Não foi emitido parecer jurídico nem avaliação de impacto formal.

## Resultado

Linha de base de desenho registada; riscos e decisões em aberto explicitados; G2 permanece em revisão à espera de validação humana.

## Próxima Ação

Validar formalmente a linha de base de âmbito/decisões definida na versão 1.0.1; só reabrir DEC-003/005/006 se surgir fonte, integração, dados pessoais ou produto operacional novo.

## Histórico de alterações

| Versão | Data | Alteração | Evidência |
|---|---|---|---|
| 1.0.0 | 2026-10-16 | Criação da revisão G2 de requisitos, arquitetura, dados, privacidade e riscos | Commit inicial deste documento |
| 1.0.1 | 2026-10-16 | Resolução conservadora das DEC-001–006 para o âmbito documental/analítico; sem expansão de produto ou dados pessoais | Mandato do proprietário para resolver pendências; alterações registadas para validação formal |
