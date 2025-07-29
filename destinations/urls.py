from .models import Attraction
from .views import DestinationsApp
from django.urls import path

urlpatterns = [
    path("Destination/",DestinationsApp.get_destination),
    path("Destination/<str:slug>",DestinationsApp.get_detils_destination),

    path("Attraction/",DestinationsApp.get_Attraction),

    path("Attraction/<str:slug>",DestinationsApp.get_details_Attraction),


]