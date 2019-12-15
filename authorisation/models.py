from django.db import models
from django.db.models import Q
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from datetime import *


class MyUser(AbstractUser):
    cash = models.CharField(max_length=100)

