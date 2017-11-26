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
