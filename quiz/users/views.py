from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterUserForm, LoginUserForm


def index(request):
    return render(request, "users/index.html")


def logout_user(request):
    logout(request)
    return redirect('users:login')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy("users:index")


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "users/login.html"

    def get_success_url(self):
        return reverse_lazy('users:index')
