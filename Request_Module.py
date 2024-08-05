# from newsapi import NewsApiClient

# # Init
# newsapi = NewsApiClient(api_key='9bad07ca86964215b9cf1c41011df6b1')

# # /v2/top-headlines
# top_headlines = newsapi.get_top_headlines(
#                                           sources='bbc-news,the-verge',
#                                           category='business',
#                                           language='en',
#                                           country='us')

# # /v2/everything
# all_articles = newsapi.get_everything(q='bitcoin',
#                                       sources='bbc-news,the-verge',
#                                       domains='bbc.co.uk,techcrunch.com',
#                                       from_param='2017-12-01',
#                                       to='2017-12-12',
#                                       language='en',
#                                       sort_by='relevancy',
#                                       page=2)

# # /v2/top-headlines/sources
# sources = newsapi.get_sources()


import requests
import json

query = input("What type of news are you interested in? \n")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-07-05&sortBy=publishedAt&apiKey=9bad07ca86964215b9cf1c41011df6b1"

r = requests.get(url)
news = json.loads(r.text)
print(news, type(news))

for article in news['articles']:
    print(article['title'])
    print(article['description'])
    print('----------------------------------')