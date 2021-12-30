import json
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import View

# from ucsafepms.authentication.models import Users
# Create your views here.

def login(request):
    return render(request,'authentication/login.html')

def reset_password(request):
    return render(request,'authentication/reset-password.html')

class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error': 'username should only contain alphanumeric characters'},status=409)
        # if Users.objects.filter(username=username).exists():
        #     return JsonResponse({'username_error': 'Sorry username in use, choose another one'},status=400)
        return JsonResponse({'username_valid': True})