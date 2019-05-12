from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView


urlpatterns = [
    url(r'^gamilton/$', views.gamiltontest, name='gamiltontest'),
    url(r'^euler/$', views.eulertest, name='eulertest'),
    url(r'^all/$', views.alltest, name='alltest'),
    url(r'^gamilton/test/$', views.TestIsOnView.as_view(), name='gamiltontestison'),
    url(r'^euler/test/$', views.TestIsOnView.as_view(), name='eulertestison'),
    url(r'^all/test/$', views.TestIsOnView.as_view(), name='alltestison'),
    #url(r'^gamilton/test/finished$', views.gamiltontestfinished, name='gamiltontestfinished'),
]

