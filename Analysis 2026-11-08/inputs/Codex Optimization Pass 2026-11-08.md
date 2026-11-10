# Owner Decision Sheet

Event Horizon Fund — Step 4, independent Codex optimization of Claude's Step 3. Cycle: November 8, 2026. Research completed November 10; prices: November 9 US close. **Proposed, not adopted.** Percentages below are of Event Horizon, not total household assets.

**Recommendation: two substitutions, four ticker-weight changes, nine holdings.** Expected CAGR rises **14.93% → 15.66%**, AI-2027 **23.43% → 24.24%**, 100GW **36.88% → 38.21%**; modeled bust improves **−61.80% → −61.29%**. These are assumption-dependent estimates, not promised returns.

- **O1 — Replace Vistra with Wesco? 8 points.** For: WCC models 18.27% expected versus VST's 12.97%, with better named-path returns and a less severe bust. Against: distribution is low-margin, working-capital-intensive and still exposed to delayed datacenter construction. **Recommend WCC 0 → 8; VST 8 → 0**, subject to refreshed fundamentals and a $330 entry ceiling.
- **O2 — Add Sterling by trimming nVent? 5 points.** For: STRL models 19.52% versus NVT's 13.68%, buying installation capacity at 14× terminal owner earnings. Against: project execution, customer concentration and unsigned pipeline make the apparent bargain fragile. **Recommend STRL 0 → 5; NVT 12 → 7**, with a $315 entry ceiling; do not fund it from MU.
- **E1 — Buy Modine before its post-spin update? 5 points.** For: Step 3's 18.7% expected return is attractive. Against: cash conversion and the new business perimeter remain unproven. **Keep 0%; reconsider after the confirmed November 18 investor day**, using stable margins, positive H2 FCF guidance and targets supporting *2030* owner EPS $8.84. If passed, fund from VRT −3/NVT −2.
- **E2 — NVIDIA 15% or 12% during the board review? 3 points.** For 15: highest-return eligible incumbent and central acceleration exposure. Against: governance/event risk is not captured adequately in an earnings model. **Retain the 15% target, but no incremental purchase before November 17 earnings and a review-status check.** Resolve the deployment document's conflicting pre-earnings purchase first.
- **E3 — Vistra or Talen for the second power position? 8 points.** For VST: existing generation can gain scarcity rents; for TLN: less Texas concentration. Against both: opportunity cost versus WCC; new-project restrictions are not merely hypothetical. **Prefer O1 over either.** If O1 is rejected, require an updated cash-flow/legal-impact review before a VST/TLN decision, not an automatic headline-triggered trade.
- **E4 — Does Meta belong? 15 points.** For: monetization exposure and better modeled downside diversify supplier earnings. Against: substantial capex, negative quarterly FCF and overlap with Continuity. **Keep 15%; approve the buyer-inclusive mandate and verify household look-through.** No change to Continuity is proposed.
- **E5 — Eight or sixteen holdings? Whole sleeve.** For concentration: stronger modeled returns; against: common buyers and funding risks persist. **Choose nine targeted holdings**, not sixteen by compromise. Top-three weight remains 44%; this is not broad diversification.

Owner can accept O1 and O2 separately. If either fails its price/fundamental gate, retain that funding position pending a new decision. Nothing here authorizes execution or changes the adopted allocation. Supporting analysis and implementation implications follow.

## 1. Top 20 alternatives

### 1.1 Scope, evidence and comparable valuation rules

I read the final analysis, Candidate Ranking, both original deep dives, Prompt 1, the Step 3 model and its reproduction instructions. I reproduced **both** published Step 3 output datasets exactly without modifying their files. New research covered issuer releases and reconciliations, acquisitions/spins, cash conversion, historical prices, current consensus and relevant framework updates. The strongest new candidates were not found by simply selecting the lowest quoted P/E.

All 20 names in the main table are **outside the 58-name Step 3 ranked pool**. Several were mentioned or qualitatively screened in earlier reports; “outside the pool” does not mean nobody previously noticed them. Section 1.5 explicitly revisits those prior objections. Existing-pool challengers MOD, MSFT, FN and ALAB are considered separately below rather than padding the new-name list.

Quotes and consensus were freshly retrieved from Yahoo Finance's public chart/quote-summary data on November 10. The latest completed US session was November 9, so the correct comparable price date is unchanged from Step 3. Prices below are split-adjusted where applicable, in USD; the table uses **11/09/26**. Public verification examples: [WCC history](https://finance.yahoo.com/quote/WCC/history/), [STRL history](https://finance.yahoo.com/quote/STRL/history/), [WCC estimates](https://finance.yahoo.com/quote/WCC/analysis/), [STRL estimates](https://finance.yahoo.com/quote/STRL/analysis/). Vendor consensus is not company guidance, and calendar/fiscal periods differ. Sanmina and Onto released results **after** that close: their valuations combine new information with a pre-announcement price and are watchlist comparisons, not executable quotes.

**A1 held constant for the principal comparison:**

- Terminal date December 31, 2030; **T = 4.14236824 years** from the common price date.
- Ordinary four-state probabilities: **12.5% bust / 12.5% plateau / 50% base / 25% bull**. The displayed three-way bear value is the equal average of bust and plateau, with bucket probabilities **25/50/25**. Existing NRG/VST retain **15/15/45/25**, or **30/45/25** by bucket. New-project political-risk symmetry is tested in §3.
- Owner EPS charges economic SBC once, retains ordinary operating expenses, and avoids awarding both buyback-driven EPS and the cash spent on those buybacks. Where adjusted EPS already includes SBC, no second blanket haircut is applied. Historical GAAP floors retained for some screens are deliberately conservative proxies, not a claim that every acquisition-amortization adjustment has been perfectly normalized.
- Default exit multiples are **0.70× / 0.85× / 1.00× / 1.20×** the selected base P/E. Storage cyclicals have explicit inverse-cycle multiples. Cash/reserves and cumulative dividends are separate.
- `TV(state) = max(0, owner EPS × exit P/E + cash/reserve per share) + cumulative dividends`. `E[TV] = 0.125×bust + 0.125×plateau + 0.50×base + 0.25×bull`; `Expected CAGR = (E[TV]/price)^(1/T) − 1`. Returns are pre-tax, before trading costs; dividends are not assumed reinvested.
- Named paths use the existing A1 rule: `EPS(path) = EPS(base) + λ × s × [EPS(bull) − EPS(base)]`, with **λ = 0.80 for AI-2027** and **2.50 for 100GW**, at the **base** multiple. Cash follows the same interpolation; dividend interpolation uses `min(λ,1)`. The existing EV-valued power names retain Step 3's EBITDA/claims/share-count formulas.

The named-path probabilities remain **35% for the AI-2027 path** and **10% for 100GW**, the latter a bull-subset descriptor. They are overlapping conditional-path judgments, **not additional probabilities added to the 100% state distribution**. The broader expansion base remains 50%. Section 3 distinguishes following that convention from validating every macro or company-level extrapolation.

### 1.2 Ranked alternatives

Ranking is by modeled Expected CAGR, **not permission to allocate**. “A1 screen” means all state/named-path arithmetic is supplied, but it is not equivalent to the full underwriting of the two additions. Confidence and cash/perimeter gates override a deceptively high number. “Expensive” is relative to the modeled opportunity, not necessarily to the stock's recent trading history.

