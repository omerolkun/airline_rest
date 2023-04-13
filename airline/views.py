from django.shortcuts import render
# Create your views here.


# todo/todo_api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Airline 
from .serializers import AirlineSerializer

class AirlineApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the Airline items for given requested user
        '''
        airlines = Airline.objects
        serializer = AirlineSerializer(airlines, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Airline with given Airline data
        '''
        data = {
            'name': request.data.get('name'), 
            'callsign': request.data.get('callsign'), 
            'founded_year': request.data.get('founded_year'),
            'base_airport': request.data.get('base_airport')

        }

        serializer = AirlineSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
