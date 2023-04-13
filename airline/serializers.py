from rest_framework import serializers
from .models import  Airline, Aircraft


class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = ["name", "callsign", "founded_year", "base_airport"]



class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = ["manufacturer_serial_number", "aircraft_type", "model", "number_of_engines", "operatior_airline"]
        
