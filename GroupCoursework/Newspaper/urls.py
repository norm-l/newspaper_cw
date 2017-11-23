from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^al/$', views.article_list_placeholder, name='article_list_placeholder') # Testing purposes only
]