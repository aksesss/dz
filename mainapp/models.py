from django.db import models
from django.db.models import Q
#from django.contrib.auth.models import User
#from django.contrib.auth.models import AbstractUser
from authorisation.models import MyUser
from datetime import *
#from dz.settings import AUTH_USER_MODEL
from django.conf import settings


class Jockey(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(verbose_name='Дата рождения')

    def age(self):
        today = datetime.utcnow()
        # born = datetime.strptime(self.birth_date, "%d.%m.%Y")
        born = self.birth_date
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    def __str__(self):
        return '%s %s' % (str(self.last_name), str(self.first_name))


class Horse(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False, verbose_name='Имя')
    age = models.IntegerField(null=False, verbose_name='Возраст')
    photo = models.ImageField(null=True, blank=True, default=None, verbose_name='Фото')
    jockey = models.ForeignKey(Jockey, verbose_name='Жокей', default=None, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " _  " + self.name

    def get_jockey(self):
        return str(self.jockey.last_name) + str(self.jockey.first_name)

    get_jockey.short_description = 'Жокей'


class Run(models.Model):
    date = models.DateField(verbose_name='Дата')
    time = models.TimeField(verbose_name='Время')
    place = models.CharField(max_length=255, verbose_name='Место')
    horse = models.ManyToManyField(Horse, through='HorseInRun', through_fields=('run', 'horse'))
    place_image = models.ImageField(null=True, blank=True, default=None, verbose_name='меcто')

    def __str__(self):
        return '%s ___ %s  ___   %s' % (str(self.id), str(self.date), str(self.time))

    def get_horses(self):
        return [{'id': horse.id, 'name': horse.name, 'age': horse.age} for horse in self.horse.all()]

    get_horses.short_description = 'Участники'


class HorseInRun(models.Model):
    horse = models.ForeignKey(Horse, on_delete=models.CASCADE, verbose_name='Лошадь')
    run = models.ForeignKey(Run, on_delete=models.CASCADE, verbose_name='Забег')
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Bet', through_fields=('horse_in_run', 'user'))

    def __str__(self):
        return '%s %s' % (str(self.run.date), str(self.horse.name))


class Bet(models.Model):
    horse_in_run = models.ForeignKey(HorseInRun, verbose_name='Ставка на лошадь', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Пользователь', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Ставка')

    def __str__(self):
        return '%s %s: %s' % (str(self.user.username), str(self.horse_in_run.run.id), str(self.horse_in_run.horse.name))


