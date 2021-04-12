import pandas as pd
import twint

ticker_path = '~/Downloads/stock tickers251073e.csv'

data = pd.read_csv(ticker_path)

TweetsCollection = {}
ll = 0
for index, row in data.iterrows():
    ticker = row[0]
    name = row[1]
    QUERY = '$'+ticker
    MIN_LIKES =  5
    VERIFIED = True
    tweets = []
    # trail = twint.Config()
    # trail.Search = QUERY
    # trail.Verified = VERIFIED
    # trail.Min_likes = MIN_LIKES
    # #trail.Members_list = "kk3799/StockNews"
    # trail.Since = '2020-1-1 00:00:00'
    # trail.Until = '2020-2-1 00:00:00'
    # trail.Lang = 'en'
    # trail.Store_object = True
    # trail.Store_object_tweets_list = tweets
    # trail.Hide_output = True
    # twint.run.Search(trail)
    # print(len(tweets))
    # if len(tweets) > 100:
    #     MIN_LIKES = 20
    #     if len(tweets) > 1000:
    #         QUERY = QUERY + ' stock'
    # #break
    print(index + 1, ': ', QUERY, MIN_LIKES, VERIFIED)

    c = twint.Config()
    c.Search = QUERY
    c.Verified = VERIFIED
    c.Min_likes = MIN_LIKES
    #c.Members_list = 'kk3799/StockNews'
    c.Since = '2012-1-1 00:00:00'
    c.Until = '2020-1-1 00:00:00'
    c.Output = 'CashTag/' + ticker
    c.Lang = 'en'
    c.Store_csv = True
    c.Hide_output = True

    twint.run.Search(c)

    #break