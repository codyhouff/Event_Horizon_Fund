"""Step 3 data snapshot: quoteSummary (consensus, valuation, earnings history) +
fundamentals-timeseries (annual diluted EPS, revenue, shares) + last daily closes.
Usage: python -I fetch_step3.py OUT.json SYM1,SYM2,...
"""
import json, sys, time, urllib.request, http.cookiejar, datetime as dt

OUT = sys.argv[1]
SYMS = sys.argv[2].split(",")

cj = http.cookiejar.CookieJar()
op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
op.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)")]
try:
    op.open("https://fc.yahoo.com", timeout=20)
except Exception:
    pass
crumb = op.open("https://query2.finance.yahoo.com/v1/test/getcrumb", timeout=20).read().decode()

MODS = "price,summaryDetail,defaultKeyStatistics,financialData,earningsTrend,earningsHistory,calendarEvents"


def g(d, *ks):
    for k in ks:
        if d is None:
            return None
        d = d.get(k)
    if isinstance(d, dict):
        return d.get("raw")
    return d


def get(url):
    return json.loads(op.open(url, timeout=30).read())


out = {}
now = int(time.time())
for s in SYMS:
    rec = {}
    try:
        r = get(f"https://query2.finance.yahoo.com/v10/finance/quoteSummary/{s}?modules={MODS}&crumb={crumb}")["quoteSummary"]["result"][0]
        trend = {}
        for t in (r.get("earningsTrend") or {}).get("trend", []):
            trend[t.get("period")] = {"end": t.get("endDate"), "eps": g(t, "earningsEstimate", "avg"),
                                      "rev": g(t, "revenueEstimate", "avg"), "n": g(t, "earningsEstimate", "numberOfAnalysts")}
        hist = [{"q": h.get("quarter", {}).get("fmt"), "act": g(h, "epsActual"), "est": g(h, "epsEstimate")}
                for h in (r.get("earningsHistory") or {}).get("history", [])]
        ce = r.get("calendarEvents") or {}
        rec.update({
            "name": g(r, "price", "shortName"), "currency": g(r, "price", "currency"),
            "price": g(r, "price", "regularMarketPrice"), "mcap": g(r, "price", "marketCap"),
            "ev": g(r, "defaultKeyStatistics", "enterpriseValue"),
            "trailingPE": g(r, "summaryDetail", "trailingPE"), "forwardPE": g(r, "summaryDetail", "forwardPE"),
            "ev_ebitda": g(r, "defaultKeyStatistics", "enterpriseToEbitda"),
            "shares": g(r, "defaultKeyStatistics", "sharesOutstanding"),
            "trailingEps": g(r, "defaultKeyStatistics", "trailingEps"), "forwardEps": g(r, "defaultKeyStatistics", "forwardEps"),
            "divRate": g(r, "summaryDetail", "dividendRate"), "divYield": g(r, "summaryDetail", "dividendYield"),
            "revenue": g(r, "financialData", "totalRevenue"), "fcf": g(r, "financialData", "freeCashflow"),
            "ocf": g(r, "financialData", "operatingCashflow"), "ebitda": g(r, "financialData", "ebitda"),
            "cash": g(r, "financialData", "totalCash"), "debt": g(r, "financialData", "totalDebt"),
            "opMargin": g(r, "financialData", "operatingMargins"), "netMargin": g(r, "financialData", "profitMargins"),
            "target_mean": g(r, "financialData", "targetMeanPrice"), "n_analysts": g(r, "financialData", "numberOfAnalystOpinions"),
            "next_earnings": [x.get("fmt") for x in (ce.get("earnings") or {}).get("earningsDate", [])],
            "trend": trend, "hist": hist,
        })
    except Exception as e:
        rec["qs_error"] = repr(e)[:200]
    try:
        types = "annualDilutedEPS,annualTotalRevenue,annualDilutedAverageShares,annualNetIncomeCommonStockholders,annualStockBasedCompensation"
        j = get(f"https://query2.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/timeseries/{s}?type={types}&period1=1483228800&period2={now}&crumb={crumb}")
        ts = {}
        for res in j["timeseries"]["result"]:
            typ = res["meta"]["type"][0]
            ts[typ] = {x["asOfDate"]: x["reportedValue"]["raw"] for x in res.get(typ, []) if x}
        rec["annual"] = ts
    except Exception as e:
        rec["ts_error"] = repr(e)[:200]
    try:
        j = get(f"https://query1.finance.yahoo.com/v8/finance/chart/{s}?range=10d&interval=1d")
        res = j["chart"]["result"][0]
        closes = res["indicators"]["quote"][0]["close"]
        rec["closes"] = {dt.datetime.utcfromtimestamp(t).strftime("%Y-%m-%d"): c for t, c in zip(res["timestamp"], closes)}
    except Exception as e:
        rec["chart_error"] = repr(e)[:200]
    out[s] = rec
    time.sleep(0.35)

json.dump(out, open(OUT, "w"), indent=1)
print("done", len(out), "errors:", {k: [e for e in ("qs_error", "ts_error", "chart_error") if e in v] for k, v in out.items() if any(e in v for e in ("qs_error", "ts_error", "chart_error"))})
