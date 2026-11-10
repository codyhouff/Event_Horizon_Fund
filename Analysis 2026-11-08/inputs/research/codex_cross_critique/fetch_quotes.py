"""Read-only public market data; fixed Nov 9 regular-session close."""
import concurrent.futures
import datetime as dt
import json
from pathlib import Path
import urllib.parse
import urllib.request

BASE = Path(__file__).resolve().parent
TICKERS = 'NVDA AVGO VRT CLS NVT NRG VST COHR TSM MU ASML SNPS CEG ETN CRDO PWR KTOS MP BNTX SNDK RELX VRSK MSI GEN LRCX ALAB'.split()
CUTOFF = '2026-11-09'

def fetch(ticker):
    params = {'period1': int(dt.datetime(2026, 11, 6, tzinfo=dt.timezone.utc).timestamp()),
              'period2': int(dt.datetime(2026, 11, 10, tzinfo=dt.timezone.utc).timestamp()),
              'interval': '1d', 'events': 'div,splits'}
    url = f'https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?' + urllib.parse.urlencode(params)
    try:
        request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(request, timeout=40) as response:
            raw = json.load(response)
        data = raw['chart']['result'][0]
        rows = [{'date': dt.datetime.fromtimestamp(t, dt.timezone.utc).date().isoformat(), 'close': p}
                for t, p in zip(data['timestamp'], data['indicators']['quote'][0]['close']) if p is not None]
        row = next(r for r in rows if r['date'] == CUTOFF)
        assert data['meta']['currency'] == 'USD'
        (BASE / f'{ticker}_chart.json').write_text(json.dumps(raw, indent=2), encoding='utf-8')
        return {'ticker': ticker, **row, 'currency': 'USD', 'source': url, 'rows': rows,
                'retrieved_utc': dt.datetime.now(dt.timezone.utc).isoformat()}
    except Exception as exc:
        return {'ticker': ticker, 'error': str(exc), 'source': url}

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        records = list(pool.map(fetch, TICKERS))
    (BASE / 'quotes.json').write_text(json.dumps(records, indent=2), encoding='utf-8')
    for row in records:
        print(row['ticker'], row.get('date'), row.get('close', row.get('error')))
    if any('error' in row for row in records):
        raise SystemExit('Incomplete quotes; do not silently mix dates.')
