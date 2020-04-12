from rest_framework import serializers
from .model import Todo

class TodoSerializerUnrelated(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = ['name', 'start_date', 'end_date']

