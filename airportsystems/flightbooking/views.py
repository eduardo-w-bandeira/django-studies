from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Passenger, Flight, Booking
from .forms import PassengerForm, FlightForm, BookingForm


# Views for Passenger
def index(request):
    return HttpResponse("Airport System!")


def list_passengers(request):
    passengers = Passenger.objects.all()
    return render(request, "list_passengers.html", {"passengers": passengers})


def get_passenger(request, passenger_id):
    passenger = Passenger.objects.get(pk=passenger_id)
    json = passenger.serialize()
    return JsonResponse(json, safe=False)


def create_passenger(request):
    PAGE_TITLE = "Create Passenger"
    if request.method == "POST":
        form = PassengerForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the passenger list page after creating a passenger
            return redirect("list_passengers")
    else:
        form = PassengerForm()
    context = {"form": form,
               "page_title": PAGE_TITLE,
               "button_label": "Create", }
    return render(request, "creating_or_updating_base.html", context)


def update_passenger(request, passenger_id):
    PAGE_TITLE = "Update Passenger"
    passenger = get_object_or_404(Passenger, pk=passenger_id)
    if request.method == "POST":
        form = PassengerForm(request.POST, instance=passenger)
        if form.is_valid():
            form.save()
            # Redirect to the updated passenger"s details page
            return redirect("get_passenger", passenger_id=passenger_id)
    else:
        form = PassengerForm(instance=passenger)
    context = {"form": form,
               "page_title": PAGE_TITLE,
               "button_label": "Update", }
    return render(request, "creating_or_updating_base.html", context)


def delete_passenger(request, passenger_id):
    passenger = get_object_or_404(Passenger, pk=passenger_id)
    name = passenger.name
    passenger.delete()
    return JsonResponse({"message": f"Passenger {name} (id: {passenger_id}) deleted!"}, safe=False)


# Views for Flights
def list_flights(request):
    flights = Flight.objects.all()
    return render(request, "list_flights.html", {"flights": flights})


def get_flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    json = flight.serialize()
    return JsonResponse(json, safe=False)


def create_flight(request):
    PAGE_TITLE = "Create Flight"
    if request.method == "POST":
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the flight list page after creating a flight
            return redirect("list_flights")
    else:
        form = FlightForm()
    context = {"form": form,
               "page_title": PAGE_TITLE,
               "button_label": "Create", }
    return render(request, "creating_or_updating_base.html", context)


def update_flight(request, flight_id):
    PAGE_TITLE = "Update Flight"
    flight = get_object_or_404(Flight, pk=flight_id)
    if request.method == "POST":
        form = FlightForm(request.POST, instance=flight)
        if form.is_valid():
            form.save()
            # Redirect to the updated flight"s details page
            return redirect("get_flight", flight_id=flight_id)
    else:
        form = FlightForm(instance=flight)
    context = {"form": form,
               "page_title": PAGE_TITLE,
               "button_label": "Update", }
    return render(request, "creating_or_updating_base.html", context)


def delete_flight(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)
    flight_number = flight.flight_number
    flight.delete()
    return JsonResponse({"message": f"Flight Number {flight_number} deleted!"}, safe=False)


# Views for Bookings
def list_bookings(request):
    bookings = Booking.objects.all()
    return render(request, "list_bookings.html", {"bookings": bookings})


def get_booking(request, booking_id):
    booking = Booking.objects.get(pk=booking_id)
    json = booking.serialize()
    return JsonResponse(json, safe=False)


def create_booking(request):
    PAGE_TITLE = "Create Booking"
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the booking list page after creating a booking
            return redirect("list_bookings")
    else:
        form = BookingForm()
    context = {"form": form,
               "page_title": PAGE_TITLE,
               "button_label": "Create", }
    return render(request, "creating_or_updating_base.html", context)


def update_booking(request, booking_id):
    PAGE_TITLE = "Update Booking"
    booking = get_object_or_404(Booking, pk=booking_id)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            # Redirect to the updated booking"s details page
            return redirect("get_booking", booking_id=booking_id)
    else:
        form = BookingForm(instance=booking)
    context = {"form": form,
               "page_title": PAGE_TITLE,
               "button_label": "Update", }
    return render(request, "creating_or_updating_base.html", context)


def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    booking_number = booking.booking_number
    booking.delete()
    return JsonResponse({"message": f"Booking Number {booking_number} deleted!"}, safe=False)
