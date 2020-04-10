from django.db import models

# Create your models here.


class Hero(models.Model):
    name = models.CharField(null=False, max_length=60)
    alias = models.CharField(null=False, max_length=60)

    def __str__(self):
        return self.name

class Todo(models.Model):
    name = models.CharField(null=False, max_length=100)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)

    def __str__(self):
        return self.name
    
class Task(models.Model):
    name = models.CharField(null=False, max_length=100)
    todo = models.ForeignKey(Todo, related_name='tasks', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
