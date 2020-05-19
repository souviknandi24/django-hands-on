# views.py
from rest_framework_json_api import views
from .components.no_association.heroes.view import HeroViewSet
from .components.one_to_many_association.todos.view import TodoViewSet
from .components.one_to_many_association.tasks.view import TaskViewSet
