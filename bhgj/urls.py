from django.conf.urls import include, url

from . import views

app_name = 'bhgj'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id_num>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<id_num>[0-9]+)/del/$', views.delete, name='del'),
    url(r'^conf/$', views.conf, name='conf'),
    url(r'^(?P<id_num>[0-9]+)/stat/$', views.list, name='list'),
    url(r'^(?P<id_num>[0-9]+)/stat/(?P<name>[0-9]+)/$', views.stat, name='stat'),
    url(r'^(?P<id_num>[0-9]+)/reset/$', views.reset, name='reset'),
    url(r'^(?P<id_num>[0-9]+)/reset/stat/$', views.relist, name='relist'),
    url(r'^(?P<id_num>[0-9]+)/reset/stat/(?P<name>[0-9]+)/$', views.restat, name='restat'),
]