from django.shortcuts import render
from .models import Flight
# Create your views here.
def flights(request):
    return render(request , "flights/flights.html" , {
        "flights"  : Flight.objects.all()
    })
def flight(request ,flight_id ):
      flight =  Flight.objects.get(pk=flight_id)
      return render(request , "flights/flight.html",{
        "flight" : flight,
        "companies" : flight.companies.all()
    })    