# Estrutura inicial do projeto CONSORCIO

| Campo | Valor |
|---|---|
| **ID** | CONSORCIO-ARQ-EST-001 |
| **Projeto** | CONSORCIO |
| **Repositório** | [carlos-andrade/CONSORCIO](https://github.com/carlos-andrade/CONSORCIO) |
| **Tipo documental** | ARQUITETURA_ESTRUTURA |
| **Fase** | G3 — Construção controlada |
| **Estado** | EM_CURSO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 79267ce86fa6e10b05cc2446375e61dc7eb224b3f406d810909985e251a1300d |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-16 |
| **Data de atualização** | 2026-10-16 |
| **Responsável** | Responsável pelo projeto CONSORCIO |
| **Aprovador** | Proprietário do projeto — baseline G2 aprovada em 2026-10-16 |
| **Origem** | Decisão CONSORCIO-DEC-G2-001 |
| **Autoridade superior** | [Política CONSORCIO](GOVERNANCA.md) e [GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Estado

Estrutura inicial criada para separar governação, dados, modelos analíticos, análises, relatórios, testes e automação. Os diretórios reservados não significam que os módulos estejam implementados.

## Estrutura

```text
.github/workflows/       Workflows de validação e governação
GOVERNANCA/
  decisoes/              Decisões formais e referências
  requisitos/            Requisitos e critérios de aceitação
  arquitetura/           Registos de arquitetura
  riscos/                Riscos e mitigação
  evidencias/            Evidências e referências de auditoria
DADOS/
  fontes/                Fontes públicas/autorizadas e proveniência
  dados_sinteticos/      Dados sintéticos para testes
  esquemas/              Esquemas e dicionários de dados
MODELOS/
  custos/                Componentes de custos e encargos
  parcelas/              Regras e cenários de prestações
  lances/                Simulações analíticas de lances, sem execução real
  cenarios/              Cenários reproduzíveis e pressupostos
ANALISES/                Análises documentadas e reproduzíveis
RELATORIOS/              Relatórios com fontes e limitações
TESTES/                  Casos de referência, regressão e qualidade
automation/              Ferramentas de auditoria e automação
README.md                Entrada principal do projeto
GOVERNANCA.md            Política local e hierarquia normativa
ESTRUTURA.md             Este documento
```

## Limites de implementação

- Âmbito inicial documental e analítico; não é uma aplicação transacional.
- Utilizar fontes públicas ou autorizadas e dados sintéticos/agregados.
- Não inserir dados pessoais reais, documentos de identidade, dados bancários, dados de crédito ou segredos.
- A pasta de lances destina-se apenas a simulações; não executa operações reais.
- Cada fonte concreta exige validação de licença, condições de uso, proveniência e data.
- Não escolher framework, base de dados, cloud ou microsserviços antes de necessidade demonstrada.
- Fórmulas financeiras exigem unidades, pressupostos, casos de referência e testes antes de suportar decisões.
- Diretórios vazios são marcadores estruturais, não evidência de funcionalidade concluída.

## Critérios de aceitação da estrutura

1. Diretórios separados por responsabilidade e limites de segurança documentados.
2. Governação e auditoria existentes preservadas.
3. Nenhuma integração externa, operação financeira ou dado pessoal real introduzido.
4. README alinhado com a fase e a decisão G2.
5. Workflow de auditoria executado após as alterações e resultados verificados.

## Evidências

- [Decisão formal G2](GOVERNANCA/decisao-aprovacao-g2.md)
- [Revisão técnica G2](GOVERNANCA/revisao-requisitos-arquitetura-dados-privacidade-riscos.md)
- [Roadmap](GOVERNANCA/roadmap-adocao.md)
- [Workflow de governação](.github/workflows/governanca-diaria.yml)

## Validação

A criação dos diretórios é uma alteração estrutural inicial. A validação final depende da auditoria automatizada, revisão do diff e verificação do commit remoto.

## Resultado

A estrutura inicial está preparada para receber documentação e componentes analíticos incrementais, sem declarar módulos de negócio implementados.

## Próxima Ação

Executar auditoria documental e atualizar o roadmap com o resultado comprovado. Corrigir qualquer falha antes de declarar G3 concluído.
