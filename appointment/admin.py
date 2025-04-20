from django.contrib import admin
from . import models
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import redirect
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
    def save_model(self, request, obj, form, change):
        obj.save()
        if obj.appointment_Status == "Running":
            email_subject = "Your Appointment is Running"
            email_body = render_to_string('admin_emailRunning.html', {'user' : obj.patient.user, 'doctor' : obj.doctor})
            
            email = EmailMultiAlternatives(email_subject , '', to=[obj.patient.user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
        elif obj.appointment_Status == "Completed" and obj.payment== True :
            email_subject = "Your Appointment is Completed and paid done!"
            email_body = render_to_string('admin_emailCompleted.html', {'user' : obj.patient.user, 'doctor' : obj.doctor})
            
            email = EmailMultiAlternatives(email_subject , '', to=[obj.patient.user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
        elif obj.appointment_Status == "Pending":
            email_subject = "Your Appointment is Accepted!"
            email_body = render_to_string('admin_emailPending.html', {'user' : obj.patient.user, 'doctor' : obj.doctor})
            
            email = EmailMultiAlternatives(email_subject , '', to=[obj.patient.user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()

admin.site.register(models.Appointment,AppointmentAdmin)