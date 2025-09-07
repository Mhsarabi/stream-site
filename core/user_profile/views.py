from django.shortcuts import render,redirect
from django.views.generic import CreateView,TemplateView
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from .models import *
from .forms import *

# Create your views here.
class signup_user(TemplateView):
    template_name='account/sign_up.html'

class login_user(TemplateView):
    template_name='account/login.html'

class ChangePassword(TemplateView):
    template_name='account/change_password.html'

class SendEmail(TemplateView):
    template_name='account/send_email.html'