| Rank | Ticker | Bottleneck / theme | Competes with | Price + date | Valuation status | Expected CAGR vs held | AI-2027 CAGR | 100GW CAGR | Verdict | Why or why not |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | STRL | Site preparation, electrical installation | NVT | $290.67 · 11/09/26 | Attractive; full | 19.52% vs 13.68% | 28.67% | 43.73% | Add 5%, NVT −5 | Real execution bottleneck; 14× exit; cap project risk. |
| 2 | WCC | Electrical/datacom distribution and procurement | VST | $316.47 · 11/09/26 | Attractive; full | 18.27% vs 12.97% | 25.67% | 38.39% | Replace VST, 8% | Higher return without relying on power-price rerating; cash conversion essential. |
| 3 | PRIM | Utility and renewable construction | NVT | $71.24 · 11/09/26 | Speculative; A1 screen | 17.54% vs 13.68% | 26.39% | 43.30% | Watchlist, gated 0% | Project losses; historical “bust” EPS exceeds plateau, invalidating apparent safety. |
| 4 | SANM | AI system manufacturing / ZT | CLS | $149.64 · 11/09/26 | Attractive; A1 screen | 16.18% vs 14.80% | 26.78% | 44.20% | Watchlist | Margin normalization and contingent payment narrow edge; after-close release. |
| 5 | SPXC | Cooling towers and HVAC | NVT | $150.92 · 11/09/26 | Fair; A1 screen | 14.69% vs 13.68% | 21.03% | 32.02% | Watchlist | Small expected edge, weaker named paths, cash conversion needs improvement. |
| 6 | EME | Electrical/mechanical contracting | NVT | $652.89 · 11/09/26 | Fair; A1 screen | 13.47% vs 13.68% | 19.97% | 32.30% | Watchlist | Better modeled bust, not a return-led replacement. |
| 7 | ONTO | Advanced packaging inspection/metrology | MU | $194.04 · 11/09/26 | Fair; A1 screen | 13.39% vs 13.09% | 22.91% | 38.60% | Watchlist | New orders matter; MU wins named-path tie-break; after-close price mismatch. |
| 8 | IESC | Electrical installation / datacenters | NVT | $173.92 · 11/09/26 | Speculative; A1 screen | 13.28% vs 13.68% | 22.57% | 39.70% | Watchlist, gated 0% | Thin estimate coverage, older release, split normalization and execution risk. |
| 9 | HUBB | Utility-grid electrical equipment | NVT | $441.57 · 11/09/26 | Fair; A1 screen | 12.09% vs 13.68% | 17.11% | 28.01% | Watchlist | More utility diversity, but slower organic mix and acquisition debt limit upside. |
| 10 | JBL | AI infrastructure manufacturing | CLS | $252.56 · 11/09/26 | Fair; A1 screen | 11.89% vs 14.80% | 21.36% | 36.57% | Reject at price | Growth does not overcome owner-margin and valuation disadvantage. |
| 11 | TER | Semiconductor test | MU | $246.00 · 11/09/26 | Fair; A1 screen | 10.69% vs 13.09% | 19.16% | 32.97% | Reject at price | Recovery is real; valuation already pays for substantial testing growth. |
| 12 | MTZ | Grid/communications construction | NVT | $189.05 · 11/09/26 | Fair; A1 screen | 10.53% vs 13.68% | 17.69% | 30.83% | Reject at price | Project/mix risk without sufficient expected-return compensation. |
| 13 | FIX | Mechanical/electrical installation | VRT | $1,113.23 · 11/09/26 | Fair; A1 screen | 10.21% vs 13.84% | 18.58% | 32.62% | Reject at price | Excellent backlog, but stronger current earnings are already priced. |
| 14 | FICO | Proprietary data / decision infrastructure | META | $723.76 · 11/09/26 | Speculative; A1 screen | 10.10% vs 14.95% | 11.98% | 16.30% | Reject at price | Mortgage-pricing transition and leverage; weak acceleration capture. |
| 15 | FLEX | Power, racks and systems manufacturing | CLS | $78.17 · 11/09/26 | Fair; A1 screen | 9.46% vs 14.80% | 19.16% | 35.54% | Reject at price | Spin complexity and low owner margins; avoid double-counting spin value. |
| 16 | APH | Connectors and interconnect content | CLS | $80.71 · 11/09/26 | Expensive; A1 screen | 9.30% vs 14.80% | 16.89% | 30.89% | Reject at price | Excellent franchise; multiple and acquisition burden consume much of growth. |
| 17 | TT | Thermal equipment / HVAC | VRT | $420.56 · 11/09/26 | Expensive; A1 screen | 9.11% vs 13.84% | 13.37% | 21.31% | Reject at price | Broad HVAC exposure dilutes high-density AI upside. |
| 18 | WDC | Nearline HDD capacity | MU | $289.78 · 11/09/26 | Fair, cyclical; A1 screen | 8.42% vs 13.09% | 20.04% | 36.36% | Reject at price | Cash generation strong; normalize cycle and exclude Sandisk-related gains. |
| 19 | JCI | Applied HVAC / building systems | VRT | $141.49 · 11/09/26 | Expensive; A1 screen | 7.73% vs 13.84% | 13.02% | 22.20% | Reject at price | Genuine demand, but lower owner-earnings upside and material net debt. |
| 20 | STX | HAMR / nearline HDD | MU | $506.14 · 11/09/26 | Fair, cyclical; A1 screen | 7.09% vs 13.09% | 18.53% | 34.29% | Reject at price | Technology leadership does not make peak earnings permanent. |

### 1.3 WCC — replace VST at 8%

**The opportunity.** Wesco connects component availability, procurement, inventory and delivery schedules across electrical and datacom projects. Customers can buy products elsewhere; the scarce service is qualified, coordinated supply at scale. This is a weaker proprietary moat than NVIDIA's platform, but it can capture installation spending without assuming that merchant electricity prices retain every scarcity rent.

**Fresh evidence.** Q3 revenue was $7.23bn, including $1.8bn of datacenter sales growing 55%; non-datacenter sales grew 7%. Adjusted EBITDA margin was 7.8%. Nine-month operating cash flow less capex was **$388.3m**, below the company's $429.9m adjusted FCF measure because the latter adds back digital-transformation/restructuring cash. Net debt was approximately $5.22bn and leverage 2.8×; net debt itself was essentially unchanged from year-end, so improved leverage is not evidence of equivalent debt repayment. Adjusted EPS retains ordinary SBC; do not subtract it twice. These facts support demand, not yet the modeled mature cash conversion. [Wesco Q3 release and reconciliations, October 29](https://www.sec.gov/Archives/edgar/data/929008/000092900826000029/wcc-3q2026earnings.htm).

**Why the discount exists.** Low distribution margins, financing costs, working-capital demands and cyclical customer budgets deserve a discount to high-margin electrical OEMs. That discount can be structural. My thesis is earnings growth at an ordinary multiple, not that WCC becomes an OEM or deserves Grainger's valuation.

