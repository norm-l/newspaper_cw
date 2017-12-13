from django.conf.urls import url
from rest_framework.authtoken import views as authviews

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/articles/$', views.get_articles, name='get_articles'),
    url(r'^api/latestarticles/$', views.get_latest_articles, name='get_latest_articles'),
    url(r'^api/article/(?P<pk>[0-9]*)', views.get_article, name='get_article'),
    # url(r'^login$', views.authentication, name='login'),
    url(r'^register$', views.register, name='register'),
    url(r'^comment$', views.comment, name='comment'),
    url(r'^login$', authviews.obtain_auth_token),

    url(r'^like/(?P<id>[\d]+)/$', views.like, name='like'),
]
