from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Customer Endpoints
    path('customer/', views.customer_handler),
    path('customer/<int:id>/', views.customer_info),

    # Product Endpoints
    path('product/', views.product_handler),
    path('product/<int:id>/', views.product_info),

    # Order Endpoints
    path('order/', views.order_handler),
    path('order/<int:id>/', views.order_info),

    # Order Details Endpoints
    path('order/<int:id>/detail/', views.order_detail_handler),
    path('order/<int:orderId>/detail/<int:detailId>/',
         views.order_detail_info),

    # Category Endpoints
    path('category/', views.category_handler),
    path('category/<int:id>/', views.category_info),

    # Payment Endpoints
    path('payment/', views.payment_handler),
    path('payment/<int:id>/', views.payment_info),

    # Shipping Endpoints
    path('shipping/', views.shipping_handler),
    path('shipping/<int:id>/', views.shipping_info),

    # Customer-Order Interaction
    path('customer/<int:customerId>/order/', views.customer_order_handler),
    path('order/<int:orderId>/customer/', views.order_customer_info),

    # Product-Order Interaction
    path('product/<int:productId>/orders/', views.product_order_list),
    path('order/<int:orderId>/products/', views.order_product_list),
    path('order/<int:orderId>/product/<int:productId>/',
         views.order_product_handler),

    # Order-Payment Interaction
    path('order/<int:orderId>/payment/',
         views.order_payment_info_handler),

    # Order-Shipping Interaction
    path('order/<int:orderId>/shipping/',
         views.order_shipping_info_handler),

    # Product-Category Interaction
    path('product/<int:productId>/category/', views.product_category_info),
    path('category/<int:categoryId>/products/', views.category_product_handler),
    path('product/<int:productId>/category/<int:categoryId>/',
         views.product_category_handler),
]
