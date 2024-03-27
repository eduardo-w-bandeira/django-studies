from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customer/', views.customer_list, name='customer_list'),
    path('customer/<int:id>/', views.customer_handler, name='customer_handler'),
    path('customer/<int:id>/order', views.customer_order_list,
         name='customer_order_list'),
    path('category/', views.category_list, name='category_list'),
    path('category/<int:id>/', views.category_handler, name='category_handler'),
    path('product/', views.product_list, name='product_list'),
    path('product/<int:id>/', views.product_handler, name='product_handler'),
    path('order/', views.order_list, name='order_list'),
    path('order/<int:id>/', views.order_handler, name='order_handler'),
    path('order/<int:id>/detail', views.order_detail_list,
         name='order_detail_list'),
    path('order/<int:id>/detail/<int:id>', views.order_detail_handler,
         name='order_detail_handler'),
    path('order/<int:id>/customer', views.order_customer_handler,
         name='order_customer_handler'),
    path('payment/', views.payment_list, name='payment_list'),
    path('payment/<int:id>/', views.payment_handler, name='payment_handler'),
    path('shipping/', views.shipping_list, name='shipping_list'),
    path('shipping/<int:id>/', views.shipping_handler, name='shipping_handler'),
]
