# 06 — Workflow de produção (com a camada de footage)

A Cá é um canal de **comentário**: ela mistura talking-head (ela falando) com
material de terceiros mostrado na tela — clipes de TikTok, reportagens, prints,
casos virais — e comenta em cima ("vou mostrar pra vocês...", "olha esse caso aqui",
"presta atenção nesse..."). Confirmado nas transcrições.

Pra Hani isso precisa de cuidado, porque no mercado anglófono **Content ID + strike
de copyright são muito mais agressivos** que no Brasil. Aqui está como fazer sem
queimar o canal.

## A realidade legal (sem rodeio)

- Comentário/crítica **transformativa** é uma categoria gigante e legítima no
  YouTube (roda em *fair use* nos EUA / *fair dealing* no Reino Unido).
- MAS fair use é **defesa, não permissão**. Mesmo certo, você pode levar um claim
  do Content ID (perde monetização daquele vídeo) ou, no pior caso, um strike — e
  pra um canal **novo, sem histórico**, isso machuca mais.
- Logo: a gente trata clipe de terceiro como **risco a gerenciar**, não como base.

## A jogada que alinha tudo: evergreen = talking-head + stock

O modelo mais seguro juridicamente é também o que **mais cresce** (decisão do `01`/`03`):
vídeo evergreen de comportamento **não precisa de clipe de terceiro**. É a Hani
falando + B-roll de banco livre + tipografia na tela. Zero risco, e é justamente o
que vira breakout. Os vídeos trend/react (que precisam do clipe) são a minoria
arriscada, usada cirurgicamente.

| Tipo de vídeo (~%) | Visual | Risco |
|---|---|---|
| **Evergreen comportamental** (~70%) | talking-head + B-roll de stock livre + texto na tela | nenhum |
| **Trend-hook** (~30%) | base + trecho curto/print do que critica, com comentário pesado | médio, gerenciável |

## Tiers de footage (do mais seguro pro mais arriscado)

1. **Próprio + stock livre (a espinha dorsal)**: a Hani gravada + B-roll de
   bancos gratuitos e sem atribuição obrigatória — **Pexels, Pixabay, Coverr,
   Mixkit**. Cobre quase todo vídeo evergreen (ilustra o conceito, não um caso
   específico). 100% seguro.
2. **Trecho transformativo de terceiro (fair use)**: o snippet do que está sendo
   criticado (uma trend, uma reportagem), com a regra: **curto, sempre com
   comentário/crítica em cima, nunca o vídeo inteiro**. Prefira **print/screenshot**
   a vídeo quando der (print é menos "Content-IDável").
3. **Reportagem/jornal**: tem Content ID forte. Usar pouco, curto, com comentário —
   ou trocar pelo **print da manchete** em vez do vídeo.

## Clipes de TikTok (a rotina react — decidido)

A Hani vai querer mostrar **clipes reais, geralmente de TikTok**. Dá pra fazer — é o
modelo de canal de comentário — desde que os clipes virem **ilustração/evidência da
tese dela**, não o vídeo inteiro. A voz/reflexão dela é a espinha; o clipe é a prova.

### O maior risco no TikTok é a MÚSICA
A trilha do TikTok é licenciada pro TikTok, **não pro YouTube** → Content ID na hora.
O visual do criador também pode gerar claim. A disciplina que mata ~90% do risco:

> **Voz dela por cima + áudio original do clipe abaixado/mutado + clipe curto +
> cortar de volta pro rosto dela.**

Isso, sozinho, (a) tira a música que dispara o Content ID e (b) torna o uso
claramente transformativo (comentário, não reupload).

### Regras práticas
- Clipe **curto**, sempre voltando pra ela falando (transformação visível).
- **Comentário substancial** por cima — ela nomeia o fenômeno e disseca, não é "olha
  que doido". Isso é o que torna fair use E o que sustenta monetização (canal de
  clipe com comentário raso cai em "reused content").
- **Áudio original abaixado/mutado**; a voz dela manda.
- **Manter o @ do criador na tela** (a marca do TikTok serve de crédito) + creditar
  na descrição.
- Nunca enfileirar vários clipes inteiros (vira compilação, não comentário).
- Música de fundo só de biblioteca livre (YouTube Audio Library, Uppbeat, Pixabay).
- Antes de publicar: rodar a checagem de direitos no Studio. Se vier só claim de
  música, dá pra mutar o trecho; o resto continua.

### Como baixar os clipes
`ferramentas/baixar-clipes.sh` — recebe uma lista de URLs de TikTok (uma por linha) e
baixa os .mp4 (yt-dlp pega o TikTok sem marca d'água; o autor já vem no nome do
arquivo). Os clipes ficam em `dados/clipes/<video>/` e **não vão pro repo**
(copyright + peso, estão no `.gitignore`).

```bash
bash ferramentas/baixar-clipes.sh dados/clipes/meu-video urls.txt
```

## O pipeline por vídeo (ponta a ponta)

1. **Pauta** (`05`): escolher o tema da semana no `backlog.csv` + escrever o gancho
   "Have you ever noticed...".
2. **Roteiro**: aplicar a estrutura da DNA (`02`) — gancho → escada de exemplos →
   nomear o fenômeno → desnormalizar → fecho íntimo.
3. **Levantar o visual**: listar o que ilustra cada bloco. Evergreen: B-roll de stock.
   React/trend: colar as URLs dos TikToks num `urls.txt` e rodar
   `baixar-clipes.sh` pra pasta do vídeo (lembrar das regras de clipe acima).
4. **Gravar** o talking-head (áudio é prioridade).
5. **Editar**: intercalar talking-head + B-roll/prints + texto na tela pro "rótulo do
   fenômeno". Cortes de respiração. Sem firula.
6. **Publicar**: título (3 registros do `03`), thumbnail de rosto + 2-4 palavras,
   descrição + créditos de footage. Conferir o Content ID antes de tornar público.

## Fontes (consolidado)

**B-roll/footage livre**: Pexels, Pixabay, Coverr, Mixkit.
**Música livre**: YouTube Audio Library, Uppbeat, Pixabay Music.
**Mineração de tema** (já definido no `05`):
- Banco evergreen: catálogo da Cá (`dados/videos-index.txt`) + canais EN vizinhos.
- Demanda: `ferramentas/minerar-pautas.py` (autocomplete YT) + VidIQ/TubeBuddy + Google Trends.
- Radar de trend: Reddit (r/mildlyinfuriating, r/antiwork, r/decidingtobebetter...),
  TikTok/Reels, YouTube *Popular*, X.
