# Register your models here.
from django.contrib import admin
from .models import Hero, Todo, Task

admin.site.register(Hero)
admin.site.register(Todo)
admin.site.register(Task)
