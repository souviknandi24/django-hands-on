from django.db.models import Prefetch
from rest_framework import viewsets
from .model import Appointment
from .serializer import AppointmentSerializer

from ..doctors.model import Doctor
from ..patients.model import Patient
from ..doctors.serializer import DoctorSerializer
from ..patients.serializer import PatientSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all().order_by('id')
    serializer_class = AppointmentSerializer
    select_for_includes = {
        'doctor': ['doctor__name'],
        'patient': ['patient__name']
    }
    prefetch_for_includes = {
        '__all__': [],
        'all_doctors': [Prefetch('all_doctors', queryset=Doctor.objects.select_related('name'))],
        'all_patients': [Prefetch('all_patients', queryset=Patient.objects.select_related('name'))],
    }
