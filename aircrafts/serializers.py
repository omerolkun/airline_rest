from rest_framework import serializers
from .models import  Aircraft


class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft 
        fields = ["manufacturer_serial_number", "type", "model", "operator_airline", "number_of_engines"]



    
