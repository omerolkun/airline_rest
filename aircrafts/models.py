import sys
sys.path.append("../")
from airline import Airline
from django.db import models
# Create your models here.



class Aircraft(models.Model):
    aircraft_id = models.AutoField(primary_key = True)
    manufacturer_serial_number = models.IntegerField()
    aircraft_type= models.CharField(max_length=25)
    model= models.CharField(max_length=25)
    number_of_engines = models.IntegerField()
    operator_airline = models.ForeignKey(Airline, on_delete = models.CASCADE)


    def __str__(self):
        return self.name



