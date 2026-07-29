# SCHEMA-INVENTORY

| Pagina | URL | Schema | @id principal | Entidade | Fonte dos dados | Validado em | Status | Erros | Obs |
|---|---|---|---|---|---|---|---|---|---|
| Home | https://marccycling.com/ | LocalBusiness | #localbusiness | Marc Cycling | business.json | 2026-07-28 (json.loads + estrutura) | OK local; validar no Rich Results apos publicar | 0 | Sem aggregateRating proprio, sem endereco; horario sab-dom 07-17; OfferCatalog 7 ofertas "from" |
| Home | https://marccycling.com/ | Person | #person-caetano | Caetano Marc Zammataro | prompt do proprietario | 2026-07-28 | OK | 0 | So dados profissionais publicos |
| Home | https://marccycling.com/ | WebSite | #website | marccycling.com | repo | 2026-07-28 | OK | 0 | Sem SearchAction (nao ha busca) |
| Home | https://marccycling.com/ | WebPage | #webpage | Home | repo | 2026-07-28 | OK | 0 | dateModified real |
| Home | https://marccycling.com/ | FAQPage | #faq | 8 perguntas | politicas reais do site | 2026-07-28 | OK | 0 | Espelha 1:1 a secao visivel #faq |
| Book | https://marccycling.com/book/ | WebPage | /book/#webpage | Booking | repo | 2026-07-28 | OK | 0 | Referencia #website e #localbusiness por @id |
| Book | https://marccycling.com/book/ | BreadcrumbList | /book/#breadcrumb | Home > Book | repo | 2026-07-28 | OK | 0 | Breadcrumb visivel correspondente na pagina |

Validacao externa (fazer apos publicar): https://validator.schema.org e https://search.google.com/test/rich-results nas 2 URLs; registrar resultado aqui com data.

Regra: nao usar todos os schemas em todas as paginas. Paginas futuras de servico usam Service + WebPage + BreadcrumbList; About usa AboutPage + referencia a #person-caetano.
