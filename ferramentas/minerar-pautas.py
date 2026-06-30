#!/usr/bin/env python3
"""Minera demanda real de busca no YouTube (autocomplete) pra alimentar a pauta.

Sem API key, sem custo. Pra cada "semente" devolve o que as pessoas de fato
digitam no YouTube — ou seja, demanda existente em ingles. As sugestoes boas
viram candidatos no pauta/backlog.csv.

Uso:
  python minerar-pautas.py                         # sementes padrao (comportamento)
  python minerar-pautas.py "why do people" "..."   # sementes proprias
  python minerar-pautas.py --gl gb                 # mercado UK (padrao: us)
"""
import sys
import json
import time
import urllib.request
import urllib.parse

# sementes alinhadas a DNA do canal (gancho de reconhecimento + comportamento)
SEMENTES_PADRAO = [
    "why do people", "why do we", "why are people", "why is everyone",
    "have you ever noticed", "the psychology of", "the truth about",
    "people who", "the type of person who", "the problem with",
    "what nobody tells you about", "the real reason", "signs someone is",
    "how to deal with people who", "why nobody",
]


def sugerir(q: str, gl: str = "us") -> list:
    url = "https://suggestqueries.google.com/complete/search?" + urllib.parse.urlencode(
        {"client": "firefox", "ds": "yt", "hl": "en", "gl": gl, "q": q}
    )
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read().decode("utf-8"))[1]


def main() -> None:
    args = sys.argv[1:]
    gl = "us"
    if "--gl" in args:
        i = args.index("--gl")
        gl = args[i + 1]
        del args[i : i + 2]
    sementes = args or SEMENTES_PADRAO

    vistos = set()
    for s in sementes:
        try:
            sugs = sugerir(s, gl)
        except Exception as e:  # rede / bloqueio
            print(f"# erro em '{s}': {e}", file=sys.stderr)
            continue
        print(f"\n## {s}")
        for x in sugs:
            if x not in vistos and x.strip() != s.strip():
                vistos.add(x)
                print(x)
        time.sleep(0.5)


if __name__ == "__main__":
    main()
