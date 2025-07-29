from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializer import *
from django.contrib.auth.hashers  import  make_password
from rest_framework.authtoken.models import Token

class Authentication:
    user = User.objects.get(username="luffy0001")  # عدّل الاسم
    token, created = Token.objects.get_or_create(user=user)
    print(token.key)
    """"SingUp"""
    @api_view(['POST'])
    def signup_view(request):
      data=request.data
      user=SignupSerializer(data=data)
      if user.is_valid():
          if not User.objects.filter(username=data["email"]).exists():
              User.objects.create(
                  username=data["username"],
                  first_name=data["first_name"],
                  last_name=data["last_name"],
                  email=data["email"],
                  password=make_password(data["password"])
              )
              return  Response(
                  {
                      "message":"your account register susccessfuly"
                  },
                  status=status.HTTP_201_CREATED
              )
          else:
              return Response({
                  "message":"this user already exists"
              },

              status = status.HTTP_400_BAD_REQUEST
              )
      else:
          return Response(user.errors)

    """" Login """
    @api_view(['POST'])
    def login_views(request):
       serializers=CustomTokenObtainPairSerializer(data=request.data)
       if serializers.is_valid():
           return Response(serializers.validated_data)
       return Response({"error":"Invalid credentials"},status=400)

    """" logout """
    @api_view(["POST"])
    @permission_classes([IsAuthenticated])
    def logout_views(request):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            return Response({"message": "Logout successfully"}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({"error": "No token found for this user."}, status=status.HTTP_400_BAD_REQUEST)

    """" changePassword """


    @api_view(["POST"])
    @permission_classes([IsAuthenticated])
    def changePassword(request):
        user=request.user
        old_pass=request.data.get('old_password')
        new_pass=request.data.get('new_password')
        if not user.check_password(old_pass):
            return Response({"error":"password not correct"},status=400)
        user.set_password(new_pass)
        user.save()
        return Response({"message": " your password change susccessfuly "}, status=200)

    """" Current User """
    @api_view(["GET"])
    @permission_classes([IsAuthenticated])
    def current_user(request):
        user=request.user
        return Response({
            'username':user.username,
            'firstName':user.first_name,
            'LastName':user.last_name,
            'Email':user.email
        },status=200)

