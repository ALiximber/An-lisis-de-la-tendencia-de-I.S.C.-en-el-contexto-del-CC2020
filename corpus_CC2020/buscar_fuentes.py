"""Utilidades de búsqueda y descarga para el bloque 3 (usa las dependencias ya instaladas)."""
from pathlib import Path
import sys, re, html, urllib.parse
BASE = Path(__file__).resolve().parent
sys.path.append(str(BASE / ".researchdeps"))
import requests, urllib3
urllib3.disable_warnings()
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126 Safari/537.36",
      "Accept-Language": "es-MX,es;q=0.9,en;q=0.5"}

def _real(u):
    import base64
    u = html.unescape(u)
    m = re.search(r"[?&]u=a1([^&]+)", u)
    if not m:
        return u
    s = urllib.parse.unquote(m[1])
    s += "=" * (-len(s) % 4)
    try:
        return base64.urlsafe_b64decode(s).decode("utf-8")
    except Exception:
        return u

def buscar(q, n=8):
    r = requests.get("https://www.bing.com/search", params={"q": q, "setlang": "es", "cc": "MX"}, headers=UA, timeout=30)
    out = []
    for m in re.finditer(r'<h2[^>]*><a[^>]*href="([^"]+)"[^>]*>(.*?)</a></h2>', r.text, re.S):
        t = html.unescape(re.sub(r"<[^>]+>", "", m[2]))
        out.append((_real(m[1]), t))
    return out[:n]

if __name__ == "__main__":
    for q in sys.argv[1:]:
        print("##", q)
        for u, t in buscar(q):
            print("  ", u, "|", t[:90])
