import pandas as pd

Companies = pd.read_csv('stock tickers.csv')

tickers = Companies['ticker'].tolist()
ind1 = 0


News = pd.read_csv('us_equities_news_dataset.csv')
print(News['ticker'][ind1])
News.drop('id',axis='columns',inplace=True)
News.drop('url',axis='columns',inplace=True)
News.drop('article_id',axis='columns',inplace=True)

for ind in News.index:
	if News['ticker'][ind] not in tickers:
		print(News['ticker'][ind])
		print(ind)
		News.drop(ind,inplace=True)


News.to_csv('final_News_Data.csv')

