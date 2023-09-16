from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return HttpResponse("Hello, world. Welcome to CatChat.")


def signup_request(request):
    #return render(request, 'signup.html')
    return HttpResponse("Hello, world. Welcome to CatChat. Sign up here.")


def login_request(request):
    #return render(request, 'login.html')
    return HttpResponse("Hello, world. Welcome to CatChat. Log in here.")


def logout_request(request):
    #return render(request, 'logout.html')
    return HttpResponse("Hello, world. Welcome to CatChat. Log out here.")
