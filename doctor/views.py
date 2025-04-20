
from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticated,IsAdminUser, IsAuthenticatedOrReadOnly
# Create your views here.
class DoctorViewset(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]

    queryset = models.Doctor.objects.all()
    serializer_class = serializers.DoctorSerializer
    
class SpecializationViewset(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]

    queryset = models.Specialization.objects.all()
    serializer_class = serializers.SpecializationSerializer
    
class DesignationViewset(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]

    queryset = models.Designation.objects.all()
    serializer_class = serializers.DesignationSerializer
    
class AvailableTimeViewset(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    
    queryset = models.AvailableTime.objects.all()
    serializer_class = serializers.AvailableTimeSerializer
    
    