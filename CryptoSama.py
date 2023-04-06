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
    df = pd.DataFrame(binance.fetch_ohlcv(pair, timeframe, since),
                        columns=['time', 'open', 'high', 'low', 'close', 'volume'])
    df['time'] = df['time'].apply(lambda t: dt.datetime.fromtimestamp(t/1000))
    return df

# Analyst OHLCV data & Produce signal (BUY, SELL, WAIT)
def produce_indicators(df):
    df.ta.ema(length=5, append=True)
    df.ta.ema(length=8, append=True)
    df.ta.ema(length=13, append=True)
    return df

def produce_signal(df):
    ...

if __name__ == '__main__':
    pair = 'BTC/USDT'
    timeframe = '1h'
    df = fetch_OHLCV(pair, timeframe)
    df = produce_indicators(df)
    signal = produce_signal(df)
    print(df)

    plt.style.use('dark_background')

    plt.title(pair)
    plt.xlabel('')
    plt.ylabel('USDT')

    body_width = .4
    wick_width = .05
    up = df[df.close>=df.open]
    plt.bar(up.index, up.close-up.open, body_width, up.open, color='green')
    plt.bar(up.index, up.high-up.close, wick_width, up.close, color='green')
    plt.bar(up.index, up.open-up.low, wick_width, up.low, color='green')
    down = df[df.close<df.open]
    plt.bar(down.index, down.open-down.close, body_width, down.close, color='red')
    plt.bar(down.index, down.high-down.open, wick_width, down.open, color='red')
    plt.bar(down.index, down.close-down.low, wick_width, down.low, color='red')

    plt.plot(df[['EMA_5', 'EMA_8', 'EMA_13']])
    plt.legend(['EMA_5', 'EMA_8', 'EMA_13'])

    plt.grid()
    plt.show()
