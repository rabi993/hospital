from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from . import models
from . import serializers
class AppointmentViewset(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializer
    
    