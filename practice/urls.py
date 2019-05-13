from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView
from practice.models import Task


urlpatterns = [
    url(r'^gamilton/$', views.gamiltontest, name='gamiltontest'),
    url(r'^euler/$', views.eulertest, name='eulertest'),
    url(r'^all/$', views.alltest, name='alltest'),
    url(r'^yourtestlist/$', views.yourtestlist, name='yourtestlist'),
    url(r'^gamilton/test/$', views.TestIsOnView.as_view(), name='gamiltontestison'),
    url(r'^euler/test/$', views.TestIsOnView.as_view(), name='eulertestison'),
    url(r'^all/test/$', views.TestIsOnView.as_view(), name='alltestison'),
    url(r'^yourtest/([0-9]+)$', views.yourtest, name='yourtest'),
]

