from rest_framework import serializers
from .model import Appointment

from ..doctors.serializer import DoctorSerializer
from ..patients.serializer import PatientSerializer


class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    included_serializers = {
        'doctor': DoctorSerializer,
        'patient': PatientSerializer,
    }

    class Meta:
        model = Appointment
        fields = ['scheduled_at', 'doctor', 'patient']

    class JSONAPIMeta:
        select_related = ['doctor', 'patient']
