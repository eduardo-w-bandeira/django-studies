from django.urls import path
from . import views

urlpatterns = [
    path("", views.index,
         name="index"),
    # Passenger views
    path("passengers/", views.list_passengers,
         name="list_passengers"),
    path("passengers/<int:passenger_id>",
         views.get_passenger, name="get_passenger"),
    path("passengers/create/", views.create_passenger,
         name="create_passenger"),
    path("passengers/<int:passenger_id>/update",
         views.update_passenger, name="update_passenger"),
    path("passengers/<int:passenger_id>/delete/",
         views.delete_passenger, name="delete_passenger"),
    # Flight views
    path("flights/", views.list_flights,
         name="list_flights"),
    path("flights/<int:flight_id>",
         views.get_flight, name="get_flight"),
    path("flights/create/", views.create_flight,
         name="create_flight"),
    path("flights/<int:flight_id>/update", views.update_flight,
         name="update_flight"),
    path("flights/<int:flight_id>/delete/",
         views.delete_flight, name="delete_flight"),
    # Booking views
    path("bookings/", views.list_bookings,
         name="list_bookings"),
    path("bookings/<int:booking_id>",
         views.get_booking, name="get_booking"),
    path("bookings/create/", views.create_booking,
         name="create_booking"),
    path("bookings/<int:booking_id>/update", views.update_booking,
         name="update_booking"),
    path("bookings/<int:booking_id>/delete/",
         views.delete_booking, name="delete_booking"),
]
