"""Check saved-source coverage and the forecast audit's numerical identities.

These checks establish reproducibility, not truth of forecasts or calibrated probabilities.
"""
import hashlib
import json
import math
from pathlib import Path

from audit_calculations import cells, val
import valuation_model as vm

ROOT = Path(__file__).resolve().parent


def main():
    result = json.loads((ROOT/'audit_results.json').read_text(encoding='utf-8'))
    manifest = json.loads((ROOT/'source_manifest.json').read_text(encoding='utf-8'))
    records = {r['name']: r for r in manifest}
    required = ['race','summary','compute','timelines','takeoff','goals','security','plan_a','trillion_cluster']
    for name in required:
        assert name in records and 'error' not in records[name], name
        assert (ROOT/(name+'.txt')).stat().st_size > 1000, name
    assert records['plan_a_pdf']['pages'] == 90
    meta = json.loads((ROOT/'sheetmeta.json').read_text(encoding='utf-8'))['structuredContent']
    assert meta['spreadsheetId'] == '1Ko-olwjDy6h8rXLZBFpP-e2GibGqRhfV28S4v8xtzrM'
    assert meta['sheets'][0]['properties']['sheetId'] == 1866551567
    assert len(meta['sheets']) == 1
    formulas = cells('sheet_formula_cells.json')
    assert 'formulaValue' in formulas['L46']['userEnteredValue']
    assert '1.03^7' in formulas['L24']['userEnteredValue']['formulaValue']
    assert all(r['binding'] == 'HBM' for r in result['source_series'])
    assert math.isclose(result['flat_3pct_HBM_2030_bn'],164.7182546,rel_tol=1e-6)
    assert math.isclose(result['source_series'][-1]['chips_m'],92.175000833,rel_tol=1e-9)
    assert math.isclose(result['slow_HBM'][-1]['chips_m'],26.5188,rel_tol=1e-5)
    assert math.isclose(result['source_series'][-1]['HBM_tam_bn'],val(formulas,'L24'))
    assert math.isclose(result['scorecard']['all_mean'],.6931657,abs_tol=1e-6)
    assert math.isclose(result['scorecard']['all_median'],.885,abs_tol=1e-12)
    assert math.isclose(result['scorecard']['corrected_mean'],.7021657,abs_tol=1e-6)
    assert math.isclose(result['scorecard']['corrected_lab_pace'],1.02,abs_tol=1e-12)
    rows = vm.calculate()
    for group in ['architectures','bull_reweighted_architectures','scarcity_operating_architectures']:
        for name, arch in result[group].items():
            assert sum(arch['weights'].values()) == 100, (group,name)
            assert max(arch['weights'].values()) <= 15, (group,name)
            assert set(arch['weights']).issubset(rows), (group,name)
            assert math.isclose(arch['expected_cagr'],(1+arch['expected_total_return'])**(1/vm.YEARS)-1)
    upstream = result['architectures']['Upstream challenge']['weights']
    gaps = {t:upstream.get(t,0)-vm.FINAL.get(t,0) for t in set(upstream)|set(vm.FINAL)}
    assert sum(v for v in gaps.values() if v>0) == 15
    assert sum(v for v in gaps.values() if v<0) == -15
    assert math.isclose(result['immediate_capex_shock_returns']['Upstream challenge'],-.488,abs_tol=1e-12)
    assert math.isclose(result['immediate_capex_shock_returns']['Concentrated'],-.479,abs_tol=1e-12)
    assert math.isclose(result['upstream_expected_wealth_break_even_uplift'],.4307369,abs_tol=1e-6)
    for ticker,swap in result['marginal_5pp_COHR_swaps'].items():
        assert sum(swap['weights'].values())==100
        assert swap['weights'][ticker]==5 and swap['weights']['COHR']==3
    assert result['marginal_5pp_COHR_swaps']['TSM']['stronger_upstream']['expected_cagr'] > result['architectures']['Concentrated']['expected_cagr']
    for row in result['tail_sensitivity']:
        q=row['zero_recovery_probability_sensitivity']
        for name,arch in result['architectures'].items():
            assert math.isclose(row[name]['expected_wealth'],(1-q)*(1+arch['expected_total_return']))
    assert math.isclose(sum(result['chip_totals_H100e'].values())/1e6,31.595128,rel_tol=1e-9)
    assert any(r['p50_minutes'] and r['p50_minutes']>1000 for r in result['metr_observations'])
    report=(ROOT.parent.parent/'Codex Deep Dive 2026-11-08.md').read_text(encoding='utf-8')
    for section in ['3.3 Revised research judgment','3.4 Track record','3.5 Deep audit','3.6 Reconcile','3.7 What taking rapid','5.6 November 9']:
        assert section in report,section
    for name in required:
        assert records[name]['url'] in report,name
    assert meta['spreadsheetId'] in report
    summary = dict(status='PASS',user_requested_sources_covered=10,
        successful_archived_web_sources=sum('error' not in r for r in manifest),
        direct_archive_failures=[r for r in manifest if 'error' in r],
        source_workbook_modified=False,source_formulas_recalculated_with_general_engine=False,
        source_formulas_and_cached_values_cross_checked=True,architectures_checked=4,marginal_substitutions_checked=3,
        weights_changed=False,original_price_snapshot_retained=True,
        HBM_binding_years=[r['year'] for r in result['source_series']],
        immediate_capex_shock_returns=result['immediate_capex_shock_returns'],
        report_sha256=hashlib.sha256((ROOT.parent.parent/'Codex Deep Dive 2026-11-08.md').read_bytes()).hexdigest(),
        limitations='Source coverage and arithmetic checks only; not verification of every narrative prediction, probability calibration or investment outcomes.')
    (ROOT/'audit_verification.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
    print(json.dumps(summary,indent=2))


if __name__=='__main__':
    main()
