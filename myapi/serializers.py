# serializers.py
from .components.no_association.heroes.serializer import HeroSerializer

from .components.one_to_many_association.todos.serializer import TodoSerializer
from .components.one_to_many_association.tasks.serializer import TaskSerializer

from .components.many_to_many_association.doctors.serializer import DoctorSerializer
from .components.many_to_many_association.patients.serializer import PatientSerializer
from .components.many_to_many_association.appointments.serializer import AppointmentSerializer
