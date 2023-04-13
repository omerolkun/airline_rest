from rest_framework import serializers
from .models import  Airline, Aircraft


class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = ["name", "callsign", "founded_year", "base_airport"]
