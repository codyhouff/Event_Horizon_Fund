"""Reproducible public Yahoo chart snapshot; no brokerage/account access."""
import concurrent.futures
import datetime as dt
import json
from pathlib import Path
import requests

BASE = Path(__file__).resolve().parent
TICKERS = ('TSM NVDA AVGO MU ASML AMAT SNPS ANET VRT DELL CEG VST PWR CRWD PLTR AVAV KTOS MRNA MP INTC GEV CCJ BE COHR '
           'GOOGL MSFT AMZN META LITE MRVL AMD KLAC LRCX CDNS ETN NVT MOD TLN NRG CORZ IREN CRWV APLD CLS '
           'PANW ZS OKTA RELX VRSK MSI AXON FCX BNTX LEU EQIX DLR HPE SMCI GFS ARM ENTG ONTO AMKR KLIC '
           'HUBB APH POWL MYRG MTZ CAT CMI GNRC EQT GLW FN CIEN LHX CACI TDY DRS LMT NOC RTX GD NOW SNOW '
           'SPGI MCO FICO GEN CLBT CGNT ARLO ABT QDEL PFE IBM NVTS ALAB CRDO SPY QQQ SMH XLU ITA IBB').split()
START = int(dt.datetime(2026, 5, 8, tzinfo=dt.timezone.utc).timestamp())
END = int(dt.datetime(2026, 11, 8, tzinfo=dt.timezone.utc).timestamp())

def fetch(ticker):
    url = f'https://query1.finance.yahoo.com/v8/finance/chart/{ticker}'
    params = {'period1': START, 'period2': END, 'interval': '1d', 'events': 'div,splits'}
    try:
        response = requests.get(url, params=params, headers={'User-Agent': 'Mozilla/5.0'}, timeout=30)
        response.raise_for_status()
        data = response.json()['chart']['result'][0]
        quote = data['indicators']['quote'][0]['close']
        adj = data['indicators']['adjclose'][0]['adjclose']
        rows = [(dt.datetime.fromtimestamp(t, dt.timezone.utc).date().isoformat(), p, a)
                for t, p, a in zip(data['timestamp'], quote, adj) if p is not None and a is not None]
        first, last = rows[0], rows[-1]
        dividends = list(data.get('events', {}).get('dividends', {}).values())
        out = {'ticker': ticker, 'source': response.url, 'first_date': first[0], 'first_close': first[1],
               'first_adjusted': first[2], 'last_date': last[0], 'last_close': last[1], 'last_adjusted': last[2],
               'price_return_pct': (last[1]/first[1]-1)*100,
               'total_return_pct': (last[2]/first[2]-1)*100, 'dividends': dividends,
               'splits': data.get('events', {}).get('splits', {}), 'currency': data['meta'].get('currency'),
               'retrieved_utc': dt.datetime.now(dt.timezone.utc).isoformat()}
        (BASE / f'{ticker}_chart.json').write_text(json.dumps(data, indent=2), encoding='utf-8')
        return out
    except Exception as exc:
        return {'ticker': ticker, 'error': str(exc), 'source': url}

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        results = list(pool.map(fetch, TICKERS))
    (BASE / 'market_snapshot.json').write_text(json.dumps(results, indent=2), encoding='utf-8')
    print('Ticker | May 8 close | Nov 6 close | Price return % | Adjusted total return %')
    for row in results:
        if 'error' in row:
            print(row['ticker'], 'UNAVAILABLE', row['error'])
        else:
            print(f"{row['ticker']} | {row['first_close']:.2f} | {row['last_close']:.2f} | {row['price_return_pct']:.2f} | {row['total_return_pct']:.2f}")
