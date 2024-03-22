from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    # URLs for Passenger
    path('passengers/', views.list_passengers, name='list_passengers'),
    path('passengers/create/', views.create_passenger, name='create_passenger'),
    path('passengers/<int:passenger_id>/',
         views.get_passenger, name='get_passenger'),
    path('passengers/<int:passenger_id>/update/',
         views.update_passenger, name='update_passenger'),
    path('passengers/<int:passenger_id>/delete/',
         views.delete_passenger, name='delete_passenger'),

    # URLs for Flight

    # URLs for Booking
]
