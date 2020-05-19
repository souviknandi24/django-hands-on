from rest_framework import serializers
from .model import Task


class TaskSerializerUnrelated(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['name']
