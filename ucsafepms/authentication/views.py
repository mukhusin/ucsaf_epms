import json
import django
from django.core.mail.message import EmailMessage
from django.http import request
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
import re
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse

from django.utils.encoding import force_bytes,  DjangoUnicodeDecodeError, force_str
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import auth
from .utils import token_generator
# Create your views here.

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

class RegisterView(View):
    def get(self, request):
        return render(request,'authentication/login.html')
    def post(self, request):
        username = request.POST.get('username',"")
        email = request.POST.get('email',"")
        password = request.POST.get('password',"")

        context = {
            'fieldValue' : request.POST
        }

        if not User.objects.filter(username=username).exists():
            if len(password) < 6:
               messages.error(request, 'Password too short')
               return render(request,'authentication/register-user.html', context)

            user = User.objects.create_user(username=username, email=email)
            user.set_password(password)
            user.is_active=False
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            domain=get_current_site(request).domain
            link=reverse('activate', kwargs={'uidb64':uidb64,'token':token_generator.make_token(user)})
            activate_url = 'http://'+domain+link
            email_body = 'Hi '+ user.username + 'Please use the link to verify your account\n ' + activate_url
            email_subject = 'Activate your account'
            email = EmailMessage(
                email_subject,
                email_body,
                'info@g3net.co.tz',
                [email],
            )
            email.send(fail_silently=False)
            user.save()
            messages.success(request, "Account created successfully")
            return render(request,'authentication/register-user.html')
        return render(request,'authentication/register-user.html')

class ResetPasswordView(View):
    def get(self, request):
        return render(request,'authentication/reset-password.html')
    

class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not re.search(regex,email):
            return JsonResponse({'email_error': 'Email is invalid'},status=409)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'Sorry email in use, choose another one'},status=400)
        return JsonResponse({'email_valid': True})

class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error': 'username should only contain alphanumeric characters'},status=409)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'Sorry username in use, choose another one'},status=400)
        return JsonResponse({'username_valid': True})

class VerificationView(View):
    def get(self, request, uidb64, token):
        try:
            id=force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not token_generator.check_token(user, token):
                return redirect('login'+'?message='+'User already activated')

            if user.is_active:
                return redirect('login')
            user.is_active = True
            user.save()

            messages.success(request,"Account activated successfully")
            return redirect('login')
        except Exception as ex:
            pass
        
        return redirect('login')

class LoginView(View):
    def get(self, request):
        return render(request,'authentication/login.html')

    def post(self, request):
        username = request.POST.get('username',"")
        password = request.POST.get('password',"")

        if username and password:
            user=auth.authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    auth.login(request, user)
                    messages.success(request, 'Welcome, '+ user.username+ 'you are now logged in')
                messages.error(request,'Account is not active, please contact system admin')
                return render(request,'authentication/login.html')
            messages.error(request,'Invalid credentials, please try again')
            return render(request,'authentication/login.html')
        messages.error(request,'All fields are required!')
        return render(request,'authentication/login.html')

