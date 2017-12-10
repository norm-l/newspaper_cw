from django.contrib import admin
# Register your models here.

from .models import Article, User, Comments, Likes

admin.site.register(Article)
admin.site.register(User)
admin.site.register(Comments)
admin.site.register(Likes)
