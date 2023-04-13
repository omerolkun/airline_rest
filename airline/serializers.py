from rest_framework import serializers
from .models import  Airline


class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = ["name", "callsign", "founded_year", "base_airport"]


