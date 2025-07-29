from django.shortcuts import render
from rest_framework.decorators import  APIView
from rest_framework.response import Response


# Create your views here.

class getAllResutrant(APIView):
    def get(self,request):
        try:
            pass
        except Exception as e:
            return Response({"message":"Int"})
