from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *
from .filter import *


class DestinationsApp:
    @api_view(["GET"])
    def get_destination(request):
        try:
           query=Destination.objects.all().order_by("-create")
           filterDest=DestinationFilter(request.GET,queryset=query)
           serializer=DestinationsSerializer(filterDest.qs,many=True)
           
           return Response({"destinations":serializer.data},status=status.HTTP_200_OK)

        except Exception as e:
            print("ERROR:", e)  # يظهر في console
            return Response({"message": "Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    @api_view(["GET"])
    def get_detils_destination(request,slug):
      try:
           DestinationDetails = get_object_or_404(Destination,slug=slug)
           serializer=DestinationsSerializer(DestinationDetails,many=False)

           return Response({"detials":serializer.data},status=status.HTTP_200_OK)
      except Exception as e :
          print("ERROR:", e)  # يظهر في console
          return Response({"message": "Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      # -------------------------------------------#
    @api_view(["GET"])
    def get_Attraction(request):
        try:
           query=Attraction.objects.all().order_by("-create")
           filterAttracton=AttractionFilter(request.GET,queryset=query)
           serializer=AttractionSerializer(filterAttracton.qs,many=True)
           return  Response({"Attractions":serializer.data},status=status.HTTP_200_OK)
        except Exception as e :
            print("ERROR",e)
            return Response({"message":"Internal server error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    @api_view(["GET"])
    def get_details_Attraction(request,slug):
        try:
           AttractionDetails=get_object_or_404(Attraction,slug=slug)

           serializer=AttractionSerializer(AttractionDetails,many=False)
           return Response({"details":serializer.data},status=status.HTTP_200_OK)
        except Exception as e :
            print("ERROR",e)
            return Response({"message":"Internal server error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)




