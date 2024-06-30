
import newspaper
import json
from pygooglenews import GoogleNews
gn = GoogleNews()
science = gn.topic_headlines('science')
articles=[]
for entry in science["entries"]:
    article = newspaper.Article(url=entry["link"])
    try:
        article.download()
        article.parse()
        articles.append(
            {
                'title':str(article.title),
                'text':str(article.text),
                'link':str(entry["link"])
            }
        )
    except:
        pass

print(articles)