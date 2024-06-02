from django.shortcuts import render
import django.http as http

# Create your views here.
def main(request):
    return http.HttpResponse('Hello World this is new views from web')

def web_render(request):
    return render(request, 'index.html')