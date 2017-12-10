from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Newspaper.serializers import ArticleSerializer, ArticleHeadlineSerializer, RegisterSerializer, CommentSerializer, LikesSerializer
from Newspaper.data import *
from rest_framework_jwt.settings import api_settings
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
            serializer = ArticleHeadlineSerializer(articles, many=True)

        serializer = ArticleHeadlineSerializer(articles, many=True)
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
        email = request.data['email']
        password = request.data['password']
        # Authenticate the user
        user = authenticate(email=email, password=password)

        # Assign JWT handlers for generating a token
        payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        encode_handler = api_settings.JWT_ENCODE_HANDLER

        # If user is not None
        if user:
            # And user is currently active
            if user.is_active:
                print("Authenticated user: ", user)
                # Generate a token
                payload = payload_handler(user)
                token = encode_handler(payload)
                # Return the token to the front-end
                return Response({'token': token})
            # User is not active
            else:
                return Response("Account is disabled!")
        # Wrong details
        else:
            print("Invalid login for user: ", user)
            return redirect("/")
    # Login was attempted but not with POST
    else:
        print("Attempted authentication with the wrong request method (not POST).")
        return redirect("/")


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


@api_view(['POST'])
def like(request):
    data = request.data
    serializer = LikesSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(status=500)
    return Response(status=200)
