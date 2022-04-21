from rest_framework import serializers
from apis1.models import plane, airport, carrier, flight

class FlightModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = flight
        fields = '__all__'
