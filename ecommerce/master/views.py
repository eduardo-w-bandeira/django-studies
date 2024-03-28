import re
import json
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Customer, Category, Product, Order, OrderDetail, Payment, Shipping
from .forms import CustomerForm, CategoryForm, ProductForm, OrderForm, OrderDetailForm, PaymentForm, ShippingForm

# Glossary
# --------
# mobj = models.Model() object
# mobjs = a collection of mobj


def pascal_to_visual(pascal: str) -> str:
    """Converts PascalCase to a Visual Format (Name Name)"""
    # Insert space before uppercase letters (except first letter)
    visual_title = re.sub(r'(?<!^)(?=[A-Z])', ' ', pascal)
    return visual_title


def _list_mobjs(request, mobjs) -> JsonResponse:
    """Abstraction to list the objects"""
    model_class = mobjs[0].__class__
    if request.method != "GET":
        return JsonResponse({'error': "Something went wrong"}, status=400)
    json_dicts = [mobj.serialize() for mobj in mobjs]
    model_name = model_class._meta.model_name
    return JsonResponse({model_name: json_dicts}, safe=False)


def _create_mobj(request, model_class) -> JsonResponse | HttpResponse:
    """Abstraction for the create function"""
    model_name = model_class._meta.model_name
    form_class = eval(f"{model_name}Form")  # E.g. CustomerForm
    if request.method == "GET":
        form = form_class()
        visual_name = pascal_to_visual(model_name)
        context = {"form": form,
                   "page_title": f"Create {visual_name}",
                   "button_label": "Create", }
        # Return a HTML page for creating a new mobject
        # render function returns a HttpResponse object (as far as I know)
        return render(request, f'form_base.html', context)
    if request.method == "POST":
        form = form_class(request.POST)
        if form.is_valid():
            # Django form.save() saves the model magically
            mobj = form.save()
            return JsonResponse({model_name: mobj.serialize()})
    return JsonResponse({'error': "Something went wrong"}, status=400)


def _get_or_update_or_delete_mobj(request, mobj) -> JsonResponse:
    """Abstraction for "getting, updating or deleting an Model.object"""
    model_name = mobj._meta.model_name
    if request.method == "GET":
        return JsonResponse({model_name: mobj.serialize()})
    if request.method == "PUT":
        data = json.loads(request.body)
        for key, value in data.items():
            setattr(mobj, key, value)
        mobj.save()
        return JsonResponse({model_name: mobj.serialize()})
    if request.method == "DELETE":
        serial_map = mobj.serialize()
        mobj.delete()
        return JsonResponse({model_name: serial_map})
    return JsonResponse({'error': "Something went wrong"}, status=400)


def index(request) -> HttpResponse:
    return HttpResponse("<h1>E-Commerce Page</h1>")


# Customer views
def customer_list(request):
    return _list_mobjs(request, Customer.objects.all())


def customer_create(request):
    return _create_mobj(request, Customer)


def customer_detail(request, customer_id):
    return _get_or_update_or_delete_mobj(request, Customer.objects.get(id=customer_id))


# Category views
def category_list(request):
    return _list_mobjs(request, Category.objects.all())


def category_create(request):
    return _create_mobj(request, Category)


def category_detail(request, category_id):
    return _get_or_update_or_delete_mobj(request, Category.objects.get(id=category_id))


# Product views
def product_list(request):
    return _list_mobjs(request, Product.objects.all())


def product_create(request):
    return _create_mobj(request, Product)


def product_detail(request, product_id):
    return _get_or_update_or_delete_mobj(request, Product.objects.get(id=product_id))


# Order views
def order_list(request):
    return _list_mobjs(request, Order.objects.all())


def order_create(request):
    return _create_mobj(request, Order)


def order_detail(request, order_id):
    return _get_or_update_or_delete_mobj(request, Order.objects.get(id=order_id))


# Order Detail views
def order_detail_list(request, order_id):
    order_details = OrderDetail.objects.filter(order_id=order_id)
    return JsonResponse(request, order_details)


def order_detail_create(request):
    return _create_mobj(request, OrderDetail)


def order_detail_detail(request, order_id, order_detail_id):
    return _get_or_update_or_delete_mobj(request, OrderDetail.objects.get(id=order_detail_id))


# Payment views
def payment_list(request):
    return _list_mobjs(request, Payment.objects.all())


def payment_create(request):
    return _create_mobj(request, Payment)


def payment_detail(request, payment_id):
    return _get_or_update_or_delete_mobj(request, Payment.objects.get(id=payment_id))


# Shipping views
def shipping_list(request):
    return _list_mobjs(request, Shipping.objects.all())


def shipping_create(request):
    return _create_mobj(request, Shipping)


def shipping_detail(request, shipping_id):
    return _get_or_update_or_delete_mobj(request, Shipping.objects.get(id=shipping_id))


# Customer-Order Interaction views
def customer_order_list(request, customer_id):
    orders = Order.objects.filter(customer_id=customer_id)
    return _list_mobjs(request, orders)


def order_customer_detail(request, order_id):
    order = Order.objects.filter(id=order_id)
    return _get_or_update_or_delete_mobj(request, order.customer)


# Product-Order Interaction views
def product_order_list(request, product_id):
    order_details = OrderDetail.objects.filter(product_id=product_id)
    orders = [order_detail.order for order_detail in order_details]
    return _list_mobjs(request, orders)


def order_product_list(request, product_id):
    order_details = OrderDetail.objects.filter(product_id=product_id)
    products = [order_detail.product for order_detail in order_details]
    return _list_mobjs(request, products)


def order_product_detail(request, order_id, product_id):
    return _get_or_update_or_delete_mobj(request, Product.objects.get(id=product_id))


# Order-Payment Interaction views
def order_payment_detail(request, order_id):
    order = Order.objects.filter(id=order_id)
    payment = Payment.objects.filter(order=order)
    return _get_or_update_or_delete_mobj(request, payment)


# Order-Shipping Interaction views
def order_shipping_detail(request, order_id):
    order = Order.objects.filter(id=order_id)
    shipping = Shipping.objects.filter(order=order)
    return _get_or_update_or_delete_mobj(request, shipping)


# Product-Category Interaction views
def product_category_detail(request, product_id):
    product = Product.objects.filter(id=product_id)
    return _get_or_update_or_delete_mobj(request, product.category)


def category_product_list(request, category_id):
    products = Product.objects.filter(category_id=category_id)
    return _list_mobjs(request, Product, products)


def product_category_detail(request, product_id, category_id):
    category = Category.objects.filter(id=category_id)
    return _get_or_update_or_delete_mobj(request, category)
