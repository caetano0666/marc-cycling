# SEARCH-CONSOLE-SETUP (acao do proprietario, ~20 min)

1. Acessar https://search.google.com/search-console com a conta Google do negocio.
2. Adicionar propriedade tipo **Dominio**: `marccycling.com`. A verificacao pede um registro TXT no DNS da GoDaddy (mesmo painel onde estao os registros A do site). Copiar o TXT que o Google mostrar e criar na GoDaddy em DNS > Records.
   - Alternativa mais simples: propriedade tipo "Prefixo de URL" `https://marccycling.com/` com verificacao por tag HTML; me pedir para inserir a meta tag real no head (NAO inserir token falso; hoje nao ha nenhum).
3. Depois de verificado: **Sitemaps** > enviar `https://marccycling.com/sitemap.xml`.
4. **Inspecao de URL**: inspecionar `/` e `/book/`, pedir indexacao.
5. Acompanhar mensalmente: Indexacao > Paginas; Experiencia > Core Web Vitals; Melhorias > dados estruturados (FAQ, Breadcrumb); Seguranca e acoes manuais (deve estar sempre vazio); Desempenho > consultas, paginas, paises, dispositivos.
6. Quando o Google liberar relatorio de recursos generativos/AI Overviews na sua conta, acompanhar junto com o AI-VISIBILITY-TRACKING.md.
