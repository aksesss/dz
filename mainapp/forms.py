from django import forms
from django.forms import ModelForm
#from django.contrib.auth.models import User
from mainapp.models import MyUser
from .models import *


class RunForm(ModelForm):

    class Meta:
        model = Run
        exclude = ['horse']
