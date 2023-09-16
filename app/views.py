from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_request(request):
    return HttpResponse("Hello, world. Welcome to CatChat.")


def signup_request(request):
    #return render(request, 'signup.html')
    return HttpResponse("Hello, world. Welcome to CatChat. Sign up here.")


def login_request(request):
    return render(request, 'app/login.html')


def logout_request(request):
    return render(request, 'app/logout.html')
