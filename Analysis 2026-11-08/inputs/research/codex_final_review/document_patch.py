"""Emit auditable apply_patch text; never write the adopted documents directly."""
import difflib
import json
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
CYCLE = ROOT/'Analysis 2026-11-08'
DATA = json.loads((HERE/'data/step6_out.json').read_text())
PX = json.loads((HERE/'data/step6_out_cxmult.json').read_text())
FINAL = DATA['PO']['V10.2 final (adopted after Step 6)']
W = DATA['PORTS']['V10.2 final (adopted after Step 6)']

def replace(s,a,b):
    assert a in s, f'Missing replacement: {a[:140]}'
    return s.replace(a,b)

def table(s, prefix, filename):
    pattern = re.escape(prefix)+r'[^\n]*\n(?:\|[^\n]*\n)+'
    s,n = re.subn(pattern, f'@@{filename}@@\n',s)
    assert n == 1, (prefix,n)
    return s

def insert_tables(s):
    return re.sub(r'@@(\w+)@@',lambda m:(HERE/'tables6'/f'{m[1]}.md').read_text(encoding='utf-8').rstrip(),s)

def line_replace(s, prefix, text):
    lines=s.splitlines()
    matched=[i for i,line in enumerate(lines) if line.startswith(prefix)]
    assert len(matched)==1,(prefix,matched)
    lines[matched[0]]=text
    return '\n'.join(lines)+'\n'

def block(s,start,end,new):
    i=s.index(start); j=s.index(end,i)
    return s[:i]+new.rstrip()+'\n\n'+s[j:]

