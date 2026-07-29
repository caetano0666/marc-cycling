# FUTURE-MAINTENANCE - protecao contra regressao estrutural

## Intocaveis (nunca remover/quebrar em alteracao futura)

JSON-LD @graph da home e do /book (entidades e @id do ENTITY-MAP.md), canonicals, robots.txt, sitemap.xml, secao FAQ + FAQPage schema (sempre em espelho 1:1), bloco de resposta direta no topo da home, breadcrumb do /book, links internos do rodape/menu, GA4 + listener de eventos, conversoes do Google Ads, chave IndexNow, llms.txt.

## Antes de QUALQUER deploy

1. Rodar `python3 docs-geo/seo-tests.py` (tudo PASS).
2. Se mudou dado comercial (preco, horario, telefone, area): atualizar `docs-geo/business.json` PRIMEIRO e replicar em: texto visivel, JSON-LD, FAQ, llms.txt, GBP, Bing Places.
3. Se mudou preco: atualizar "Prices updated [mes ano]" nas 2 paginas e a data da tabela de comparacao.
4. Pagina nova: title/description/canonical proprios, WebPage schema com isPartOf #website e about #localbusiness, breadcrumb visivel + schema, entrada no sitemap.xml, link interno.
5. Apos publicar: ping IndexNow (comando no BING-WEBMASTER-SETUP.md).

## Regra de numero de reviews (29/07/2026)

NUNCA publicar numero exato de reviews em texto fixo (meta, schema, FAQ, llms.txt, texto visivel). Usar marco redondo: "over 100" hoje; atualizar para "over 150" so quando cruzar 150, e assim por diante. Contagem visivel sempre acompanhada de "as of [mes ano]". O numero exato vive apenas no Google, na fonte.

## Rotinas

- **Mensal**: GEO-TESTS + AI-VISIBILITY-TRACKING; conferir reviews (meta 4-8/mes) e responder em 24h.
- **Trimestral**: revisar conteudo e datas de preco (conteudo parado >3 meses perde citacao em IA); atualizar lastmod do sitemap e dateModified dos WebPage quando houver mudanca real; conferir NAP-CONSISTENCY-CHECKLIST.
- **Ao mudar horario da agenda**: site (/book e FAQ), schema (openingHoursSpecification), descricao do agendador do Google, GBP e Bing Places, tudo junto.
