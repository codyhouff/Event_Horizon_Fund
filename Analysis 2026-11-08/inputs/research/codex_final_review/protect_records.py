"""Hash immutable cycle inputs; verify no Step 1-5 file changed during review."""
import hashlib
import json
from pathlib import Path
import sys

here = Path(__file__).resolve().parent
inputs = here.parents[1]
manifest = here/'data/protected_records.json'
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
if not manifest.exists():
    records = {str(p.relative_to(inputs)).replace('\\','/'):digest(p)
        for p in inputs.rglob('*') if p.is_file() and here not in p.parents
        and not p.name.startswith('Step 6 Review Log') and '__pycache__' not in p.parts}
    manifest.write_text(json.dumps(records,indent=2)+'\n',encoding='utf-8')
    print(f'Protected {len(records)} existing input files.')
else:
    records = json.loads(manifest.read_text())
    changed = [k for k,v in records.items() if not (inputs/k).exists() or digest(inputs/k)!=v]
    print(json.dumps(dict(checked=len(records),changed=changed)))
    sys.exit(bool(changed))
