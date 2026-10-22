from pathlib import Path
import sys,json,re
BASE=Path(__file__).resolve().parent
sys.path.append(str(BASE/".researchdeps"))
from bs4 import BeautifulSoup
import fitz,requests
SRC=BASE/"fuentes_bloque_02"
raw={}
def add(id,name,w,code="",cond="Obligatoria",loc=""):
    raw.setdefault(id,[]).append(dict(Asignatura=name,Peso=float(w),Codigo=code,Condicion=cond,Localizador=loc))
# HTML UDLAP
soup=BeautifulSoup((SRC/"D016.html").read_text(encoding="utf-8"),"html.parser")
for s in soup.select("section.semestre"):
    vals=[d.get_text(" ",strip=True) for d in s.select(".gridplanestudios > div")]
    for i in range(6,len(vals)-5,6):
        code,name,req,hd,hi,cr=vals[i:i+6]
        if code=="Total":continue
        if cr.replace(".","",1).isdigit():
            add("D016",name,cr,code,"Optativa" if "Optativa" in name else "Obligatoria",s.get("id"))
# UPN layout exact code + columns
txt=(SRC/"D019.txt").read_text(encoding="utf-8").split("CURSOS ELECTIVOS")[0]
for line in txt.splitlines():
    m=re.match(r"\s*(?:\d+\s+)?([A-Z]{4}\d+[A-Z]?)\s{2,}(.+?)\s{2,}(\d+)\s+\d+\s+\d+\s+\d+\s+\d+",line)
    if m:add("D019",m[2],m[3],m[1],loc="p. 1")
for i in (1,2):add("D019","ELECTIVO "+str(i),2,cond="Optativa",loc="p. 1")
# Callao left column only
txt=(SRC/"D023.txt").read_text(encoding="utf-8")
p=0
for line in txt.splitlines():
    if "--- PAGINA" in line:p+=1
    m=re.match(r"\s*(ISE[A-Z]\d+)\s{2,}(.+?)\s{2,}(\d+)\s+(Obligatorio|Electivo)",line)
    if m:add("D023",m[2],m[3],m[1],m[4],f"p. {p}")
# UNLPam table rows names and hours
tables=json.loads((SRC/"D026_tables.json").read_text(encoding="utf-8"))
for t in tables:
    for row in t:
        if len(row)>=2 and re.fullmatch(r"\d+",row[1]):
            add("D026",row[0],row[1],loc="tabla del plan 2023")
# Unillanos
tables=json.loads((SRC/"D028_tables.json").read_text(encoding="utf-8"))
for t in tables:
    for row in t:
        if len(row)>=6 and re.fullmatch(r"\d{6}",row[0]):
            add("D028",row[1],row[5].replace(",","."),row[0],
                "Optativa" if "ELECTIVA" in row[1] or "PROFUNDIZACIÓN" in row[1] else "Obligatoria","plan PIS 603 2018-I")
(BASE/"bloque_02_asignaturas_base.json").write_text(json.dumps(raw,ensure_ascii=False,indent=2),encoding="utf-8")
for k,items in raw.items():
    print(k,len(items),sum(x["Peso"] for x in items))
    for x in items:print(x["Asignatura"],"|",x["Peso"],"|",x["Condicion"])
# Render needed sources
for id,pages in {"D017":[0],"D019":[0],"D020":[0],"D021":[0],"D029":[0]}.items():
    d=fitz.open(SRC/(id+".pdf"))
    for p in pages:
        d[p].get_pixmap(matrix=fitz.Matrix(1.4,1.4)).save(SRC/f"{id}_p{p+1}.png")
# Fetch small UNAD, public URL; certificate chain unavailable in environment
r=requests.get("https://estudios.unad.edu.co/images/2025/mallas-pdf/Plan-de-estudios-Ingenieria-de-sistemas.pdf",verify=False,timeout=30)
r.raise_for_status()
(SRC/"D024.pdf").write_bytes(r.content)
d=fitz.open(stream=r.content,filetype="pdf")
(SRC/"D024.txt").write_text("\n".join(p.get_text(sort=True) for p in d),encoding="utf-8")
d[0].get_pixmap(matrix=fitz.Matrix(1.5,1.5)).save(SRC/"D024_p1.png")

