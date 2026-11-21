"""
URL configuration for uas_ssp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from produk.views import show_table, produk, add_item, change_item, delete_item, show_user, add_user, change_user, delete_user


def faq(request):
    title = "FAQ"
    var = {
        "title": title
    }
    return render(request, "faq.html", var)

def about(request):
    title = "About"
    var = {
        "title": title
    }
    return render(request, "about.html", var)

def dashboard(request):
    title = "Dashboard"
    var = {
        "title": title,
    }
    return render(request, "dashboard.html", var)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('dashboard/', dashboard),
    path('produk/', produk),
    path('login/', include('login.urls')),
    path('register/', include('register.urls')),
    path('faq/', faq),
    path('about/', about),
    
    path('stok/', show_table, name="show_table"),
    path('tambah/', add_item),
    path('ubah/<id_barang> ', change_item, name="ubah_barang"),
    path('hapus/<id_barang>', delete_item, name='hapus_brg'),
    
    path('list-user/', show_user, name="show_user"),
    path('daftar/', add_user),
    path('ubah-user/<id_user>', change_user, name="ubah_user"),
    path('hapus-user/<id_user>', delete_user, name='hapus_user'),
]