"""Mechanically redact embedded third-party Mapbox tokens from research snapshots.

Never print token contents. Preserve research text and all unrelated bytes.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MAPBOX_TOKEN = re.compile(rb'\b(?:pk|sk)\.[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{10,}')


def redact_mapbox_tokens(raw):
    return MAPBOX_TOKEN.subn(b'[REDACTED_EMBEDDED_MAPBOX_TOKEN]', raw)


def main():
    changed = []
    for path in sorted(ROOT.rglob('*')):
        if not path.is_file() or path.suffix not in {'.html', '.txt', '.json'}:
            continue
        raw = path.read_bytes()
        sanitized, count = redact_mapbox_tokens(raw)
        if count:
            path.write_bytes(sanitized)
            changed.append(dict(file=str(path.relative_to(ROOT)), redactions=count,
                                original_bytes=len(raw), archived_bytes=len(sanitized)))
    if changed:
        manifest_path = ROOT/'source_manifest.json'
        manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
        for record in manifest:
            for change in changed:
                if change['file'] == record['name']+'.html':
                    record['archived_bytes'] = change['archived_bytes']
                    record['embedded_token_redactions'] = change['redactions']
                    record['sanitization_note'] = 'Embedded third-party Mapbox tokens redacted before publication; original response byte count retained in bytes.'
        manifest_path.write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    remaining = sum(len(MAPBOX_TOKEN.findall(p.read_bytes())) for p in ROOT.rglob('*')
                    if p.is_file() and p.suffix in {'.html', '.txt', '.json'})
    assert remaining == 0
    print(json.dumps(dict(changed=changed, remaining_mapbox_tokens=remaining), indent=2))


if __name__ == '__main__':
    main()
