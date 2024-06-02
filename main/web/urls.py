from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('/main', views.web_render, name='main_render')
]
