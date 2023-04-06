import ccxt
import pandas_ta as ta
import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

# Fetch OHLCV data from Binance using CCXT
def fetch_OHLCV(pair, timeframe, since=None):
    binance = ccxt.binance()
    since = binance.parse8601(f'{since} 00:00:00')
    ohlcv = pd.DataFrame(binance.fetch_ohlcv(pair, timeframe, since),
                        columns=['time', 'open', 'high', 'low', 'close', 'volume'])
    ohlcv['time'] = ohlcv['time'].apply(lambda t: dt.datetime.fromtimestamp(t/1000))
    return ohlcv

# Analyst OHLCV data & Produce signal (BUY, SELL, WAIT)
def analyst(ohlcv):
    ...

ohlcv = fetch_OHLCV('BTC/USDT', '1h')
print(ohlcv)

signal = analyst(ohlcv)
print(signal)