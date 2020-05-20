from django.db import models

from ..doctors.model import Doctor
from ..patients.model import Patient


class Appointment(models.Model):
    scheduled_at = models.DateTimeField(null=False)
    doctor = models.ForeignKey(
        Doctor, related_name='doctor', on_delete=models.CASCADE)
    patient = models.ForeignKey(
        Patient, related_name='patient', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
