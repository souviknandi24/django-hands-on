from django.db import models


class Patient(models.Model):
    name = models.CharField(null=False, max_length=100)

    def __str__(self):
        return self.name
