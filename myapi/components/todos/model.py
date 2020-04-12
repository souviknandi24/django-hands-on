from django.db import models

class Todo(models.Model):
    name = models.CharField(null=False, max_length=100)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)

    def __str__(self):
        return self.name
