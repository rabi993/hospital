from django.contrib import admin
from . import models
# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display =['doctor_name','patient_name','appointment_Status','symptom','time','fees','cancel','payment',]

    def patient_name(self,obj):
        return obj.patient.user.first_name
    def doctor_name(self,obj):
        return obj.doctor.user.first_name
    def fees(self,obj):
        return obj.doctor.fee
    def payment(self,obj):
        return obj.doctor.payment
    
admin.site.register(models.Appointment,AppointmentAdmin)