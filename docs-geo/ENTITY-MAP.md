# ENTITY-MAP - Marc Cycling

Gerado em 2026-07-28. Toda pagina do site reutiliza estas entidades pelos mesmos @id. Nunca criar entidade duplicada.

## Entidades canonicas (JSON-LD @id)

| Entidade | @id | Onde e declarada |
|---|---|---|
| Marc Cycling (LocalBusiness, que E a Organization) | `https://marccycling.com/#localbusiness` | index.html |
| Logo | `https://marccycling.com/#logo` | index.html (dentro do LocalBusiness) |
| Caetano Marc Zammataro (Person) | `https://marccycling.com/#person-caetano` | index.html |
| WebSite | `https://marccycling.com/#website` | index.html |
| Home WebPage | `https://marccycling.com/#webpage` | index.html |
| FAQ | `https://marccycling.com/#faq` | index.html |
| Book WebPage | `https://marccycling.com/book/#webpage` | book/index.html (referencia #website e #localbusiness) |
| Book Breadcrumb | `https://marccycling.com/book/#breadcrumb` | book/index.html |

Decisao registrada: `#organization` foi fundido em `#localbusiness` (LocalBusiness e subtipo de Organization). Duas entidades separadas para a mesma empresa violariam a regra "nunca criar entidades duplicadas". Se um dia existir mais de um ponto de operacao, separar.

## Relacoes

```
Marc Cycling ─ legalName ─→ Marc Cycling LLC
Marc Cycling ─ founder ──→ Caetano Marc Zammataro (Person #person-caetano)
Caetano ────── worksFor ─→ Marc Cycling
Marc Cycling ─ provides ─→ Flat Tire Repair (standard $49+, e-bike $120+)
Marc Cycling ─ provides ─→ Tune-Ups Bronze $95 / Silver $140 / Gold $215
Marc Cycling ─ provides ─→ E-Bike Service Silver $150 / Gold $220
Marc Cycling ─ serves ───→ Broward County + Fort Lauderdale, Hollywood, Pembroke Pines,
                            Pompano Beach, Coral Springs, Davie, Plantation, Sunrise,
                            Weston, Miramar, Coconut Creek, Miami (FL)
Marc Cycling ─ hasWebsite → marccycling.com (#website)
Marc Cycling ─ booking ──→ /book (+ https://calendar.app.google/XbpMuHghJ2v7AP5z6)
Marc Cycling ─ sameAs ───→ https://g.page/marccycling (Google Business Profile)
Marc Cycling ─ FAQ ──────→ /#faq (visivel + FAQPage schema)
Marc Cycling ─ reviews ──→ Google (5.0, 115+, exibidas no site com link para a fonte)
Marc Cycling ─ Instagram/Facebook/Yelp → NEEDS-OWNER-INPUT (urls nao estao no repositorio)
```

## Regras de reuso

1. Nova pagina = novo `WebPage` com `isPartOf {#website}` e `about {#localbusiness}`. Nunca redeclarar LocalBusiness/Person completos em outra pagina; referenciar por @id.
2. Nome sempre "Marc Cycling"; "Marc Cycling LLC" apenas em legalName.
3. Telefone unico: +1-754-252-5245. Booking unico: /book.
4. Cidades novas so entram aqui (e no schema) depois de confirmadas pelo proprietario.
