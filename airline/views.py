from django.shortcuts import render
# Create your views here.


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Airline 
from .serializers import AirlineSerializer


class AirlineApiView(APIView):
    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]

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






class AirlineDetailApiView(APIView):
    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]

    def get_object(self, airline_idx): #chande paramater name 
        '''
        Helper method to get the object with given airline id 
        '''
        try:
            return Airline.objects.get( airline_id = airline_idx )
        except Airline.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, airline_idx, *args, **kwargs):
        '''
        Retrieves the Todo with given todo_id
        '''
        airline_instance = self.get_object( airline_idx )
        if not airline_instance:
            return Response(
                {"res": "Object with airline_id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = AirlineSerializer( airline_instance  )
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, airline_idx, *args, **kwargs):
        '''
        Updates the todo item with given todo_id if exists
        '''
        airline_instance = self.get_object( airline_idx )
        if not airline_instance:
            return Response(
                {"res": "Object with airline_id does not exists"}, 
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
        serializer = AirlineSerializer(instance = airline_instance, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, airline_idx, *args, **kwargs):
        '''
        Deletes the todo item with given todo_id if exists
        '''
        airline_instance = self.get_object(airline_idx)
        if not airline_instance:
            return Response(
                {"res": "Object with airline_id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        airline_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )




