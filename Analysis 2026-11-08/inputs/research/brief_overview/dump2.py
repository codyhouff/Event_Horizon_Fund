import sys, zipfile, re, xml.etree.ElementTree as ET
sys.stdout.reconfigure(encoding="utf-8")
ns={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
z=zipfile.ZipFile(sys.argv[1])
print(z.namelist())
ss=[]
if 'xl/sharedStrings.xml' in z.namelist():
    for si in ET.fromstring(z.read('xl/sharedStrings.xml')).findall('m:si',ns):
        ss.append(''.join(t.text or '' for t in si.iter('{%s}t'%ns['m'])))
wb=ET.fromstring(z.read('xl/workbook.xml'))
rels=ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))
rmap={r.get('Id'):r.get('Target') for r in rels}
for sh in wb.find('m:sheets',ns):
    name=sh.get('name'); rid=sh.get('{%s}id'%ns['r']); tgt=rmap[rid].lstrip('/')
    if not tgt.startswith('xl/'): tgt='xl/'+tgt
    print('=== TAB:',name,tgt)
    root=ET.fromstring(z.read(tgt))
    for row in root.iter('{%s}row'%ns['m']):
        out=[]
        for c in row.findall('m:c',ns):
            t=c.get('t'); v=c.find('m:v',ns); f=c.find('m:f',ns)
            val=None
            if t=='s' and v is not None: val=ss[int(v.text)]
            elif t=='inlineStr':
                val=''.join(x.text or '' for x in c.iter('{%s}t'%ns['m']))
            elif v is not None:
                val=v.text
                try:
                    fv=float(val); val=f"{fv:.6g}"
                except: pass
            if val is None and f is None: continue
            s=f"{c.get('r')}={val}"
            if f is not None and f.text: s+=f" [={f.text[:70]}]"
            out.append(s)
        if out: print(' | '.join(out))
