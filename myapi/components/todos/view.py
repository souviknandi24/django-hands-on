from rest_framework import viewsets
from .model import Todo
from .serializer import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all().order_by('id')
    serializer_class = TodoSerializer
