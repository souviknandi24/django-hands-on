# tasks.py
from django.db import models
from django.db.models import Prefetch
from rest_framework import viewsets, serializers

from .todos import Todo, TodoSerializer


class Task(models.Model):
    name = models.CharField(null=False, max_length=100)
    todo = models.ForeignKey(Todo, related_name='tasks', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    included_serializers = {
        'todo': TodoSerializer
    }

    class Meta:
        model = Task
        fields = ['name', 'todo']
    
    class JSONAPIMeta:
        select_related = ['todo']


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