**Valuation discipline.** Fresh forward P/E was 14.42×. Distributor peers were GWW 27.77×, FAST 38.68×, AVT 6.36×, ARW 7.12× and Rexel 11.56×; the median is 11.56×. The chosen **14×** is within the own/peer band, near its upper end. This intentionally mixed distribution set spans richer MRO franchises and cheaper electronics distributors; it is a range, not a claim of identical economics. The December 2025 closing price of $244.64 divided by reported FY2025 EPS $13.05 is approximately **18.75×**; current price divided by modeled 2026 EPS $18.39 is **17.21×**. These are ex-post same-year earnings ratios, **not a contemporaneous forward-P/E history or a five-year median**. Historical EPS: [Wesco FY2025 release](https://investors.wesco.com/news-releases/news-release-details/wesco-international-reports-fourth-quarter-and-full-year-2025).

**Operating and financing bridge — my forecasts, not guidance:**

| Input | Base, 2030 | Bull, 2030 | What must happen |
|---|---|---|---|
| Revenue | $40bn | $52bn | Base about $15bn DC plus $25bn other; bull about $25bn plus $27bn. |
| Owner net margin | 5.5% | 6.5% | After ordinary SBC, financing, tax and recurring operating costs. |
| Owner net income | $2.20bn | $3.38bn | Revenue multiplied by owner margin. |
| Diluted shares | 50m | 52m | No EPS benefit from an unfunded buyback program. |
| Owner EPS | $44.00 | $65.00 | Net income divided by diluted shares. |
| Cumulative dividends through 2030 | $10/share | $12/share | Paid out of cash; no terminal dividend perpetuity added. |
| Additional terminal cash value | $0 | $0 | Retained funding is not capitalized a second time. |

Base revenue requires approximately **11.3% annual growth from 2027 consensus revenue of $29.04bn**. That is above the older investor presentation's 5–8% longer-run revenue aspiration. Its 10%+ EBITDA target is an aspiration set before the latest AI ramp, not current guaranteed guidance. [Wesco investor presentation, older than 30 days](https://investors.wesco.com/static-files/6da5e262-57ff-497d-b112-ff02b3aa1af2). My illustrative 2026 segment starting point of $6.5bn DC/$20.4bn other is an extrapolation, not reported annual segment guidance; reaching the base split needs roughly 23%/5% annual growth respectively through 2030.

A concrete base profit bridge is $3.80bn adjusted EBITDA, less approximately $0.26bn physical depreciation, $0.08bn SBC, $0.10bn recurring digital costs and $0.427bn interest, then 25% tax: about $2.20bn owner income. This bridge assumes adjusted EBITDA excludes those listed costs; it does **not** deduct them again from the already derived owner net margin. The bull needs approximately 11% EBITDA margin and stronger scale economics to reach $3.38bn after costs/tax. Neither forecast assumes all announced AI spending turns into distributor profit.

My base owner-FCF path after capex, working capital and an economic SBC charge is **$0.9/$1.2/$1.5/$1.8bn in 2027–2030**, totaling $5.4bn. The 2030 check is $2.20bn owner income + $0.26bn depreciation − $0.35bn capex − $0.31bn incremental working capital = $1.80bn. Allocate roughly $2bn of cumulative FCF to net-debt reduction and $0.5bn to dividends; retain the rest for liquidity/acquisitions **without adding it to terminal value or assuming acquisition earnings for free**. Incremental working capital is already deducted in FCF, not spent twice. This is a demanding improvement from current cash conversion, which is why the position is 8%, not 15%.

| A1 state | Probability | Owner EPS | P/E | Cumulative dividends | Terminal value | Total return |
|---|---|---|---|---|---|---|
| Bust | 12.5% | $13.05 | 9.8× | $7 | $134.89 | −57.38% |
| Plateau | 12.5% | $18.39 | 11.9× | $8 | $226.84 | −28.32% |
| Base | 50.0% | $44.00 | 14.0× | $10 | $626.00 | +97.81% |
| Bull | 25.0% | $65.00 | 16.8× | $12 | $1,104.00 | +248.85% |

Bear-bucket TV **$180.87** (−42.85%), base **$626**, bull **$1,104**, probabilities **25/50/25**. **E[TV] $634.2164; expected total return +100.40%; Expected CAGR 18.27%.** The bust uses reported GAAP EPS as a conservative historical floor, retaining amortization rather than inventing an unsupported normalized addback. Forward owner margins explicitly include economic SBC and financing costs.

For the named paths, `s=0.8`: AI-2027 EPS **$57.44**, dividends **$11.28**, TV **$815.44**, CAGR **25.67%**. At 100GW, EPS **$86**, dividends **$11.60**, TV **$1,215.60**, CAGR **38.39%**. These retain 14×, not the bull's richer multiple. The extreme EPS remains a mechanical A1 sensitivity, not an independently contracted revenue forecast.

**Why displace VST:** advantages of **5.31pp expected**, **5.47pp AI-2027** and **11.62pp 100GW**, with a roughly 9.77-point milder single-name bust. It also reduces direct generation/retail power exposure. WCC still depends on hyperscaler budgets, approvals, suppliers and customer credit; it is **not** a hedge against a wholesale construction stop. Existing power scarcity can benefit VST, so the recommendation rests on relative valuation, not “Texas is uninvestable.” NRG's higher expected return and 12% cap make it the retained power exposure.

**Catalysts and falsifiers.** Further backlog conversion, sustained DC orders and real deleveraging could establish earnings durability. Re-underwrite if DC growth falls below 15% without offsetting non-DC strength; raw FCF/owner income remains below 50% for two reporting periods; leverage exceeds 3.5×; shares approach 55m without proportional earnings; or project cancellations invalidate the revenue split. Persistent inability to move margins toward the modeled range is a thesis failure, not merely a delayed rerating.

**Confidence 3/5. Entry rule:** fresh quote at or below **$330**, no material estimate/cash-conversion deterioration, and owner approval. At $330 the stock's modeled Expected CAGR is **17.08%**, still above VST's 12.97%. A statistical confidence interval is unavailable; this is an underwriting score.

### 1.4 STRL — add 5%, funded by NVT

**The opportunity.** Sterling supplies the site and electrical work that converts purchased equipment into usable capacity. Its value depends on trained crews, project management and execution, not possession of a patent monopoly. The addition broadens the route by which the fund captures AI construction spending; it does not diversify away the spending cycle.

**Fresh evidence.** Q3 revenue was $1.56bn, up 127%, with 70% organic growth; E-Infrastructure revenue was $1.30bn. Signed backlog was **$4.14bn**; the $6.14bn combined figure includes $2bn of unsigned work. FY2026 adjusted EPS guidance was $21.70–21.96. Nine-month CFO less capex was **$311.6m**, after a substantial working-capital outflow. Contract liabilities of approximately $917m require attention: customer-funded cash is not automatically distributable surplus. Cash was approximately $217m versus $95m debt, excluding leases. [Sterling Q3 release, October 28](https://www.strlco.com/news/sterling-reports-record-third-quarter-results-and-raises-full-year-2026-guidance/).

**Why the discount exists.** Recent growth includes acquisition/perimeter effects; investors must distinguish organic growth from purchased earnings. Customer concentration, labor constraints, fixed-price mistakes and cancelled site approvals can rapidly impair contractor profit. The firm's [2025 10-K](https://www.sec.gov/Archives/edgar/data/874238/000087423826000024/strl-20251231.htm) describes project and geographic exposure, including Texas operations. I did not obtain a reliable current Texas share of consolidated profit. That unresolved exposure justifies a **5% ceiling**, not a claim that STRL eliminates the portfolio's Texas risk.

**Valuation discipline.** Fresh forward P/E was **10.34×**. Comparable contractor forward multiples were EME 15.97×, FIX 16.59×, MTZ 15.47×, IESC approximately 12.87× and PRIM 13.40×: median **15.47×**. Select **14×**, within the band and below that median, rather than awarding a datacenter-OEM multiple. The December 2025 close of $306.23 divided by reconstructed 2025 owner EPS $10.2586 is approximately **29.85×**; today's price divided by the 2026 owner anchor is **13.94×**. These ex-post ratios illustrate earnings catch-up, not a valid continuous forward-multiple history. A return to 30× is not part of the case.

**Owner-earnings bridge.** The adjusted EPS measure excludes SBC, so I charge it back: 2025 owner EPS = `10.88 − 24m×0.80/30.9m = $10.25864`; 2026 owner EPS = `21.83 − 38m×0.80/31.1m = $20.85251`. The 20% tax shield is a modeling convention; it is not a claim about the precise reported tax rate. These historical shares and SBC anchor the model, not an extrapolation of future buybacks.

| Input | Base, 2030 | Bull, 2030 | Interpretation |
|---|---|---|---|
| Revenue | $9.0bn | $13.0bn | Base about 15.3% annual growth from $5.86bn 2027 consensus. |
| Owner net margin | 15% | 16% | After SBC, interest, taxes and noncontrolling interests. |
| Owner net income | $1.35bn | $2.08bn | Real earnings, not EBITDA treated as distributable cash. |
| Diluted shares | 31.5m | 33.0m | No funded buyback assumption; allow dilution. |
| Owner EPS | $42.8571 | $63.0303 | Revenue × margin / shares. |
| Dividends / terminal cash add-on | $0 / $0 | $0 / $0 | No credit for distributing or double-counting working cash. |

A base operating cross-check is a 20% EBIT margin **after SBC**, $60m net interest, 20% tax and $42m noncontrolling interests: `(9bn×20% − 0.060bn)×0.80 − 0.042bn = $1.35bn`. Bull uses 21.5% EBIT margin, $80m interest and $92m noncontrolling interests, producing $2.08bn. These are forecasts, not issuer targets. They require continued high-value project mix and controlled labor/rework costs, not simply more contracted revenue.

Base owner FCF after capex/working capital is modeled at **$0.60/$0.80/$1.00/$1.15bn in 2027–2030**, or $3.55bn cumulatively. The terminal-year check is $1.35bn owner income + $0.18bn depreciation − $0.28bn capex − $0.10bn working capital = $1.15bn. Cash retained for capacity, bonding, acquisitions and liquidity gets **no separate terminal-value credit**. Forecast EPS does not also assume that this entire balance buys back shares. Customer advances are not annualized into permanent cash generation.

| A1 state | Probability | Owner EPS | P/E | Terminal value | Total return |
|---|---|---|---|---|---|
| Bust | 12.5% | $10.2586 | 9.8× | $100.53 | −65.41% |
| Plateau | 12.5% | $20.8525 | 11.9× | $248.14 | −14.63% |
| Base | 50.0% | $42.8571 | 14.0× | $600.00 | +106.42% |
| Bull | 25.0% | $63.0303 | 16.8× | $1,058.91 | +264.30% |

Bear-bucket TV **$174.34** (−40.02%), base **$600**, bull **$1,058.91**, probabilities **25/50/25**. **E[TV] $608.3122; expected total return +109.28%; Expected CAGR 19.52%.** Historical acquisition perimeters limit the precision of any “return to 2025” bust; the explicit downside stresses in §3 are essential.

With `s=1`, AI-2027 EPS **$58.9957**, TV **$825.94**, CAGR **28.67%**; 100GW EPS **$93.2900**, TV **$1,306.06**, CAGR **43.73%**, both at 14×. The extreme path assumes that crew capacity, project funding and permits expand enough to monetize demand; it is not an assertion that all of today's unsigned work is guaranteed.

**Why fund from NVT:** advantages of **5.84pp expected**, **7.27pp AI-2027** and **9.70pp 100GW**. The trade worsens the isolated bust by about 5.46 points, or only **0.27 percentage point at portfolio weight 5%**, while O1 more than offsets it. NVT remains a strong business at 7%; this is an opportunity-cost trim, not a broken-thesis sale. Funding STRL from MU buys an immaterial additional 0.028pp portfolio expected return but sacrifices approximately 0.27pp AI-2027 and 0.59pp 100GW return. Preserve the memory bottleneck exposure under the prompt's close-call tie-break.

**Catalysts and falsifiers.** Signed backlog converting at stable margins, clean cash conversion after working-capital investment and repeatable electrical integration would validate the discount. Re-underwrite on signed book-to-burn below 1 for two periods; owner-FCF conversion below 60% without a credible timing bridge; customer advances reversing faster than cash collections; permit/cancellation losses affecting over 15% of signed backlog; or dilution above 34m shares without matching earnings. These are monitoring thresholds chosen here, not issuer covenants. No assumption that unspecified pipeline converts at 100%.

**Confidence 3/5. Entry rule:** refreshed quote at or below **$315**, current project/cash evidence intact, owner approval. At $315 modeled Expected CAGR is **17.22%**. Do not expand beyond 5% before geographic/customer exposure and a further cash-conversion period support it.

### 1.5 Why the other alternatives do not earn capital

**Sanmina deserves serious attention, but not a third change.** The November 9 release reports FY2026 revenue $14.53bn and adjusted EPS $13.28. CFO $944.1m less capex $403.3m gives **positive $540.8m FCF**: a stale negative vendor FCF field is not a valid rejection. Subtract economic SBC from adjusted EPS, normalize a reported tariff benefit and reserve for the acquisition's contingent payment rather than treating fair-value accounting addbacks as free economics. FY2027 guidance calls for revenue $17.5–19.5bn and adjusted EPS $15.50–17.50. [Sanmina FY2026 results](https://ir.sanmina.com/news/news-details/2026/Sanmina-Reports-Fourth-Quarter-and-Fiscal-2026-Financial-Results/default.aspx).

The [investor presentation](https://s201.q4cdn.com/209924174/files/doc_financials/2026/q4/FINAL-SANM-Q4-and-FY26-Presentation-11_9_26.pdf) supports a genuine cloud/AI ramp, including initial Helios shipments; it does not make every prospective platform win firm revenue. The [ZT acquisition announcement](https://ir.sanmina.com/news/news-details/2025/SANMINA-ANNOUNCES-ACQUISITION-OF-DATA-CENTER-INFRASTRUCTURE-MANUFACTURING-BUSINESS-OF-ZT-SYSTEMS-FROM-AMD/default.aspx) discloses up to $450m contingent consideration. The [third-party-hosted earnings-call transcript](https://www.earningswhispers.com/transcript/SANM/Q42026) attributes $0.42 quarterly EPS to tariff recoveries; I deduct that amount conservatively. That transcript is not independently audited primary financial data.

My base/bull revenue $28/$42bn, owner net margin 5.7%/6.5%, and shares 58/62m imply owner EPS $27.52/$44.03. Reserve approximately $450m across state share counts. E[TV] is $278.52 and Expected CAGR 16.18%, versus CLS 14.80%; bust is **−81.52%**. A 5-point CLS-to-SANM swap increases portfolio expected return only **0.07pp** and worsens bust by **0.31pp**. Although the named-path tie-break favors SANM, confidence in newly acquired-system margins and post-announcement pricing is not equal. Require refreshed price, clean cash conversion and a fully reconciled earnout/working-capital bridge. Around **$146**, the current model would clear CLS by about 2pp, but a price threshold alone does not clear those gates. Neither original report fully underwrote SANM; this is a real new challenger, not a previously refuted thesis.

**PRIM: high modeled return, wrong apparent downside floor.** Six challenged renewable projects and reduced guidance make a 2025 EPS floor misleading; the model's $5.02 bust EPS exceeds $2.21 plateau EPS. Its −35.88% “bust” is therefore not credible evidence of defensive economics. Much of backlog consists of master service agreements rather than irrevocable orders. Require two clean execution/cash periods and a project-loss-adjusted downside before allocating; confidence **2/5, zero weight**. [Primoris Q3 release, November 3](https://ir.prim.com/~/media/Files/P/Primoris-IR-v2/press-release/2026/primoris-services-corporation-reports-third-quarter-2026-results.pdf). A mechanical A1 number cannot overrule the reason A1 fails for this particular turnaround.

**SPXC and HUBB: better diversification is not sufficient by itself.** Codex previously rejected SPXC's absence of a verified edge. The new model produces 14.69% expected, only 1.01pp over NVT, with lower AI-2027/100GW returns. Q3 raw FCF was $20.1m; full-year EPS guidance's upper end was trimmed despite growth. That supports watching cash conversion, not paying for another overlapping position. [SPX Q3 release, October 29](https://spx.gcs-web.com/news-releases/news-release-details/spx-reports-third-quarter-2026-results).

Claude's “ETN covers the layer” was not a sufficient rejection of Hubbell, particularly after ETN exited the final. However, Utility organic growth was 5% versus Electrical 22%, with considerable acquisition contribution; net debt rose substantially. Applying AI-like growth to the entire company overstated its opportunity. My revised $9.5/$13bn revenue cases yield only 12.09% expected. Its milder bust can be useful if the owner's objective changes, but it loses under the current return-led mandate. [Hubbell Q3 release, October 27](https://hubbell.gcs-web.com/node/32291).

**EME, FIX and MTZ: re-evaluate economics, not layer coverage.** The earlier claim that PWR already covered construction is no longer relevant because PWR is absent. EMCOR's $18.57bn remaining performance obligations and raised EPS guidance establish demand; my 13.47% expected return still fails to beat NVT meaningfully, and named returns are lower. [EMCOR Q3 release, October 29](https://www.sec.gov/Archives/edgar/data/105634/000010563426000132/eme-ex991_2026930xq3.htm). Comfort's backlog reached $17.81bn and nine-month CFO $2.54bn; I do not annualize customer advances into sustainable cash. At $1,113, even $101 terminal base EPS produces only 10.21% expected. [Comfort Q3 release, October 22](https://investors.comfortsystemsusa.com/news-releases/news-release-details/comfort-systems-usa-reports-third-quarter-2026-results). MasTec's communications weakness and execution history remain material; the $9.11 adjusted EPS anchor is not interchangeable with GAAP earnings. Expected return 10.53% is inadequate compensation. [MasTec Q3 release, October 29](https://investors.mastec.com/node/20611).

**IESC: promising bottleneck, incomplete confidence.** Its July 31 report is **stale by more than 30 days**. Reported per-share results preceded the 2-for-1 split; I normalized them rather than comparing pre-split EPS to post-split price. Only one analyst supports the forward estimate used here. The modeled 13.28% expected and attractive named upside do not justify a position before fresh results, split/perimeter reconciliation and a stronger cash bridge. [IES Q3 release](https://investors.ies-corporate.com/news-releases/news-release-details/ies-holdings-reports-fiscal-2026-third-quarter-results-and). Confidence 2/5 is a gate, not a reason to quietly use a full weight anyway.

**JBL and FLEX: volume does not equal owner profit.** Jabil's FY2027 $44.5bn revenue/$17.55 core-EPS guide supports the AI ramp; FY2026 SBC must still be charged against core earnings. I use normalized owner EPS $12.04 for the plateau and $36/$55 for base/bull, but only 11× terminal P/E. Expected 11.89% loses to CLS. [Jabil FY2026 release, September 30 — stale >30 days](https://www.sec.gov/Archives/edgar/data/898293/000162828026063890/jbl-20260930ex991.htm). FLEX's raised outlook and real FCF are encouraging, but owner margins and the planned Axiom separation require caution. The valuation represents the combined value accruing to today's shareholder; it does not add spin proceeds to an unchanged parent earnings stream. A small downside reserve recognizes separation costs. The previous Codex objection about margins/execution still holds at 9.46% expected. [Flex Q2 FY2027 release, October 28](https://investors.flex.com/news/news-details/2026/FLEX-REPORTS-SECOND-QUARTER-FISCAL-2027-RESULTS/default.aspx).

**ONTO and TER: prior price declines were not adequate rejection reasons.** Onto's November 9 release shows strong revenue, orders and a higher Q4 guide. Its adjusted EPS reconciliation retains regular SBC; subtracting SBC again would understate owner earnings. The updated 13.39% expected return is credible enough for a watchlist, but MU's 26.81%/45.33% named returns win the close-call comparison. [Onto Q3 release](https://investors.ontoinnovation.com/news/news-details/2026/Onto-Innovation-Reports-2026-Third-Quarter-Results/default.aspx). Teradyne's AI test demand is real; my $18.41/$27 terminal EPS cases acknowledge it. Expected return still reaches only 10.69%, with a severe cyclical bust. [Teradyne Q3 release, October 27](https://investors.teradyne.com/sec-filings/all-sec-filings/content/0001193125-26-434981/ter-ex99_1.htm). These are current fundamental comparisons, not “down a lot for a reason.”

**WDC and STX: strong businesses at peak-cycle-looking earnings.** HDD scarcity and Seagate's HAMR execution deserve more respect than a generic “less bottleneck intensity” label. WD reported $1.38bn quarterly FCF and Seagate $1.48bn. Nevertheless, near-term consensus EPS is far above a normalized cycle; WD's GAAP annual figure also includes Sandisk-related gains. Explicit inverse-cycle multiples, normalized downside EPS and generous retained-cash allowances still yield only 8.42%/7.09% expected. Their named returns remain below MU's. [WD Q1 FY2027 release, October 22](https://wdc.gcs-web.com/news-releases/news-release-details/wd-reports-fiscal-first-quarter-2027-financial-results), [Seagate Q1 FY2027 release, October 27](https://investors.seagate.com/news/news-details/2026/Seagate-Technology-Reports-Fiscal-First-Quarter-2027-Financial-Results/default.aspx). Do not call 7× peak EPS a deep discount without normalizing that denominator.

**APH, TT and JCI: leaders, but not superior stocks here.** APH's post-split share base and acquisition debt matter; the model uses approximately 2.5–2.6bn diluted shares and no duplicate SBC deduction. Its 9.30% expected return confirms the earlier lack of incremental valuation edge. [Amphenol Q3 release](https://investors.amphenol.com/news-and-events/news-details/2026/Amphenol-Reports-Record-Third-Quarter-2026-Results-and-Announces-Dividend-Increase-and-New-Stock-Repurchase-Program/default.aspx). Trane's broad HVAC economics dilute the named-path upside relative to Vertiv. [Trane Q3 release](https://investors.tranetechnologies.com/news-and-events/news-release-details/2026/Trane-Technologies-Reports-Strong-Third-Quarter-Results-Raises-Full-Year-Revenue-Guidance-Reaffirms-Full-Year-EPS-Guidance/default.aspx). JCI's $23bn backlog and 44% organic orders growth are strong, but exclude discontinued operations: reported continuing diluted EPS was $2.63 in FY2025 and adjusted continuing EPS $5.16 in FY2026. Those primary figures replace inconsistent vendor/initial working estimates. [JCI FY2026 release, October 27](https://www.sec.gov/Archives/edgar/data/833444/000083344426000101/q4exh991xq4fy26earningsrel.htm).

**FICO: the discount has a substantive cause.** Management declined FY2027 guidance during the mortgage-pricing transition; debt and one-off settlement/accounting items complicate headline EPS. My owner-earnings cases do not presume unlimited pricing power or free buybacks. Expected 10.10% and modest named-path upside lose to META. This sustains the prior regulatory/pricing objection with current evidence rather than the share-price decline itself. [FICO FY2026 release, November 4](https://investors.fico.com/news-releases/news-release-details/fico-announces-earnings-812-share-fourth-quarter-fiscal-2026).

### 1.6 Existing-pool challenges: what did the ranking get wrong?

I did not find an **actionable A1** omitted-pool replacement strong enough to displace WCC/STRL from the main list. That is narrower than endorsing every published rank.

- **ALAB:** reconstructing owner earnings with current results raises Expected CAGR to **5.93%**, versus the old negative screen; AI-2027/100GW are **16.41%/33.57%**. Q3 SBC was $82.6m and GAAP tax effects require normalization. It still does not beat the held set. Model EPS $1.22/$3.40/$10/$17.0667, base P/E 26×, `s=1`, no cash/dividends. [Astera Q3 release, November 3](https://www.asteralabs.com/news/astera-labs-reports-third-quarter-2026-financial-results/).
- **FN:** the fresh full-state reconstruction gives **4.71% expected**, **12.63% AI-2027**, **27.18% 100GW** at $365.94. Its large GAAP/non-GAAP EPS difference must not disappear in an “owner” model. Inputs $13.05/$15.70/$27.6316/$43, 15×, `s=1`; base revenue $10bn, owner margin 10.5%, shares 38m; bull $16bn/10.75%/40m. A strong business, not a superior allocation. [Fabrinet Q1 FY2027 release, November 2](https://investor.fabrinet.com/news-releases/news-release-details/fabrinet-announces-first-quarter-fiscal-year-2027-financial).
- **MOD:** the exclusion is defensible pending its cash/perimeter gate; the investor-day date is now independently confirmed. See E1 and §3.6.
- **MSFT:** the A1 exclusion is not overturned. The stronger finding is that the published **alternative-multiple robustness claim** does not survive a feasible replacement test; see §4. That does not justify importing Microsoft's higher alternative multiple into an otherwise A1 portfolio.

### 1.7 Numerical input ledger for reproducibility

The following is the complete incremental input set. EPS order is **bust / plateau / base / bull**; all numbers are USD per current share. Default state multiples and probabilities are in §1.1. `D` and `C` are four-state cumulative dividends and terminal cash/reserves. Figures are rounded for presentation; the explicit operating formulas for the additions govern their exact values.

| Ticker | Owner EPS: four states | Base P/E | s | D: four states | C: four states |
|---|---|---|---|---|---|
| STRL | 10.258641 / 20.852508 / 42.857143 / 63.030303 | 14 | 1.0 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 |
| WCC | 13.05 / 18.39 / 44 / 65 | 14 | 0.8 | 7 / 8 / 10 / 12 | 0 / 0 / 0 / 0 |
| PRIM | 5.02 / 2.21 / 9.818182 / 17.068966 | 13 | 0.8 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 |
| SANM | 5.12 / 11.39 / 27.517241 / 44.032258 | 10 | 1.0 | 0 / 0 / 0 / 0 | −8.18 / −8.18 / −7.76 / −7.26 |
| SPXC | 5.03 / 8.35 / 15.576923 / 21.818182 | 17 | 0.8 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 |
| EME | 28.19 / 35 / 66 / 97.872340 | 16 | 0.8 | 4 / 4.5 / 5 / 6 | 0 / 0 / 0 / 0 |
| ONTO | 2.78 / 8.47 / 17.647059 / 27.259259 | 18 | 1.0 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 |
| IESC | 7.51 / 11.57 / 19.090909 / 31.304348 | 14 | 1.0 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 |
| HUBB | 16.54 / 20.50 / 32.264151 / 48.148148 | 20 | 0.7 | 21 / 22 / 24 / 28 | 0 / 0 / 0 / 0 |
| JBL | 8.98 / 12.04 / 36 / 55 | 11 | 1.0 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 |
| TER | 3.47 / 9.44 / 18.40625 / 27 | 20 | 1.0 | 2 / 2 / 2.5 / 3 | 0 / 0 / 0 / 0 |
| MTZ | 5.07 / 9.11 / 18.333333 / 28.351064 | 15 | 0.8 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 |
| FIX | 28.88 / 50.73 / 101.111111 / 150 | 16 | 1.0 | 7 / 8 / 10 / 12 | 0 / 0 / 0 / 0 |
| FICO | 26.54 / 36.32 / 59.130435 / 80.510638 | 18 | 0.3 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 |
| FLEX | 2.99 / 4.65 / 10.8 / 17.5 | 10 | 1.0 | 0 / 0 / 0 / 0 | −2 / −1 / 0 / 0 |
| APH | 1.67 / 2.835 / 4.94 / 7.673077 | 22 | 0.9 | 1.4 / 1.5 / 1.8 / 2.2 | 0 / 0 / 0 / 0 |
| TT | 12.98 / 15.25 / 25.116279 / 33.454545 | 23 | 0.7 | 17 / 18 / 20 / 24 | 0 / 0 / 0 / 0 |
| WDC | 10 / 24.2 / 48 / 75 | 7.5* | 1.0 | 2 / 3 / 4 / 6 | 0 / 0 / 50 / 100 |
| JCI | 2.63 / 5.16 / 9.75 / 13.709677 | 19 | 0.7 | 6 / 6.5 / 7 / 8 | 0 / 0 / 0 / 0 |
| STX | 13.90 / 39 / 80 / 125 | 7.5* | 1.0 | 10 / 12 / 15 / 18 | 0 / 0 / 80 / 150 |

\* WDC/STX explicit four-state multiples are **10 / 9 / 7.5 / 7**. Their retained-cash assumptions are scenario allowances **after** capex, dividends and required financing, not present cash balances. At illustrative share counts of 380m/230m, the base allowances are about $19bn/$18.4bn. No further buyback EPS uplift is credited. Their normalized cyclical downside EPS is judgment, not reported FY2025 owner EPS; neither name is promoted to a fully underwritten addition. Removing these generous cash allowances only strengthens the rejection.

Additional base/bull operating bridges, expressed as **revenue $bn / owner net margin / diluted shares millions**, make the principal screen forecasts inspectable:

| Ticker | Base bridge | Bull bridge |
|---|---|---|
| SANM | 28 / 5.7% / 58 | 42 / 6.5% / 62 |
| PRIM | 12 / 4.5% / 55 | 16.5 / 6% / 58 |
| SPXC | 4.5 / 18% / 52 | 6 / 20% / 55 |
| EME | 33 / 9% / 45 | 46 / 10% / 47 |
| ONTO | 3 / 30% / 51 | 4.6 / 32% / 54 |
| IESC | 8 / 10.5% / 44 | 12 / 12% / 46 |
| HUBB | 9.5 / 18% / 53 | 13 / 20% / 54 |
| TER | 9.5 / 31% / 160 | 13.5 / 34% / 170 |
| MTZ | 30 / 5.5% / 90 | 41 / 6.5% / 94 |
| FIX | 26 / 14% / 36 | 38 / 15% / 38 |
| FICO | 3.4 / 40% / 23 | 4.4 / 43% / 23.5 |
| APH | 65 / 19% / 2,500 | 95 / 21% / 2,600 |
| TT | 36 / 15% / 215 | 46 / 16% / 220 |
| JCI | 39 / 15% / 600 | 50 / 17% / 620 |

These are independent forecasts, **not consensus 2030 estimates**. For the remaining rejected screens JBL/FLEX/WDC/STX, terminal EPS is a directional scenario input rather than a fully financed segment build. That limitation cannot support an Add verdict and is not hidden by calling every row “full.” Historical anchors are normalized where reconciliations permit; otherwise conservative reported EPS is retained and identified as a proxy. The main additions have explicit financing/cash/share bridges above.

**Multiple evidence cross-check.** All cited forward ratios are the fresh November 9 snapshot. EMS reference median CLS/DELL/HPE is approximately **10.04×**: own ratios JBL 11.39, FLEX 10.05, SANM 9.22 support selected 11/10/10×. Broad electrical reference median NVT/VRT/ETN is **20.37×**: own HUBB 19.15, SPXC 15.45, APH 22.27, TT 23.71 and JCI 19.10 support 20/17/22/23/19×. That reference is a rough sector anchor, not proof that a connector or HVAC company has identical economics. Contractor median **15.47×** and own EME 15.97/FIX 16.59/MTZ 15.47/PRIM 13.40 support 16/16/15/13×. IESC's own ratio is approximately 12.87× using the thinly covered FY2027 estimate; 14× lies inside the contractor band.

WFE reference AMAT/LRCX/KLAC/ASML has a median approximately **20.65×**; own ONTO 16.29/TER 20.52 supports 18/20×. Data references RELX/VRSK/SPGI have median **23.04×**; own FICO 14.08 supports 18× without assuming a return to its historical premium. Storage's own WDC 7.17/STX 7.75 brackets 7.5×, but the inverse-cycle policy is more important than that superficial match. Small choices just below the lower band are conservative rounding; none relies on an unexplained premium multiple. **The common forward-multiple/terminal-trailing-EPS convention is inherited from A1**, not presented as an exact accounting equivalence.

## 2. Weakest current holdings

### 2.1 Rank all eight: return is not the same as conviction

Holding models remain the published A1 inputs, so this is a weight/opportunity-cost critique rather than an undisclosed rewrite of their earnings. Conviction ranks are my qualitative assessment of business evidence, cash quality and uncertainty; they are not calibrated probabilities. NVIDIA's business conviction is high while its deployment gate is separate. NVT's integration exposure keeps its score below VRT's despite good current demand.

| Expected-return rank | Ticker | Final weight | Expected CAGR | AI-2027 CAGR | 100GW CAGR | Conviction rank / score | Implication |
|---|---|---|---|---|---|---|---|
| 1 | NVDA | 15% | 17.80% | 26.78% | 41.52% | 1 / 4 of 5, event-gated | Keep target cap; pause incremental deployment until gate. |
| 2 | NRG | 12% | 17.07% | 24.87% | 35.57% | 5 / 3 of 5 | Keep risk cap; no automatic increase after VST exits. |
| 3 | META | 15% | 14.95% | 20.00% | 33.91% | 3 / 4 of 5 | Keep; monetization rather than supplier exposure. |
| 4 | CLS | 10% | 14.80% | 23.23% | 35.64% | 7 / 3 of 5 | Keep dilution/cash cap; SANM edge not yet bankable. |
| 5 | VRT | 14% | 13.84% | 22.03% | 34.86% | 2 / 4 of 5 | Keep strong execution exposure. |
| 6 | NVT | 12% | 13.68% | 21.41% | 34.03% | 4 / 3 of 5 | Trim 5 points to STRL, retain a material core. |
| 7 | MU | 14% | 13.09% | 26.81% | 45.33% | 6 / 3 of 5 | Keep despite low expected rank; wins acceleration tie-break. |
| 8 | VST | 8% | 12.97% | 20.20% | 26.77% | 8 / 3 of 5 | Replace with WCC. |

### 2.2 Bottom five, examined rather than automatically sold

| Ticker | Final % | Expected CAGR | AI-2027 CAGR | 100GW CAGR | Main weakness | Best replacement | Decision | Why |
|---|---|---|---|---|---|---|---|---|
| CLS | 10 | 14.80% | 23.23% | 35.64% | Customer concentration, capex, dilution and severe bust | SANM, conditional | Keep 10 | SANM adds just 0.07pp portfolio E at a 5-point swap and has lower cash/perimeter confidence. |
| VRT | 14 | 13.84% | 22.03% | 34.86% | High starting expectations; hyperscaler capex dependence | STRL; MOD after gate | Keep 14 | Favor NVT funding for STRL; marginal modeled differences are tiny, VRT execution conviction higher. |
| NVT | 12 | 13.68% | 21.41% | 34.03% | Integration and overlapping electrical/thermal exposure | STRL | Trim to 7 | STRL's return advantage is material, while 7% retains NVT's product franchise. |
| MU | 14 | 13.09% | 26.81% | 45.33% | Peak margins, supply response and eventual memory-cycle reversal | STRL on E alone | Keep 14 | MU's named-path advantage is valuable under the stated mandate; LTAs are not permanent margin guarantees. |
| VST | 8 | 12.97% | 20.20% | 26.77% | Leverage, acquisition/claims bridge, duplicate power risk | WCC | Replace | Clearer expected and named-path gains than a VST/TLN geographic shuffle. |

The fresh evidence does **not** support declaring the retained bottom-ranked businesses broken:

- **CLS:** the 2027 revenue/EPS outlook is strong, but the equity raise, investment program and limited near-term FCF explain the 10% cap. Strong sales do not remove funding risk. [Celestica Q3 release, October 26](https://www.sec.gov/Archives/edgar/data/1030894/000103089426000049/cls-20260930prcondensedfs.htm).
- **VRT/NVT:** Vertiv's orders and cash conversion are strong; nVent's Q3 organic growth was 44% and FCF $268m, with Maverick acquired October 1. The trim is about the next dollar, not extrapolating a slowdown that the releases do not show. [Vertiv Q3 release](https://www.sec.gov/Archives/edgar/data/1674101/000162828026067707/q32026exhibit991vrt10282026.htm), [nVent Q3 release](https://www.sec.gov/Archives/edgar/data/1720635/000162828026068391/q32026nvtpressrelease.htm).
- **MU:** strategic agreements cover a substantial portion of revenue through 2030, but floors and ceilings do not lock in current peak margins. Do not confuse total DRAM/NAND revenue with HBM revenue when evaluating the macro forecast. [Micron FY2026 prepared remarks, September 30 — stale >30 days](https://s25.q4cdn.com/621799436/files/doc_financials/2026/q4/Q4-FY26-Prepared-Remarks.pdf).
- **VST:** current generation and contracted capacity can retain value even if new datacenter approvals slow; its raised 2027 EBITDA guidance includes acquisition effects that must be matched to claims and shares. [Vistra Q3 release, November 6](https://www.sec.gov/Archives/edgar/data/1692819/000169281926000023/vistra-20260930xearningsre.htm).

NRG remains the better power allocation, but its sale proceeds and acquired earnings must be counted once, not both as debt reduction and unchanged earnings. [NRG Q3 release, November 9](https://investors.nrg.com/news-releases/news-release-details/nrg-energy-reports-third-quarter-2026-results-reaffirms-2026). META's monetization thesis does not make it a cash substitute: Q3 FCF was negative amid heavy investment. [Meta Q3 release, October 21](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Third-Quarter-2026-Results/default.aspx).

## 3. Allocation optimization

### 3.1 Proposed allocation — two decisions, not a compromise average

All weights refer to the sleeve. The changes are relative to **Step 3's proposed targets**, not the owner's live holdings or tax lots. An instruction to execute Step 4 is not authority to trade. Costs, tax consequences and actual position drift require a separate implementation check.

| Ticker | Final % | Proposed % | Delta | Funding source | Reason |
|---|---|---|---|---|---|
| NVDA | 15.0 | 15.0 | 0.0 | Unchanged | Highest-return eligible incumbent; governance/earnings gate governs timing. |
| META | 15.0 | 15.0 | 0.0 | Unchanged | Monetization exposure; mandate/household overlap needs owner acceptance. |
| VRT | 14.0 | 14.0 | 0.0 | Unchanged | High execution conviction; preserve cooling exposure. |
| MU | 14.0 | 14.0 | 0.0 | Unchanged | Strongest 100GW return; retain named-path tie-break. |
| NRG | 12.0 | 12.0 | 0.0 | Unchanged | Better power return; retain 12% claims/political-risk cap. |
| CLS | 10.0 | 10.0 | 0.0 | Unchanged | Better established owner bridge than SANM; maintain 10% cap. |
| WCC | 0.0 | 8.0 | +8.0 | VST −8.0 | O1: distribution/procurement at superior relative return. |
| NVT | 12.0 | 7.0 | −5.0 | Funds STRL | O2: preserve core, release capital for higher-return execution exposure. |
| STRL | 0.0 | 5.0 | +5.0 | NVT −5.0 | O2: attractive contractor economics, capped for project/permission risk. |
| VST | 8.0 | 0.0 | −8.0 | Funds WCC | O1: weakest return and duplicate power exposure. |
| **Checksum** | **100.0** | **100.0** | **0.0** | **13.0 added = 13.0 removed** | **Four ticker-weight changes; two paired decisions; nine nonzero holdings.** |

**Constraints:** maximum name weight 15%; NRG ≤12%, NVT ≤12%, CLS ≤10%; semiconductor/server cluster 39% ≤50%; NRG+VST 12% ≤20%; no confidence-2 candidate enters; no derivatives, leverage or private investments; no mandatory sleeve quotas. The primary bust is less severe than the V9.1 comparison's approximately −67.3%. Foundation, Continuity and the zero Moonshot target remain unchanged. At an approximately 50% household Event Horizon sleeve, WCC/STRL would be about **4%/2.5% of household assets**, before any overlap elsewhere.

**Why WCC only 8% and STRL only 5% when they rank so highly?** These are new underwriting limits, not inherited sector quotas: WCC's cash conversion/leverage and STRL's customer/project/geographic uncertainty do not justify maximum positions. The limits are explicitly judgmental and can be relaxed only with better evidence. The target is a constrained, confidence-aware recommendation, **not proof of a unique mathematical global optimum over every listed company**.

### 3.2 Portfolio returns — aggregate terminal wealth first

For each path, portfolio wealth is `Σ(weight × stock terminal value / stock price)`. Expected portfolio CAGR is the CAGR of that expected wealth; it is **not** the weighted average of stock CAGRs. Bust and plateau below are simultaneous terminal-state losses, not predicted maximum interim drawdowns.

| Metric | Step 3 final | Proposed | Change |
|---|---|---|---|
| Expected terminal wealth per $1 | 1.779720 | 1.827085 | +0.047365 |
| Expected total return | +77.97% | +82.71% | +4.74pp |
| **Expected CAGR** | **14.93%** | **15.66%** | **+0.73pp** |
| **AI-2027 Scenario CAGR** | **23.43%** | **24.24%** | **+0.80pp** |
| **100GW 2030 Scenario CAGR** | **36.88%** | **38.21%** | **+1.33pp** |
| **Bust-case total return** | **−61.80%** | **−61.29%** | **+0.51pp** |
| Plateau / 2–3-year delay total return | −23.87% | −23.31% | +0.56pp |
| Base total return | +76.55% | +79.73% | +3.17pp |
| Bull total return | +206.72% | +216.71% | +9.99pp |
| Number of holdings | 8 | 9 | +1 |
| Top-three weight | 44% | 44% | Unchanged |
| HHI, sum of squared weights | 0.1294 | 0.1224 | −0.0070 |

For a complete recommended-holding valuation reference, the incumbents' terminal values below are **carried forward from the reproduced Step 3 model**, not independently reforecast to favor this proposal. All prices are November 9; three CAGRs are in §2 or §1.2. “Bear” here is the bucket average, not the bust loss reported separately.

| Ticker | Price | Status | Bear / base / bull TV | Bucket probabilities | E[TV] | Expected CAGR | Confidence | Key retained assumption |
|---|---|---|---|---|---|---|---|---|
| NVDA | $178.67 | Attractive | $103.95 / $347 / $610.80 | 25/50/25 | $352.19 | 17.80% | 4, event gate | Base owner EPS $19, 18×. |
| META | $641.37 | Attractive | $463.85 / $994.60 / $2,116.56 | 25/50/25 | $1,142.40 | 14.95% | 4 | Base owner EPS $49.23, 20×. |
| VRT | $200.47 | Attractive | $97.36 / $346.50 / $581.60 | 25/50/25 | $342.99 | 13.84% | 4 | Base owner EPS $15, 23×. |
| MU | $733.15 | Deep Discount, cyclical | $416.25 / $1,258 / $1,949.50 | 25/50/25 | $1,220.44 | 13.09% | 3 | Base owner EPS $110, 10× plus cash/dividends. |
| NRG | $97.40 | Attractive | $62.03 / $185.05 / $340.83 | 30/45/25 | $187.09 | 17.07% | 3 | Base EBITDA $6.5bn, 7.3×; $14bn claims/190m shares. |
| CLS | $222.92 | Attractive | $91.55 / $407.96 / $672 | 25/50/25 | $394.87 | 14.80% | 3 | Base owner EPS $29.14, 14×; dilution included. |
| WCC | $316.47 | Attractive | $180.87 / $626 / $1,104 | 25/50/25 | $634.22 | 18.27% | 3 | Base $40bn revenue, 5.5% owner margin, 50m shares, 14×. |
| NVT | $114.44 | Attractive | $66.33 / $194 / $324.20 | 25/50/25 | $194.63 | 13.68% | 3 | Base owner EPS $10, 19×. |
| STRL | $290.67 | Attractive | $174.34 / $600 / $1,058.91 | 25/50/25 | $608.31 | 19.52% | 3 | Base $9bn revenue, 15% owner margin, 31.5m shares, 14×. |

### 3.3 Test the weights and alternative funding choices

| Construction | Expected CAGR | AI-2027 CAGR | 100GW CAGR | Bust return | Decision |
|---|---|---|---|---|---|
| Step 3 unchanged | 14.93% | 23.43% | 36.88% | −61.80% | Baseline. |
| Existing-eight cosmetic reweight: VRT +1, MU +1, VST −2 | 14.94% | 23.52% | 37.13% | −61.82% | Reject tiny expected gain. |
| O1 only: WCC 8 for VST 8 | 15.36% | 23.86% | 37.72% | −61.02% | Independently worthwhile if O2 rejected. |
| STRL 5 for VST 5, no WCC | 15.27% | 23.87% | 37.69% | −61.71% | Credible fallback, but not the selected funding plan. |
| WCC 8 for VST; STRL 5 from MU | 15.69% | 23.97% | 37.62% | −61.09% | Higher E by only 0.028pp; inferior acceleration exposure. |
| WCC 8 for VST; STRL 5 from VRT | 15.65% | 24.21% | 38.17% | −60.68% | Better bust, but not the objective; prefer retaining higher-conviction VRT. |
| **WCC 8 for VST; STRL 5 from NVT** | **15.66%** | **24.24%** | **38.21%** | **−61.29%** | **Selected.** |
| New-name caps fixed, pure expected-wealth ranking | 15.70% | 23.92% | 37.51% | −61.17% | VRT 15/NVT 12/MU 8; reject 0.035pp gain at cost of fast-path upside. |
| SANM 5 for CLS 5, otherwise baseline | 15.00% | 23.62% | 37.34% | −62.11% | Too little expected gain for uncertainty/new position. |
| HUBB 8 for VST 8, otherwise baseline | 14.87% | 23.21% | 36.96% | −59.85% | Defensive diversification costs expected return. |

The pure expected-wealth allocation in the table retains all other selected weights; its VRT/NVT/MU changes are stated explicitly. With a common horizon and fixed terminal outcomes, maximizing expected wealth is a linear allocation problem. The actual prompt adds confidence constraints and the roughly 2pp stock-level AI-path tie-break, which is why I do not force the numerically largest E to be the final answer. No 0.01pp cosmetic optimization is worth implying false precision.

### 3.4 Shared economic drivers and holding count

| Driver grouping | Step 3 | Proposed | Interpretation |
|---|---|---|---|
| C1: NVDA + MU + CLS | 39% | 39% | Same accelerator/memory/server manufacturing chain. |
| C3: thermal/electrical/install/distribute | 26% | 34% | VRT 14 + NVT 7 + WCC 8 + STRL 5; still common project approvals. |
| C4: power generators/retailers | 20% | 12% | NRG retained; VST removed. |
| C5: monetizing platform | 15% | 15% | META; still the same AI investment ecosystem. |
| C3 + C4 combined | 46% | 46% | No reduction in broad power/site-buildout exposure. |

Counting tickers overstates diversification when the customers are the same hyperscalers, projects use the same financing and permits, and supplier orders respond to the same spending revision. WCC's non-DC distribution and STRL's project mix offer some diversification **within** the cycle, not independence from it. No empirical correlation estimate or reliable current revenue-weighted Texas map was established; a numerical “correlation-adjusted” diversification benefit would be invented precision.

Nine names is appropriate **for this proposal** because the incremental position has a distinct return case. The evidence does not favor adding seven weaker names merely to reach sixteen. The existing 16-name alternative's approximately 13.6% expected/−59.2% bust trade-off may be preferable for an owner with a different loss tolerance, but that changes the objective. A modeled 61% sleeve loss remains severe; at a 50% household sleeve it implies roughly a 31% household loss from this sleeve alone, **before** losses elsewhere. The small modeled improvement is not a safety certificate.

### 3.5 A1 challenge: keep AI-2027 serious, but separate forecasts from evidence

I retain the aggressive scenario framework rather than reducing the AI thesis to generic GDP growth. The [AI-2027 compute forecast](https://ai-2027.com/research/compute-forecast) describes rapid compute accumulation, and its [timeline research](https://ai-2027.com/research/timelines-forecast) links later updates; the [August 2026 AI Futures update](https://blog.aifutures.org/p/q25-2026-timelines-update-uplift) is more relevant to current timing judgments than treating the original narrative date as immutable. **That update is older than 30 days.** The sources deserve substantial weight, not automatic conversion of every capability milestone into shareholder returns.

I also rechecked [AI-2040](https://ai-2040.com/) and its [compute supplement](https://ai-2040.com/supplements/compute-supplement). Plan A is a recommended conditional course, not a guaranteed forecast; financing, export/security restrictions, coordinated slowdown and state intervention can break the link between physical buildout and public-equity returns. The current supplement explicitly includes debt financing in its 2028 investment scenario. I do not carry forward an older criticism of that number after the source changed.

For transparency, this Step 4 **reuses the existing detailed workbook/forecast audit in the repository**; it is not a new cell-by-cell audit of the 2024 shared Google Sheet. The forecast pedigree and apparent successes do not remove the need to compare forecast vintage, elapsed horizon and like-for-like quantities. Future 2027–2030 outcomes cannot yet count as demonstrated accuracy. This is particularly important for the HBM comparison flagged in §4.

The shared A1 capital paths retained for the calculations are:

| Path / descriptor probability | 2027 investment | 2028 | 2029 | 2030 | Interpretation |
|---|---|---|---|---|---|
| Bust, default 12.5% | $0.8T | $0.6T | $0.5T | $0.45T | Rollback toward 2025 demand; not a bankruptcy floor. |
| Plateau, default 12.5% | $0.75T | $0.75T | $0.8T | $0.9T | Growth delayed 2–3 years. |
| Base, 50% | $1.0T | $1.5T | $2.1T | $2.8T | Broad commercial expansion family. |
| Bull, 25% | $1.1T | $2.0T | $3.1T | $4.5T | Faster capacity and monetization expansion. |
| AI-2027, 35% overlapping descriptor | $1.0T | $2.4T | $3.2T | $4.2T | Stronger than base; company loading λ=0.8. |
| 100GW, 10% bull-subset descriptor | >$1T | ~$2T | ~$4T | ~$8T | One largest cluster ~100GW by 2030, not total global AI capacity. |

These are **inherited scenario inputs, not verified forecasts for each year**. The 100GW interpretation follows [Situational Awareness's cluster chapter](https://situational-awareness.ai/racing-to-the-trillion-dollar-cluster/); do not confuse one training cluster with a global capacity total. First constraints include interconnection, permits, transformers, skilled construction labor, then generation/chips/HBM/EUV and finance. The ordering varies by location and workload; a global aggregate cannot establish which issuer has pricing power on a particular project.

**My criticisms of A1:** historical 2025 earnings do not necessarily form a bust floor after acquisitions or debt-funded expansion; the half-plateau bear blend softens downside; λ=2.5 can extrapolate earnings beyond verified labor/capacity/capital supply; terminal multiples remain uncertain; and overlapping named probabilities do not constitute a fully specified joint macro distribution. These limitations apply to the old portfolio too. I therefore keep primary A1 numbers comparable and stress them explicitly, instead of giving newcomers favorable assumptions while marking down incumbents.

| Sensitivity | Baseline Expected CAGR | Proposed Expected CAGR | Conclusion |
|---|---|---|---|
| Primary A1 | 14.93% | 15.66% | +0.73pp modeled advantage. |
| Entire bear bucket uses bust, not half plateau | 14.14% | 14.90% | Advantage survives harsher bear construction. |
| WCC/STRL also use 30/45/25 buckets, like NRG/VST | 14.93% | 15.52% | Advantage not just a lighter political-risk probability. |
| Only new stocks' base/bull owner EPS −20% | 14.93% | 14.91% | **Advantage disappears.** |
| Only new stocks' exit multiples −20% | 14.93% | 14.85% | **Advantage reverses.** |
| WCC owner margins 4.5%/5.5%, not 5.5%/6.5% | 14.93% | 15.28% | Narrower but positive advantage. |
| STRL owner margins 12%/14%, not 15%/16% | 14.93% | 15.42% | Narrower but positive advantage. |
| Both preceding lower-margin cases together | 14.93% | 15.03% | Only +0.10pp remains. |
| New-company revenue −20% and net margins −2pp | 14.93% | 14.12% | Failure case; do not call recommendation robust to all operating misses. |
| All holdings' exit multiples −20% | 8.63% | 9.46% | Both returns compress; proposed advantage survives. |
| Common 10% probability of zero equity recovery | 12.04% | 12.76% | Both lower; broad regime loss overwhelms fine allocation choices. |

For the common multiple stress, power-company operating EV is reduced **before** subtracting fixed claims; other earnings multiples are cut while dividends and cash reserves are retained. Bust becomes **−71.99% before / −70.71% after**, so the primary downside tolerance would not survive that stress. No recommendation is made to relax the owner's loss tolerance silently. The common zero-recovery case is a sensitivity overlay that scales all expected wealth by 0.9, not an added independent 10% inside the primary distribution.

A separate **100GW terminal-wealth cap at each company's bull TV** reduces named portfolio CAGR from **31.01% before to 32.09% after**, versus uncapped 36.88%/38.21%. That is a deliberately mechanical capacity/valuation ceiling, not a newly forecast physical 100GW deployment model. The recommendation still improves the named path without relying on its most aggressive extrapolation.

At both proposed entry ceilings simultaneously — WCC $330 and STRL $315, existing prices unchanged — proposed returns are **15.44% expected / 24.00% AI-2027 / 37.95% 100GW**, bust **−61.56%**. This provides some price discipline but not immunity to earnings error. If new information lowers the operating bridge, lower the ceilings rather than using them as unconditional buy orders.

### 3.6 Owner escalations and Step 5 implications

**E1 — MOD.** The [issuer's investor-day announcement](https://investors.modine.com/news/news-details/2026/Modine-to-Host-Analyst-and-Investor-Day-on-November-18-2026/default.aspx) independently confirms **November 18, 2026**; the announcement itself is older than 30 days. The [November 3 results](https://investors.modine.com/news/news-details/2026/Modine-Reports-Second-Quarter-Fiscal-2027-Results/default.aspx) do not clear the cash/perimeter concern by themselves. Require stabilized DC margins, positive H2 FCF guidance and FY2028 targets that form a credible bridge to **2030 owner EPS $8.84**, not a mistaken demand that FY2028 already equal the 2030 forecast. If the owner accepts the proposed nine-name portfolio and MOD subsequently clears the gate, the existing conditional funding rule produces **MOD 5, VRT 11, NVT 5**, all other proposed weights unchanged. That sums to 100% across ten holdings and, on unchanged A1 inputs/prices, models **15.91% expected / 25.00% AI-2027 / 39.80% 100GW / −61.48% bust**. It is **not** part of today's unconditional recommendation.

**E2 — NVDA.** The [November 8 board statement](https://investor.nvidia.com/news/press-release-details/2026/Statement-from-NVIDIA-Board-of-Directors/default.aspx) confirms an independent review and expresses confidence; it does not establish an adverse finding. Avoid converting allegations into fact. Preserve the target, but require the earnings/review-status check before incremental deployment. If the owner instead chooses 12% temporarily, the published variant cannot be used unchanged because it places NVT at 13%, above its stated cap. A new lawful funding plan is required; do not smuggle that choice into this optimization.

**E3 — Texas/power.** A moratorium bill is not the only relevant mechanism. The governor's [September 21 directive on TCEQ datacenter approvals](https://gov.texas.gov/news/post/governor-abbott-directs-tceq-to-halt-data-center-permits) indicates an administrative restriction already exists. The page's text was available in search retrieval, but direct opening timed out; the exact current legal scope/implementation still requires confirmation before execution. Step 3's research table already mentioned the administrative pause; the problem is the later “pledge, not law” decision framing and future bill trigger, not total omission from its research. Existing generation, existing PPAs and proposed new datacenter approvals have different exposure. Recommend O1 on valuation, not an automatic sale triggered by a single chamber vote. If O1 is declined, compare current VST/TLN claims, contracted earnings and geographic exposure again before the owner chooses.

**E4 — META.** Explicitly accept a mandate that includes the monetizing buyer, consistent with the fund's prior software exposure. Verify actual household overlap through Continuity's funds before deployment; the necessary live household positions were not provided here. The approximately 7.5% direct household exposure implied by a 15% position in a 50% sleeve is arithmetic, not a complete look-through estimate. Do not equate a lower modeled bust with cash-like protection.

**E5 — concentration.** Approve nine holdings with the stated caps and common-driver exposure, or retain the original concentration decision. A preference for a materially smaller household drawdown requires redesigning the risk budget, not merely changing eight ticker names to sixteen. Only the owner can resolve that preference.

**Step 5 handoff:** record accept/reject for O1, O2 and E1–E5. The synthesis model should then apply accepted weights, reconcile gates and factual fixes, update the final/deployment PDFs and README, and mark the version adopted. No final, Candidate Ranking, Deployment Strategy or README has been changed by this Step 4 report.

## 4. Sanity check — problems only

1. **Contradictory NVIDIA deployment authority.** E2 says buy only after November 17; Deployment Strategy T1 nevertheless buys **1.93 sleeve points before earnings**. Choose one rule. Also, the published NVDA-12 variant assigns **NVT 13%**, violating the 12% integration cap. These are implementation issues, not rounding differences.

2. **The MOD gate changes meaning across documents.** Candidate Ranking correctly links FY2028 targets to **2030** owner EPS $8.84; the final's action table instead requires FY2028 EPS ≥$8.8. Correct that horizon mismatch. November 18 is independently confirmed, so the “unconfirmed date” qualification is obsolete. Sources and conditional weights are in §3.6.

3. **“The same eight names win under Codex multiples” is too strong.** Reproducing that run gives the fixed eight-name portfolio **18.1512%** expected. Under exactly those alternative multiples, MSFT has **18.0170%** expected versus VST **15.7855%**; replacing VST's 8% with MSFT yields **18.3235%**, bust **−53.69%** versus −56.02%, within the stated caps. It slightly lowers AI-2027 (26.75% → 26.73%), but the stock-level expected gap exceeds about 2pp. The published comparison establishes the best of its tested portfolios, not invariant optimal constituents. This is **not** the primary A1 recommendation.

4. **The ranked pool is methodologically mixed.** Twenty-seven names receive reconstructed A1 models; 31 retain prior three-state screen TVs/probabilities and interpolate named *values*, not the same owner-earnings bridge. Calling the better of two old screens an “upper bound” does not make it a mathematical upper bound under a fresh A1 rebuild. The table should distinguish those methods without implying exhaustive optimization. ALAB/FN checks above do not produce an actionable replacement, but illustrate why the distinction matters.

5. **Some owner-EPS haircuts charge SBC twice.** Vertiv's published adjusted-EPS reconciliation already retains SBC, yet the Step 3 plateau applies a further 0.98 multiplier. nVent's adjusted measure likewise retains ordinary SBC, while its model applies 0.96 to the historical/plateau anchors. Reconcile those items from the issuer tables before adoption rather than applying a generic haircut. I left incumbent inputs unchanged in the primary comparison; this is a small conservative bias, not the basis of O1/O2. [Vertiv reconciliation](https://www.sec.gov/Archives/edgar/data/1674101/000162828026067707/q32026exhibit991vrt10282026.htm), [nVent reconciliation](https://www.sec.gov/Archives/edgar/data/1720635/000162828026068391/q32026nvtpressrelease.htm).

6. **The HBM forecast scorecard compares different quantities.** The final compares a forecast of annual **HBM-market revenue** with approximately $54bn of **total Micron quarterly revenue**, then calls the HBM prediction confirmed. Total DRAM/NAND sales cannot validate HBM-only market size or establish that HBM was the binding system constraint. Replace that claim with like-for-like HBM shipment/revenue evidence, or mark it unverified. This correction does not negate MU's AI exposure or the need to take the forecasts seriously.

No other allocation-table, five-largest-holding CAGR, candidate-omission or unexplained averaging issue is asserted here. Calculations and sensitivity tests were performed in temporary scratch files; the input ledger and formulas above preserve the incremental model without modifying the synthesis research directory. This report is an independent proposal for owner decision, not an adopted allocation or trade instruction.
