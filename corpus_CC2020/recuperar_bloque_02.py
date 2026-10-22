from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent / '.deps'))
import json,concurrent.futures,io,urllib.request,re,html
from pypdf import PdfReader
BASE=Path(__file__).resolve().parent
OUT=BASE/"fuentes_bloque_02"
OUT.mkdir(exist_ok=True)
def fetch(item):
    id,url=item
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'}),timeout=40) as r:
            data=r.read()
        if data.startswith(b"%PDF"):
            (OUT/(id+".pdf")).write_bytes(data)
            reader=PdfReader(io.BytesIO(data))
            text="\n".join(f"\n--- PAGINA {i+1} ---\n"+(p.extract_text(extraction_mode="layout") or "") for i,p in enumerate(reader.pages))
            (OUT/(id+".txt")).write_text(text,encoding="utf-8")
            return [id,"pdf",len(reader.pages),len(text)]
        s=data.decode('utf-8',errors='replace')
        def clean(s):return re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>',' ',s))).strip()
        (OUT/(id+".html")).write_text(s,encoding="utf-8")
        (OUT/(id+".txt")).write_text(clean(s),encoding="utf-8")
        tables=[[[clean(c) for c in re.findall(r'<t[dh]\b[^>]*>(.*?)</t[dh]>',tr,re.S|re.I)] for tr in re.findall(r'<tr\b.*?</tr>',t,re.S|re.I)] for t in re.findall(r'<table\b.*?</table>',s,re.S|re.I)]
        (OUT/(id+"_tables.json")).write_text(json.dumps(tables,ensure_ascii=False,indent=2),encoding="utf-8")
        links=re.findall(r'(?:href|src)="([^"]+)"',s)
        links=[l for l in links if '.pdf' in l or 'drive.google' in l]
        return [id,"html",len(tables),links]
    except Exception as e:return [id,"ERROR",str(e)]
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
    for out in pool.map(fetch,json.loads((BASE/"bloque_02_fuentes.json").read_text(encoding="utf-8"))):
        print(json.dumps(out,ensure_ascii=False))

