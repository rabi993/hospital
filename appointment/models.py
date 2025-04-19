from django.db import models
from patient.models import Patient
from doctor.models import Doctor
# Create your models here.
class Appointment(models.Model):
    patient= models.ForeignKey(Patient, on_delete= models.CASCADE)
    doctor= models.ForeignKey(Doctor, on_delete= models.CASCADE)