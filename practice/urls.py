from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView


urlpatterns = [
    url(r'^gamilton/$', views.gamiltontest, name='gamiltontest'),
    url(r'^gamilton/test/$', views.gamiltontestison, name='gamiltontestison'),
    url(r'^gamilton/test/finished$', views.gamiltontestfinished, name='gamiltontestfinished'),
]

