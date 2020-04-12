# heroes.py
from django.db import models
from rest_framework import viewsets, serializers


class Hero(models.Model):
    name = models.CharField(null=False, max_length=60)
    alias = models.CharField(null=False, max_length=60)

    def __str__(self):
        return self.name


class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ['name', 'alias']


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('id')
    serializer_class = HeroSerializer
