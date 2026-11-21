from django.db import models

class Jenis(models.Model):
    nama = models.CharField(max_length=50)
    ket = models.TextField()

    def __str__(self):
        return self.nama

class Barang(models.Model):
    kode_barang = models.CharField(max_length=8)
    nama = models.CharField(max_length=128)
    stok = models.IntegerField()
    harga = models.BigIntegerField()
    link_gambar = models.CharField(max_length=150, blank=True)
    post_time = models.DateTimeField(auto_now_add=True)
    jenis = models.ForeignKey(Jenis, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "[ {} ] {} -- Stok tersedia: {}".format(self.kode_barang, self.nama, self.stok)

class Jenis_User(models.Model):
    nama = models.CharField(max_length=50)
    ket = models.TextField()

    def __str__(self):
        return self.nama

class User(models.Model):
    id_user = models.CharField(max_length=8, verbose_name="ID")
    nama = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    jenis_akun = models.ForeignKey(Jenis_User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "[ {} ] {}".format(self.id_user, self.nama)