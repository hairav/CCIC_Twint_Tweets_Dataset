import yfinance as yf
import pandas as pd
import time
import io
import requests
import datetime

start = datetime.datetime(2012, 1, 1)
end = datetime.datetime(2020, 1, 1)

tickers = pd.read_csv('/Users/kk3799/Downloads/stock tickers251073e.csv')

stock_final = pd.DataFrame()
nf = []
for ticker in tickers['ticker']:
    #print(ticker)

    stock = yf.download(ticker, start = start, end = end, progress = False)

    if len(stock) == 0:
        print(ticker)
        nf.append(ticker)
    else:
        stock['Name'] = ticker
        stock.to_csv('stock_history/' + ticker + '.csv', index = False)

for ticker in nf:
    print(ticker)