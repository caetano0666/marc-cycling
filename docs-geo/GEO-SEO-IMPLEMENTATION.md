# GEO-SEO-IMPLEMENTATION - o que foi feito em 2026-07-28

## Arquivos criados

- `robots.txt` - allow para Googlebot, Bingbot, GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, Claude-User, Claude-SearchBot, PerplexityBot, Perplexity-User, Google-Extended, Applebot e *; Disallow /docs-geo/; aponta o sitemap.
- `sitemap.xml` - 2 URLs canonicas com lastmod real.
- `llms.txt` - resumo experimental do negocio (nao e padrao universal; Google afirma nao usar; custo zero).
- `8e30c0b2dfac43307aebbd4e5ec63a8f.txt` - chave IndexNow (ver BING-WEBMASTER-SETUP.md).
- `docs-geo/` - fonte de verdade (business.json) + 14 documentos. Bloqueada no robots.txt.

## index.html (home)

1. Head: og:image absoluta + dimensoes, og:site_name, og:locale, Twitter Card completa.
2. JSON-LD reescrito como @graph com @id estaveis: LocalBusiness (sem aggregateRating, sem endereco, horario sab-dom 07-17, paymentAccepted, areaServed 13 areas com containedInPlace FL, hasOfferCatalog com 7 Offers "from" aprovados), Person Caetano, WebSite, WebPage, FAQPage.
3. Bloco de resposta direta visivel logo apos o hero (quem, o que, onde, precos from, como agendar, idiomas). GEO: resposta direta primeiro.
4. Secao FAQ visivel (#faq) com 8 perguntas/respostas em details/summary, espelhando 1:1 o FAQPage schema. Linkada no menu e no rodape.
5. "Prices updated July 2026." na secao de precos (a tabela de comparacao ja tinha data propria).
6. Rodape: links "Book online" e "Frequently asked questions".
7. GA4: listener ampliado (whatsapp_click, phone_click, book_appointment_click, google_reviews_click) + contact_form_submit no formulario. Conversoes do Google Ads intocadas.

## book/index.html

1. Head: mesmas correcoes de OG/Twitter + JSON-LD proprio (WebPage + BreadcrumbList referenciando as entidades da home por @id).
2. Breadcrumb visivel "Home › Book your service" coerente com o schema.
3. "Prices updated July 2026." no resumo de precos. Link FAQ no menu.
4. GA4: mesmo listener ampliado.

## Decisoes registradas

- Horario oficial: sab-dom 7am-5pm ET. Confirmado pelo proprietario em 27/07/2026 quando pediu a ampliacao da agenda ate 5pm (agenda do Google e site ja refletem). A divergencia apontada no prompt esta RESOLVIDA.
- #organization fundido em #localbusiness (evita entidade duplicada; LocalBusiness e subtipo de Organization).
- Sem subtipo BicycleStore/Store: modelo e movel, LocalBusiness generico e o correto.
- areaServed usa as 12 cidades + Broward County JA PUBLICADAS na secao Service Area do site (aprovadas anteriormente pelo proprietario). Confirmacao fina pendente em BUSINESS-DATA-NEEDED.md.
- Sem SearchAction (site nao tem busca interna). Sem priceRange (evita ambiguidade; precos reais estao no OfferCatalog).
- Paginas /services/* e /service-areas/* NAO foram criadas nesta rodada: exigem conteudo original com evidencias do proprietario (fotos, casos, detalhes). Especificadas em CONTENT-PLAN.md como proxima prioridade.
