from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def userinput(request):
    return render(request, "input.html")

def user(request):
    email = request.POST["email"]
    password = request.POST["pass"]
    data = {
        "email": email,
        "password": password
    }
    return render(request, "user.html", data)