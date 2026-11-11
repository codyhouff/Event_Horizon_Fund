"""Step 6 audit overlay. Run from any directory; never modifies Step 1-5 files.

Reuses the original Step 5 evaluator and Nov 9 snapshot. Only WCC's duplicate
4% SBC deduction is removed; its growth, multiple, probabilities and sensitivity
are retained. Pool order is frozen to Step 5: this is not a new ranking exercise.
"""
import contextlib
import copy
import hashlib
import io
import json
import os
from pathlib import Path
import runpy
import sys

HERE = Path(__file__).resolve().parent
SYN = HERE.parent / 'claude_synthesis'
ROOT = HERE.parents[3]
DATA = HERE / 'data'
TABLES = HERE / 'tables6'
DATA.mkdir(exist_ok=True)
TABLES.mkdir(exist_ok=True)

def dump(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

original = json.loads((SYN / 'data/step5_out.json').read_text())
ports = copy.deepcopy(original['PORTS'])
FINAL_NAME = 'V10.2 final (adopted after Step 6)'
final = dict(NVDA=15, META=15, VRT=14, MU=14, NRG=12, NVT=12, CLS=10, STRL=8)
ports[FINAL_NAME] = final
ports['V10.2 if MOD gate passes'] = dict(final, VRT=11, NVT=10, MOD=5)
ports['V10.2 if Texas impact confirmed'] = dict(final, NRG=8, STRL=3, TLN=9)
ports['V10.2 if NVDA review adverse'] = dict(final, NVDA=8, AVGO=7)
dump(DATA / 'ports6.json', ports)

def evaluate_earnings(ns, k, d):
    x = d['x']; e = d['eps']; s = d['s']
    xm = [0.7*x, 0.85*x, x, 1.2*x]
    dv = d.get('d', [0]*4); c = d.get('c', [0]*4)
    tv = [max(0, e[i]*xm[i]+c[i])+dv[i] for i in range(4)]
    def named(L):
        return max(0, (e[2]+L*s*(e[3]-e[2]))*x+c[2]+L*s*(c[3]-c[2])) + dv[2]+min(L,1)*s*(dv[3]-dv[2])
    return ns['res_from_tvs'](k, tv, d['pr'], named(ns['L27']), named(ns['L100']),
        'Earnings (A1)', d['tag'], d['cl'], s,
        dict(eps=e, mult=[round(v,1) for v in xm], div=dv, cash=c))

all_outputs = []
for suffix, extra in [('', []), ('_cxmult', ['codexmult'])]:
    prior_cwd = Path.cwd()
    try:
        os.chdir(SYN)
        sys.argv = ['step5_model.py', 'data/step5_snap.json',
                    '../codex_initial_deep_dive/valuation_outputs.json',
                    str(DATA / ('reproduced_step5' + suffix + '.json')),
                    (SYN / 'data/ports5.json').read_text(), *extra]
        with contextlib.redirect_stdout(io.StringIO()):
            ns = runpy.run_path(str(SYN / 'step5_model.py'), run_name='__main__')
    finally:
        os.chdir(prior_cwd)
    expected = SYN / ('data/step5_out' + suffix + '.json')
    replica = DATA / ('reproduced_step5' + suffix + '.json')
    assert expected.read_bytes() == replica.read_bytes()
    # Reverse only the demonstrable duplicate factor in the stored rounded EPS.
    # No new growth forecast or restoration of Codex's $44/$65 operating case.
    wcc = copy.deepcopy(ns['E']['WCC'])
    wcc['eps'] = [wcc['eps'][0], *[v/0.96 for v in wcc['eps'][1:]]]
    wcc['tag'] = ('Step 6 correction to D3: remove duplicate 4% SBC from stored '
                  'plateau/base/bull; ordinary SBC already in adjusted EPS. '
                  'Retain Step 5 9% growth judgment, x15, s0.6 and probabilities. '
                  'No verified 2027 mid-high-single-digit company sales guide.')
    ns['R']['WCC'] = evaluate_earnings(ns, 'WCC', wcc)
    for ticker, tag in {
        'AVGO': 'D1: base owner EPS 27; retains 13% owner adjustment and credit reserve; management target is not guaranteed owner EPS.',
        'VRT': 'D2: plateau 7.19 consensus adjusted EPS; ordinary SBC already retained; no extra 0.98 factor.',
        'NVT': 'D2: bust 3.35 and plateau 5.38; ordinary SBC retained; no extra 0.96 factor.',
        'STRL': 'D4: Codex operating bridge; Step 6 weight correction only; all Step 5 valuation inputs unchanged.'
    }.items():
        ns['R'][ticker]['tag'] = tag
    po = {name: ns['port'](weights) for name, weights in ports.items()}
    result = dict(T=ns['T'], L27=ns['L27'], L100=ns['L100'], R=ns['R'], PORTS=ports, PO=po)
    dump(DATA / ('step6_out' + suffix + '.json'), result)
    all_outputs.append(result)
    if not extra:
        sensitivities = {}
        for mult in (14, 12, 10.3):
            d = copy.deepcopy(ns['E']['STRL']); d['x'] = mult
            sensitivities[str(mult)] = evaluate_earnings(ns, 'STRL', d)
        dump(DATA / 'strl_multiple_sensitivity.json', sensitivities)

d, dx = all_outputs
old = original['PO']['V10.1 final (adopted)']; new = d['PO'][FINAL_NAME]
delta = {k: new[k]-old[k] for k in ['E','A27','G100','bust','delay']}
assert delta['E'] >= .1 and delta['A27'] > 0 and delta['bust'] >= -1
for name, weights in ports.items():
    if not name.startswith('V10.2'): continue
    assert sum(weights.values()) == 100 and max(weights.values()) <= 15
    assert weights.get('NRG',0)+weights.get('VST',0)+weights.get('STRL',0) <= 20
    assert weights.get('NRG',0) <= 12 and weights.get('NVT',0) <= 12
    assert weights.get('CLS',0) <= 10 and weights.get('STRL',0) <= 10
    assert d['PO'][name]['clusters'].get('C1',0) <= 50
    assert d['PO'][name]['bust'] > original['PO']['V9.1 baseline']['bust']
dump(DATA / 'rule2_test.json', dict(before=old, after=new, delta_pp=delta,
    passes_rule2=True, valuation_inputs_changed_for_weight_test=False,
    cap_note='Adopted satellite cap 10%; NRG+STRL cap 20%. D4 residual 6% is not a hard cap.'))

# Extend the original table generator in memory. All products go here, not to
# claude_synthesis. The original Step 5 table generator remains byte-for-byte intact.
src = (SYN / 'step5_tables.py').read_text(encoding='utf-8')
src = src.replace('FINAL = P["V10.1 final (adopted)"]', f'FINAL = P[{FINAL_NAME!r}]')
src = src.replace('rank = {k: i for i, k in enumerate(sorted(R, key=lambda k: -R[k]["E"]), 1)}',
    'original_R = json.load(open("data/step5_out.json"))["R"]\nrank = {k: i for i, k in enumerate(sorted(original_R, key=lambda k: -original_R[k]["E"]), 1)}')
src = src.replace('for k in sorted(R, key=lambda k: -R[k]["E"]):', 'for k in sorted(R, key=lambda k: rank[k]):')
src = src.replace('V9.1 → V10.1', 'V9.1 → V10.2').replace('V10.1 target', 'V10.2 target')
src = src.replace('| Rank | Ticker | Bottleneck', '| Step 5 rank | Ticker | Bottleneck')
src = src.replace('**Adopted V10.1 %** |', 'Step 5 V10.1 % | **Step 6 % (V10.2)** |')
src = src.replace('(len(cols) + 3)', '(len(cols) + 4)')
src = src.replace(' | **{FINAL.get(k, 0)}** |', ' | {P[\'V10.1 final (adopted)\'].get(k, 0)} | **{FINAL.get(k, 0)}** |')
src = src.replace(' | **{sum(FINAL.values())}** |', ' | 100 | **{sum(FINAL.values())}** |')
src = src.replace('for n in order:', 'order += [n for n in P if n.startswith("V10.2")]\nfor n in order:')
src = src.replace('n.startswith("V10.1 final")', 'n.startswith("V10.2 final")')
src = src.replace('o = PO["V10.1 final (adopted)"]', f'o = PO[{FINAL_NAME!r}]')
for stem in ['pool','recon','portfolios','trades','destination']:
    src = src.replace(stem+'5.md', stem+'6.md')
src = src.replace('r = R[k]\n    L.append(f"| {k} | {FINAL[k]}%',
    'r = R[k]\n    limit = min(r["etv"] / 1.12 ** T, 315) if k == "STRL" else r["etv"] / 1.12 ** T\n    L.append(f"| {k} | {FINAL[k]}%')
src = src.replace("{r['etv'] / 1.12 ** T:,.0f}", "{limit:,.0f}")
prior_cwd = Path.cwd()
try:
    os.chdir(SYN)
    sys.argv = ['step5_tables.py', str(DATA/'step6_out.json'), str(DATA/'step6_out_cxmult.json'),
                'data/step5_snap.json', str(TABLES), str(DATA)]
    table_ns = {}
    exec(compile(src, 'step6_table_overlay', 'exec'), table_ns)
finally:
    os.chdir(prior_cwd)
dump(DATA/'cash_path.json', table_ns['path'])
dump(DATA/'tranche_ledger.json', {'buys':table_ns['BUY'],'sells':table_ns['SELL'],
    'drift':table_ns['dr'],'targets':final,'turnover':table_ns['buys']})

# Compact authoritative comparison and full numerical valuation rows.
lines = ['| Metric | Step 5 V10.1 | Step 6 V10.2 | Change (pp) |', '|---|---:|---:|---:|']
for label,k in [('Expected CAGR','E'),('AI-2027 Scenario CAGR','A27'),('100GW 2030 Scenario CAGR','G100'),('Bust total return','bust'),('Delay total return','delay')]:
    lines.append(f'| {label} | {old[k]:.4f}% | {new[k]:.4f}% | {delta[k]:+.4f} |')
(TABLES/'before_after6.md').write_text('\n'.join(lines)+'\n', encoding='utf-8')
print(json.dumps({'before_after':delta,'WCC':{k:d['R']['WCC'][k] for k in ['eps','E','A27','G100','bust','delay']},
                  'STRL_sensitivity':{k:v['E'] for k,v in sensitivities.items()}},indent=2))
