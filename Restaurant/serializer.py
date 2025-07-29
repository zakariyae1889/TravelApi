from  rest_framework import  serializers
from .models import  *


class RestaurantSirailzer(serializers.ModelSerializer):

    class Meta:
        model=Restaurants
        fileds=("")
