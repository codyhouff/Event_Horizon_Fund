"""Capture the public PJM auction schedule without changing model inputs."""
import io
import json
from pathlib import Path
import urllib.request
import zipfile
import xml.etree.ElementTree as ET

url = 'https://www.pjm.com/-/media/DotCom/markets-ops/rpm/rpm-auction-info/rpm-auction-schedule.xlsx'
with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'}),timeout=40) as r:
    raw = r.read()
ns = {'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
book = zipfile.ZipFile(io.BytesIO(raw))
strings = [''.join(x.itertext()) for x in ET.fromstring(book.read('xl/sharedStrings.xml')).findall('s:si',ns)]
rows = {}
for name in book.namelist():
    if not name.startswith('xl/worksheets/sheet') or not name.endswith('.xml'): continue
    sheet_rows = []
    for row in ET.fromstring(book.read(name)).findall('.//s:row',ns):
        vals = []
        for cell in row.findall('s:c',ns):
            val = cell.find('s:v',ns)
            if val is None: continue
            text = strings[int(val.text)] if cell.get('t') == 's' else val.text
            vals.append([cell.get('r'),text])
        if vals: sheet_rows.append(vals)
    rows[name] = sheet_rows
result = dict(url=url, rows=rows)
here = Path(__file__).resolve().parent
(here/'data/pjm_calendar.json').write_text(json.dumps(result,default=str,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,default=str,indent=2))
