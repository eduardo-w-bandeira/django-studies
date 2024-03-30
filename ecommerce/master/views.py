import re
import json
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.db import models
from django.views.decorators.csrf import csrf_exempt
from .models import Customer, Category, Product, Order, OrderDetail, Payment, Shipping
from .forms import CustomerForm, CategoryForm, ProductForm, OrderForm, OrderDetailForm, PaymentForm, ShippingForm

# Glossary
# --------
# mobj = models.Model() object
# mobjs = a mobj collection (list or iterator)


def pascal_to_visual(pascal: str) -> str:
    """Converts PascalCase to a Visual Format (Name Name)"""
    # Insert space before uppercase letters (except first letter)
    visual: str = re.sub(r'(?<!^)(?=[A-Z])', ' ', pascal)
    return visual


def _list_mobjs(request, model_class, mobjs="all") -> JsonResponse:
    """Abstraction to list the objects"""
    if request.method != "GET":
        return JsonResponse({'error': "Something went wrong"}, status=400)
    s_page_number = request.GET.get('page_number')
    s_page_size = request.GET.get('page_size')
    if s_page_number and s_page_size:
        page_number = int(s_page_number)
        page_size = int(s_page_size)
        start = (page_number - 1) * page_size
        end = start + page_size
        if mobjs == "all":
            mobjs = model_class.objects.all()[start:end]
        else:
            mobjs = mobjs[start:end]
    elif mobjs == "all":
        mobjs = model_class.objects.all()
    json_dicts = [mobj.serialize() for mobj in mobjs]
    table_name = model_class._meta.model_name
    return JsonResponse({table_name: json_dicts})


def _create_mobj(request, model_class) -> JsonResponse | HttpResponse:
    """Abstraction for the create function"""
    table_name = model_class._meta.model_name
    class_name = model_class.__name__
    form_class = eval(f"{class_name}Form")  # E.g. CustomerForm
    if request.method == "GET":
        form = form_class()
        visual_name = pascal_to_visual(class_name)
        context = {"form": form,
                   "page_title": f"Create {visual_name}",
                   "button_label": "Create", }
        # Return a HTML page for creating a new mobject.
        # The `render` function returns a HttpResponse object.
        return render(request, f'form_base.html', context)
    if request.method == "POST":
        form = form_class(request.POST)
        if form.is_valid():
            # Django form.save() saves the model "magically"
            mobj = form.save()
            return JsonResponse({table_name: mobj.serialize()})
    return JsonResponse({'error': "Something went wrong"}, status=400)


def _update_mobj(request, mobj, table_name) -> JsonResponse:
    data = json.loads(request.body)
    for key, value in data.items():
        field = mobj._meta.get_field(key)
        if isinstance(field, (models.ForeignKey, models.OneToOneField, models.ManyToManyField)):
            key += "_id"  # E.g. 'category' becomes 'category_id', so it can assigned
        setattr(mobj, key, value)
    mobj.save()
    return JsonResponse({table_name: mobj.serialize()})


def _get_or_update_or_delete_mobj(request, mobj, methods=["GET", "PUT", "DELETE"]) -> JsonResponse:
    """Abstraction for getting, updating or deleting an Model.object"""
    table_name = mobj._meta.model_name
    if "GET" in methods and request.method == "GET":
        return JsonResponse({table_name: mobj.serialize()})
    if "PUT" in methods and request.method == "PUT":
        return _update_mobj(request, mobj, table_name)
    if "DELETE" in methods and request.method == "DELETE":
        id = mobj.id
        mobj.delete()
        return JsonResponse({table_name: f"id {id} deleted"})
    return JsonResponse({'error': "Something went wrong"}, status=400)


# index page
def index(request) -> HttpResponse:
    title = "Ecommerce Page"
    return HttpResponse(f"<h1>{title}</h1>")


# Customer views
def customer_list(request):
    return _list_mobjs(request, Customer)


def customer_create(request):
    return _create_mobj(request, Customer)


