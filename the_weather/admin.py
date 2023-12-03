from django.contrib import admin
from .models import *
@admin.register(WeatherModel)
class WeatherAdmin(admin.ModelAdmin):
    pass