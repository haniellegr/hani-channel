#!/usr/bin/env python3
"""Limpa auto-legendas .vtt do YouTube em texto corrido (UTF-8).

A auto-legenda do YouTube vem com timestamps por palavra e a "repeticao
rolante" (cada linha aparece 2x conforme a legenda sobe). Aqui a gente tira as
tags <...>, descarta linhas de tempo/cabecalho e remove a repeticao consecutiva.

Uso:
  python limpar_vtt.py <arquivo.vtt> <saida.txt>     # um arquivo
  python limpar_vtt.py --lote <dir_vtt> <dir_txt>    # todos os .vtt da pasta
"""
import re
import sys
import os
import glob


def limpar(path: str) -> str:
    out, prev = [], None
    with open(path, encoding="utf-8") as f:
        for ln in f:
            ln = ln.rstrip("\n")
            if "-->" in ln or ln == "WEBVTT" or ln.startswith(("Kind:", "Language:")):
                continue
            ln = re.sub(r"<[^>]+>", "", ln).strip()  # tira <c>/<timestamp>
            if not ln or ln == prev:                  # vazio ou repeticao
                continue
            out.append(ln)
            prev = ln
    return " ".join(out)


def main() -> None:
    args = sys.argv[1:]
    if args and args[0] == "--lote":
        dir_vtt, dir_txt = args[1], args[2]
        os.makedirs(dir_txt, exist_ok=True)
        n = 0
        for vtt in sorted(glob.glob(os.path.join(dir_vtt, "*.vtt"))):
            vid = os.path.basename(vtt).split(".")[0]
            with open(os.path.join(dir_txt, vid + ".txt"), "w", encoding="utf-8") as o:
                o.write(limpar(vtt))
            n += 1
        print(f"{n} transcricoes limpas -> {dir_txt}")
    else:
        vtt, saida = args[0], args[1]
        with open(saida, "w", encoding="utf-8") as o:
            o.write(limpar(vtt))


if __name__ == "__main__":
    main()
