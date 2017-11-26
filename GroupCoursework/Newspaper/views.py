from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Newspaper.data import *
from Newspaper.serializers import ArticleSerializer

# Create your views here.
def index(request):
    return render(request, 'Newspaper/index.html')


def article(request):
	return render(request,'Newspaper/single.html')
	
# Web API

@api_view(['GET'])
def get_latest_articles(request):
    """
    Get the latest articles, limited to 10
    """
    if request.method == 'GET':
        articles = GetLatestArticles()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_article(request, pk):
    """
    Get one article by referencing the primary key
    """

    try:
        if(request.method == 'GET'):
            article = GetArticleById(pk)
            serializer = ArticleSerializer(article, many=False)
            return Response(serializer.data)
    except:
        return Response(status=400)