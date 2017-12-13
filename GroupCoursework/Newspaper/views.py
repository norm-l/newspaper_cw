from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Newspaper.serializers import ArticleSerializer, ArticleHeadlineSerializer, RegisterSerializer, CommentSerializer, LikesSerializer
from Newspaper.data import *
from rest_framework_jwt.settings import api_settings
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from Newspaper.models import User, Like, Comment
# UNUSED:
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.parsers import JSONParser
# from django.views.decorators.csrf import csrf_exempt, csrf_protect
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication


def index(request):
    return render(request, 'Newspaper/index.html')

# Web API
@api_view(['GET'])
@permission_classes((AllowAny, ))
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
@permission_classes((AllowAny, ))
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
@permission_classes((AllowAny, ))
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

        # If user is not None
        if user:
            # And user is currently active
            if user.is_active:
                print("Authenticated user: ", user)
                login(request, user)
                # Return 
            # User is not active
            else:
                return Response("Account is disabled!")
        # Wrong details
        else:
            print("Invalid login for user: ", user)
            return Response(status=403)
    # Login was attempted but not with POST
    else:
        print("Attempted authentication with the wrong request method (not POST).")
        return redirect("/")


@api_view(['POST'])
@permission_classes((AllowAny, ))
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

@api_view(['POST'])
def like(request, id):
    likes = Like.objects.filter(article__id=id, profile=request.user, )
    if len(likes) > 0:
        for l in likes:
            if l.liked:
                l.delete()
        return JsonResponse({'msg': "Completed Successfully", 'type': 'Info'})

    else:
        if request.method == "POST":
            comment = Like.objects.create(profile=request.user, article=get_object_or_404(Article, id=id), liked=True)
            return JsonResponse({'msg': "Liked", 'type': 'Info', 'data': comment.id})
        else:
            return JsonResponse({'msg': "Like", 'type': 'Warning'})

