from django.db import models
from datetime import datetime

FLIGHT_CLASS_SELECTION = (
    ("A", "A"),
    ("B", "B"),
    ("C", "C"),
)

CARRIER_RATE_SELECTION = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
)


class plane(models.Model):
    plane_name = models.CharField(max_length=50)
    plane_capacity = models.IntegerField()


class airport(models.Model):
    airport_city_name = models.CharField(max_length=50)
    airport_abreviation = models.CharField(max_length=50)


class carrier(models.Model):
    carrier_name = models.CharField(max_length=50)
    carrier_rate = models.CharField(max_length=50, choices=CARRIER_RATE_SELECTION)


class flight2(models.Model):
    flight_datetime = models.DateTimeField()
    flight_price = models.IntegerField()
    flight_class = models.CharField(max_length=50, choices=FLIGHT_CLASS_SELECTION)
    flight_source_city = models.CharField(max_length=50)
    flight_source_airport = models.ForeignKey(airport, on_delete=models.CASCADE, related_name='flight_source_airport')
    flight_destination_city = models.CharField(max_length=50)
    flight_destination_airport = models.ForeignKey(airport, on_delete=models.CASCADE, related_name='flight_destination_airport')
    flight_carrier = models.ForeignKey(carrier, on_delete=models.CASCADE)
    flight_plane = models.ForeignKey(plane, on_delete=models.CASCADE)

class flight(models.Model):
    flight_datetime = models.DateTimeField()
    flight_price = models.IntegerField()
    flight_class = models.CharField(max_length=50)
    flight_source_city = models.CharField(max_length=50)
    flight_source_airport = models.CharField(max_length=50)
    flight_destination_city = models.CharField(max_length=50)
    flight_destination_airport = models.CharField(max_length=50)
    flight_carrier = models.CharField(max_length=50)
    flight_plane = models.CharField(max_length=50)

    def __str__(self):
        return self.flight_source_city
