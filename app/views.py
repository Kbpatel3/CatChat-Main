from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_request(request):
    print("Home request received")
    return render(request, 'app/home.html')


def signup_request(request):
    print("Signup request received")
    return render(request, 'app/signup.html')


def login_request(request):
    if request.method == 'POST':
        print("Login request received")
        return render(request, 'app/home.html')
    return render(request, 'app/login.html')


def logout_request(request):
    return render(request, 'app/logout.html')


def confirm_email(request):
    # TODO: Add email confirmation logic
    return render(request, 'app/confirm-email.html')
