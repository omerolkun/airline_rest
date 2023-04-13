from django.db import models

# Create your models here.



class Airline(models.Model):
    airline_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=100)
    callsign = models.CharField(max_length=25)
    founded_year = models.IntegerField() 
    base_airport = models.CharField(max_length = 100)


    def __str__(self):
        result = ""
        result = result +str(self.airline_id) + ", " + self.name
        return result 



