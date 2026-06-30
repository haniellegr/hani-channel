# hani-channel

Inteligência de canal para o lançamento de um canal de YouTube no estilo
**Cá Fernandes** (reflexão e crítica de comportamento humano), porém em **inglês**,
mirando o público de países falantes de inglês.

Este repositório é o cérebro do projeto: engenharia reversa do canal-referência,
destilação da "assinatura" em elementos transferíveis e o playbook de adaptação
para o novo mercado.

## Objetivo

1. **Mapear** o canal da Cá Fernandes (formato, persona, pilares, ganchos, títulos,
   ritmo e o que move audiência) a partir de dados reais (metadados + transcrições).
2. **Destilar a DNA** em peças reutilizáveis, separando o que é *universal* do que é
   *Brasil-dependente*.
3. **Adaptar** essa DNA para um canal em inglês, com posicionamento próprio.

## Estrutura

```
docs/
  00-metodologia.md        — como o canal é mapeado (incl. extração de transcrições)
  01-mapeamento-canal.md   — o mapa do canal a partir dos metadados (157 vídeos)
  02-dna-e-estrutura.md    — a assinatura destilada das transcrições (voz, retórica)
  03-adaptacao-ingles.md   — playbook de adaptação pro canal em inglês
  04-plano-lancamento.md   — primeiros passos do canal da Hani
  05-engine-de-pautas.md   — mineração e seleção de temas (fontes + scorecard)
  06-workflow-de-producao.md — pipeline por vídeo + footage de terceiros (legal)
ferramentas/
  extrair-transcricoes.sh  — baixa as auto-legendas (pt-orig) do canal todo
  limpar_vtt.py            — converte .vtt em texto corrido limpo
dados/
  videos-index.txt         — índice id|título dos vídeos
  transcricoes-vtt/         — legendas brutas (.vtt)
  transcricoes-txt/         — transcrições limpas (.txt)
```

## Reproduzir a coleta

Pré-requisitos: `yt-dlp` e `python` no PATH.

```bash
bash ferramentas/extrair-transcricoes.sh
```

O script enumera os vídeos do canal, baixa a legenda automática em português
original (`pt-orig`) de cada um — resumível e com throttle para evitar bloqueio —
e gera as transcrições limpas em `dados/transcricoes-txt/`.

## Canal-referência

Cá Fernandes — https://www.youtube.com/@cafernandes_oficial
(142 mil inscritos, ~160 vídeos, formato monólogo reflexivo de 20-25 min).
