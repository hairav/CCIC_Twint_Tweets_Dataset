import pandas as pd
import twint

ticker_path = '~/Downloads/stock tickers251073e.csv'

data = pd.read_csv(ticker_path)

TweetsCollection = {}

for ticker in data['ticker']:
    print(ticker)

    c = twint.Config()
    c.Search = '#' + ticker
    c.MinLikes = 5
    c.Since = '2006-1-1 00:00:00'
    c.Until = '2020-1-1 00:00:00'
    c.Output = ticker
    c.Store_csv = True
    c.Hide_output = True
    twint.run.Search(c)