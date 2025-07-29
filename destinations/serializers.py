from rest_framework import serializers
from .models import *

class DestinationsSerializer(serializers.ModelSerializer):

  class Meta:
         model=Destination
         fields='__all__'

class AttractionSerializer(serializers.ModelSerializer):
    country=serializers.ReadOnlyField(source="destinations.country")
    city = serializers.ReadOnlyField(source="destinations.city")
    class Meta:
        model = Attraction
        fields = ("country","city","name","description","image","openigHours","ticketPrice")




