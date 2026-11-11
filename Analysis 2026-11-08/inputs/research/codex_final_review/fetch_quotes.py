"""Read-only public quote audit; keep Nov 9 valuation prices unchanged."""
import concurrent.futures
import datetime as dt
import json
from pathlib import Path
import urllib.request

HERE = Path(__file__).resolve().parent
symbols = 'NVDA META VRT MU NRG NVT CLS STRL AVGO VST TLN AEIS TSM MOD SANM ONTO'.split()
def fetch(symbol):
    url = f'https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?range=5d&interval=1d'
    req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req,timeout=25) as r:
            raw = json.load(r)
        r = raw['chart']['result'][0]; m = r['meta']
        dates = {dt.datetime.fromtimestamp(t,dt.timezone.utc).strftime('%Y-%m-%d'):p
                 for t,p in zip(r['timestamp'],r['indicators']['quote'][0]['close'])}
        prior = dates.get('2026-11-09'); current = m.get('regularMarketPrice')
        return symbol, dict(url=url, retrieved_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
            market_timestamp=m.get('regularMarketTime'), price=current, nov9=prior,
            change_percent=(current/prior-1)*100 if current and prior else None, daily_bars=dates)
    except Exception as e:
        return symbol, dict(url=url,error=str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
    data = dict(ex.map(fetch,symbols))
(HERE/'data').mkdir(exist_ok=True)
(HERE/'data/quote_audit.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print(json.dumps(data,indent=2))
