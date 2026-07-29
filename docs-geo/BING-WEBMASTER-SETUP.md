# BING-WEBMASTER-SETUP (acao do proprietario, ~30 min)

Bing alimenta Copilot e e um dos provedores de busca do ChatGPT. Prioridade alta e custo zero.

## Bing Webmaster Tools

1. https://www.bing.com/webmasters > entrar com conta Microsoft (criar se preciso).
2. "Importar do Google Search Console" (faca o Search Console primeiro) OU adicionar `https://marccycling.com` manualmente (verificacao por DNS TXT na GoDaddy).
3. Enviar o sitemap: `https://marccycling.com/sitemap.xml`.
4. Acompanhar mensal: indexacao, **AI Performance** (URLs citadas em respostas de IA), grounding queries.

## Bing Places (PRIORIDADE, ver NAP checklist)

1. https://www.bingplaces.com > "Import from Google My Business" (sincroniza tudo do GBP em minutos) ou criar manualmente.
2. Conferir: service-area business, endereco oculto, telefone (754) 252-5245, horario sab-dom 7am-5pm, areas, fotos, link de booking.

## IndexNow (ja preparado no site)

- Chave: `8e30c0b2dfac43307aebbd4e5ec63a8f` hospedada em `https://marccycling.com/8e30c0b2dfac43307aebbd4e5ec63a8f.txt` (exigencia do protocolo; nao e segredo).
- Site estatico no GitHub Pages nao tem hook de publicacao, entao o ping e manual (ou eu rodo a cada publicacao). Apos publicar mudanca relevante:

```bash
curl "https://api.indexnow.org/indexnow?url=https://marccycling.com/&key=8e30c0b2dfac43307aebbd4e5ec63a8f"
```

- IndexNow acelera descoberta no Bing; NAO garante indexacao e o Google nao o utiliza.
