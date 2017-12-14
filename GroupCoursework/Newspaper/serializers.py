# serializers.py holds the Rest Framework serializers that are used for our Newspaper App

from rest_framework import serializers
from .models import Article,User,Comment,Like

class ArticleSerializer(serializers.ModelSerializer):
    # likes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Article
        fields = ('id' , 'title' , 'author' , 'content' , 'article_img' ,  'pub_date' , 'category' , 'tags', 'likes')

class ArticleHeadlineSerializer(serializers.ModelSerializer):
    # likes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Article
        fields = ('id' , 'title' , 'author' , 'headline' , 'article_img' ,  'pub_date' , 'category' , 'tags', 'likes')

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

<<<<<<< HEAD
class UserCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name',)
=======
    def update(self, instance, validated_data):
        user = User.objects.get(pk=instance.id)
        User.objects.filter(pk=instance.id).update(**validated_data)
        return user
>>>>>>> d546772df3d8f3ea26c4476ee342da67afe63804

class CommentSerializer(serializers.ModelSerializer):
    user = UserCommentSerializer(many=False, read_only=True)
    
    class Meta:
        model = Comment
        fields = ('id', 'content' , 'user' , 'article')

class CommentAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content' , 'article')
        
class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"