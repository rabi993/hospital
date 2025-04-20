from django.db import models
# from django.contrib.auth.models import User
from patient.models import Patient
from doctor.models import Doctor, AvailableTime
# Create your models here.
APPOINTMENT_STATUS =[
    ('Completed', 'Completed'),
    ('Pending', 'Pending'),
    ('Running', 'Running'),
]

class Appointment(models.Model):
    patient= models.ForeignKey(Patient, on_delete= models.CASCADE)
    doctor= models.ForeignKey(Doctor, on_delete= models.CASCADE)
    appointment_Status = models.CharField(choices=APPOINTMENT_STATUS, max_length=15, default='Pending')
    symptom = models.TextField()
    phone_no = models.CharField(max_length=12, null=True, blank=True, default="0000000000")
    time = models.ForeignKey(AvailableTime, on_delete= models.CASCADE)
    payment = models.BooleanField(default=False)
    cancel = models.BooleanField(default=False)

    def __str__(self):
        return f"Doctor : {self.doctor.user.first_name} , Patient : {self.patient.user.first_name} "
