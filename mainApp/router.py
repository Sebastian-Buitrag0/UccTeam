from django.shortcuts import path
from . import views

app_name = 'mainApp'
urlpatterns = [
    path('/home', views.home, name='home'),
]