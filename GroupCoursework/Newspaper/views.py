from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Newspaper.serializers import ArticleSerializer, RegisterSerializer, CommentSerializer
from Newspaper.data import *
# UNUSED:
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.parsers import JSONParser
# from django.views.decorators.csrf import csrf_exempt, csrf_protect
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication


def index(request):
    return render(request, 'Newspaper/index.html')


def article(request):
    return render(request, 'Newspaper/single.html', {'data': request.POST})

# Web API


@api_view(['GET'])
def get_articles(request):
    """
    Gets all articles
    """
    if request.method == 'GET':

        query = ExtractCategory(request.query_params)
        articles = None
        if query != None:
            # We got query Parameters
            articles = GetLatestArticlesByCategory(query)
        else:
            # Return the latest Articles
            articles = GetAllArticles()
            serializer = ArticleSerializer(articles, many=True)

        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_latest_articles(request):
    """
    Get the latest articles, limited to 10
    """
    if request.method == 'GET':

        query = ExtractCategory(request.query_params)
        articles = None
        if query != None:
            # We got query Parameters
            articles = GetLatestArticlesByCategory(query)
        else:
            # Return the latest Articles
            articles = GetLatestArticles()
            serializer = ArticleSerializer(articles, many=True)

        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_article(request, pk):
    """
    Get one article by referencing the primary key
    """
    try:
        if request.method == 'GET':
            article = GetArticleById(pk)
            serializer = ArticleSerializer(article, many=False)
            return Response(serializer.data)
    except:
        return Response(status=400)


@api_view(['POST'])
def authentication(request):
    if request.method == 'POST':
        email = request.user.email
        password = request.user.password

        print("logging in with:", email, "|", password)
        user = authenticate(email=email, password=password)

        if user is not None:
            print("Authenticated!")
            login(request, user)
        #     return redirect('/')
        # else:
        #     return render(request, 'index.html', {'errors': 'user is not defined'})
    return Response(status=403)


@api_view(['POST'])
def register(request):
    data = request.data
    serializer = RegisterSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(status=500)
    return Response(status=200)


@api_view(['POST'])
def comment(request):
    data = request.data
    serializer = CommentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(status=500)
    return Response(status=200)
