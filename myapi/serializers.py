# serializers.py
from rest_framework import serializers

from .models import Hero, Todo, Task


class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ['name', 'alias']

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = ['name', 'start_date', 'end_date']

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    included_serializers = {
        'todo': TodoSerializer
    }

    class Meta:
        model = Task
        fields = ['name', 'todo']
    
    class JSONAPIMeta:
        select_related = ['todo']

