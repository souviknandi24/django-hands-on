# views.py
from rest_framework_json_api import views
from .components.heroes.view import HeroViewSet
from .components.todos.view import TodoViewSet
from .components.tasks.view import TaskViewSet
