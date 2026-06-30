# 05 — Engine de pautas (mineração e seleção de temas)

Onde a gente acha os temas, como valida e como decide o que vira vídeo. O canal
faz ~2 vídeos/semana, então o engine precisa entregar, toda semana, 2 pautas boas
com confiança — sem depender de inspiração.

Princípio (vindo da estratégia em `01`): **trend é isca, comportamento é a casa.**
Logo o engine tem duas esteiras que se cruzam:

- **Banco evergreen** (a substância) — temas atemporais de comportamento humano.
- **Radar de trend** (a isca) — o que está em alta agora no mundo anglófono.

A pauta da semana mistura: ~1 evergreen-núcleo + ~1 trend-com-gancho-evergreen.

## Onde minerar (as fontes)

### 1. Banco evergreen
- **O catálogo da Cá Fernandes** (`dados/videos-index.txt`, 157 títulos): a mina de
  ouro. São conceitos **já validados** por uma audiência real e **ainda não feitos
  em inglês**. Cada título dela é um candidato — é só localizar (ver `03`).
- **Canais anglófonos vizinhos** (human behavior / social commentary / reflexão):
  ver quais temas se repetem e performam. Lista a manter: (preencher conforme acha).
- **Taxonomia de comportamento**: status, inveja, manipulação, autossabotagem,
  hipocrisia social, consumo, relacionamentos, solidão, vergonha, pertencimento.

### 2. Demanda de busca (validação) — grátis
- **Autocomplete do YouTube** via `ferramentas/minerar-pautas.py`. Mostra o que as
  pessoas digitam de verdade. Já provou: "the psychology of" devolveu
  *"the psychology of people who don't post on social media"* — exatamente o
  "Não postou, não viveu" dela, com demanda em inglês.
- **VidIQ / TubeBuddy** (extensão de navegador, tem free): volume de busca +
  concorrência + "score" por palavra-chave. Use pra confirmar se há audiência e se
  um canal novo consegue ranquear (procurar competição média, não saturada).
- **Google Trends** (filtrar país: US/UK/CA/AU): timing e termos em ascensão.

### 3. Radar de trend (a isca do momento)
- **Reddit**: a melhor fonte de "irritação comportamental do momento" —
  r/mildlyinfuriating, r/antiwork, r/decidingtobebetter, r/TwoXChromosomes,
  r/unpopularopinion, r/NoStupidQuestions. As pessoas descrevem o comportamento
  que te dá raiva; você nomeia e disseca.
- **TikTok / Reels**: a "discussão da semana" (trends, audios, polêmicas).
- **YouTube**: aba *Popular* dos canais vizinhos + busca + trending.
- **X/Twitter**: trending topics.

## Onde isso vive (o lar operacional)

- **Fonte de verdade + método**: este repo. O backlog mora em `pauta/backlog.csv`.
- **Dia a dia da Hani**: importar o `backlog.csv` num **Google Sheets** (ou Notion/
  Trello) — mais ergonômico pra mexer todo dia. O repo guarda o método e o histórico.

## Como selecionar (o scorecard)

Cada candidato entra no backlog e recebe nota (1-5) em 4 eixos. A prioridade é a
soma ponderada — universalidade e gancho pesam mais (é o que faz crescer):

| Eixo | O que mede | Peso |
|---|---|---|
| **Universalidade** | viaja entre culturas? evergreen > trend local | x3 |
| **Força do gancho** | dá pra escrever um "Have you ever noticed..." forte? | x3 |
| **Demanda/competição** | tem busca (autocomplete/VidIQ) e dá pra ranquear? | x2 |
| **Fit de persona** | combina com a voz/POV da Hani? | x2 |

`prioridade = 3*univ + 3*gancho + 2*demanda + 2*fit` (máx 50).

Regra de corte: prioriza **alta universalidade + gancho forte + competição média**.
Trend só entra se der pra resolver num insight comportamental atemporal (senão é
conteúdo descartável). Vídeo react de caso puramente local fica de fora.

## O ritual semanal (30-45 min)

1. **Minerar** (10 min): rodar `python ferramentas/minerar-pautas.py` + dar uma
   passada em 2-3 subreddits + Google Trends. Jogar 8-12 candidatos crus no backlog.
2. **Pontuar** (10 min): dar as 4 notas em cada candidato novo.
3. **Selecionar** (5 min): pegar os 2 de maior prioridade pra semana (1 evergreen +
   1 trend-com-gancho). Mover status pra "produzir".
4. **Escrever o gancho** (10 min): pra cada um, rascunhar o "Have you ever noticed..."
   — se não sai um gancho forte, a pauta volta pro backlog.

O backlog nunca esvazia: o catálogo da Cá sozinho já dá ~150 candidatos evergreen
pré-validados. O radar de trend só tempera.
