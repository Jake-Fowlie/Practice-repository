#from newsapi import NewsApiClient

# news_api = NewsApiClient(api_key='719fa19d244843ee87bb7e3b88a9b762')

# articles = news_api.get_everything(q="artificial intelligence", language="en", page_size=3)

#for article in articles['articles']:
#    print(article['title'])
#    print(article['source']['name'])

#import json
#content = """{
# "title": "COVID-19",
# "author": "world health organization",
# "date": "7/8/2022",
# "confirmed": "551 million"
# } """
#json_content = json.loads(content)
#print(json_content['author'])

from sklearn.preprocessing import StandardScaler
data = [[10, 90], [12, 96], [9, 120], [13, 112], [8, 88]]

scaler = StandardScaler()
data = scaler.fit_transform(data)
print(data)
