# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('heartbeat', views.heartbeat, name='heartbeat'),
    path('register', views.register_device, name='register_device'),
]

