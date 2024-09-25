from django.urls import path
from . import views
urlpatterns = [
     path('', views.flights , name="flights") ,
     path('<int:flight_id>' , views.flight , name = "flight")

 ]
 