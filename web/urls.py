from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import ToDoListView
from web.views import main

urlpatterns = [
    path('', main)
]
