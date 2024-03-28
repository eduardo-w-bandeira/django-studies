from django.urls import path
from . import views

urlpatterns = [

    path('', views.index),

    # Customer Endpoints
    path('customer/', views.customer_list),
    path('customer/create', views.customer_create),
    path('customer/<int:customer_id>/', views.customer_detail),

    # Category Endpoints
    path('category/', views.category_list),
    path('category/create', views.category_create),
    path('category/<int:category_id>/', views.category_detail),

    # Product Endpoints
    path('product/', views.product_list),
    path('product/create', views.product_create),
    path('product/<int:product_id>/', views.product_detail),

    # Order Endpoints
    path('order/', views.order_list),
    path('order/create', views.order_create),
    path('order/<int:order_id>/', views.order_detail),

    # Order Details Endpoints
    path('order/<int:order_id>/detail/', views.order_detail_list),
    path('order/<int:order_id>/detail/create', views.order_detail_create),
    path('order/<int:order_id>/detail/<int:order_detail_id>/',
         views.order_detail_detail),

    # Payment Endpoints
    path('payment/', views.payment_list),
    path('payment/create', views.payment_create),
    path('payment/<int:payment_id>/', views.payment_detail),

    # Shipping Endpoints
    path('shipping/', views.shipping_list),
    path('shipping/create', views.shipping_create),
    path('shipping/<int:shipping_id>/', views.shipping_detail),

    # Customer-Order Interaction
    path('customer/<int:customer_id>/order/', views.customer_order_list),
    path('order/<int:order_id>/customer/', views.order_customer_detail),

    # Product-Order Interaction
    path('product/<int:product_id>/order/', views.product_order_list),
    path('order/<int:order_id>/product/', views.order_product_list),
    path('order/<int:order_id>/product/<int:product_id>/',
         views.order_product_detail),

    # Order-Payment Interaction
    path('order/<int:order_id>/payment/',
         views.order_payment_detail),

    # Order-Shipping Interaction
    path('order/<int:order_id>/shipping/',
         views.order_shipping_detail),

    # Product-Category Interaction
    path('product/<int:product_id>/category/', views.product_category_detail),
    path('category/<int:category_id>/product/',
         views.category_product_list),
    path('product/<int:product_id>/category/<int:category_id>/',
         views.product_category_detail),
]
