from django.db import models
from ..todos.model import Todo


class Task(models.Model):
    name = models.CharField(null=False, max_length=100)
    todo = models.ForeignKey(Todo, related_name='tasks',
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.name
