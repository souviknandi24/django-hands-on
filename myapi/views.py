# views.py
from rest_framework_json_api import views

from .components.heroes import HeroViewSet
from .components.todos import TodoViewSet
from .components.tasks import TaskViewSet
