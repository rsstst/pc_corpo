from django.forms import ModelForm
from produk.models import Barang, User
from django import forms

class FormBarang(ModelForm):
    class Meta:
        model = Barang
        fields = '__all__'

        widgets = {
            'kode_barang': forms.TextInput({'class': 'form-control'}),
            'nama': forms.TextInput({'class': 'form-control'}),
            'stok': forms.NumberInput({'class': 'form-control'}),
            'harga': forms.NumberInput({'class': 'form-control'}),
            'link_gambar': forms.TextInput({'class': 'form-control'}),
            'jenis': forms.Select({'class': 'form-control'}),
        }

class FormUser(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

        widgets = {
            'id_user': forms.TextInput({'class': 'form-control'}),
            'nama': forms.TextInput({'class': 'form-control'}),
            'email': forms.TextInput({'class': 'form-control'}),
            'password': forms.NumberInput({'class': 'form-control'}),
            'jenis_akun': forms.Select({'class': 'form-control'}),
        }