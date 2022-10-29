from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from api.models import ToDoList
from api.serializers import ToDoListSerializer


class ToDoListView(ModelViewSet):
    serializer_class = ToDoListSerializer
    queryset = ToDoList.objects.all()
