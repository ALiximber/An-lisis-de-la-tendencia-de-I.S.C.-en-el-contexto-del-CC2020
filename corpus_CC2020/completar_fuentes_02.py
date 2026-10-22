from pathlib import Path
import sys,json,concurrent.futures,io
BASE=Path(__file__).resolve().parent
sys.path.append(str(BASE/".researchdeps"))
import requests,fitz
from bs4 import BeautifulSoup
OUT=BASE/"fuentes_bloque_02"
items=[
("D018","https://ingenieria.mxl.uabc.mx/pe_lsc/wp-content/uploads/2024/04/plan2023-2_lsc.pdf"),
("D024","https://estudios.unad.edu.co/images/2025/mallas-pdf/Plan-de-estudios-Ingenieria-de-sistemas.pdf"),
("D025_plan","https://frvt.utn.edu.ar/wp-content/uploads/2024/07/1877.pdf"),
("D027_plan","https://drive.google.com/uc?export=download&id=1SF0Km-jmwQ-ZZzUl0uvCU1CjDLfeq-Zk"),
("D030","https://mexico.unir.net/ingenieria/licenciatura-ingenieria-sistemas-computacionales/")]
def fetch(item):
    id,url=item
    try:
        r=requests.get(url,timeout=(15,25));r.raise_for_status()
        if r.content.startswith(b"%PDF"):
            (OUT/(id+".pdf")).write_bytes(r.content)
            doc=fitz.open(stream=r.content,filetype="pdf")
            (OUT/(id+".txt")).write_text("\n".join(f"\n--- PAGINA {i+1} ---\n"+p.get_text(sort=True) for i,p in enumerate(doc)),encoding="utf-8")
            return id,len(doc)
        (OUT/(id+".html")).write_text(r.text,encoding="utf-8")
        soup=BeautifulSoup(r.content,"html.parser")
        (OUT/(id+".txt")).write_text(soup.get_text(" ",strip=True),encoding="utf-8")
        tables=[[[c.get_text(" ",strip=True) for c in tr.find_all(["td","th"])] for tr in t.find_all("tr")] for t in soup.find_all("table")]
        (OUT/(id+"_tables.json")).write_text(json.dumps(tables,ensure_ascii=False,indent=2),encoding="utf-8")
        return id,"html",len(tables)
    except Exception as e:return id,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
    for f in concurrent.futures.as_completed([pool.submit(fetch,i) for i in items]):
        print(f.result(),flush=True)
# Render overview of scanned Sonsonate document for identifying target page.
doc=fitz.open(OUT/"D022.pdf")
from PIL import Image,ImageDraw
thumbs=[]
for i,p in enumerate(doc):
    pix=p.get_pixmap(matrix=fitz.Matrix(0.35,0.35))
    im=Image.frombytes("RGB",[pix.width,pix.height],pix.samples)
    im.thumbnail((380,260))
    thumbs.append(im)
canvas=Image.new("RGB",(1520,1200),"white")
draw=ImageDraw.Draw(canvas)
for i,im in enumerate(thumbs):
    x=(i%4)*380;y=(i//4)*300
    draw.text((x,y),str(i+1),fill="black");canvas.paste(im,(x,y+25))
canvas.save(OUT/"D022_contacto.png")

