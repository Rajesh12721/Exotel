from django.contrib import admin
from django.urls import path
from newsapp import views

urlpatterns = [
    path('index/',views.index,name='index'),
]