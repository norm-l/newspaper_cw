# Classes methods that allow us to access the data models

from .models import Article

def GetLatestArticles():
    articles = Article.objects.all().order_by('pub_date')[:10]
    return articles