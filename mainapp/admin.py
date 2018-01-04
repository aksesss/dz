from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


class HorseAdmin(admin.ModelAdmin):
    # list_display = ["id", "name"]  # Выводит 2 поля

    list_display = [field.name for field in Horse._meta.fields]  # Выводит все поля

    # list_filter = ["good_id"]                                                            # Фильтр по поляи

    class Meta:
        model = Horse


class RunAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Run._meta.fields]  # Выводит все поля

    fieldsets = [
        ('Дата забега',     {'fields': ['date', 'time']}),
        ('Место забега',    {'fields': ['place']}),
    ]

    # list_filter = ["good_id"]                                                            # Фильтр по поляи

    class Meta:
        model = Run


class HorseInRunAdmin(admin.ModelAdmin):
    list_display = ["id", "run", "horse"]  # Выводит 2 поля

    # list_display = [field.name for field in HorseInRun._meta.fields]  # Выводит все поля

    list_filter = ["run"]  # Фильтр по поляи

    class Meta:
        model = HorseInRun


class BetAdmin(admin.ModelAdmin):
    list_display = ["user", "horse_in_run", "amount"]  # Выводит 2 поля

    list_filter = ["user", "horse_in_run"]  # Фильтр по поляи

    class Meta:
        model = Bet


admin.site.register(Horse, HorseAdmin)
admin.site.register(Run, RunAdmin)
admin.site.register(HorseInRun, HorseInRunAdmin)
admin.site.register(Bet, BetAdmin)
admin.site.register(Jockey)
