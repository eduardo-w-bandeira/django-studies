import re
import json
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from .models import Customer, Category, Product, Order, OrderDetail, Payment, Shipping
from .forms import CustomerForm, CategoryForm, ProductForm, OrderForm, OrderDetailForm, PaymentForm, ShippingForm


def _pascal_to_snake(pascal_string):
    # Insert underscore before uppercase letters (except first letter)
    snake_string = re.sub(r'(?<!^)(?=[A-Z])', '_', pascal_string)
    # Convert to lowercase
    return snake_string.lower()


def _create_obj(request, model_class):
    form_class = eval(f"{model_class._meta.model_name}Form")
    entity_name = _pascal_to_snake(model_class._meta.model_name)
    if request.method == "GET":
        form = form_class()
        context = {'form': form}
        return render(request, f'{entity_name}_form.html', context)
    if request.method == "POST":
        form = form_class(request.POST)
        if form.is_valid():
            model_obj = form.save()
            return JsonResponse({entity_name: model_obj.serialize()})
    return JsonResponse({'error': "Something went wrong"}, status=400)


def _list_objs(request, objs):
    model_class = objs[0].__class__
    if request.method != "GET":
        return JsonResponse({'error': "Something went wrong"}, status=400)
    json_dicts = [obj.serialize() for obj in objs]
    entity_name = _pascal_to_snake(model_class._meta.model_name)
    return JsonResponse({entity_name: json_dicts}, safe=False)


def _get_or_update_or_delete_obj(request, obj):
    entity_name = _pascal_to_snake(obj._meta.model_name)
    if request.method == "GET":
        return JsonResponse({entity_name: obj.serialize()})
    if request.method == "PUT":
        data = json.loads(request.body)
        for key, value in data.items():
            setattr(obj, key, value)
        obj.save()
        return JsonResponse({entity_name: obj.serialize()})
    if request.method == "DELETE":
        serial_map = obj.serialize()
        obj.delete()
        return JsonResponse({entity_name: serial_map})
    return JsonResponse({'error': "Something went wrong"}, status=400)


def index(request):
    return HttpResponse("<h1>E-Commerce Page</h1>")


# Customer views
def customer_list(request):
    return _list_objs(request, Customer.objects.all())


def customer_create(request):
    return _create_obj(request, Customer)


def customer_detail(request, customer_id):
    return _get_or_update_or_delete_obj(request, Customer.objects.get(id=customer_id))


# Category views
def category_list(request):
    return _list_objs(request, Category.objects.all())


def category_create(request):
    return _create_obj(request, Category)


def category_detail(request, category_id):
    return _get_or_update_or_delete_obj(request, Category.objects.get(id=category_id))


# Product views
def product_list(request):
    return _list_objs(request, Product.objects.all())


def product_create(request):
    return _create_obj(request, Product)


def product_detail(request, product_id):
    return _get_or_update_or_delete_obj(request, Product.objects.get(id=product_id))


# Order views
def order_list(request):
    return _list_objs(request, Order.objects.all())


def order_create(request):
    return _create_obj(request, Order)


def order_detail(request, order_id):
    return _get_or_update_or_delete_obj(request, Order.objects.get(id=order_id))


# Order Detail views
def order_detail_list(request, order_id):
    order_details = OrderDetail.objects.filter(order_id=order_id)
    return JsonResponse(request, order_details)


def order_detail_create(request):
    return _create_obj(request, OrderDetail)


def order_detail_detail(request, order_id, order_detail_id):
    return _get_or_update_or_delete_obj(request, OrderDetail.objects.get(id=order_detail_id))

# Payment views


def payment_list(request):
    return _list_objs(request, Payment.objects.all())


def payment_create(request):
    return _create_obj(request, Payment)


def payment_detail(request, payment_id):
    return _get_or_update_or_delete_obj(request, Payment.objects.get(id=payment_id))


# Shipping views
def shipping_list(request):
    return _list_objs(request, Shipping.objects.all())


def shipping_create(request):
    return _create_obj(request, Shipping)


def shipping_detail(request, shipping_id):
    return _get_or_update_or_delete_obj(request, Shipping.objects.get(id=shipping_id))


# Customer-Order Interaction views
def customer_order_list(request, customer_id):
    orders = Order.objects.filter(customer_id=customer_id)
    return _list_objs(request, orders)


def order_customer_detail(request, order_id):
    order = Order.objects.filter(id=order_id)
    return _get_or_update_or_delete_obj(request, order.customer)


# Product-Order Interaction views
def product_order_list(request, product_id):
    order_details = OrderDetail.objects.filter(product_id=product_id)
    orders = [order_detail.order for order_detail in order_details]
    return _list_objs(request, orders)


def order_product_detail(request, order_id, product_id):
    return _get_or_update_or_delete_obj(request, Product.objects.get(id=product_id))


# Order-Payment Interaction views
def order_payment_detail(request, order_id):
    order = Order.objects.filter(id=order_id)
    payment = Payment.objects.filter(order=order)
    return _get_or_update_or_delete_obj(request, payment)


# Order-Shipping Interaction views
def order_shipping_detail(request, order_id):
    order = Order.objects.filter(id=order_id)
    shipping = Shipping.objects.filter(order=order)
    return _get_or_update_or_delete_obj(request, shipping)


# Product-Category Interaction views
def product_category_detail(request, product_id):
    product = Product.objects.filter(id=product_id)
    return _get_or_update_or_delete_obj(request, product.category)


def category_product_list(request, category_id):
    products = Product.objects.filter(category_id=category_id)
    return _list_objs(request, Product, products)


def product_category_detail(request, product_id, category_id):
    category = Category.objects.filter(id=category_id)
    return _get_or_update_or_delete_obj(request, category)
