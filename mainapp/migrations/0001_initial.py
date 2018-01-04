# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-26 21:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Horse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Имя')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('photo', models.ImageField(blank=True, default=None, null=True, upload_to='', verbose_name='Фото')),
                ('jockey', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Жокей')),
            ],
        ),
        migrations.CreateModel(
            name='HorseInRun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Horse')),
            ],
        ),
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('place', models.CharField(max_length=255)),
                ('horse', models.ManyToManyField(through='mainapp.HorseInRun', to='mainapp.Horse')),
            ],
        ),
        migrations.AddField(
            model_name='horseinrun',
            name='run',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Run'),
        ),
    ]
