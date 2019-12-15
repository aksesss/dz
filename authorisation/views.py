from django.shortcuts import render
from django.contrib.auth import login, logout
from django.views.generic.edit import View, FormView
from django.contrib.auth.forms import AuthenticationForm
#from django.contrib.auth.models import User
from authorisation.models import MyUser
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import *


class LoginFormView(FormView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("runs_url"))
        else:
            return super(LoginFormView,self).get(self, request)

    form_class = AuthenticationForm
    template_name = "login.html"

    success_url = "/login"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)

        return super(LoginFormView, self).form_valid(form)


def registration(request):
    form = RegistrationForm(request.POST or None)
#    password_error = ''
    if request.method == 'POST':
        if form.is_valid():
            user = MyUser.objects.create_user(username=form.cleaned_data['username'],
                                            email=form.cleaned_data['email'],
                                            password=form.cleaned_data['password'],
                                            first_name=form.cleaned_data['firstname'],
                                            last_name=form.cleaned_data['surname'])
            # ...
            return HttpResponseRedirect(reverse("login_url"))

    return render(request, 'registration.html', {'form': form}, locals())


class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect(reverse("login_url"))
