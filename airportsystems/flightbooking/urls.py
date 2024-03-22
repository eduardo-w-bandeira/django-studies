from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('passengers/', views.list_passengers)  # , name='passenger_list'),
]
