from rest_framework import  serializers
from .models import *

class HotelSerializers(serializers.ModelSerializer):
    country = serializers.ReadOnlyField(source="destination.country")
    city=serializers.ReadOnlyField(source="destination.city")
    number_of_rooms=serializers.ReadOnlyField(source="numbr_of_rooms")
    class Meta:
        model=Hotel
        fields=("country","city","name","location","description","number_of_rooms","rating" ,"image","slug")



class RoomSerializers(serializers.ModelSerializer):
    country = serializers.ReadOnlyField(source="hotel.destination.country")
    city = serializers.ReadOnlyField(source="hotel.destination.city")
    name=serializers.ReadOnlyField(source="hotel.name")
    class Meta:
        model=Room
        fields=("country","city","name","room_type","room_number","price","image","is_available")