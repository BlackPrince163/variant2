from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import ToDoListView

router = DefaultRouter()
router.register('todo', ToDoListView, basename="todo")

urlpatterns = [
    path('', include(router.urls))
]
