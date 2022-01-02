from django.urls import path
from .views import RegisterView, ResetPasswordView,VerificationView,UsernameValidationView,LoginView,EmailValidationView
from django.views.decorators.csrf import csrf_exempt



urlpatterns = [
    path('login', LoginView.as_view(), name="login"),
    path('register-user', RegisterView.as_view(), name="register-user"),
    path('reset-password', ResetPasswordView.as_view(), name="reset-password"),
    path('validate-username', csrf_exempt(UsernameValidationView.as_view()), name="validate-username"),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()), name="validate-email"),
    path('activate/<uidb64>/<token>', csrf_exempt(VerificationView.as_view()), name="activate"),
]
 