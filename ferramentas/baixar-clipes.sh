#!/usr/bin/env bash
# Baixa clipes (TikTok, Instagram, YouTube...) pra usar como ilustracao/evidencia
# nos videos. Recebe uma lista de URLs (uma por linha) e salva os .mp4 numa pasta
# do video. O nome do arquivo ja inclui o autor (credito/atribuicao embutida).
#
# yt-dlp pega o TikTok normalmente SEM marca d'agua.
# NAO commitar os clipes no repo (copyright + peso) — dados/clipes/ esta no .gitignore.
#
# Uso:
#   bash ferramentas/baixar-clipes.sh <pasta-destino> <arquivo-urls.txt>
#   bash ferramentas/baixar-clipes.sh dados/clipes/meu-video urls.txt
set -u
DEST="${1:?uso: baixar-clipes.sh <pasta-destino> <arquivo-urls.txt>}"
URLS="${2:?informe o arquivo com as URLs (uma por linha)}"
mkdir -p "$DEST"

ok=0; falha=0
while read -r url; do
  [ -z "$url" ] && continue
  case "$url" in \#*) continue ;; esac   # ignora linhas comentadas
  if yt-dlp --no-warnings --retries 3 \
       -o "$DEST/%(uploader)s_%(id)s.%(ext)s" "$url"; then
    ok=$((ok+1)); echo "ok    $url"
  else
    falha=$((falha+1)); echo "FALHA $url"
  fi
  sleep 1
done < "$URLS"
echo "baixados: $ok | falhas: $falha | pasta: $DEST"
