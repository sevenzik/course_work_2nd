from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^graphs/$', views.theory_graphs, name='theory_graphs'),
    url(r'^gamilton/$', views.theory_gamilton, name='theory_gamilton'),
    url(r'^euler/$', views.theory_euler, name='theory_euler'),
    url(r'^fleri/$', views.theory_fleri, name='theory_fleri'),
    url(r'^cycles/$', views.theory_cycles, name='theory_cycles'),
]

