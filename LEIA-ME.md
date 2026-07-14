# Marc Cycling — Guia rápido (site pronto)

Este é o site de uma página da **Marc Cycling**, todo em inglês, feito para o público dos EUA (Broward County / South Florida) e pronto para virar a página de destino ("Final URL") de uma campanha no **Google Ads**.

Tudo funciona sem instalar nada: é **um único arquivo** (`index.html`) mais a pasta de imagens (`img/`). Não usa banco de dados nem armazenamento no navegador.

---

## O que já está pronto no site

- **Botão gigante "Call now"** que liga direto para **(754) 252-5245** (fixo na parte de baixo no celular, sempre visível).
- **Botão de WhatsApp** que abre a conversa em **wa.me/17542525245**.
- Foto do Marc, logo oficial, favicon (o ícone da abinha do navegador) e as **cores oficiais: preto + amarelo**.
- Lista de serviços (e-bikes e bikes tradicionais), como funciona, área de atendimento (Broward + arredores), selo **"100+ avaliações 5 estrelas no Google"** com o **QR Code** e o texto trilíngue (English · Español · Português).
- SEO pronto (título, descrição e dados de negócio local para o Google).
- Espaço já preparado para o **rastreamento de conversão do Google Ads** (explico no fim).

---

## Parte 1 — Como colocar o site no ar (publicar)

Você tem 2 caminhos. O mais simples é o **Netlify** (arrastar e soltar).

### Opção A — Netlify (recomendado, grátis e rápido)

1. Entre em **https://app.netlify.com** e crie uma conta (pode usar o login do Google).
2. No painel, clique em **"Add new site" → "Deploy manually"**.
3. Abra a pasta `marc-cycling` no seu computador e **arraste a pasta inteira** para dentro da área indicada no Netlify.
   - Importante: arraste a pasta que contém o `index.html` **e** a pasta `img` juntos.
4. Pronto. Em alguns segundos o Netlify te dá um endereço tipo `nome-aleatorio.netlify.app` — já está no ar.
5. Para trocar por um nome melhor: **Site settings → Change site name**.

**Para usar seu domínio próprio** (ex.: `marccycling.com`):
1. No Netlify: **Domain settings → Add a domain** e digite seu domínio.
2. O Netlify mostra os registros de DNS para configurar. Entre no site onde você comprou o domínio (GoDaddy, Registro.br, etc.) e aponte conforme as instruções que o Netlify mostrar.
3. O Netlify ativa o **HTTPS (cadeado)** automaticamente e de graça.

> Sempre que quiser atualizar o site, é só arrastar a pasta de novo em **Deploys → Drag and drop**.

### Opção B — GitHub Pages

Se preferir GitHub Pages (como no seu outro site), me avise que eu publico do mesmo jeito que fiz com o Ultra100K.

---

## Parte 2 — Onde trocar as informações do site

Tudo fica no arquivo **`index.html`**. Os pontos que você pode querer ajustar:

| O que | Onde procurar no arquivo |
|---|---|
| **Telefone** | Procure por `17542525245` (aparece nos links de ligar e WhatsApp). |
| **Depoimentos** | Procure por `DEPOIMENTOS:` — troque os 3 textos de exemplo pelas avaliações reais do Google. |
| **Domínio** | Procure por `SEU-DOMINIO.com` e troque pelo seu endereço final (2 lugares). |
| **Cidades atendidas** | Procure por `class="chip"` na seção "Service area". |

Se ficar em dúvida em qualquer um, me manda que eu troco pra você.

---

## Parte 3 — Rastreamento de conversão no Google Ads

O objetivo: **contar como "conversão" toda vez que alguém clica em Ligar ou WhatsApp**. Isso já está preparado no site — só falta você colar 2 códigos que o Google te dá. **Enquanto não colar, o site funciona normalmente** (o telefone liga e o WhatsApp abre do mesmo jeito).

### Passo 1 — Pegar o seu "Tag ID" (ID da tag do Google)

1. Entre no **Google Ads**.
2. Vá em **Ferramentas (o ícone de chave inglesa) → Conversões**.
3. Se ainda não tem uma conversão, clique em **"+ Nova ação de conversão"**, escolha **Site**, e crie duas:
   - uma chamada **"Ligação (Call)"**
   - outra chamada **"WhatsApp"**
   (tipo "Enviar" / clique em botão).
4. Depois de criar, o Google mostra a **"Tag do Google"** com um código parecido com **`AW-XXXXXXXXXX`**. Anote esse número.
5. Para cada conversão, o Google também dá um **"Rótulo de conversão"** (uma sequência de letras/números). Anote os dois rótulos (o da ligação e o do WhatsApp).

### Passo 2 — Colar o código principal (uma vez só)

1. Abra o arquivo `index.html` num editor de texto simples (Bloco de Notas, TextEdit).
2. Lá no começo, procure o bloco que começa com:
   `GOOGLE ADS (gtag.js) — COLE AQUI O SEU TAG ID.`
3. Logo abaixo há um trecho **entre `<!--` e `-->`** (isso quer dizer "desligado"). **Remova a linha `<!--` de cima e a linha `-->` de baixo** para ligar.
4. Nesse trecho, troque **`AW-XXXXXXXXXX`** (aparece 2 vezes) pelo seu número real.

### Passo 3 — Ligar a contagem nos botões

1. No **fim** do arquivo, procure por `function trackCall` e `function trackWhatsApp`.
2. Em cada uma há uma linha começando com `//` (comentada/desligada). **Apague os `//` do começo** dessa linha para ligar.
3. Troque nessa linha:
   - `AW-XXXXXXXXXX` → seu número
   - `CALL_LABEL_AQUI` → o rótulo da conversão de **ligação**
   - `WHATSAPP_LABEL_AQUI` → o rótulo da conversão de **WhatsApp**
4. Salve e publique de novo (arraste a pasta no Netlify).

> Depois disso, cada clique em Ligar/WhatsApp vira uma conversão no Google Ads. Se travar em algum passo, me manda o print que eu faço o ajuste.

### Passo 4 — Na campanha do Google Ads

- Use o endereço final do site (seu domínio) como **"URL final"** dos anúncios.
- Marque essas conversões (Ligação e WhatsApp) como as **conversões principais** da campanha, para o Google otimizar por elas.

---

## Resumo de 30 segundos

1. Arraste a pasta no **Netlify** → site no ar.
2. (Opcional) Ligue seu **domínio** no Netlify.
3. Troque os **depoimentos** pelos reais do Google.
4. Quando tiver o **Google Ads**, cole o **AW-...** e os **rótulos** nos 2 lugares indicados.

Qualquer passo que travar, me chama. 🚴
