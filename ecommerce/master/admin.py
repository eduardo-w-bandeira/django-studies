from django.contrib import admin
from .models import Customer, Category, Product, Order, OrderDetail, Payment, Shipping

# Register your models here.
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Payment)
admin.site.register(Shipping)
