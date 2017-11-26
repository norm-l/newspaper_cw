from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^article$',views.article,name='article'),
    url(r'^api/latestarticles/$', views.get_latest_articles),
    url(r'^api/article/(?P<pk>[0-9]*)', views.get_article),

]
