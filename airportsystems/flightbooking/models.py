from django.db import models
from django.core import serializers

STATUS_CHOICES = (
    ("operational", "Operational"),
    ("confirmed", "Confirmed"),
    ("pending", "Pending"),
    ("canceled", "Canceled"),
)


class Passenger(models.Model):
    passenger_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    address = models.CharField(max_length=40)

    def serialize(self) -> str:
        return serializers.serialize("json", [self])


class Flight(models.Model):
    flight_id = models.AutoField(primary_key=True)
    flight_number = models.PositiveIntegerField()
    departure_airport = models.CharField(
        max_length=3, help_text="IATA code with 3 chars")
    arrival_airport = models.CharField(
        max_length=3, help_text="IATA code with 3 chars")
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    capacity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def serialize(self):
        return serializers.serialize("json", [self])


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    booking_date = models.DateField()
    seat_number = models.PositiveSmallIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def serialize(self):
        return serializers.serialize("json", [self])
