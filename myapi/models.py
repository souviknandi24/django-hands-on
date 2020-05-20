# models.py
from .components.no_association.heroes.model import Hero

from .components.one_to_many_association.todos.model import Todo
from .components.one_to_many_association.tasks.model import Task

from .components.many_to_many_association.doctors.model import Doctor
from .components.many_to_many_association.patients.model import Patient
from .components.many_to_many_association.appointments.model import Appointment
