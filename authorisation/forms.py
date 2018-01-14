from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(forms.Form):
    username = forms.CharField(min_length=5, label='Логин', widget=forms.TextInput)
    password = forms.CharField(min_length=6, widget=forms.PasswordInput, label='Пароль')
    password2 = forms.CharField(min_length=6, widget=forms.PasswordInput, label='Повторите пароль')
    email = forms.EmailField(widget=forms.EmailInput, label='E-mail')
    firstname = forms.CharField(label='Имя')
    surname = forms.CharField(label='Фамилия')

    def is_valid(self):
        b = True
        if not super().is_valid():
            b = False

        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            self.add_error('password', 'Пароли не совпадают')
            b = False
        if User.objects.filter(username=self.cleaned_data['username']).exists():
            self.add_error('username','Такой пользователь уже существует')
            b = False
        if self.errors.get('email'):
            self.errors['email'] = ['Введите корректный email']
            b = False
        return b
