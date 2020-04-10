from django.shortcuts import render
from rest_framework import viewsets

from .serializers import HeroSerializer, TodoSerializer, TaskSerializer
from .models import Hero, Todo, Task
from rest_framework_json_api import views
from django.db.models import Prefetch


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('id')
    serializer_class = HeroSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all().order_by('id')
    serializer_class = TodoSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('id')
    serializer_class = TaskSerializer
    select_for_includes = {
        'todo': ['todo__name'],
    }
    prefetch_for_includes = {
        '__all__': [],
        'all_todos': [Prefetch('all_todos', queryset=Todo.objects.select_related('name'))],
        'category.section': ['category']
    }
