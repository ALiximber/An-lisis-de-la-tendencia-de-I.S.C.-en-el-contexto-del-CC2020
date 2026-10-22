"""Descarga las fuentes del bloque 3 y extrae texto (PDF con PyMuPDF; HTML a texto y tablas)."""
from pathlib import Path
import sys, json, re, html, concurrent.futures
BASE = Path(__file__).resolve().parent
sys.path.append(str(BASE / ".researchdeps"))
import requests, urllib3, fitz
urllib3.disable_warnings()
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126 Safari/537.36"}
OUT = BASE / "fuentes_bloque_03"
OUT.mkdir(exist_ok=True)

def limpiar(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()

def bajar(item):
    id_, url = item[0], item[1]
    try:
        r = requests.get(url, headers=UA, timeout=60, verify=False)
        data = r.content
        if data[:4] == b"%PDF":
            (OUT / f"{id_}.pdf").write_bytes(data)
            d = fitz.open(stream=data, filetype="pdf")
            txt = "\n".join(f"\n--- PAGINA {i+1} ---\n" + p.get_text(sort=True) for i, p in enumerate(d))
            (OUT / f"{id_}.txt").write_text(txt, encoding="utf-8")
            return [id_, "pdf", len(d), len(txt)]
        s = data.decode(r.encoding or "utf-8", errors="replace")
        if "Ã" in s[:5000]:
            s = data.decode("utf-8", errors="replace")
        (OUT / f"{id_}.html").write_text(s, encoding="utf-8")
        (OUT / f"{id_}.txt").write_text(limpiar(s), encoding="utf-8")
        tablas = [[[limpiar(c) for c in re.findall(r"<t[dh]\b[^>]*>(.*?)</t[dh]>", tr, re.S | re.I)]
                   for tr in re.findall(r"<tr\b.*?</tr>", t, re.S | re.I)]
                  for t in re.findall(r"<table\b.*?</table>", s, re.S | re.I)]
        (OUT / f"{id_}_tables.json").write_text(json.dumps(tablas, ensure_ascii=False, indent=1), encoding="utf-8")
        return [id_, "html", r.status_code, len(tablas), len(limpiar(s))]
    except Exception as e:
        return [id_, "ERROR", str(e)[:120]]

if __name__ == "__main__":
    items = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        for out in pool.map(bajar, items):
            print(json.dumps(out, ensure_ascii=False), flush=True)
