import json
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import View
import re
# from ucsafepms.authentication.models import Users
# Create your views here.

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def login(request):
    return render(request,'authentication/login.html')

def reset_password(request):
    return render(request,'authentication/reset-password.html')

class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not re.search(regex,email):
            return JsonResponse({'email_error': 'Email is invalid'},status=409)
        # if Users.objects.filter(email=email).exists():
        #     return JsonResponse({'username_error': 'Sorry email in use, choose another one'},status=400)
        return JsonResponse({'email_valid': True})

class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error': 'username should only contain alphanumeric characters'},status=409)
        # if Users.objects.filter(username=username).exists():
        #     return JsonResponse({'username_error': 'Sorry username in use, choose another one'},status=400)
        return JsonResponse({'username_valid': True})