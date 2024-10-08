from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.city} ({self.code})"
    
class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE , related_name= "departures")
    destination = models.ForeignKey(Airport , on_delete= models.CASCADE , related_name= "arrivals")
    duration = models.IntegerField()
    def __str__(self):
     return f"{self.origin} to {self.destination} estimated time : {self.duration}" 

class Company(models.Model):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=2)
    flights = models.ManyToManyField(Flight , blank = False , related_name="companies" )
     
    def __str__(self):
        return f"{self.name} airlines : {self.code}"
 