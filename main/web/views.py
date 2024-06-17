from django.shortcuts import render
import django.http as http

# Create your views here.
def main(request):
    return http.HttpResponse('Hello World this is new views from web')

def web_render(request):
    return render(request, 'main.html')

def orders_view(request):
    return render(request, 'orders.html')

def calculator_view(request):
    return render(request, 'calculator.html')

