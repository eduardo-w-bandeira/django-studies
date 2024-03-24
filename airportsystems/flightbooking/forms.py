from django import forms
from .models import Passenger, Flight, Booking


class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ['name', 'email', 'phone', 'address',]


class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ["flight_number", "departure_airport",
                  "arrival_airport", "departure_time",
                  "arrival_time", "capacity", "price",
                  ]


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["passenger",  "flight", "booking_date",
                  "seat_number", "status",
                  ]