@csrf_exempt  # This disables CSRF validation, so that you can delete through POSTMAN
def customer_detail(request, customer_id):
    return _get_or_update_or_delete_mobj(request, Customer.objects.get(id=customer_id))


# Category views
def category_list(request):
    return _list_mobjs(request, Category)


def category_create(request):
    return _create_mobj(request, Category)


@csrf_exempt
def category_detail(request, category_id):
    return _get_or_update_or_delete_mobj(request, Category.objects.get(id=category_id))


# Product views
def product_list(request):
    return _list_mobjs(request, Product)


def product_create(request):
    return _create_mobj(request, Product)


@csrf_exempt
def product_detail(request, product_id):
    return _get_or_update_or_delete_mobj(request, Product.objects.get(id=product_id))


# Order views
def order_list(request):
    return _list_mobjs(request, Order)


def order_create(request):
    return _create_mobj(request, Order)


@csrf_exempt
def order_detail(request, order_id):
    return _get_or_update_or_delete_mobj(request, Order.objects.get(id=order_id))


# OrderDetail views
def order_detail_list(request, order_id):
    order_details = OrderDetail.objects.filter(order_id=order_id)
    return _list_mobjs(request, OrderDetail, order_details)


def order_detail_create(request, order_id):
    return _create_mobj(request, OrderDetail)


@csrf_exempt
def order_detail_detail(request, order_id, order_detail_id):
    return _get_or_update_or_delete_mobj(request, OrderDetail.objects.get(id=order_detail_id))


# Payment views
def payment_list(request):
    return _list_mobjs(request, Payment)


def payment_create(request):
    return _create_mobj(request, Payment)


@csrf_exempt
def payment_detail(request, payment_id):
    payment = Payment.objects.get(id=payment_id)
    methods = ["GET", "PUT"]  # No DELETE
    return _get_or_update_or_delete_mobj(request, payment, methods)


# Shipping views
def shipping_list(request):
    return _list_mobjs(request, Shipping)


def shipping_create(request):
    return _create_mobj(request, Shipping)


@csrf_exempt
def shipping_detail(request, shipping_id):
    shipping = Shipping.objects.get(id=shipping_id)
    methods = ["GET", "PUT"]  # No DELETE
    return _get_or_update_or_delete_mobj(request, shipping, methods)


# Customer-Order Interaction views
def customer_order_list(request, customer_id):
    orders = Order.objects.filter(customer_id=customer_id)
    return _list_mobjs(request, Order, orders)


def order_customer_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    return _get_or_update_or_delete_mobj(request, order.customer)


# Product-Order Interaction views
def product_order_list(request, product_id):
    order_details = OrderDetail.objects.filter(product_id=product_id)
    orders = [order_detail.order for order_detail in order_details]
    return _list_mobjs(request, Order, orders)


def order_product_list(request, order_id):
    order_details = OrderDetail.objects.filter(order_id=order_id)
    products = [order_detail.product for order_detail in order_details]
    return _list_mobjs(request, Product, products)


@csrf_exempt
def order_product_detail(request, order_id, product_id):
    return _get_or_update_or_delete_mobj(request, Product.objects.get(id=product_id))


# Order-Payment Interaction views
@csrf_exempt
def order_payment_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    payment = Payment.objects.get(order=order)
    methods = ["GET", "PUT"]  # No DELETE
    return _get_or_update_or_delete_mobj(request, payment, methods)


# Order-Shipping Interaction views
def order_shipping_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    shipping = Shipping.objects.get(order=order)
    return _get_or_update_or_delete_mobj(request, shipping)


# Product-Category Interaction views
def category_product_list(request, category_id):
    products = Product.objects.filter(category_id=category_id)
    return _list_mobjs(request, Product, products)


@csrf_exempt
def product_category_detail(request, product_id, category_id):
    category = Category.objects.get(id=category_id)
    return _get_or_update_or_delete_mobj(request, category)
