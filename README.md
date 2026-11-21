# PC Corpo
## Website e-commerce yang memiliki konten dinamis. Dibuat untuk menyelesaikan tugas mata kuliah

## Setup
Using UV
```
uv init
uv sync
uv run manage.py migrate
uv run manage.py createsuperuser
from /admin, add a variable to jenis and jenis_user
uv run manage.py runserver
```
Using venv / pip
```
pip install -r requirements.txt
py run manage.py migrate
py run manage.py createsuperuser
from /admin, add a variable to jenis and jenis_user
py run manage.py runserver
```

## Kekurangan
1. Diharuskan menambahkan variabel jenis terlebih dahulu melalui superadmin, tidak bisa langsung dari dashboard
2. Dashboard belum terlindungi oleh autentikasi dan otorisasi
3. Gambar yang digunakan berupa link, bukan local storage atau public assets
4. Tested secara local, belum pernah ter-deploy langsung