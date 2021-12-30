from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt



urlpatterns = [
    path('login', views.login, name="login"),
    path('reset-password', views.reset_password, name="reset-password"),
    path('validate-username', csrf_exempt(views.UsernameValidationView.as_view()), name="validate-username")
]
