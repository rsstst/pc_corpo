from django.shortcuts import render

# Create your views here.

def register(request):
    title = "Register"
    var = {
        "title": title
    }
    return render(request, "register.html", var)