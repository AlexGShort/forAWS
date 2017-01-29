from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new$', views.new, name='new'),
    url(r'^create$', views.create, name='create'),
    url(r'^show/(?P<id>\d+)', views.show, name='show'),
    url(r'^join/(?P<trip_id>\d+)', views.join, name='join'),
]
