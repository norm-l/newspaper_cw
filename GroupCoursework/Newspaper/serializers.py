# serializers.py holds the Rest Framework serializers that are used for our Newspaper App

from rest_framework import serializers
from .models import Article,User,Comment,Like

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id' , 'title' , 'author' , 'content' , 'article_img' ,  'pub_date' , 'category' , 'tags')

class ArticleHeadlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id' , 'title' , 'author' , 'headline' , 'article_img' ,  'pub_date' , 'category' , 'tags')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = "__all__"
        fields = ('email', 'password', 'name', 'phone')
    def create(self, validated_data):
        user = User(
            email = validated_data['email'],
            name = validated_data['name'],
            phone = validated_data['phone']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        
class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"
