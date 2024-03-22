from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Passenger, Flight, Booking

# Views for Passenger


def home(request):
    return HttpResponse("Airport System")


def list_passengers(request):
    passengers = Passenger.objects.all()
    data = [{'passenger_id': passenger.passenger_id, 'name': passenger.name, 'email': passenger.email,
             'phone': passenger.phone, 'address': passenger.address} for passenger in passengers]
    return JsonResponse(data, safe=False)


def create_passenger(request):
    # Your code to create a new passenger goes here
    return JsonResponse({'message': 'Passenger created successfully'})


def get_passenger(request, passenger_id):
    passenger = get_object_or_404(Passenger, passenger_id=passenger_id)
    data = {'passenger_id': passenger.passenger_id, 'name': passenger.name,
            'email': passenger.email, 'phone': passenger.phone, 'address': passenger.address}
    return JsonResponse(data)


def update_passenger(request, passenger_id):
    # Your code to update a passenger goes here
    return JsonResponse({'message': 'Passenger updated successfully'})


def delete_passenger(request, passenger_id):
    # Your code to delete a passenger goes here
    return JsonResponse({'message': 'Passenger deleted successfully'})

# Views for Flight (similar structure to Passenger views)

# Views for Booking (similar structure to Passenger views)
