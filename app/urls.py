from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_request, name='login'),
    path('signup/', views.signup_request, name='signup'),
    path('logout/', views.logout_request, name='logout'),
    path('home/', views.home_request, name='home'),
]