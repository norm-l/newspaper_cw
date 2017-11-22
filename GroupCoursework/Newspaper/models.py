from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Article(models.Model):
    # The title of the Article
    title = models.CharField(max_length=255)
    # The author of the Article
    author = models.CharField(max_length=255)
    # The actual article content
    content = models.TextField()
    # Publication date
    pub_date = models.DateTimeField('publication date')
    # The category of the article
    category = models.CharField(max_length=255)
    # The amount of likes for the article
    likes = models.IntegerField()


'''class Comments (models.Model):
    #FK User
    user = models.ForeignKey('User')
    #FK Article
    article = models.ForeignKey('Article')
    #User comment
    commentContent = models.TextField()'''

