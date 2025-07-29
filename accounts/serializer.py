from rest_framework import serializers
from django.contrib.auth import  authenticate
from django.contrib.auth.models import User

from rest_framework_simplejwt.tokens import RefreshToken


class SignupSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
       model=User
       fields=["username","first_name","last_name","email","password"]
       extra_Kwargs={
           "username":{"required":True,"allow_blank":True},
           "first_name":{"required":True,"allow_blank":False},
           "last_name":{"required":True,"allow_blank":False},
           "email":{"required":True,"allow_blank":False},
           "password":{"required":True,"allow_blank":False,"min_length":8}
       }

class CustomTokenObtainPairSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()
    def validate(self,attrs):
       user=authenticate(username=attrs["username"],password=attrs["password"])
       if user is None:
            raise serializers.ValidationError('your password  or username not correct')
       refresh=RefreshToken.for_user(user)
       return {
            "access":str(refresh.access_token),
            "refresh":str(refresh)
        }