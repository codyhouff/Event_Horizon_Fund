"""Read-only source audit and portfolio sensitivities. Does not modify source workbooks.

All counterfactuals are analyst tests, not corrections endorsed by source authors.
Run after the saved native Sheets snapshots and valuation_model.py are available.
"""
import copy
import csv
import json
import math
import re
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent))
import valuation_model as vm


def cells(filename):
    result = json.loads((ROOT / filename).read_text(encoding='utf-8'))
    out = {}
    for sheet in result['structuredContent']['sheets']:
        for block in sheet.get('data', []):
            for r, row in enumerate(block.get('rowData', []), block.get('startRow', 0)+1):
                for c, cell in enumerate(row.get('values', []), block.get('startColumn', 0)):
                    col = chr(65+c)  # inspected ranges end before AA
                    out[f'{col}{r}'] = cell
    return out


def val(data, address):
    value = data[address].get('effectiveValue', {})
    return value.get('numberValue', value.get('stringValue'))


def main():
    source = cells('sheet_formula_cells.json')
    series = []
    cohort_kw = 0
    for year, col in zip(range(2023, 2031), 'EFGHIJKL'):
        v = lambda row: val(source, f'{col}{row}')
        cohort_kw += v(46) * v(52) / 1000
        caps = {'packaging_double_share': v(37)*v(36), 'packaging_single_share': v(37),
                'HBM': v(22)*v(23), 'logic': v(12)*v(13)}
        series.append(dict(year=year, chips_m=v(46)/1e6, chip_tam_bn=v(47),
            HBM_tam_bn=v(24), HBM_wafers_m=v(18)/1e6,
            HBM_capacity_m=caps['HBM']/1e6, packaging_double_m=caps['packaging_double_share']/1e6,
            packaging_single_m=caps['packaging_single_share']/1e6, logic_m=caps['logic']/1e6,
            binding=min((k for k in caps if k!='packaging_single_share'),key=caps.get),
            H100e_stock_m=v(51)/3.1e7/1e15/1e6, source_stock_power_GW=v(54)/1e6,
            cohort_IT_peak_GW=cohort_kw/1e6, leading_edge_wafer_share=v(15),
            training_GW=v(71)/1e6, palo_verde_units=v(75),
            flow_FLOPs_per_dollar=v(49)/(v(47)*1e9)))
    # Keep 2024 HBM market size/quantity, change only 2025-30 price growth to 3%/yr.
    flat_hbm = val(source,'F24') * val(source,'L22')/val(source,'F22') * 1.03**6
    # 50% smaller HBM wafer expansion than the workbook: 1.3x instead of 1.6x.
    slow_hbm = []
    for year, col in zip(range(2024,2031),'FGHIJKL'):
        ratio=(1.3/1.6)**(year-2024)
        chips=min(val(source,f'{col}37')*val(source,f'{col}36'),
                  val(source,f'{col}22')*val(source,f'{col}23')*ratio,
                  val(source,f'{col}12')*val(source,f'{col}13'))
        slow_hbm.append(dict(year=year, chips_m=chips/1e6, ratio_to_original=chips/val(source,f'{col}46')))

    graded=cells('august_scorecard_cells.json')
    # Review dormant displayed-value typo and an active interpolation exponent discrepancy.
    original_lab_pace=val(graded,'C12')
    revised_date=round(2026.33+round(4*math.log(3e27/2.2e27)/math.log(3.2e27/2.2e27),2)/12,2)
    revised_pace=round((revised_date-2025.25)/(val(graded,'G12')-2025.25),2)
    cats=[statistics.mean([val(graded,'C3'),val(graded,'C4')]),
          statistics.mean([val(graded,'C5'),val(graded,'C6')]),
          statistics.mean([val(graded,'C7'),val(graded,'C8')]),
          statistics.mean([val(graded,f'C{r}') for r in range(9,13)]),val(graded,'C13')]
    fixedcats=cats.copy(); fixedcats[3]+=(revised_pace-original_lab_pace)/4

    rows=vm.calculate()
    upstream=dict(NVDA=15,AVGO=15,VRT=15,CLS=12,NVT=9,NRG=8,VST=7,COHR=4,TSM=5,MU=5,ASML=5)
    architectures={name:vm.architecture(weights,rows) for name,weights in
                   [('Current',vm.BASELINE),('Concentrated',vm.FINAL),('Core-satellite',vm.CORE),('Upstream challenge',upstream)]}
    shocks=dict(NVDA=-.50,AVGO=-.45,VRT=-.55,CLS=-.60,NVT=-.40,NRG=-.35,VST=-.40,COHR=-.60,
        TSM=-.45,ASML=-.45,AMAT=-.45,GEV=-.45,MU=-.60,SNPS=-.30,CCJ=-.30,MSFT=-.30,
        ANET=-.50,DELL=-.50,INTC=-.50,CEG=-.35,PWR=-.35,CRWD=-.25,GOOGL=-.25,
        PLTR=-.40,MP=-.40,AVAV=-.15,KTOS=-.20,MRNA=-.05,BE=-.60)
    shock_returns={n:sum(w/100*shocks[t] for t,w in a['weights'].items()) for n,a in architectures.items()}
    bullish=copy.deepcopy(rows)
    for item in bullish.values():
        # Identical 50% bull weight; preserve half original bear weight; base is residual.
        p=[item['probabilities'][0]/2, .5-item['probabilities'][0]/2, .5]
        item['probabilities']=p
        item['expected_terminal']=sum(x*y for x,y in zip(item['terminal_values'],p))
    bull_arch={n:vm.architecture(a['weights'],bullish) for n,a in architectures.items()}
    upstream_wealth=sum(upstream[t]/100*rows[t]['expected_terminal']/rows[t]['price'] for t in ['TSM','MU','ASML'])
    upstream_break_even=(architectures['Concentrated']['expected_total_return']-architectures['Upstream challenge']['expected_total_return'])/upstream_wealth
    # Targeted operating stress, not adopted earnings forecasts: stronger upstream rents only.
    scarcity=copy.deepcopy(rows)
    for t,revs,margins in [('TSM',[140,370,520],[.32,.47,.49]),
                         ('MU',[120,280,450],[.20,.42,.50]),
                         ('ASML',[40,90,130],[.24,.37,.40])]:
        a=scarcity[t];a['revenue']=revs;a['margin']=margins
        a['terminal_values']=[revs[i]*margins[i]/a['shares'][i]*a['multiple'][i]+a['dividends'][i]+a['excess_cash_per_share'][i] for i in range(3)]
        a['expected_terminal']=sum(x*y for x,y in zip(a['terminal_values'],a['probabilities']))
    scarcity_arch={n:vm.architecture(a['weights'],scarcity) for n,a in architectures.items()}
    marginal_swaps={}
    for t in ['TSM','MU','ASML']:
        weights=dict(vm.FINAL);weights['COHR']-=5;weights[t]=5
        marginal_swaps[t]=dict(weights=weights,original=vm.architecture(weights,rows),
            stronger_upstream=vm.architecture(weights,scarcity),
            stronger_stock_cagr=(scarcity[t]['expected_terminal']/scarcity[t]['price'])**(1/vm.YEARS)-1)
    hurdle=rows['COHR']['expected_cagr']
    candidates={}
    for t in ['TSM','MU','ASML','LRCX','MSFT','GOOGL']:
        a=rows[t]; b=bullish[t]
        candidates[t]=dict(price=a['price'],expected_cagr=a['expected_cagr'],
            bull_reweighted_cagr=(b['expected_terminal']/b['price'])**(1/vm.YEARS)-1,
            price_for_COHR_cagr=a['expected_terminal']/(1+hurdle)**vm.YEARS,
            expected_wealth_required=a['price']*(1+hurdle)**vm.YEARS,
            expected_wealth_uplift_to_COHR=a['price']*(1+hurdle)**vm.YEARS/a['expected_terminal']-1)
    tail=[]
    for p in [0,.05,.10,.20,.30]:
        entry={'zero_recovery_probability_sensitivity':p}
        for name,a in architectures.items():
            wealth=(1-p)*(1+a['expected_total_return'])
            entry[name]={'expected_wealth':wealth,'cagr':wealth**(1/vm.YEARS)-1}
        tail.append(entry)
    revenue=list(csv.DictReader((ROOT/'epoch_revenue_csv.html').open(encoding='utf-8',newline='')))
    latest=[]
    for company in ['Anthropic','OpenAI']:
        choices=[r for r in revenue if r['Company']==company and r.get('Annualized revenue (USD)')]
        latest.append(sorted(choices,key=lambda r:r['Date'],reverse=True)[0])
    chip_rows=list(csv.DictReader((ROOT/'epoch_chip_timelines_csv.html').open(encoding='utf-8',newline='')))
    chip_totals={}
    for year in range(2022,2027):
        included=[r for r in chip_rows if r['End date'].startswith(str(year)) and r['End date']<='2026-06-30' and r['Incomplete']!='True']
        chip_totals[year]=sum(float(r['Compute estimate in H100e (median)']) for r in included)
    # Compact extraction from the simple nested YAML; no execution or external packages.
    raw_metr=(ROOT/'metr_data.html').read_text(encoding='utf-8')
    metr=[]
    for match in re.finditer(r'^  ([a-zA-Z0-9_]+):\n(.*?)(?=^  [a-zA-Z0-9_]+:|\Z)',raw_metr,re.M|re.S):
        name,body=match.groups()
        release=re.search(r'release_date: ([0-9-]+)',body)
        if not release: continue
        def metric(key):
            value=re.search(key+r':\n.*?estimate: ([0-9.]+)',body,re.S)
            return float(value[1]) if value else None
        metr.append(dict(model=name,release_date=release[1],p50_minutes=metric('p50_horizon_length'),p80_minutes=metric('p80_horizon_length')))
    result=dict(source_series=series, flat_3pct_HBM_2030_bn=flat_hbm, slow_HBM=slow_hbm,
        scorecard=dict(category_means=cats,all_mean=statistics.mean(cats),all_median=statistics.median(cats),
            corrected_lab_pace=revised_pace,corrected_mean=statistics.mean(fixedcats),
            original_lab_pace=original_lab_pace,unused_revenue_display_bn=val(graded,'I7')/1e9,
            normalized_revenue_display_bn=val(graded,'I7')/1e10),
        architectures=architectures,immediate_capex_shock_returns=shock_returns,bull_reweighted_architectures=bull_arch,
        scarcity_operating_architectures=scarcity_arch,marginal_5pp_COHR_swaps=marginal_swaps,
        upstream_expected_wealth_break_even_uplift=upstream_break_even,
        scarcity_operating_inputs={t:{k:scarcity[t][k] for k in ['revenue','margin','terminal_values','expected_terminal']} for t in ['TSM','MU','ASML']},
        challenger_hurdles=candidates,tail_sensitivity=tail,latest_revenue=latest,
        chip_totals_H100e=chip_totals,metr_observations=metr)
    (ROOT/'audit_results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
