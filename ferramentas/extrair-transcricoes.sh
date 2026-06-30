#!/usr/bin/env bash
# Extrai as auto-legendas (pt-orig = portugues original falado) de todos os
# videos do canal e limpa em texto corrido. Sem Whisper, sem custo, resumivel.
#
# Resumivel: pula o que ja baixou. Throttle (sleep + retries) pra driblar o
# HTTP 429 (Too Many Requests) do YouTube em lote.
set -u

CANAL="https://www.youtube.com/@cafernandes_oficial/videos"
IDS="dados/videos-index.txt"
VTT="dados/transcricoes-vtt"
TXT="dados/transcricoes-txt"
mkdir -p "$VTT" "$TXT"

# 1) indice de videos (id|titulo) — so se ainda nao existir
if [ ! -s "$IDS" ]; then
  yt-dlp --flat-playlist --extractor-args "youtube:lang=pt" \
    --print "%(id)s|%(title)s" "$CANAL" > "$IDS"
fi
echo "videos no indice: $(wc -l < "$IDS")"

# 2) baixa a pt-orig de cada video (um idioma so = uma requisicao por video)
ok=0; falha=0
while IFS='|' read -r id titulo; do
  [ -z "$id" ] && continue
  if [ -f "$VTT/$id.pt-orig.vtt" ]; then ok=$((ok+1)); continue; fi
  if yt-dlp --skip-download --write-auto-subs --sub-langs "pt-orig" --sub-format vtt \
       --extractor-args "youtube:lang=pt" --retries 5 --retry-sleep 8 --no-warnings \
       -o "$VTT/%(id)s.%(ext)s" "https://www.youtube.com/watch?v=$id" >/dev/null 2>&1; then
    ok=$((ok+1)); echo "ok    $id  $titulo"
  else
    falha=$((falha+1)); echo "FALHA $id  $titulo"
  fi
  sleep 2
done < "$IDS"
echo "baixados: $ok | falhas: $falha"

# 3) limpa todos os .vtt -> .txt
python ferramentas/limpar_vtt.py --lote "$VTT" "$TXT"
