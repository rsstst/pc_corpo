from django.contrib import admin
from .models import Barang, Jenis, User, Jenis_User

class kolomBarang(admin.ModelAdmin):
    list_display = ['kode_barang', 'nama', 'stok', 'harga', 'link_gambar', 'jenis']
    search_fields = ['kode_barang', 'nama']
    list_filter = ('jenis',)
    list_per_page = 5

class daftarUser(admin.ModelAdmin):
    list_display = ['id_user', 'nama', 'email', 'jenis_akun']
    serach_fields = ['id_user', 'nama']
    list_filter = ('jenis_akun',)
    list_per_page = 5

admin.site.register(Barang, kolomBarang)
admin.site.register(User, daftarUser)
admin.site.register(Jenis)
admin.site.register(Jenis_User)