from django.db.models import Prefetch
from rest_framework import viewsets
from .model import Task
from .serializer import TaskSerializer
from ..todos.model import Todo

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('id')
    serializer_class = TaskSerializer
    select_for_includes = {
        'todo': ['todo__name'],
    }
    prefetch_for_includes = {
        '__all__': [],
        'all_todos': [Prefetch('all_todos', queryset=Todo.objects.select_related('name'))],
    }


