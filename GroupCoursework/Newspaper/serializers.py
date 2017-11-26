# serializers.py holds the Rest Framework serializers that are used for our Newspaper App

from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title' , 'author' , 'content' , 'pub_date' , 'category' , 'likes')