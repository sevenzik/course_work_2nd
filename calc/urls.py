from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^fleri$', views.FleriCalc.as_view(), name='fleri_calc'),
]
