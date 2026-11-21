from django.urls import path
from . import views

urlpatterns = [
    path('', views.produk, name='produk'),
]