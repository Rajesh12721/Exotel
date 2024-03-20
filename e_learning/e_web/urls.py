from django.contrib import admin
from django.urls import path
from e_web import views

urlpatterns = [
    path('index/',views.index,name='index'),
]