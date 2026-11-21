from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def login(request):
    title = "Login"
    var = {
        "title": title
    }
    return render(request, "login.html", var)