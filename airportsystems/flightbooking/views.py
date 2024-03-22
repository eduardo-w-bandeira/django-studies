from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Passenger, Flight, Booking

# Views for Passenger


def home(request):
    return HttpResponse("Airport System")


def list_passengers(request):
    passengers = Passenger.objects.all()
    return render(request, 'list_passengers.html', {'passengers': passengers})
