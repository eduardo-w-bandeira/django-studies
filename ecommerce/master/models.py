from django.forms.models import model_to_dict
from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    def serialize(self) -> dict:
        return model_to_dict(self)


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def serialize(self) -> dict:
        return model_to_dict(self)


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    stock = models.IntegerField()

    def serialize(self) -> dict:
        return model_to_dict(self)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField()
    # total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def serialize(self) -> dict:
        return model_to_dict(self)


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def serialize(self) -> dict:
        return model_to_dict(self)


class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=100)

    def serialize(self) -> dict:
        return model_to_dict(self)


class Shipping(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    ship_date = models.DateField()
    delivery_date = models.DateField()
    status = models.CharField(max_length=100)

    def serialize(self) -> dict:
        return model_to_dict(self)
