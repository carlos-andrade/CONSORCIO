# Casos de referência — modelo de custos

| Campo | Valor |
|---|---|
| **ID** | CONSORCIO-TEST-CUSTO-001 |
| **Projeto** | CONSORCIO |
| **Repositório** | [carlos-andrade/CONSORCIO](https://github.com/carlos-andrade/CONSORCIO) |
| **Tipo documental** | CASOS_DE_TESTE |
| **Fase** | G3 — Construção controlada |
| **Estado** | EM_CURSO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 87659bf4cae249e001debee8f664769b970e38918ed68f85abeef292a27c5cf0 |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-16 |
| **Data de atualização** | 2026-10-16 |
| **Responsável** | Responsável pelo projeto CONSORCIO |
| **Aprovador** | Pendente de revisão humana |
| **Origem** | Modelo CONSORCIO-MOD-CUSTO-001 |
| **Autoridade superior** | [Política CONSORCIO](../GOVERNANCA.md) e [GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Objetivo

Fixar resultados esperados e validações negativas antes da implementação do motor de cálculo. Os dados são sintéticos.

## Casos

| ID | Entrada/condição | Resultado esperado | Estado |
|---|---|---|---|
| TC-CST-001 | C=100000; a=0,15; r=0,02; S=1200; O=300; N=100 | TA=15000; FR=2000; CT=118500; P média=1185; encargos=18500; percentagem=18,5% | ESPECIFICADO |
| TC-CST-002 | C=0 | Rejeitar por crédito não positivo | ESPECIFICADO |
| TC-CST-003 | N=0 ou N fracionário | Rejeitar por número de parcelas inválido | ESPECIFICADO |
| TC-CST-004 | a<0 ou a>1 | Rejeitar taxa de administração fora do intervalo | ESPECIFICADO |
| TC-CST-005 | r<0 ou r>1 | Rejeitar fundo de reserva fora do intervalo | ESPECIFICADO |
| TC-CST-006 | S ausente/desconhecido | Marcar seguro como desconhecido; não assumir zero | ESPECIFICADO |
| TC-CST-007 | O negativo | Rejeitar encargo negativo | ESPECIFICADO |
| TC-CST-008 | Fonte sem referência/data | Sinalizar proveniência incompleta; impedir classificação como facto validado | ESPECIFICADO |
| TC-CST-009 | Lance analítico informado | Mostrar separadamente como cenário de liquidez; não executar nem somar automaticamente ao custo contratual | ESPECIFICADO |
| TC-CST-010 | Comparação com prazo/base de taxas diferentes | Bloquear ranking direto ou exigir normalização explícita | ESPECIFICADO |

## Implementação inicial

Foi adicionada uma bateria de testes unitários em [test_calculadora_custos.py](../tests/test_calculadora_custos.py). O estado de execução só será confirmado após a conclusão bem-sucedida do workflow CI.

## Critérios de execução

- A especificação dos casos não equivale a testes executados.
- Quando o cálculo for implementado, cada caso deve registar resultado observado, PASS/FAIL, versão do código e evidência.
- O arredondamento monetário é aplicado apenas à apresentação; os cálculos internos devem preservar precisão decimal adequada.
- Nenhum caso pode chamar APIs financeiras, enviar pagamentos, executar lances ou usar dados pessoais reais.

## Estado

EM_CURSO — casos especificados; execução automatizada pendente.

## Evidências

- [Modelo analítico de custos](../MODELOS/custos/modelo-custo-consorcio.md)
- [Esquema JSON de custos](../DADOS/esquemas/consorcio-custo.schema.json)
- [Baseline G2 aprovada](../GOVERNANCA/decisao-aprovacao-g2.md)

## Validação

Casos especificados para orientar futura implementação. Execução automatizada pendente.

## Resultado

Existe uma primeira bateria de referência e validação negativa, rastreável ao modelo de custos.

## Próxima Ação

Validar o JSON Schema, implementar o motor determinístico e executar os casos TC-CST-001 a TC-CST-010 antes de aprovar o modelo.
