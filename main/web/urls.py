from django.urls import path
from . import views

urlpatterns = [
    path('', views.web_render, name='main'),
    path('calculate', views.calculator_view, name='calculator.view'),
    path('orders', views.orders_view, name='orders.view')
]
