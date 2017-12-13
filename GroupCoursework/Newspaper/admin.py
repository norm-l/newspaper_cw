from django.contrib import admin
# Register your models here.

from .models import Article, User, Comment, Like

admin.site.register(Article)
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Like)
