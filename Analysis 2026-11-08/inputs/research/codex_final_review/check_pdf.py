"""Check generated PDF page bounds and capture representative pages for review."""
import json
from pathlib import Path
import pypdfium2 as pdfium

here=Path(__file__).resolve().parent
cycle=here.parents[2]
paths=[cycle/'Event Horizon Fund Analysis 2026-11-08.pdf',cycle/'Deployment Strategy/Deployment Strategy 2026-11-08.pdf',cycle/'inputs/Step 6 Review Log 2026-11-08.pdf',cycle.parent/'README.pdf']
result=[]
for p in paths:
    if not p.exists(): continue
    doc=pdfium.PdfDocument(str(p)); bad=[]; targets=[]
    for i,page in enumerate(doc):
        tp=page.get_textpage(); width,height=page.get_size()
        outside=[]
        for j in range(tp.count_chars()):
            b=tp.get_charbox(j)
            if b[0]<-1 or b[2]>width+1 or b[1]<-1 or b[3]>height+1:
                outside.append(j)
        if outside: bad.append({'page':i+1,'chars_outside':len(outside),'first_index':outside[0]})
        text=tp.get_text_range()
        normal=' '.join(text.split())
        if any(v in normal for v in ['Weights by source','Every portfolio on the same','Zero-Based Ranking','Decision audit:','T1: fund']):
            targets.extend([i,min(i+1,len(doc)-1)])
    for i in list(dict.fromkeys([0,*targets]))[:9]:
        doc[i].render(scale=1.5).to_pil().save(here/'data'/f'preview_{p.stem[:15].replace(" ","_")}_{i+1}.png')
    result.append({'file':str(p),'pages':len(doc),'out_of_bounds':bad,'target_pages':[i+1 for i in targets]})
(here/'data/pdf_validation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
