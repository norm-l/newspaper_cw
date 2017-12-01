from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^article$',views.article,name='article'),
    url(r'^api/articles/$', views.get_articles, name='get_articles'),
    url(r'^api/latestarticles/$', views.get_latest_articles, name='get_latest_articles'),
    url(r'^api/article/(?P<pk>[0-9]*)', views.get_article, name='get_article'),
    url(r'^login$',views.authentication,name='login'),
    url(r'^register$',views.register,name='register'),

]
