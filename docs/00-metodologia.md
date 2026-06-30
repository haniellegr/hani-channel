# 00 — Metodologia do mapeamento

Como a gente extrai a "assinatura" de um canal sem chutar nada: dados reais,
em duas camadas.

## Camada 1 — Metadados (o esqueleto)

O que dá pra ler sem assistir nada:

- **Índice de vídeos**: `yt-dlp --flat-playlist` enumera todos os ~157 vídeos
  (id + título original em PT). Saída em `dados/videos-index.txt`.
- **Performance**: o feed RSS do canal
  (`youtube.com/feeds/videos.xml?channel_id=...`) entrega título, data e contagem
  de views dos vídeos recentes — isso revela cadência e quais temas viram breakout.
- **Posicionamento**: tags/keywords do canal e bio do Instagram (quem é, tom, promessa).

Disso sai o **mapa do canal** (`01-mapeamento-canal.md`): pilares de conteúdo,
fórmulas de título, séries recorrentes, ritmo de publicação e a curva de audiência.

## Camada 2 — Transcrições (a voz e a retórica)

O esqueleto não revela COMO ela fala. Pra isso a gente precisa do texto real dos
vídeos. A pergunta central foi: *como extrair a transcrição de 100+ vídeos sem
gastar uma fortuna transcrevendo?*

**Resposta: não transcrever do zero. Puxar a legenda automática que o YouTube já gera.**

Cada vídeo dela tem três faixas de legenda automática: `pt-orig` (português
original — o que ela realmente fala), `pt` e `pt-PT`. A `pt-orig` é a que importa.

### O pipeline

1. **Baixar a `pt-orig` de cada vídeo** com `yt-dlp` (um idioma só = uma requisição
   por vídeo). Resumível (pula o que já tem) e com throttle (`--retries`,
   `--retry-sleep`, `sleep` entre vídeos) porque o YouTube responde **HTTP 429
   (Too Many Requests)** se você pede rápido demais em lote.

2. **Limpar o `.vtt`**: a legenda vem com timestamp por palavra e "repetição
   rolante" (cada linha aparece duas vezes conforme a legenda sobe). O
   `limpar_vtt.py` remove as tags `<...>`, descarta linhas de tempo/cabeçalho e
   tira a repetição consecutiva — sobra texto corrido limpo.

Tudo isso está em `ferramentas/extrair-transcricoes.sh`. Rendimento de referência:
um vídeo de ~24 min vira ~2.900 palavras de texto limpo. 157 vídeos ≈ **450 mil
palavras** do conteúdo real dela.

### Por que não Whisper / AssemblyAI?

Transcrição por IA (Whisper, AssemblyAI) custa tempo e dinheiro e só faz sentido
quando **não existe legenda**. Como o canal tem auto-legenda em todos os vídeos,
ela fica só de **fallback** para algum vídeo eventual sem legenda.

### Limites e cuidados

- Auto-legenda erra pontuação e alguns nomes próprios. Pra extrair voz, estrutura
  e vocabulário (que é o objetivo), isso é irrelevante.
- O uso é **pesquisa de formato/estilo** — a gente extrai a *estrutura* e a *voz*,
  nunca copia roteiro. Formato não é protegido; roteiro específico é.

## O que sai disso

A Camada 2 vira `02-dna-e-estrutura.md`: ganchos de abertura, como ela constrói o
argumento, bordões e vocabulário recorrente, ritmo e o fechamento típico — a parte
realmente transferível pro canal em inglês.
