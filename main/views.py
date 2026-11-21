from django.shortcuts import render

def main(request):
    title = "Utama"
    var = {
        "title": title
    }
    return render(request, "main.html", var)

# Create your views here.
