from django.conf.urls import url
from rest_framework.authtoken import views as authviews

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/articles/$', views.get_articles, name='get_articles'),
    url(r'^api/latestarticles/$', views.get_latest_articles, name='get_latest_articles'),
    url(r'^api/article/(?P<pk>[0-9]*)', views.get_article, name='get_article'),
    url(r'^register$', views.register, name='register'),
    url(r'^comment$', views.comment, name='comment'),
    url(r'^login$', authviews.obtain_auth_token),
    url(r'^like/(?P<id>[\d]+)$', views.like, name='like'),
    url(r'^get_likes/(?P<id>[\d]+)$', views.get_likes, name='get_likes'),
<<<<<<< HEAD

    url(r'^like/(?P<id>[\d]+)/$', views.like, name='like'),

    url(r'^api/comments/(?P<id>[\d]+)/$',views.get_comments_for_article,name='get_comments_for_article'),
    url(r'^api/comment/(?P<id>[\d]+)/$',views.comment,name='comment'),
    
=======
    url(r'^get_user_info$', views.get_user_info, name='get_likes'),
    url(r'^modify$', views.modify_user, name='modify_user'),
>>>>>>> d546772df3d8f3ea26c4476ee342da67afe63804
]
