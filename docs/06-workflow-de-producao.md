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

### Regras práticas pra reduzir claim
- Clipe curto, sempre cortando de volta pra ela falando (transformação visível).
- Comentário substancial por cima (não deixar o clipe "rodar sozinho").
- Print/screenshot no lugar do vídeo sempre que possível.
- Creditar a fonte na tela/descrição quando fizer sentido.
- Nunca reupar conteúdo inteiro de outra pessoa.
- Música: só de biblioteca livre de direitos (YouTube Audio Library, etc.) — música
  comercial é claim na hora.

## O pipeline por vídeo (ponta a ponta)

1. **Pauta** (`05`): escolher o tema da semana no `backlog.csv` + escrever o gancho
   "Have you ever noticed...".
2. **Roteiro**: aplicar a estrutura da DNA (`02`) — gancho → escada de exemplos →
   nomear o fenômeno → desnormalizar → fecho íntimo.
3. **Levantar o visual**: listar os B-rolls/prints que ilustram cada bloco. Evergreen:
   B-roll de stock. Trend-hook: o snippet/print do caso (tier 2/3).
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
