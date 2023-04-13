from django.shortcuts import render
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Aircraft
from .serializers import AircraftSerializer


class AircraftApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the Aircraft items for given requested user
        '''
        aircrafts = Aircraft.objects
        serializer = AircraftSerializer(aircrafts, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Aircraft with given Aircraft data
        '''
        data = {
            'manufacturer_serial_number': request.data.get('manufacturer_serial_number'),
            'aircraft_type': request.data.get('aircraft_type'),
            'model': request.data.get('model'),
            'operator_airline': request.data.get('operator_airline'),
            'number_of_engines': request.data.get('number_of_engines')

        }

        serializer = AircraftSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





