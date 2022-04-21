from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from apis1.models import plane, airport, carrier, flight
from apis1.serializers import FlightModelSerializer
import django_filters.rest_framework


class GetAllData(APIView):
    search_fields = ['flight_source_airport']
    filter_backends = (filters.SearchFilter,)

    def get(self, request):
        query = flight.objects.all()
        serializer = FlightModelSerializer(query, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


# پروازهای ورودی و خروجی یک فرودگاه خاص
"""class GetAllFlightsFromSpecialAirportData(APIView):
    def get(self, request):
        query = flight.objects.filter(flight__datetime='4/4/2020 19:00')
        serializer = FlightModelSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)"""


"""class first(generics.ListAPIView):
    queryset = flight.objects.all()
    serializer_class = FlightModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['flight_source_airport']
    filter_backends = [filters.SearchFilter]
    search_fields = ['flight_source_city']
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['flight_source_city']"""

class customizd_filterset(django_filters.FilterSet):
   missing = django_filters.BooleanFilter(field_name='returned', lookup_expr='isnull')

   class Meta:
       model = flight
       fields = ['flight_source_airport', 'flight_destination_airport']


class first(generics.ListAPIView):
    queryset = flight.objects.all()
    serializer_class = FlightModelSerializer
    filter_backends = [DjangoFilterBackend]

    filterset_class = customizd_filterset

    #filterset_fields = ['flight_source_airport']
    #filterset_fields = ['flight_destination_airport']



"""class first(generics.ListAPIView):
    queryset = flight.objects.all()

    order_id = request.data["order_id"]
    zipcode = request.data["zipcode"]
    queryset = flight.objects.all()

    order = queryset.filter(order_id=order_id, zipcode=zipcode)
"""

"""    from django.db.models import Q
    queryset = flight.objects.all()
    serializer_class = FlightModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['flight_source_airport']

    order = queryset.filter(Q(order_id=order_id) & Q(zipcode=zipcode))"""

class second(generics.ListAPIView):
    queryset = flight.objects.all()
    serializer_class = FlightModelSerializer
    filter_backends = [DjangoFilterBackend]

    #filterset_class = customizd_filterset

    filterset_fields = ['flight_source_city', 'flight_destination_city']

class third(generics.ListAPIView):
    queryset = flight.objects.all()
    serializer_class = FlightModelSerializer
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['flight_price', 'flight_source_city', 'flight_destination_city']

class forth(generics.ListAPIView):
    queryset = flight.objects.all()
    serializer_class = FlightModelSerializer
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['flight_datetime', 'flight_price', 'flight_carrier']


class fifth(generics.ListAPIView):
    queryset = flight.objects.all()
    serializer_class = FlightModelSerializer
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['flight_carrier']