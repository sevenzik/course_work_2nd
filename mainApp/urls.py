from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^theory$', views.index, name='index'),
    url(r'^theory/', include('theory.urls')),
    url(r'^practice/', include('practice.urls')),
]
