
from .views import  HotelApp

from django.urls import  path

urlpatterns=[
    path("Hotels/",HotelApp.get_Hotel),
    path("Hotels/<str:slug>",HotelApp.get_deitals_hotel),
    path("Hotels/Rooms/",HotelApp.get_Room)
]