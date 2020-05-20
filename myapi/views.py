# views.py
from rest_framework_json_api import views
from .components.no_association.heroes.view import HeroViewSet

from .components.one_to_many_association.todos.view import TodoViewSet
from .components.one_to_many_association.tasks.view import TaskViewSet

from .components.many_to_many_association.doctors.view import DoctorViewSet
from .components.many_to_many_association.patients.view import PatientViewSet
from .components.many_to_many_association.appointments.view import AppointmentViewSet
