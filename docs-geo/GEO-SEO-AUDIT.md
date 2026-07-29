# GEO-SEO-AUDIT - marccycling.com

Auditoria em 2026-07-28, antes das alteracoes desta rodada.

## Arquitetura

1. **Framework**: nenhum. HTML/CSS/JS puro, single-file por pagina. 2. **Versao**: n/a.
3. **Rotas**: estaticas por arquivo: `/` (index.html) e `/book/` (book/index.html).
4. **Renderizacao**: 100% estatica (equivalente a SSG). Todo conteudo ja vem no HTML do servidor.
5. **Metadata**: tags manuais no head de cada arquivo.
6-7. **Rotas/paginas indexaveis**: `/` e `/book/`. 8. **Bloqueadas**: nenhuma (nao existia robots.txt).

## Achados (estado ANTES desta rodada)

| Item | Situacao encontrada |
|---|---|
| robots.txt | NAO EXISTIA (critico para declarar sitemap e bots de IA) |
| sitemap.xml | NAO EXISTIA |
| canonical | OK nas 2 paginas |
| Open Graph | Presente, mas og:image RELATIVA (quebra compartilhamento) e sem og:site_name/locale |
| Twitter Card | NAO EXISTIA |
| JSON-LD | 1 LocalBusiness simples na home com 2 ERROS: aggregateRating proprio (contra diretriz Google) e horario Mon-Sat 08-18 (errado; oficial e Sat-Sun 07-17) |
| Favicon/manifest | favicon OK; manifest nao existe (nao critico) |
| Titles/descriptions | Exclusivos e bons nas 2 paginas |
| Headings | Home: h1 unico (visually-hidden, ok) + h2/h3 logicos. Book: h1 unico |
| Links internos | OK; faltava link de FAQ (nao existia FAQ) |
| URLs quebradas / redirects / duplicadas / parametros | Nenhum problema. GitHub Pages redireciona www->apex e forca HTTPS (canonico: apex sem www) |
| Alt text | Todas as imagens tem alt factual |
| Imagens grandes | Galeria otimizada (max 1600px, q80, lazy). hero.jpg 1536x1024 com fetchpriority=high. OK |
| Conteudo dependente de JS | **Teste curl real**: servicos, precos, telefone e booking presentes no HTML bruto de `/` e `/book/` (site estatico). UNICA exceсao: texto do hero esta DENTRO da imagem hero.jpg; mitigado por h1 visually-hidden e, agora, pelo bloco de resposta direta visivel |
| Core Web Vitals | Risco baixo: pagina unica, CSS inline, 2 fontes Google, gtag async. Imagens da galeria sem width/height (aspect-ratio via CSS controla CLS) |
| Acessibilidade | Boa base: aria-labels nos hotspots/carrossel, foco visivel, reduce-motion respeitado |
| Formularios/CTAs | 3 forms (lead x2, reminder) com labels; CTAs tel/wa.me/book |
| Consistencia de dados | DIVERGENCIA: schema dizia Mon-Sat 8-18; booking e sab-dom 7-17. Corrigido. "Available 7 days a week" refere-se a RESPOSTA por telefone/WhatsApp, nao a agenda; FAQ agora explica |
| Dados falsos/placeholder | Nenhum |
| Conteudo insuficiente / canibalizacao | Nao ha paginas concorrentes; servico/cidades ainda sem paginas dedicadas (ver CONTENT-PLAN) |
| Staging/admin indexavel | Nao existe |
| CDN/WAF | GitHub Pages (Fastly). NAO bloqueia bots de IA por padrao, nao ha painel de WAF/bot-fight. Nada a fazer no painel. Verificacao pos-publicacao: `curl -A "GPTBot" https://marccycling.com/` deve retornar 200 |

## Correcoes aplicadas nesta rodada

Ver GEO-SEO-IMPLEMENTATION.md. Criticas: robots.txt + sitemap criados; aggregateRating removido; horario corrigido para Sat-Sun 07:00-17:00; og:image absoluta; Twitter Cards; @graph completo com entidades estaveis; FAQ visivel + schema; resposta direta no topo da home; datas nos precos.
