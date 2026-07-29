# AI-VISIBILITY-TRACKING - rotina mensal de Share of Model

Este e o indicador real de progresso do GEO (nao a posicao no Google). Rotina manual, 1x por mes, ~40 min. Pode ser feita comigo (Claude) guiando.

## Rotina

1. Abrir GEO-TESTS.md e rodar as 56 perguntas (ou um subconjunto fixo de 20, sempre as mesmas) em: ChatGPT (com busca), Claude, Perplexity, Copilot e Google (AI Overviews / AI Mode).
2. Para cada pergunta x plataforma, registrar na tabela do mes:
   - **C** = citada com link para marccycling.com
   - **M** = mencionada sem link
   - **X** = nao apareceu
   - Quem apareceu no lugar (nome do concorrente/franquia).
3. Salvar como `docs-geo/tracking/YYYY-MM.md`. Comparar com o mes anterior.

## Modelo da tabela

```
# Share of Model YYYY-MM (data)
| # | Pergunta | ChatGPT | Claude | Perplexity | Copilot | Google AI | Quem apareceu |
|---|---|---|---|---|---|---|---|
| 1 | Who repairs bicycles near me? | X | X | X | X | X | (nomes) |
Resumo: C=_, M=_, X=_ de N respostas. Variacao vs mes anterior: _
```

## Complementos no mesmo dia

- GA4: Relatorios > Aquisicao > verificar referencias contendo chatgpt.com (inclui utm_source=chatgpt.com), bing.com, copilot.microsoft.com, perplexity.ai, gemini.google.com, claude.ai. Anotar sessoes/mes de cada.
- Bing Webmaster > AI Performance: URLs citadas e grounding queries.
- Anotar o numero atual de reviews no Google (meta: +4 a 8/mes).

Linha de base: julho/2026 = site recem-otimizado, presenca esperada proxima de zero fora de "Marc Cycling reviews". Progresso realista aparece em 2-4 meses com GBP ativo + Bing Places + mencoes de terceiros.
