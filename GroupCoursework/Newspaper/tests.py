from django.test import TestCase
from django.urls import reverse
from Newspaper.data import *
from Newspaper.serializers import ArticleSerializer
import json

from rest_framework import status
from rest_framework.test import APITestCase

from Newspaper.models import Article

# Create your tests here.

# Article API Tests

# The default set up for the articles


def SetUp(TestCase):
    Article.objects.create(title="Title1", author="Author1", content="Content1", article_img="None",
                           pub_date="2017-02-01 16:30:10", category="Business", likes=10, tags="Business")
    Article.objects.create(title="Title2", author="Author1", content="Content1", article_img="None",
                           pub_date="2017-03-10 11:10:11", category="Business", likes=5, tags="Business")
    Article.objects.create(title="Title3", author="Author1", content="Content1", article_img="None",
                           pub_date="2017-05-28 12:44:22", category="Business", likes=2, tags="Business")
    Article.objects.create(title="Title4", author="Author2", content="Content1", article_img="None",
                           pub_date="2017-05-28 12:44:30", category="Business", likes=4, tags="Business")
    Article.objects.create(title="Title5", author="Author3", content="Content2", article_img="None",
                           pub_date="2017-02-05 13:10:01", category="Business", likes=10, tags="Business")
    Article.objects.create(title="Title6", author="Author2", content="Content3", article_img="None",
                           pub_date="2016-08-02 13:44:43", category="Business", likes=4, tags="Business")
    Article.objects.create(title="Title7", author="Author2", content="Content4", article_img="None",
                           pub_date="2016-01-01 23:50:22", category="Business", likes=9, tags="Business")
    Article.objects.create(title="Title8", author="Author3", content="Content5", article_img="None",
                           pub_date="2017-05-05 23:12:41", category="Business", likes=0, tags="Business")
    Article.objects.create(title="Title9", author="Author1", content="Content6", article_img="None",
                           pub_date="2015-12-11 02:05:59", category="Business", likes=0, tags="Business")
    Article.objects.create(title="Title10", author="Author5", content="Content6", article_img="None",
                           pub_date="2015-04-11 01:01:59", category="Business", likes=10, tags="Business")
    Article.objects.create(title="Title11", author="Author5", content="Content6", article_img="None",
                           pub_date="2015-03-22 07:56:49", category="Politics", likes=3, tags="Business")
    Article.objects.create(title="Title12", author="Author1", content="Content6", article_img="None",
                           pub_date="2015-05-23 18:48:32", category="Business", likes=4, tags="Business")
    Article.objects.create(title="Title13", author="Author3", content="Content6", article_img="None",
                           pub_date="2018-11-21 10:32:03", category="Technology", likes=5, tags="Business")
    Article.objects.create(title="Title14", author="Author1", content="Content62", article_img="None",
                           pub_date="2017-06-01 17:12:30", category="Politics", likes=1, tags="Business")
    Article.objects.create(title="Title15", author="Author3", content="Content16", article_img="None",
                           pub_date="2017-01-22 10:32:03", category="Technology", likes=200, tags="Business")


# These tests test the API end points to make sure that the data presented to the user is the same as the one that is serialized
class ArticleApiTests(APITestCase):
    def setUp(self):
        SetUp(self)

#'%Y-%m-%d %H:%M:%S'

    def test_articles_returns_all_articles(self):
        articles = GetAllArticles()
        serializer = ArticleSerializer(articles, many=True)
        response = self.client.get(reverse('get_articles'))
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(len(response.data), 15)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_latest_articles_returns_10_elements(self):
        articles = GetLatestArticles()
        serializer = ArticleSerializer(articles, many=True)
        response = self.client.get(reverse('get_latest_articles'))
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(len(response.data), 10)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_article_by_id_returns_the_correct_element(self):
        article = GetArticleById(5)
        serializer = ArticleSerializer(article, many=False)
        response = self.client.get(reverse('get_article', kwargs={'pk': 5}))
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# These tests check if the data layer is returning the correct objects
class DataLayerTests(TestCase):
    def setUp(self):
        SetUp(self)

    def test_data_all_articles_returns_all_articles(self):
        articles = GetAllArticles()
        self.assertEqual(articles.count(), 15)

    def test_data_latest_articles_returns_10_elements(self):
        articles = GetLatestArticles()
        self.assertEqual(articles.count(), 10)

    def test_get_article_by_id_returns_the_correct_element(self):
        article = GetArticleById(5)
        self.assertEqual(article.id, 5)
        self.assertEqual(article.title, "Title5")
        self.assertEqual(article.author, "Author3")
        self.assertEqual(article.content, "Content2")
        self.assertEqual(article.pub_date.strftime(
            "%Y-%m-%d %H:%M:%S"), "2017-02-05 13:10:01")
        self.assertEqual(article.category, "Business")
        self.assertEqual(article.likes, 10)
