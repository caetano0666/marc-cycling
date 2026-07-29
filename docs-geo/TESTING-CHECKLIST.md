# TESTING-CHECKLIST

## Automatizado (rodar antes de todo deploy)

```bash
python3 docs-geo/seo-tests.py
```

Valida: title/description/canonical unicos por pagina, og:image absoluta, twitter card, html lang, H1 unico por pagina, robots.txt existe e referencia sitemap, sitemap so com URLs canonicas https, JSON-LD parseavel em todas as paginas, sem aggregateRating no LocalBusiness, @id estaveis presentes, alt em todas as <img>, FAQ visivel espelhando o FAQPage schema, conteudo essencial (precos, telefone, booking) presente no HTML bruto.

## Manual pos-publicacao

- [ ] `curl -s https://marccycling.com/robots.txt` retorna o arquivo (200)
- [ ] `curl -s https://marccycling.com/sitemap.xml` retorna as 2 URLs
- [ ] `curl -sA "GPTBot" https://marccycling.com/ -o /dev/null -w "%{http_code}"` = 200 (CDN nao corta bots de IA)
- [ ] https://validator.schema.org na home e /book/: 0 erros
- [ ] https://search.google.com/test/rich-results: FAQ e Breadcrumb reconhecidos
- [ ] Lighthouse (Chrome DevTools) mobile na home: registrar Performance/A11y/SEO antes e depois de mudancas grandes
- [ ] Compartilhar https://marccycling.com no WhatsApp: imagem e titulo corretos (og)

## Regras permanentes

- Pagina nova nao entra sem: title/description proprios, canonical, WebPage schema referenciando #website/#localbusiness, presenca no sitemap, link interno apontando pra ela.
- URL noindex nunca entra no sitemap. Canonical nunca aponta para redirect.
