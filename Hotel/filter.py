import  django_filters
from .models import *

class HotelFilter(django_filters.FilterSet):
    keyword = django_filters.filters.CharFilter(field_name="name", lookup_expr="icontains")
    search_city = django_filters.filters.CharFilter(field_name="destination__city", lookup_expr="icontains")
    search_country = django_filters.filters.CharFilter(field_name="destination__country", lookup_expr="icontains")

    class Meta:
        model=Hotel
        fields=("keyword","location","search_country","search_city","rating")

class RoomFilter(django_filters.FilterSet):
    keyword=django_filters.filterset.CharFilter(field_name="hotel__name",lookup_expr="icontains")
    minPrice=django_filters.filters.NumberFilter(field_name="price" or 0,lookup_expr="get")
    maxPrice=django_filters.filters.NumberFilter(field_name="price" or 1000,lookup_expr="lte")

    class Meta:
        model=Room
        fields=("keyword","room_type","room_number","is_available","minPrice","maxPrice")