from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.login, name='index'),
    url(r'^login$', views.login, name='login'),
    url(r'^registration$', views.registration, name='registration'),
    url(r'^success$', views.success, name='success'),
    url(r'^logout$', views.logout, name='logout'),
]
