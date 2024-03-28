from django import forms
from .models import Customer, Category, Product, Order, OrderDetail, Payment, Shipping


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class OrderDetailForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        fields = '__all__'


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'


class ShippingForm(forms.ModelForm):
    class Meta:
        model = Shipping
        fields = '__all__'
