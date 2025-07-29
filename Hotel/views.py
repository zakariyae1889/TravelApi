from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *
from .filter import *

class HotelApp:



    @api_view(["GET"])
    def get_Hotel(request):
        try:
           query=Hotel.objects.all().order_by("-create")
           filterHotel=HotelFilter(request.GET,queryset=query)
           serializer=HotelSerializers(filterHotel.qs,many=True)
           return Response({"Hotels":serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return  Response({"message":"Internal server error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    #------------------------------------------#
    @api_view(["GET"])
    def get_deitals_hotel(request,slug):
        try:
           hotelDetails=get_object_or_404(Hotel,slug=slug)
           serializer=HotelSerializers(hotelDetails,many=False)
           return Response({"Hotel": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": "Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    # ------------------------------------------#
    @api_view(["GET"])
    def get_Room(request):
        try:
            query = Room.objects.all().order_by("-create")

            filterRoom = RoomFilter(request.GET, queryset=query)

            serializer = RoomSerializers(filterRoom.qs, many=True)

            return Response({"Rooms": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": "Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



