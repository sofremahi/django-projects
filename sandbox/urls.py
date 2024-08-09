from django.urls import path
from sandbox import views
#https://mysite.com/
urlpatterns = [
    path("", views.hello) ,
]
