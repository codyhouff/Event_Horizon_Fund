"""Insert generated evidence and a diff-derived section inventory using apply_patch."""
import difflib
import json
from pathlib import Path

here=Path(__file__).resolve().parent
cycle=here.parents[2]
path=cycle/'inputs/Step 6 Review Log 2026-11-08.md'
old=path.read_text(encoding='utf-8')
new=old.replace('@@BEFORE_AFTER@@',(here/'tables6/before_after6.md').read_text(encoding='utf-8').strip())
quotes=json.loads((here/'data/quote_audit.json').read_text())
lines=['| Name | Nov 10 observed price | Change vs Nov 9 | >10% flag |','|---|---:|---:|---|']
for k,v in quotes.items():
    lines.append(f'| {k} | ${v["price"]:.2f} | {v["change_percent"]:+.2f}% | {"YES" if abs(v["change_percent"])>10 else "No"} |')
new=new.replace('@@QUOTE_TABLE@@','\n'.join(lines))

def contexts(lines):
    stack={}; result=[]
    for line in lines:
        if line.startswith('#'):
            n=len(line)-len(line.lstrip('#'))
            if n<=4:
                stack={k:v for k,v in stack.items() if k<n}
                stack[n]=line[n:].strip()
        result.append(' → '.join(v for k,v in sorted(stack.items()) if k>=2) or 'Header / process / market-data convention')
    return result

sections={}
for name,current,backup in [
    ('Final analysis',cycle/'Event Horizon Fund Analysis 2026-11-08.md',cycle/'inputs/superseded/Event Horizon Fund Analysis 2026-11-08 (V10.1 before Step 6).md'),
    ('Deployment Strategy',cycle/'Deployment Strategy/Deployment Strategy 2026-11-08.md',cycle/'inputs/superseded/Deployment Strategy/Deployment Strategy 2026-11-08 (V10.1 before Step 6).md')]:
    a=backup.read_text(encoding='utf-8').splitlines(); b=current.read_text(encoding='utf-8').splitlines()
    ctx=contexts(b); changed=[]
    for op,i,j,k,l in difflib.SequenceMatcher(None,a,b).get_opcodes():
        if op=='equal': continue
        for n in range(k,max(k+1,l)):
            value=ctx[min(n,len(ctx)-1)]
            if value not in changed: changed.append(value)
    sections[name]=changed
(here/'data/edited_sections.json').write_text(json.dumps(sections,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
lines=[]
for name,changed in sections.items():
    lines+=['### '+name,'']+[f'- {s}' for s in changed]+['']
lines+=['### README','', '- Active version / Read This First; Current Allocation Snapshot; Sleeve Rollup; Synthesis Log; File Structure. The analysis-flow instructions and background-reading links are unchanged.']
if '@@SECTION_DIFF@@' in new:
    new=new.replace('@@SECTION_DIFF@@','\n'.join(lines))
else:
    start=new.index('### Final analysis',new.index('## 6. Sections edited'))
    end=new.index('The edits are confined',start)
    new=new[:start]+'\n'.join(lines)+'\n\n'+new[end:]
diff=list(difflib.unified_diff(old.splitlines(),new.splitlines(),n=3,lineterm=''))[2:]
patch='*** Begin Patch\n*** Update File: '+str(path).replace('\\','/')+'\n'+'\n'.join('@@' if x.startswith('@@') else x for x in diff)+'\n*** End Patch'
print(json.dumps({'patch':patch},ensure_ascii=False))
