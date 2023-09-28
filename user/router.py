from django.shortcuts import path
from . import views

app_name = 'user'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]