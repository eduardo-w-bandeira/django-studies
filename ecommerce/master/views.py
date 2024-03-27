from .models import Customer, Category, Product, Order, OrderDetail, Payment, Shipping
from datetime import datetime
from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse("<h1>E-Commerce!</h1>")


def customer_list(request):
    ...


def customer_handler(request, id):
    ...


def category_list(request):
    ...


def category_handler(request, id):
    ...


def product_list(request):
    ...


def product_handler(request, id):
    ...


def order_list(request):
    ...


def order_handler(request, id):
    ...


def payment_list(request):
    ...


def payment_handler(request, id):
    ...


def shipping_list(request):
    ...


def shipping_handler(request, id):
    ...
