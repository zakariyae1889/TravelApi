import django_filters
from .models import *

class DestinationFilter(django_filters.FilterSet):
    search_city = django_filters.filters.CharFilter(field_name="city", lookup_expr="icontains")
    search_country = django_filters.filters.CharFilter(field_name="country", lookup_expr="icontains")
    class Meta:
        model=Destination
        fields=("search_city","search_country")

class AttractionFilter(django_filters.FilterSet):
    keyword=django_filters.filters.CharFilter(field_name="name",lookup_expr="icontains")
    minPrice=django_filters.filters.NumberFilter(field_name="ticketPrice" or 0 , lookup_expr="get")
    maxPrice=django_filters.filters.NumberFilter(field_name="ticketPrice" or 10000 , lookup_expr="lte")

    class Meta:
        model=Attraction
        fields=("keyword","minPrice","maxPrice")
        


        