from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^article$',views.article,name='article'),
     url(r'^latestarticles/$', views.get_latest_articles),

]