def final_doc(s):
    for prefix,fn in [('| Ticker | Rank (of 60)','recon6'),('| Portfolio | Names |','portfolios6'),('| Rank | Ticker | Bottleneck','pool6')]:
        s=table(s,prefix,fn)
    # Generated historical comparison tables are protected from current-version edits.
    s=s.replace('V10.1','V10.2')
    s=replace(s,'**V10.2 (adopted November 10, 2026).**','**V10.2 (adopted after Step 6 review by Codex on November 10, 2026).**')
    s=line_replace(s,'**Status:**','**Status:** **Adopted after Step 6 independent review by Codex.** Claude\'s Step 5 V10.1 and its PDF are preserved in `inputs/superseded/` as "V10.1 before Step 6". The unchanged Step 5 decisions remain in `inputs/Step 5 Decision Log 2026-11-08.md`; verdicts, corrections and the same-model weight test are in `inputs/Step 6 Review Log 2026-11-08.md`.')
    s=s.replace('the adopted final of the five-step analysis flow, synthesized by Claude (Opus 5.5)','the adopted final of the five-step analysis flow, synthesized by Claude (Opus 5.5), with an independent sixth-step review by Codex')
    s=s.replace('valued them on **one** consistent model at current prices','put them into a common terminal-value framework at current prices (full A1 underwrites plus explicitly labeled screens)')
    s=replace(s,'A change was accepted only if it beat the model\'s noise.','A change was accepted only if it passed the stated decision rule.\n- **Step 6:** exact Step 5 reproduction passed. One sizing decision was overturned under rule 2: STRL 6 → 8%, funded VRT 15 → 14% and MU 15 → 14%. WCC\'s duplicate SBC deduction was corrected without adding it. Historical pool ranks are frozen, not re-ranked.')
    s=s.replace('Conclusions taken from either model\'s work were re-checked at the primary source.','Decision-driving facts were spot-checked at primary sources; unresolved source/date gaps are identified in Appendix A and the Review Log.')
    # Current allocation rows, outside historical/generated tables and prior-cycle accountability.
    lines=s.splitlines(); section=''
    for i,line in enumerate(lines):
        if line.startswith('## '): section=line
        if not line.startswith('|') or section.startswith('## Part II:'): continue
        for ticker,old,new in [('VRT',15,14),('MU',15,14),('STRL',6,8)]:
            if not re.search(r'\|\s*(?:\*\*)?'+ticker+r'(?:\*\*)?\s*\|',line): continue
            if line.startswith('| Ticker'): continue
            # Weight is the first standalone old integer cell; return cells have decimals.
            line=re.sub(r'\| (\*\*)?'+str(old)+r'(%)?(\*\*)? \|',
                lambda m:'| '+(m[1] or '')+str(new)+(m[2] or '')+(m[3] or '')+' |',line,count=1)
            if section.startswith('## Part VI:') and '| Core' in line: line=line.replace('| +9 |','| +8 |')
            if ticker=='STRL' and '| Satellite' in line: line=line.replace('| +6 |','| +8 |')
        lines[i]=line
    s='\n'.join(lines)+'\n'
    for a,b in [
        ('15 + 15 + 15 + 15 + 12 + 12 + 10 + 6','15 + 15 + 14 + 14 + 12 + 12 + 10 + 8'),
        ('VRT 15 + MU 15','VRT 14 + MU 14'),('CLS 10 + STRL 6','CLS 10 + STRL 8'),
        ('VRT 15, MU 15, NRG 12, NVT 12','VRT 14, MU 14, NRG 12, NVT 12'),
        ('VRT 15, NVT 12, STRL 6','VRT 14, NVT 12, STRL 8'),
        ('VRT 15%, NVT 12%, STRL 6%','VRT 14%, NVT 12%, STRL 8%'),
        ('VRT 6 → 15, STRL 0 → 6','VRT 6 → 14, STRL 0 → 8'),
        ('NRG (12%) and STRL (6%)','NRG (12%) and STRL (8%)'),
        ('STRL\'s 6%','STRL\'s 8%'),('STRL 6% (installation)','STRL 8% (installation)'),
        ('STRL 6 → 3, TLN +7','STRL 8 → 3, TLN +9'),
        ('STRL 6 → 3','STRL 8 → 3'),('MU 15 → 7','MU 14 → 7'),
        ('MU 15 → 10','MU 14 → 10'),('VRT 15 → 10','VRT 14 → 10'),
        ('MU at 15% and VRT/NVT/CLS at 37%','MU at 14% and VRT/NVT/CLS at 36%'),
        ('Core** (NVDA, META, VRT, MU, NRG, NVT): 84%','Core** (NVDA, META, VRT, MU, NRG, NVT): 82%'),
        ('Satellites** (CLS, STRL): 16%','Satellites** (CLS, STRL): 18%'),
        ('**Satellites:** CLS 10 and STRL 6','**Satellites:** CLS 10 and STRL 8'),
        ('MU +9, NRG','MU +8, NRG'),('VRT +9, MU','VRT +8, MU'),('STRL +6 =','STRL +8 ='),
        ('NRG + STRL = 18%','NRG + STRL = 20%'),('*18% (limit 20%)*','*20% (limit 20%)*'),
        ('| NVDA, MU, CLS | 40% |','| NVDA, MU, CLS | 39% |'),
        ('| VRT, NVT, STRL | 33% |','| VRT, NVT, STRL | 34% |'),
        ('reasonably priced | 33% |','reasonably priced | 34% |'),
        ('rising estimates | 40% |','rising estimates | 39% |'),
        ('**33%** (VRT 14','**34%** (VRT 14'),
        ('| VRT, NVT, NRG, STRL | 45% |','| VRT, NVT, NRG, STRL | 46% |'),
        ('is 30%, or 45% including VRT','is 32%, or 46% including VRT'),
        ('Thermal, Electrical and Site Work — 33%','Thermal, Electrical and Site Work — 34%'),
        ('*VRT increase 6% → 15%;','*VRT increase 6% → 14%;'),
        ('**Vertiv (VRT) — 15% (+9):**','**Vertiv (VRT) — 14% (+8):**'),
        ('HBM / Memory — 15% (MU) · *Increase 6% → 15%*','HBM / Memory — 14% (MU) · *Increase 6% → 14%*'),
        ('**Sterling Infrastructure (STRL) — 6% (new, Step 5):**','**Sterling Infrastructure (STRL) — 8% (added in Step 5; resized in Step 6):**'),
        ('**Y (6%)**','**Y (8%)**'),
        ('top three = 45%; HHI 0.132','top three = 44%; HHI 0.1294'),
        ('Four positions sit at the 15% cap.','Two positions sit at the 15% cap.'),
        ('| 15% / 45% |\n| HHI','| 15% / 44% |\n| HHI'),
        ('| 0.132 |','| 0.129 |'),('40 / 0 / 33 / 12 / 15','39 / 0 / 34 / 12 / 15'),
    ]: s=s.replace(a,b)
    # Headline performance changes are current-version prose only; old comparison tables inserted last.
    for a,b in [('15.4%','15.5%'),('24.0%','24.1%'),('38.1%','38.2%'),('−22.3%','−22.1%'),('18.4% | 27.1% | 41.5% | −56.3% | −13.3%','18.5% | 27.2% | 41.6% | −56.2% | −13.2%'),('**1.81×**','**1.82×**'),('**+81%**','**+82%**'),('**+81% (','**+82% ('),('**+281% (','**+282% ('),('**+78% (14.9%/yr)**','**+79% (15.0%/yr)**')]:
        s=s.replace(a,b)
    # The 15.4% replacement also touched DELL's *stock* named scenario: restore explicitly.
    s=s.replace('DELL | AI servers | $346.31 | Fair | 5.6% | 15.5%','DELL | AI servers | $346.31 | Fair | 5.6% | 15.4%')
    s=s.replace('V10.2 on Codex\'s higher terminal multiples | 18.4%','V10.2 on Codex\'s higher terminal multiples | 18.5%')
    s=s.replace('on Codex\'s higher multiples V10.2 returns 18.4%','on Codex\'s higher multiples V10.2 returns 18.5%')
    s=s.replace('| Expected CAGR on Codex\'s multiples | 9.1% | 16.6% | 18.6% | 18.4% |','| Expected CAGR on Codex\'s multiples | 9.1% | 16.6% | 18.6% | 18.5% |')
    s=s.replace('Raised to the cap in Step 5','14% after the Step 6 funded STRL increase').replace('raised to the cap in Step 5','14% after the Step 6 funded STRL increase')
    s=s.replace('Raised from 14% to the 15% cap in Step 5.','Step 5 raised it to 15%; Step 6 returns it to 14% to fund STRL under rule 2.')
    s=s.replace('15% cap (raised in Step 5 as VST\'s exit freed capital)','14% after the rule-2 STRL increase (Step 6)')
    s=s.replace('15% cap; wins the AI-2027 tie-break','14%; wins the AI-2027 tie-break within its return band')
    s=s.replace('Residual after the caps; Texas and project risk','Texas cap binds at 20% jointly with NRG; satellite cap 10%')
    s=s.replace('which has the highest AI-2027 (26.8%) and 100GW (45.3%) CAGRs of any holding','which has a 26.8% AI-2027 CAGR and the highest 100GW CAGR among holdings (45.3%); STRL has the highest held AI-2027 CAGR (28.7%)')
    s=s.replace('tied highest in the pool\'s top 15','highest within MU\'s ±2pp expected-return band')
    s=s.replace('it\'s the highest-ranked eligible stock of the 58','it is #3 of the 60-name Step 5 pool; eligible STRL ranks #1')
    s=s.replace('All 20 V9.1 positions not in V10.2 went to 0%, and VST (raised to 8% in Step 3) left in Step 5.','Twenty-one of the 24 V9.1 positions go to 0%, including VST (raised to 8% in Step 3 and removed in Step 5).')
    s=block(s,'### D. Final decisions (Step 5)','### E. Additional risks', '''### D. Final decisions (Step 5, reviewed in Step 6)

Rule 2 accepts **at least +0.25pp Expected CAGR, OR at least +0.1pp with higher AI-2027 CAGR and no more than 1pp worse bust**. Both branches matter. The unchanged Step 5 Decision Log and the Step 6 Review Log separate historical decisions from corrections.

| ID | Item | Reviewed decision | Effect |
|---|---|---|---|
| D1 | AVGO EPS | Retain $27 owner EPS as judgment, not a guaranteed management outcome; 13.5% expected. Bench, not held | No weight effect |
| D2 | VRT/NVT duplicate SBC | Remove duplicate deductions; ordinary SBC remains in adjusted EPS | Step 5 correction retained |
| D3 | WCC | Reject holding; remove duplicate 4% SBC haircut. 8.0% expected. The 9% growth assumption is judgment, not company 2027 guidance | No held-weight effect |
| D4 | STRL / VST | Keep STRL's operating bridge and VST exit. **Overturn sizing: STRL 8%, VRT 14%, MU 14%** | Versus V10.1: +0.1243pp Expected, +0.0891pp AI-2027, +0.0726pp 100GW, +0.0528pp better bust |
| D5 | Bench | AVGO; VST/TLN; AEIS; TSM. Risk-specific replacement and eligibility override generic order | No automatic purchase |
| D6 | Texas | Re-underwrite within 5 sessions; inspect existing administrative restrictions now. If cash-flow impact confirmed: **NRG 8, STRL 3, TLN 9** | Conditional Expected 15.0% |
| D7 | MOD | Nov 18 gate kept: FY28 targets must bridge to **2030** owner EPS $8.84, stable DC margin and positive H2 FCF. MOD 5 from VRT −3/NVT −2 | Conditional Expected 15.7% |
| D8 | NVDA | 15%; no buy before Nov 17 report and review-status check. Adverse review: NVDA 8 / AVGO 7 | Conditional Expected 15.2% |
| D9 | META | Keep 15%; verify household look-through before orders | No change |
| D10 | Architecture | Eight names; 82% core, 18% satellites | No name-count change |
| D11 | Multiple sensitivity | Retain primary multiple policy; remove claim of multiple-invariant optimality | No repricing |
| D12 | Screens | Distinguish full underwrites from screens; no certified upper bounds | No re-ranking |
| D13 | HBM | Qualitative tightness corroborated; workbook HBM-market forecast not verified like-for-like | No probability change |
| D14 | Other alternatives | Retain rejection/watchlist; restore omitted EME/IESC/HUBB comparison rows | No new candidates |
''')
    s=s.replace('At its own multiple it returns ~6–7%.','At 12× it returns 15.15%, and at its own 10.3×, 10.98% (same Step 5 operating bridge; regenerated Step 6 sensitivity).')
    s=s.replace('V10.2 is the best of the tested portfolios under **both** policies.','V10.2 beats the named unconditional comparison portfolios on primary A1 Expected CAGR; this is not a global optimum or an invariant ranking under different multiples.')
    s=s.replace('while they stay ahead of it on the AI-2027 tie-break.','and the MSFT–VRT expected-return gap exceeds the 2pp tie band. A tie-break cannot erase that gap; a higher-multiple optimization belongs to the next cycle.')
    s=block(s,'**Reading the comparison:**','### How the two models', '''**Reading the comparison:**

- V10.2 returns 15.5% expected versus 14.4% for either Step 2 portfolio, 14.9% for the Step 3 proposal and 14.9% for Codex's WCC/STRL proposal after the WCC accounting fix. AI-2027 and 100GW are also higher; the diversified and WCC variants have milder modeled busts.
- **D4 sizing correction:** the already-tested STRL-8 alternative equals V10.2. Its unrounded gains over V10.1 are +0.124331pp Expected and +0.089072pp AI-2027, with a 0.052802pp better bust. It passes rule 2's lower branch. Rule 4 does not override that pass, and its better bust also favors V10.2.
- STRL remains below the adopted 10% satellite cap; NRG + STRL = 20%, exactly the existing Texas cap. D4 called 6% a residual, not a hard cap. Codex's proposed 5% ceiling was not the adopted constraint; this correction does not reinstate that earlier proposal.
- The MOD variant has higher modeled returns but is ineligible until its gate passes. The concentrated architecture violates the NRG/CLS confidence caps. No claim of exhaustive or multiple-invariant optimization is made.
- The table retains historical weights and conditional variants for accountability. WCC-containing portfolios are re-evaluated only for the duplicate-SBC correction; original Step 5 outputs remain unchanged. Ranks are frozen to Step 5.
''')
    s=s.replace('V10.2 is the best tested portfolio under either side\'s multiples, but the constituents aren\'t invariant (MSFT, Step 5 D11)','the primary A1 result is retained; higher multiples can change both the constituent ranking and the best tested architecture (D11)')
    s=s.replace('**15%.** Wins the AI-2027 tie-break','**14%.** Wins the AI-2027 tie-break')
    s=s.replace('WCC 7.0%: +6.7pp','WCC 8.0%: +5.8pp')
    s=s.replace('WCC (7.0%)','WCC (8.0%)')
    s=s.replace('7.0% on consistent inputs','8.0% after the Step 6 SBC correction')
    s=s.replace('Codex\'s bridge exceeds Wesco\'s own growth and margin guidance (D3)','Retains Step 5\'s lower growth judgment; no verified 2027 numeric company sales guide (D3)')
    s=s.replace('Codex\'s 18.3% needs growth above Wesco\'s own guidance (D3)','Codex\'s 18.3% uses a stronger operating bridge; no verified 2027 numeric company sales guide (D3)')
    s=s.replace('Codex\'s 18.3% needs revenue and margin growth above Wesco\'s own guidance','Codex\'s stronger revenue/margin bridge is not disproved by company 2027 guidance; the conservative judgment stands')
    s=s.replace('| 7.0% (Codex: 18.3%) | 10.5% | 16.9% |','| 8.0% (Codex: 18.3%) | 11.6% | 18.0% |')
    s=s.replace('| WCC | Electrical/datacom distribution | Codex Step 4 (O1) | Worse | N | 7.0%','| WCC | Electrical/datacom distribution | Codex Step 4 (O1) | Worse | N | 8.0%')
    s=s.replace('### Removed from V9.1','''| EME | Claude Step 4 | 13.5% | 20.0% | 32.3% | Below the selected contractor STRL; within noise of VRT/NVT | Re-underwrite if valuation improves enough to clear rule 2 |
| IESC | Claude Step 4 | 13.3% | 22.6% | 39.7% | Backlog/cash cushion weaker; not enough portfolio advantage | Fresh FY26 cash conversion and backlog support |
| HUBB | Claude Step 4 | 12.1% | 17.1% | 28.0% | Less AI sensitivity and lower return than NVT | Re-underwrite if price or growth closes that gap |

Step 4-only returns retain their authors' models and are not new A1 ranks. Other rejected Step 4 names remain in D14's record: LRCX/KLAC/AMAT/TER/BESI need a better priced packaging/WFE cash bridge; HUBB/ABB/Schneider/MTZ/PWR/FIX need better relative return; CSCO/APH/TEL/AMKR/ETN/COHR/CRDO need a stronger owner-cash/valuation case. These are review conditions, not automatic entry orders; no candidate is added to the frozen pool.

### Removed from V9.1''')
    s=s.replace('**Tighter than modeled, but not verified like-for-like**','**Qualitative tightness corroborated; quantitative forecast unverified**')
    s=s.replace('SK hynix: DRAM and HBM "sold out to 2029"; Micron\'s $54B quarter is *total* DRAM + NAND, so it can\'t measure HBM market size','Micron reports most CY27 HBM bits contracted with higher prices; its $54B quarter is total DRAM + NAND, not industry HBM-market revenue')
    s=s.replace('- STRL (#1), added in Step 5, is held at 6%: the residual after the caps, sized for Texas and project risk.','- STRL (#1), added in Step 5, is 8% after the Step 6 rule-2 correction; the 20% combined Texas cap binds.')
    s=s.replace('- MU (#11) is held at the cap on the AI-2027 tie-break.','- MU (#11) is held at 14% on the AI-2027 tie-break within its return band.')
    s=s.replace('Part V shows V10.2 is the best tested portfolio under both multiple policies, though the constituents aren\'t invariant (MSFT would rank higher on Codex\'s multiples).','Part V compares the named architectures on primary A1 inputs; different multiples change the ranking and can change the preferred portfolio.')
    s=block(s,'- **Owner-basis model (corrected in Step 5, D1):**','- That gives **13.5%**', '''- **Owner-basis model (D1, retained):** base 2030 owner EPS $27.0, 20×, credit reserves −$8/−$4/−$2/$0 per share and about $13 cumulative dividends. The reported FY28 adjusted-EPS target above $30 is corroborated by the [Q3 call transcript](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/), not by the issuer release itself. Step 6 did not authenticate the call audio or the claimed September 14 reaffirmation. $27 after a 13% deduction implies about $31.03 adjusted EPS; it is a delayed-target judgment, not a mechanical conversion of $30 or a guaranteed floor. The older $23.50 owner case did not itself prove an earnings decline versus an adjusted target. The [Oct 27 8-K](https://investors.broadcom.com/static-files/0ee4f6b7-4a23-4de0-8f3e-48f147ae30d3) directly confirms the contingent ~$43B maximum, not a booked loss.
''')
    s=s.replace('**AVGO is bench #1:** the first destination for capital freed by any trigger.','**AVGO is bench #1:** a default candidate, not an automatic destination for every trigger. Specific risk-matched replacements and fresh underwriting take precedence.')
    s=block(s,'- **Why 15% when it ranks #11:**','- **It is a deliberate cyclical holding', '''- **Why 14% when it ranks #11:** within the 2pp expected-return band, MU wins the AI-2027 tie-break and retains upstream HBM exposure. Step 6 moves one point from MU and one from VRT to STRL because that funded alternative clears rule 2; no valuation input changes.
''')
    s=s.replace('| SK hynix (KRX: 000660) | **Comparable or Better**, but not a US-listed common or ADR | Not investable under the mandate |','| SK hynix (KRX: 000660) | **Comparable or Better** operationally; access/liquidity not established | The mandate is global common stock, not US-only. Broker access and a full like-for-like valuation belong to the next cycle; no new pool entry now |')
    s=block(s,'- **Why only 6%:**','- **Buy ceiling:**', '''- **Why 8%, not a larger position:** NRG 12% plus STRL 8% reaches the adopted Texas cap of 20%; the satellite cap remains 10%. Project risk, 0.9 signed book-to-burn and unsigned backlog remain material.
- **Cash/history cross-check:** Q3's nine-month CFO $427.095M less capex $115.458M gives $311.637M FCF. The adopted Codex bridge projects 2027–30 base FCF $0.60/$0.80/$1.00/$1.15B; terminal owner income $1.35B + depreciation $0.18B − capex $0.28B − working capital $0.10B = $1.15B. These are forecasts, not guidance, and no cumulative FCF or excess cash is added to the earnings terminal value. Owner anchors are $10.88 − $24M × 0.8 / 30.9M = $10.26 (2025) and $21.83 − $38M × 0.8 / 31.1M = $20.85 (2026 estimate). Source: [Q3 release](https://www.sec.gov/Archives/edgar/data/874238/000087423826000122/a20261028ex991earningsrele.htm); the historical/forecast bridge is preserved in Codex's Step 4 pass.
- **Multiple sensitivity on that same bridge:** Expected CAGR 19.52% at 14×, 15.15% at 12×, 10.98% at 10.3×. The old ~10%/~6% statements belonged to a different operating case. The 10.3–15.5× band is a current forward comparison, not a verified multi-year forward-multiple history; the historical ex-post P/E check is not directly comparable.
''')
    s=s.replace('Its 8% funded STRL (19.5%), with VRT and MU rising to the cap: **+0.41pp** of portfolio expected return.','In Step 5 its 8% funded STRL 6% and one point each of VRT/MU, adding 0.41pp expected. Step 6 reallocates those two points to STRL, adding a further 0.1243pp versus V10.1.')
    s=s.replace('KTOS: positive owner FCF for two quarters |','KTOS: positive owner FCF for two quarters; AVAV: clean audit and a program-of-record win |')
    s=s.replace('Priced as an oncology success | n/a |','Priced as an oncology success | Re-underwrite on cash-funded clinical/commercial evidence and valuation above the marginal holding; no automatic pandemic purchase |')
    s=s.replace('−7.1%; priced as an oncology success | n/a |','−7.1%; priced as an oncology success | Cash-funded clinical/commercial evidence plus valuation above the marginal holding; not an automatic pandemic purchase |')
    s=s.replace('**(3) Core-and-satellite (V10.2, adopted in Step 5):**','**(3) Core-and-satellite (V10.2, adopted after Step 6):**')
    s=s.replace('0.2pp a year less than V10.2','0.3pp a year less than V10.2').replace('0.2pp a year below (3)','0.3pp a year below (3)')
    s=s.replace('1.7pp of expected return a year to save','1.8pp of expected return a year to save').replace('1.7pp a year less expected return','1.8pp a year less expected return').replace('about 11pp less cumulative return','about 12pp less cumulative return')
    s=block(s,'**The explicit price of risk control:**','### D. Three-Fund', '''**The explicit price of risk control:** STRL 8% + NRG 12% now binds the existing Texas cap at 20%; CLS remains at its 10% confidence cap and NVT at 12%. The already-tested STRL-8 alternative passed rule 2's +0.1pp branch, so it cannot be rejected merely as rounded "noise." V10.2 does not claim global optimality and does not adopt Codex's earlier STRL-5/WCC-8 proposal.

**Replacement precedence:** the specific risk-matched destination above overrides the generic bench ordering. Re-underwrite the replacement at live prices, within the approved total weights and caps; do not rotate into another name exposed to the same invalidating risk. In a Taiwan event, TSM/AVGO are not automatic safe destinations. If no candidate qualifies, retain temporary reserve and obtain a revised funded allocation. No single-name trigger authorizes overlapping, unfunded conditional trades.
''')
    s=block(s,'    - It already holds about 2.5% META','---\n\n## Part VI', '''    - Index look-through is not verified live. The earlier FSKAX estimates (META ~2.5%, NVDA ~6%) are illustrative only. At exactly 50% Event Horizon / 50% Continuity and 80% FSKAX, direct META is 7.5% of investments and that illustrative index weight adds 1.0%; verify fund holdings, accounts and actual sleeve values before treating 8.5% as household exposure. META is #6, not top five.
- **Event Horizon (~50% target):**
    - The earlier 46–47% estimate used the Nov 6 drawdown, not the Nov 9 rebound or actual account balances. No live household weight is established.
    - Direct contributions to Event Horizon **only if** verified current weight is below 50%; stop at target. Foundation and Continuity remain unchanged. Rebalance review if Event Horizon exceeds 55%.
''')
    s=s.replace('| MU | 6% | 14% | **+9** | ASML −8, VST −1 |','| MU | 6% | 14% | **+8** | ASML −8 |')
    s=s.replace('| VRT | 6% | 14% | **+9** | ANET −4, DELL −2, COHR −2, VST −1 |','| VRT | 6% | 14% | **+8** | ANET −4, DELL −2, COHR −2 |')
    s=s.replace('| STRL | 0% | 8% | **+6** | VST −4, MP −2 |','| STRL | 0% | 8% | **+8** | VST −6, MP −2 |')
    s=s.replace('*+7%* if the Texas','*+9%* if the Texas')
    s=s.replace('first destination for freed capital (incl.','default bench candidate, subject to risk-specific precedence (incl.')
    s=s.replace('Hold the 18 points in reserve','Hold the 19 points in reserve (C1 + C3 becomes 54%)')
    s=s.replace('If two of the three trip, the same action applies without waiting for the re-underwrite','If two trip, expedite the review; confirmed cash-flow impact is still required before applying the funded substitution')
    s=s.replace('The other holdings are at their caps, so add **TLN**','Preserve the approved targets of the other holdings; add **TLN**').replace('remaining ~2 points','remaining 1 point')
    s=s.replace('**12.5%**, and 20% cuts it to **9.3%**','**12.6%**, and 20% cuts it to **9.4%**')
    s=s.replace('The same overlay cuts both models\' Step 2 portfolios by the same amount, so it doesn\'t change the choice.','A common zero-recovery probability scales expected terminal wealth equally and preserves the ordering; the CAGR reductions are not identical in percentage points.')
    s=s.replace('V10.2 is the best of the tested portfolios under both multiple policies, though the constituents are not invariant: on Codex\'s multiples MSFT would outrank VRT and MU on expected return.','The primary A1 conclusion is conditional on its multiple policy: under Codex\'s multiples MSFT outranks VRT/MU, and a different portfolio may win.')
    s=s.replace('**Core-and-satellite with eight names is optimal for this mandate.**','**Core-and-satellite with eight names wins the named primary-A1 architecture comparison; this is not proof of a global optimum.**')
    s=s.replace('after Steps 4 and 5:', 'after Step 6:')
    s=s.replace('(14.0% vs 11.4%)','(14.3% vs 11.5% on the adopted model)')
    # Calendar and sources: opening an auction is not its clearing/result release.
    s=s.replace('**The 2029/30 auction is Dec 9, 2026.**','**The 2029/30 auction opens Dec 9, closes Dec 15, and results are scheduled Dec 22, 2026** ([PJM schedule](https://www.pjm.com/-/media/DotCom/markets-ops/rpm/rpm-auction-info/rpm-auction-schedule.xlsx), BRA rows 59–61).')
    s=s.replace('**The 2029/30 auction is Dec 9.**','**The 2029/30 auction runs Dec 9–15, with results scheduled Dec 22.**')
    s=s.replace('**AVGO and PJM BRA (Dec 9)**','**AVGO (Dec 9); PJM opens Dec 9, results Dec 22**')
    s=s.replace('PJM\'s Dec 9 auction clears','PJM\'s Dec 22 scheduled results show the auction clears')
    s=s.replace('PJM 2029/30 auction (**Dec 9**)','PJM 2029/30 results (**Dec 22 scheduled**)').replace('**Dec 9; Jan session**','**Dec 22; Jan session**')
    s=s.replace('the Dec 9 PJM auction','the Dec 22 scheduled PJM results')
    s=s.replace('at the Jan 14 report','at the next TSM earnings report (Jan 14 unconfirmed)')
    s=s.replace('TSM (Jan 14)','TSM (Jan 14 unconfirmed)')
    s=s.replace('**MU (Dec 23)**','**MU (Dec 23 unconfirmed)**')
    s=s.replace('FQ1 report Dec 23','FQ1 date unconfirmed; Dec 23 tentative').replace('The Dec 23 report','The next report (Dec 23 unconfirmed)')
    s=s.replace('(Dec 23) |','(Dec 23 unconfirmed) |').replace('| **Dec 23** |','| **Date unconfirmed (Dec 23 tentative)** |')
    s=s.replace("MU's Dec 23 report", "MU's next report (Dec 23 unconfirmed)")
    s=s.replace('three weeks before its Dec 23 report','subject to its issuer-confirmed earnings date (Dec 23 unconfirmed)')
    s=s.replace('| Jan 27 |','| Jan 27 unconfirmed |')
    s=s.replace('Texas moratorium becomes law; ERCOT','Texas restriction demonstrably impairs cash flow after re-underwrite; ERCOT')
    s=s.replace('a Texas moratorium becomes law; net claims rise','confirmed cash-flow impairment from Texas restrictions after re-underwrite; net claims rise')
    s=s.replace('    - No 8-K or regulator action was reported, and Huang has not stepped aside.','    - The [Nov 8 NVIDIA board statement](https://investor.nvidia.com/news/press-release-details/2026/Statement-from-NVIDIA-Board-of-Directors/default.aspx) confirms an independent review and says the board has no reason to believe sensitive information was compromised. It is not a completed finding; the alleged foreign-agent connection remains unverified. No adverse conclusion was located in the Step 6 check.')
    s=s.replace('Existing and under-construction projects are likely exempt.','Do not assume exemptions: before NRG/STRL buys, check operative permits and project exposure under the [existing September TCEQ directive](https://gov.texas.gov/news/post/governor-abbott-directs-tceq-to-halt-data-center-permits), not just the future bill.')
    s=s.replace('updated in Step 5 for the adopted V10.2','updated in Step 6 for the adopted V10.2')
    s=s.replace('~23.9%','~23.8%').replace('~6.1% |','~5.5% |').replace('~9.0% |','~8.7% |')
    s=s.replace('- Pair each sale with a same-day buy in the same economic theme.','- Pair sales and same-theme buys only when all gates and limits pass; otherwise retain the temporary reserve.')
    s=s.replace('- Deploy all reserve by **Dec 11** unless the financing-shock or Taiwan scenario is active.','- **Dec 11 is a reserve review checkpoint, not a forced-buy deadline.** Gates, risk pauses, tax checks, limits and all position/cluster caps override schedules and acceleration rules. PJM results are not scheduled until Dec 22. Buy only remaining approved gaps; carry blocked cash to a documented owner review, not an over-target position.')
    s=s.replace('so the rotation can be roughly tax-neutral. Verify against actual lots.','but this is not a tax-neutrality estimate for the account. Verify actual lots, gains/loss character and the wash-sale window (30 days before and after, including relevant household/IRA transactions) with the broker or tax adviser.')
    s=s.replace('On May-basis lots, realized losses roughly offset the gains (Deployment Strategy §3).','May-price lot illustrations suggest losses exceed gains; actual tax consequences require the account\'s lots and wash-sale review (Deployment Strategy §3).')
    s=s.replace('**Process (five-step flow):**','**Process (five steps plus independent final review):**')
    s=s.replace('**Step 5 (this report):**','**Step 5:**').replace('producing the adopted V10.2.','producing V10.1.\n6. **Step 6:** Codex reproduced all eight Step 5 artifacts byte for byte, audited D1–D14 and corrected the final to V10.2. New scripts, overlays, generated tables and the quote/calendar audit are only in `inputs/research/codex_final_review/`; Step 1–5 records are unchanged.')
    s=replace(s,'**Unverified items:**','**Step 6 verification and remaining gaps:**')
    s=s.replace('- Broadcom\'s ~$43B maximum undiscounted exposure: Codex\'s citation of the Oct 27 8-K. Adopted as the newer and more conservative figure, but not re-fetched for this report.','- Broadcom\'s ~$43B maximum contingent exposure was re-fetched and verified in its Oct 27 8-K. The FY28 EPS target is corroborated by a third-party call transcript; the September 14 reaffirmation was not verified.')
    s=s.replace('- The NVIDIA board-review details: from Yahoo/24/7 Wall St (read in full) and CNN\'s headline. No company filing was found.','- NVIDIA\'s Nov 8 board statement confirms the review, not the reported foreign-agent allegation. The Nov 17 earnings date is issuer-confirmed; MOD Nov 18 and AVGO Dec 9 are also issuer-confirmed. MU Dec 23, TSM Jan 14 and CLS Jan 27 are unconfirmed; refresh the issuer calendars before orders. Other read-through dates in this report are inherited, not an authorization to trade without checking.\n- PJM\'s downloaded schedule (2029/30 BRA rows 59–61) distinguishes Dec 9 opening, Dec 15 close and Dec 22 results. All reserve deadlines are subordinate to trading gates.\n- WCC\'s investor presentation explicitly retains SBC in adjusted EPS; Step 6 reverses only the duplicate 4% factor in the stored plateau/base/bull EPS. Its 2027 growth rate is the synthesis model\'s judgment, not verified guidance.\n- Nov 10 approximately 20:27 UTC live-quote check: none of 16 held/bench/gated/watchlist names moved more than 10% versus Nov 9 (largest: NVDA −5.85%; SANM +4.30%). These intraday observations do not reprice the report. Raw timestamps and public quote endpoints are in `codex_final_review/data/quote_audit.json`.\n- The 60-name table combines 29 full A1 underwrites and 31 screens; screen stress values are not equivalent to full modeled bust states. Rankings are frozen Step 5 ordinal references even where WCC\'s accounting correction raises its return. A complete uniform-model re-ranking belongs to the next cycle.')
    s=s.replace('Every change from the Step 3 proposal (VST −8; STRL +6, VRT +1, MU +1) is funded by VST\'s exit','Net change from Step 3 is VST −8 / STRL +8; Step 6 specifically funds STRL +2 from VRT −1 and MU −1')
    s=s.replace('**Status:** V10.2 is marked **adopted** (Step 5, Nov 10).','**Status:** V10.2 is marked **adopted after Step 6 review** (Codex, Nov 10).')
    s=s.replace('every accepted change passed the noise rule on the same model','Step 6 corrected D4\'s omitted lower rule-2 branch with the same prices/model/caps')
    s=s.replace('at the 15% cap. Codex\'s stock','at the 15% cap. Codex\'s stock')
    s=insert_tables(s)
    return s

