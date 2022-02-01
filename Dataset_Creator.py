import requests
import pandas as pd
import functools as ft

api = "1OE3G5M4NFNO409U"
syms = ['MSFT', 'JPM', 'AMZN', 'UNH', 'KO', 'FB', 'NVDA', 'TSLA', 'AMZN']
for sym in syms:
    #RSI
    par = {"function": "RSI",
                   "symbol": f"{sym}",
                   "interval": "daily",
                   "apikey": api,
                   "datatype": "csv",
                   "time_period": "14",
                   "series_type": "close"}

    rsi = requests.get(url="https://www.alphavantage.co/query", params=par)

    with open("temp.csv", mode = 'w') as f:
        f.write(rsi.text)
    rsi = pd.read_csv("temp.csv")

    #Bollinger Band
    par = {"function": "BBANDS",
                   "symbol": f"{sym}",
                   "interval": "daily",
                   "apikey": api,
                   "datatype": "csv",
                   "time_period": "20",
                   "series_type": "close",
                   "nbdevup": "2",
                   "nbdevdn": "2",
                   "matype": "1"}

    bbands = requests.get(url="https://www.alphavantage.co/query", params=par)
    with open("temp.csv", mode='w') as f:
        f.write(bbands.text)
    bbands = pd.read_csv("temp.csv")

    # TIME SERIES DAILY
    par = {"function": "TIME_SERIES_DAILY_ADJUSTED",
           "symbol": f"{sym}",
           "outputsize": "full",
           "apikey": api,
           "datatype": "csv"}

    ohlcv = requests.get(url="https://www.alphavantage.co/query", params=par)
    with open("temp.csv", mode='w') as f:
        f.write(ohlcv.text)
    ohlcv = pd.read_csv("temp.csv").loc[:,['timestamp', 'open', 'high', 'low', 'close', 'volume']]
    ohlcv.rename(columns={'timestamp':'time'}, inplace=True)

    #MACD
    par = { "function": "MACD",
            "symbol": f"{sym}",
            "interval": "daily",
            "series_type": "close",
            "apikey": api,
            "datatype": "csv"
           }

    macd = requests.get(url="https://www.alphavantage.co/query", params=par)
    with open("temp.csv", mode='w') as f:
         f.write(macd.text)
    macd = pd.read_csv("temp.csv")


    df_list = [ohlcv, rsi, bbands, macd]
    df = ft.reduce(lambda x,y: pd.merge(x, y, on='time', how='inner'), df_list)
    df.to_csv(f'{sym}.csv')
    print(f'{sym} Added')