from django.shortcuts import render
from django.views import View
# Create your views here.

def login(request):
    return render(request,'authentication/login.html')

def reset_password(request):
    return render(request,'authentication/reset-password.html')