from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Login", widget=forms.TextInput(attrs={'placeholder': "Введите имя"}))
    password1 = forms.CharField(label="Create password", widget=forms.PasswordInput(attrs={"placeholder": "Придумайте пароль"}))
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput(attrs={"placeholder": "Повторите пароль"}))

    class Meta:
        model = User
        fields = ("username", "password1", "password2")


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Login", widget=forms.TextInput(attrs={"placeholder": "Введите имя"}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"placeholder": "Введите пароль"}))
