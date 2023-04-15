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
            'type': request.data.get('type'),
            'model': request.data.get('model'),
            'operator_airline': request.data.get('operator_airline'),
            'number_of_engines': request.data.get('number_of_engines')

        }

        serializer = AircraftSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







class AircraftDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, aircraft_idx): #chande paramater name 
        '''
        Helper method to get the object with given aircraft id 
        '''
        try:
            return Aircraft.objects.get( aircraft_id = aircraft_idx )
        except Aircraft.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, aircraft_idx, *args, **kwargs):
        '''
        Retrieves the Aircraft with given aircraft id 
        '''
        aircraft_instance = self.get_object( aircraft_idx )
        if not aircraft_instance:
            return Response(
                {"res": "Object with aircraft_id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = AircraftSerializer( aircraft_instance  )
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, aircraft_idx, *args, **kwargs):
        '''
        Updates the aircraft item with given aircraft_id if exists
        '''
        aircraft_instance = self.get_object( aircraft_idx )
        if not aircraft_instance:
            return Response(
                {"res": "Object with aircraft_id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            # i think no need for here, maybe i will delete later...
            # because the argument came from request
            'name': request.data.get('name'),
            'callsign': request.data.get('callsign'),
            'founded_year': request.data.get('founded_year'),
            'base_airport': request.data.get('base_airport')

        }
        serializer = AircraftSerializer(instance = aircraft_instance, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, aircraft_idx, *args, **kwargs):
        '''
        Deletes the aircraft item with given aircraft id if exists
        '''
        aircraft_instance = self.get_object(aircraft_idx)
        if not aircraft_instance:
            return Response(
                {"res": "Object with aircraft_id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        aircraft_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )




