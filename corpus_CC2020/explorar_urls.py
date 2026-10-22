"""Explora páginas candidatas: estado HTTP, título y enlaces que parezcan planes/mallas/PDF."""
from pathlib import Path
import sys, re, html, urllib.parse
BASE = Path(__file__).resolve().parent
sys.path.append(str(BASE / ".researchdeps"))
import requests, urllib3
urllib3.disable_warnings()
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126 Safari/537.36"}
KEY = re.compile(r"plan|malla|reticula|curricul|pdf|creditos|asignatur|programa", re.I)

def explorar(url, mostrar=25):
    try:
        r = requests.get(url, headers=UA, timeout=30, verify=False, allow_redirects=True)
    except Exception as e:
        print("ERR", url, str(e)[:90]); return
    ct = r.headers.get("content-type", "")
    print("==", r.status_code, ct[:30], len(r.content), r.url)
    if "html" not in ct:
        return
    t = re.search(r"<title[^>]*>(.*?)</title>", r.text, re.S | re.I)
    print("   título:", html.unescape(t[1]).strip()[:100] if t else "-")
    seen = set()
    for m in re.finditer(r'<a[^>]+href="([^"#]+)"[^>]*>(.*?)</a>', r.text, re.S | re.I):
        href = urllib.parse.urljoin(r.url, html.unescape(m[1]))
        txt = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", m[2]))).strip()
        if href in seen or not (KEY.search(href) or KEY.search(txt)):
            continue
        seen.add(href)
        if len(seen) <= mostrar:
            print("   -", txt[:60], "|", href[:140])

if __name__ == "__main__":
    for u in (Path(sys.argv[1]).read_text(encoding="utf-8").split() if sys.argv[1].endswith(".txt") else sys.argv[1:]):
        explorar(u)