def deployment(s):
    s=table(s,'| Ticker | V10.1 target','destination6')
    s=table(s,'| Ticker | V9.1 target','trades6')
    s=s.replace('V10.1','V10.2')
    s=s.replace('(Step 5 final assembly) for the adopted V10.2.','(Step 6 independent review, Codex) for adopted V10.2.')
    s=s.replace('**VRT and MU** go to 15%.','**VRT and MU** are 14%, and **STRL is 8%** after the Step 6 rule-2 correction (funded STRL +2 / VRT −1 / MU −1).')
    s=s.replace('The Step 3 version is preserved in `inputs/superseded/Deployment Strategy/`.','The Step 3 and pre-review V10.1 versions are preserved in `inputs/superseded/Deployment Strategy/`; Step 6 findings are in `inputs/Step 6 Review Log 2026-11-08.md`.')
    s=s.replace('The adopted total is 18%.','The adopted total is 20%; this cap binds.')
    s=s.replace('**TLN:** +7%','**TLN:** +9%').replace('STRL 6 → 3','STRL 8 → 3').replace('TLN +7','TLN +9')
    s=s.replace('Never buy a name back within 30 days of selling it at a loss.','Wash-sale review covers 30 days **before and after** a loss sale and substantially identical purchases in relevant household accounts, including IRAs. Consult the broker/tax adviser; a simple same-ticker wait is not a complete tax rule. [IRS Publication 550](https://www.irs.gov/publications/p550).')
    s=s.replace('1. **Weights:** V10.2 was adopted on Nov 10 (Step 5).','1. **Weights:** V10.2 was adopted on Nov 10 after Step 6.')
    s=s.replace('List any name sold at a loss in the last 30 days (wash-sale window), and don\'t repurchase any name sold at a loss within 30 days.','Check purchases in the 30 days before and planned purchases in the 30 days after each loss sale, across relevant household/IRA accounts; flag substantially identical securities and automatic reinvestments.')
    s=s.replace('so **the rotation can be roughly tax-neutral.**','but **this does not establish account-level tax neutrality** (character, actual basis and wash sales matter).')
    s=s.replace('**T1 sells everything with no role in V10.2**','**T1 sells 18 of the 21 V9.1 exits** (TSM/ASML follow in T2/T3; AVGO in T3)')
    s=s.replace('**STRL** +3.00','**STRL** +4.00').replace('STRL +3.00','STRL +4.00')
    s=s.replace('**VRT** +5.60','**VRT** +5.10').replace('VRT +2.24','VRT +2.04').replace('VRT +3.36','VRT +3.06')
    s=s.replace('**MU** +3.47','**MU** +3.07').replace('MU +2.60','MU +2.30')
    s=s.replace('**23.9%**','**23.8%**').replace('**6.1%**','**5.5%**').replace('**9.0%**','**8.7%**')
    s=s.replace('three weeks before its Dec 23 report','subject to its issuer-confirmed earnings date (Dec 23 unconfirmed)')
    s=s.replace('three weeks before its Dec 23 report.','subject to its issuer-confirmed earnings date (Dec 23 unconfirmed).')
    s=s.replace('It is deployed by **Dec 11** (after the Dec 9 AVGO report and PJM auction) unless Scenario C is active.','Dec 11 is a review checkpoint, not a forced-buy deadline; PJM results are scheduled Dec 22. The modeled cash path is 23.78% → 5.48% → 8.67% → 0%, only if all baseline trades fill and no gate is active.')
    s=s.replace('Hold up to 10% cash and re-evaluate after Dec 9 (AVGO and PJM)','Retain blocked cash (10% is a guideline, not authority to force buys); review after AVGO Dec 9 and PJM results scheduled Dec 22')
    s=s.replace('If two of {Texas bill, ≥ 3 states legislate, FERC voids bring-your-own-power} fire, apply the same action without waiting for the re-underwrite','If two of {Texas bill, ≥ 3 states legislate, FERC voids bring-your-own-power} fire, expedite the review; confirmed cash-flow impact remains required')
    s=s.replace('The Dec 9 auction clears well below the cap','PJM\'s scheduled Dec 22 results show a clearing price well below the cap')
    s=s.replace('No change to V10.2 (MP is already sold).','No baseline target change to V10.2 (MP is scheduled to be sold in T1; confirm actual fills).')
    s=s.replace('skip that piece and redistribute pro-rata to names below their limits.','skip that piece; redistribution is only into remaining approved target gaps of eligible names below limits. Never overfill a target or confidence/cluster cap; retain blocked cash.')
    s=block(s,'- **R3: Hard deadline','## 9. Calendar', '''- **R3: Dec 11 review checkpoint, not a forced-buy deadline.** Deploy only eligible remaining target gaps below limits. All risk, event, tax and execution gates override dates and acceleration instructions. PJM results are scheduled Dec 22, not Dec 9.
- **R4:** If any gate remains active, retain the blocked reserve and review with the owner on Jan 8, 2027. Do not deploy on Jan 8 merely because the truce expires Jan 10. Refresh MU's report date (Dec 23 unconfirmed), the political events and valuations first. Cash can exceed 10% temporarily when necessary to avoid violating gates; this is execution reserve, not a permanent new allocation.
- **R5:** Buy no position above its approved target or any tighter cap: name ≤15%, NRG/NVT ≤12%, CLS/STRL ≤10%, NRG + STRL ≤20%, C1 ≤50%. Monitoring tolerances do not authorize over-cap orders. Concurrent triggers require a single reconciled, funded target vector; do not stack conditional portfolios.

## 9. Calendar''')
    # block includes heading exactly once.
    s=s.replace('## 9. Calendar\n\n## 9. Calendar','## 9. Calendar')
    s=s.replace('**AVGO FQ4; PJM 2029/30 auction**','**AVGO FQ4; PJM auction opens**').replace('| Scenario I; R3 |','| AVGO review; no PJM clearing result yet |')
    s=s.replace('| Dec 11 | Reserve deadline | R3 |','| Dec 11 | Reserve review checkpoint | R3; gates override timetable |\n| Dec 15 / Dec 22 | PJM auction closes / results scheduled (no earlier than 4 p.m. Eastern) | Scenario I only on published results |')
    s=s.replace('| Dec 23 | MU FQ1 FY27 |','| Dec 23 (unconfirmed) | MU FQ1 FY27; verify issuer date |')
    s=s.replace('TSM (Jan 14)','TSM (Jan 14 unconfirmed)')
    s=s.replace('NVDA 15, META 15, VRT 15, MU 15, NRG 12, NVT 12, CLS 10, STRL 6','NVDA 15, META 15, VRT 14, MU 14, NRG 12, NVT 12, CLS 10, STRL 8')
    s=s.replace('- No position above 15%; NRG + STRL ≤ 20% (Texas).','- No position above its approved target; all R5 caps apply. ±0.5pp is a monitoring band, not permission to buy above a cap.')
    s=s.replace('direct new contributions to Event Horizon until it is back at ~50%.','measure live sleeve values and direct contributions here only while below the ~50% target; do not use the stale 46–47% estimate.')
    s=s.replace('## 2. Preflight (before any order)','''**Precedence:** specific risk-matched replacements in final Part V.C override generic bench order. No automatic AVGO/TSM purchase during a Taiwan or shared-financing shock. If no candidate passes refreshed valuation, caps and gates, retain reserve. Scenario A/G acceleration never overrides these controls. MOD, Texas and NVDA conditional target vectors are separately generated in `codex_final_review/data/ports6.json`; simultaneous triggers require reconciliation before orders.

## 2. Preflight (before any order)''')
    s=s.replace('## 3. Trade List (drift basis, % of sleeve)','''6. **Texas permits:** check the existing [September TCEQ directive](https://gov.texas.gov/news/post/governor-abbott-directs-tceq-to-halt-data-center-permits) and project exemptions before any NRG/STRL addition. A future bill is not the only possible restriction. If operative restrictions plausibly impair the modeled cash flows, pause affected additions pending the D6 review.
7. **Household exposure:** verify actual Event Horizon/Continuity balances and index look-through; 8.5% household META is illustrative, not measured. Check all dated catalysts at issuer sites immediately before orders.

## 3. Trade List (drift basis, % of sleeve)''')
    s=s.replace('## 10. Final Checks After T4','''Calendar sources checked in Step 6: [NVIDIA Nov 17](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Sets-Conference-Call-for-Third-Quarter-Financial-Results/default.aspx), [Modine Nov 18](https://investors.modine.com/news/news-details/2026/Modine-to-Host-Analyst-and-Investor-Day-on-November-18-2026/default.aspx), [Broadcom Dec 9](https://investors.broadcom.com/news-releases/news-release-details/broadcom-inc-announce-fourth-quarter-and-fiscal-year-2026), [PJM schedule](https://www.pjm.com/-/media/DotCom/markets-ops/rpm/rpm-auction-info/rpm-auction-schedule.xlsx), [Micron calendar](https://investors.micron.com/events-and-presentations/), [TSMC calendar](https://investor.tsmc.com/english/financial-calendar). MU/TSM dates above were not confirmed; other inherited read-through/split dates must also be rechecked before execution. Nov 10 ~20:27 UTC quote audit found no >10% move in the 16 checked names; prices and limits here remain Nov 9 based.

## 10. Final Checks After T4''')
    s=insert_tables(s)
    s=s.replace('Maximum buy price (expected return falls to 12%)','Maximum buy price (12% model hurdle; STRL stricter limit)')
    return s

