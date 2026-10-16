# Modelo analítico — custos de consórcio

| Campo | Valor |
|---|---|
| **ID** | CONSORCIO-MOD-CUSTO-001 |
| **Projeto** | CONSORCIO |
| **Repositório** | [carlos-andrade/CONSORCIO](https://github.com/carlos-andrade/CONSORCIO) |
| **Tipo documental** | MODELO_ANALITICO |
| **Fase** | G3 — Construção controlada |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 198b225a1554955038146df899135d9699cc4658000dd07480cfaa110699682c |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-16 |
| **Data de atualização** | 2026-10-16 |
| **Responsável** | Responsável pelo projeto CONSORCIO |
| **Aprovador** | Pendente de revisão humana |
| **Origem** | Baseline G2 aprovada; requisito de cálculo do custo total |
| **Autoridade superior** | [Política CONSORCIO](../../GOVERNANCA.md) e [GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## 1. Objetivo

Definir um modelo determinístico, explicável e reproduzível para estimar os encargos de um plano de consórcio usando exclusivamente dados sintéticos ou condições contratuais públicas/autorizadas. O documento especifica o cálculo; não declara uma aplicação executável.

## 2. Âmbito e limites

- Moeda de referência: BRL (R$), por ser o mercado-alvo desta análise.
- Entradas são valores documentados, sintéticos ou agregados; cada entrada deve indicar origem, data de observação, unidade e natureza (`FACTO`, `HIPOTESE` ou `SINTETICO`).
- Não usar dados pessoais reais, documentos de identidade, dados bancários ou de crédito.
- Não executar lances, pagamentos, contratação ou qualquer transação.
- O resultado é uma estimativa analítica, não aconselhamento financeiro nem garantia de contemplação.
- Impostos, reajustes, multas, juros de mora e custos não especificados não são presumidos como zero: devem ser apresentados como desconhecidos ou modelados explicitamente.

## 3. Variáveis de entrada

| Campo | Símbolo | Regra |
|---|---|---|
| Crédito de referência | C | Valor positivo em BRL |
| Taxa de administração total | a | Percentagem decimal do crédito, 0 ≤ a ≤ 1 |
| Fundo de reserva total | r | Percentagem decimal do crédito, 0 ≤ r ≤ 1 |
| Seguro total estimado | S | Valor total em BRL, S ≥ 0; usar zero apenas se contratualmente confirmado ou num cenário sintético explícito |
| Outros encargos conhecidos | O | Total em BRL, O ≥ 0, discriminado por categoria |
| Número de parcelas | N | Inteiro positivo |
| Entrada ou lance próprio modelado | L | Valor analítico em BRL, L ≥ 0; não representa execução de lance |
| Reajustes futuros | J | Cenário explícito; não incluído no cenário-base quando desconhecido |

As taxas `a` e `r` representam o total contratual durante o prazo, não taxas anuais, salvo se a fonte definir expressamente outra base. A base de incidência deve ser documentada para cada encargo.

## 4. Fórmulas do cenário-base

Encargos conhecidos associados ao crédito:

`TA = C × a`

`FR = C × r`

`CT_conhecido = C + TA + FR + S + O`

Parcela média indicativa, antes de reajustes e diferenças de calendário:

`P_media = CT_conhecido / N`

Custo adicional conhecido face ao crédito:

`Encargos_conhecidos = TA + FR + S + O`

Percentagem de encargos conhecidos face ao crédito:

`Pct_encargos = Encargos_conhecidos / C × 100`

`L` é uma variável de cenário de liquidez, não deve ser somado automaticamente ao custo contratual total: se utilizado, o relatório deve distinguir desembolso inicial, saldo financiado pelo grupo e custo total. A parcela média não deve ser apresentada como cronograma contratual de pagamentos.

## 5. Tratamento de incerteza

1. Campo ausente ou fonte não validada: resultado do encargo = `DESCONHECIDO`, nunca zero implícito.
2. Reajustes do crédito ou das parcelas: apresentar cenário separado com regra, índice, frequência, data-base e hipótese explícitos.
3. Seguros e encargos variáveis: distinguir total fixo conhecido de estimativa e de item desconhecido.
4. Comparações entre planos só são válidas quando crédito, prazo, data-base, base das taxas e itens incluídos são comparáveis.
5. Não produzir ranking definitivo quando existirem componentes materiais desconhecidos; assinalar a limitação.
6. O motor distingue subtotal conhecido de custo total completo: se faltar qualquer componente material, `complete_total_cost`, parcela média e percentagem total de encargos ficam desconhecidos; não se apresenta o subtotal como custo total.

## 6. Exemplo sintético de referência

Dados exclusivamente ilustrativos: `C = R$ 100.000,00`, `a = 0,15`, `r = 0,02`, `S = R$ 1.200,00`, `O = R$ 300,00`, `N = 100`.

- `TA = R$ 15.000,00`
- `FR = R$ 2.000,00`
- `CT_conhecido = R$ 118.500,00`
- `P_media = R$ 1.185,00`
- `Encargos_conhecidos = R$ 18.500,00`
- `Pct_encargos = 18,5%`

Este exemplo não representa oferta, contrato ou preço de uma administradora real.

## 7. Saída obrigatória

Cada execução futura do modelo deve reportar: versão do modelo; entradas e unidades; origem e data de cada entrada; classificação facto/hipótese/sintético; fórmulas; resultados em BRL; componentes desconhecidos; limitações; identificador do cenário; e resultado dos testes aplicáveis.

## 8. Critérios de aceitação

- Rejeitar `C ≤ 0`, `N ≤ 0`, percentagens fora do intervalo permitido e encargos negativos.
- Não converter dados ausentes em zero sem uma hipótese explícita e visível.
- Reproduzir exatamente o exemplo sintético acima, com arredondamento monetário a duas casas decimais.
- Distinguir custo total conhecido, parcela média indicativa e cenário de lance.
- Manter rastreabilidade para cada entrada e impedir afirmações de execução transacional.


## 9. Cenário explícito de reajuste (sensibilidade)

A função `project_adjustment_scenario` aplica uma sequência de taxas informadas pelo utilizador, em períodos sucessivos, sobre o custo total-base fornecido. É uma análise de sensibilidade matemática, não uma previsão contratual. Não é aplicada automaticamente à estimativa-base.

- Só pode ser calculada quando o custo total-base é conhecido.
- Cada taxa deve ser explicitamente fornecida e ser superior a -100%.
- A função compõe as taxas sucessivamente sobre o total-base; não presume que esta base corresponde ao mecanismo de reajuste de qualquer contrato real.
- Antes de comparar com uma oferta, confirmar índice, periodicidade, data-base e componentes efetivamente reajustados no contrato.
- O resultado é rotulado `SENSITIVITY_ONLY` e deve ser separado do custo-base.

Exemplo sintético: base de R$ 1.000,00 e taxas de 10% e 5% em dois períodos resultam em R$ 1.100,00 e depois R$ 1.155,00. O exemplo ilustra apenas composição matemática.


## 10. Comparação controlada de planos

A função `compare_cost_scenarios` compara cenários apenas quando todos têm custo total completo e coincidem em crédito, número de parcelas, data-base e classificação da fonte. Se algum componente material for desconhecido ou as bases divergirem, a comparação é bloqueada, sem ranking parcial.

Cada cenário deve ter `scenario_id`, `as_of_date`, `source_classification` e todas as entradas do cálculo. O ranking é estritamente matemático por custo total conhecido; não considera qualidade da administradora, probabilidade de contemplação, reajustes contratuais não modelados, liquidez ou adequação individual. Não constitui recomendação financeira.


## 11. Proveniência mínima e classificação

- `FACTO`: exige referência identificável à fonte e data de observação ISO (`AAAA-MM-DD`); sem estes campos, a comparação é rejeitada.
- `HIPOTESE`: exige uma lista não vazia de pressupostos explícitos.
- `SINTETICO`: deve permanecer claramente rotulado como dado ilustrativo, não como observação de mercado.
- Todos os cenários comparados exigem identificador não vazio e data-base ISO válida.
- A existência de uma referência não prova, por si só, a autenticidade ou autorização da fonte; a revisão humana continua necessária.

## Estado

EM_REVISAO — especificação inicial; não está aprovada para uso decisório.

## Evidências

- [Baseline G2 aprovada](../../GOVERNANCA/decisao-aprovacao-g2.md)
- [Esquema JSON de custos](../../DADOS/esquemas/consorcio-custo.schema.json)
- [Casos de referência](../../TESTES/casos-referencia-custos.md)

## Validação

O documento define fórmulas e limites para revisão. A implementação inicial existe em [calculadora_custos.py](calculadora_custos.py) e os testes unitários estão em [test_calculadora_custos.py](../../tests/test_calculadora_custos.py). A execução CI e a revisão humana deste modelo ainda são necessárias; a aprovação G2 não equivale a aprovação deste modelo.

## Resultado

Primeira especificação do modelo de custos criada como artefacto de G3, sujeita a revisão humana e validação por casos de referência antes de utilização decisória.

## Próxima Ação

Validar o esquema de dados, implementar os testes de referência/regressão e rever este modelo antes de o marcar como aprovado.
