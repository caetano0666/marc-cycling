#!/usr/bin/env python3
"""Testes SEO/GEO do marccycling.com (site estatico). Rodar antes de todo deploy."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = {"home": ROOT / "index.html", "book": ROOT / "book" / "index.html"}
falhas = []
ok = 0

def check(nome, cond, detalhe=""):
    global ok
    if cond:
        ok += 1
        print(f"  PASS  {nome}")
    else:
        falhas.append(nome)
        print(f"  FAIL  {nome} {detalhe}")

htmls = {k: p.read_text(encoding="utf-8") for k, p in PAGES.items()}

print("== Arquivos de rastreamento ==")
robots = (ROOT / "robots.txt")
check("robots.txt existe", robots.exists())
rt = robots.read_text() if robots.exists() else ""
check("robots.txt referencia sitemap absoluto", "Sitemap: https://marccycling.com/sitemap.xml" in rt)
for bot in ["GPTBot", "OAI-SearchBot", "ClaudeBot", "Claude-SearchBot", "PerplexityBot", "Bingbot", "Googlebot"]:
    check(f"robots.txt libera {bot}", f"User-agent: {bot}" in rt)
sm = (ROOT / "sitemap.xml")
check("sitemap.xml existe", sm.exists())
smt = sm.read_text() if sm.exists() else ""
urls = re.findall(r"<loc>(.*?)</loc>", smt)
check("sitemap so tem URLs https canonicas", all(u.startswith("https://marccycling.com/") for u in urls) and len(urls) >= 2, str(urls))
check("sitemap nao inclui docs-geo", not any("docs-geo" in u for u in urls))
check("llms.txt existe", (ROOT / "llms.txt").exists())

titles, descs = [], []
for nome, html in htmls.items():
    print(f"== Pagina: {nome} ==")
    t = re.search(r"<title>(.*?)</title>", html, re.S)
    d = re.search(r'<meta name="description" content="(.*?)"', html)
    titles.append(t.group(1) if t else "")
    descs.append(d.group(1) if d else "")
    check("title presente", bool(t and t.group(1).strip()))
    check("meta description presente", bool(d and d.group(1).strip()))
    check("canonical presente", 'rel="canonical" href="https://marccycling.com' in html)
    check("og:image absoluta", 'property="og:image" content="https://marccycling.com' in html)
    check("twitter card presente", 'name="twitter:card"' in html)
    check("html lang=en", '<html lang="en">' in html)
    h1s = re.findall(r"<h1[\s>]", html)
    check("exatamente 1 H1", len(h1s) == 1, f"({len(h1s)})")
    imgs = re.findall(r"<img\b[^>]*>", html)
    sem_alt = [i for i in imgs if " alt=" not in i]
    check("todas as <img> tem alt", not sem_alt, f"({len(sem_alt)} sem alt)")
    blobs = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)
    check("JSON-LD presente", len(blobs) >= 1)
    for i, b in enumerate(blobs):
        try:
            data = json.loads(b)
            check(f"JSON-LD #{i+1} parseia", True)
        except Exception as e:
            check(f"JSON-LD #{i+1} parseia", False, str(e))
            continue
        raw = json.dumps(data)
        check(f"JSON-LD #{i+1} sem aggregateRating proprio", "aggregateRating" not in raw)
    check("conteudo essencial no HTML bruto: telefone", "(754) 252-5245" in html)
    check("conteudo essencial no HTML bruto: booking", "/book" in html or "calendar.app.google" in html)
    check("conteudo essencial no HTML bruto: preco", "$95" in html and "$49" in html)
    check("data de preco visivel", "Prices updated July 2026" in html or "updated July 2026" in html)

print("== Entidades e consistencia ==")
home = htmls["home"]
for eid in ["#localbusiness", "#person-caetano", "#website", "#webpage", "#faq"]:
    check(f"@id estavel {eid} na home", f"https://marccycling.com/{eid}" in home)
check("book referencia #website por @id", "https://marccycling.com/#website" in htmls["book"])
check("titles exclusivos", titles[0] != titles[1])
check("descriptions exclusivas", descs[0] != descs[1])
check("horario correto no schema (Sat-Sun 07-17)", '"opens": "07:00"' in home and '"closes": "17:00"' in home and '"Saturday"' in home)
check("horario antigo removido (Mon 08:00)", '"Monday"' not in home.split('application/ld+json')[1].split('</script>')[0])
faq_schema = re.search(r'"@type": "FAQPage".*?\]', home, re.S)
vis_faq = home.count('<details class="faq-item">')
sch_faq = home.count('"@type": "Question"')
check(f"FAQ visivel ({vis_faq}) espelha schema ({sch_faq})", vis_faq == sch_faq and vis_faq > 0)
check("sem endereco residencial no site", "street" not in home.lower() and '"address"' not in home)

print()
print(f"RESULTADO: {ok} PASS, {len(falhas)} FAIL")
if falhas:
    print("Falhas:", *falhas, sep="\n  - ")
    sys.exit(1)
