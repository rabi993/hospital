from rest_framework import serializers
from . import models
class AppointmentSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(many= False)
    
    
    class Meta:
        model = models.Appointment
        fields= '__all__'


