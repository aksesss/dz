from django.conf.urls import url, include
from django.contrib import admin
from .views import *
from django.views.generic.base import RedirectView

urlpatterns = [

    url(r'^login/$', LoginFormView.as_view(), name="login_url"),
    url(r'^registration/$', registration, name="registration_url"),
    url(r'^logout/$', LogoutView.as_view(), name="logout_url"),
    url(r'^$', RedirectView.as_view(url='/login/', permanent=False), name='index'),

]
