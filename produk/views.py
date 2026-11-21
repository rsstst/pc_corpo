from django.shortcuts import render, redirect
from produk.models import Barang, User
from produk.forms import FormBarang, FormUser
from django.contrib import messages

# Create your views here.

def produk(request):
    title = "Produk"
    brg = Barang.objects.all()
    var = {
        'brg': brg,
        "title": title
    }
    return render(request, "produk.html", var)

# Tabel Barang

def show_table(request):
    title = "Tabel Barang"
    brg = Barang.objects.all()
    context = {
        'title':title,
        'brg':brg,
    }
    return render(request, "tabel.html", context)

def add_item(request):
    title = "Tambah Barang"
    if request.POST:
        form = FormBarang(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil ditambahkan")
            konteks = {
                'title': title,
                'form': form,
            }
            return render(request, 'tambah.html', konteks)
    else:
        form = FormBarang()
        konteks = {
            'title': title,
            'form': form,
        }
    return render(request, "tambah.html", konteks)

def change_item(request, id_barang):
    barangs = Barang.objects.get(id = id_barang)
    if request.POST:
        form = FormBarang(request.POST, instance=barangs)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diubah")
            return redirect('ubah_barang', id_barang = id_barang)
    else:
        form = FormBarang(instance=barangs)
        konteks = {
            'form': form,
            'barangs': barangs,
        }
    return render(request, 'ubah.html', konteks)

def delete_item(request, id_barang):
    barangs = Barang.objects.filter(id = id_barang)
    barangs.delete()
    messages.success(request, "Data terhapus")
    return redirect('show_table')

# End Tabel Barang

# Tabel user

def show_user(request):
    title = "Daftar Akun"
    user = User.objects.all()
    context = {
        'title':title,
        'usr':user,
    }
    return render(request, "user/tampil_user.html", context)

def add_user(request):
    title = "Daftar"
    if request.POST:
        form = FormUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil ditambahkan")
            konteks = {
                'title': title,
                'form': form,
            }
            return render(request, 'user/tambah_user.html', konteks)
    else:
        form = FormUser()
        konteks = {
            'title': title,
            'form': form,
        }
    return render(request, "user/tambah_user.html", konteks)

def delete_user(request, id_user):
    user = User.objects.filter(id = id_user)
    user.delete()
    messages.success(request, "Data terhapus")
    return redirect('show_user')

def change_user(request, id_user):
    user = User.objects.get(id = id_user)
    if request.POST:
        form = FormUser(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diubah")
            return redirect('ubah_user', id_user = id_user)
    else:
        form = FormUser(instance=user)
        konteks = {
            'form': form,
            'usr': user,
        }
    return render(request, 'user/ganti_user.html', konteks)