def readme(s):
    s=s.replace('V10.1','V10.2')
    s=s.replace('after Steps 4 and 5 of the 2026-11-08 cycle','after Codex\'s Step 6 review of the 2026-11-08 cycle')
    s=s.replace('**Rack Thermal & Power (15%):** VRT (15%)','**Rack Thermal & Power (14%):** VRT (14%)')
    s=s.replace('**HBM / Memory (15%):** MU (15%)','**HBM / Memory (14%):** MU (14%)')
    s=s.replace('**Site Development & Electrical Installation (6%):** STRL (6%)','**Site Development & Electrical Installation (8%):** STRL (8%)')
    s=s.replace('Expected CAGR 15.4%','Expected CAGR 15.5%').replace('Scenario 24.0%','Scenario 24.1%').replace('Scenario 38.1%','Scenario 38.2%').replace('delay −22.3%','delay −22.1%')
    s=re.sub(r'(\| HBM / Memory \(MU\)\s*\| )15%',r'\g<1>14%',s)
    s=re.sub(r'(\| Thermal, Electrical & Site Work \(VRT \+ NVT \+ STRL\)\s*\| )33%',r'\g<1>34%',s)
    s=s.replace('Codex (pending) | **V10.2**','Codex (done Nov 10; exact reproduction; D4 sizing overturned; STRL +2 / VRT −1 / MU −1; other corrections logged) | **V10.2**')
    s=s.replace('- How the final decisions were made:', '- Independent final review: `Analysis 2026-11-08/inputs/Step 6 Review Log 2026-11-08.md` (D1–D14 verdicts; same-model rule-2 test; preserved V10.1 backup)\n- How the final decisions were made:')
    s=s.replace('│       ├── superseded/', '│       ├── Step 6 Review Log 2026-11-08.md / .pdf          (Step 6, Codex)\n│       ├── superseded/')
    s=s.replace('(Step 3 proposal; Codex single-model run)','(Step 3 proposal; V10.1 before Step 6; Codex single-model run)')
    s=s.replace('│           ├── claude_synthesis/', '│           ├── codex_final_review/                           (Step 6 overlays, verification and generated tables)\n│           ├── claude_synthesis/')
    return s

if __name__=='__main__':
    key=sys.argv[1]
    path,fn={
        'final':(CYCLE/'Event Horizon Fund Analysis 2026-11-08.md',final_doc),
        'deployment':(CYCLE/'Deployment Strategy/Deployment Strategy 2026-11-08.md',deployment),
        'readme':(ROOT/'README.md',readme),
    }[key]
    old=path.read_text(encoding='utf-8'); new=fn(old)
    diff=list(difflib.unified_diff(old.splitlines(),new.splitlines(),n=3,lineterm=''))[2:]
    diff=['@@' if line.startswith('@@') else line for line in diff]
    patch='*** Begin Patch\n*** Update File: '+str(path).replace('\\','/')+'\n'+'\n'.join(diff)+'\n*** End Patch'
    print(json.dumps({'patch':patch,'changed_lines':sum(x.startswith(('+','-')) for x in diff)},ensure_ascii=False))
