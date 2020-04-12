# todos.py
from django.db import models
from django.db.models import Prefetch
from rest_framework import viewsets, serializers



class Todo(models.Model):
    name = models.CharField(null=False, max_length=100)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)

    def __str__(self):
        return self.name


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class TaskSerializer1(serializers.HyperlinkedModelSerializer):
        class Meta:
            class Task1(models.Model):
                name = models.CharField(null=False, max_length=100)
                
                def __str__(self):
                    return self.name

            model = Task1
            fields = ['name']

    included_serializers = {
        'tasks': TaskSerializer1,
    }

    class Meta:
        model = Todo
        fields = ['name', 'start_date', 'end_date', 'tasks']

    class JSONAPIMeta:
        select_related = ['tasks']


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all().order_by('id')
    serializer_class = TodoSerializer
