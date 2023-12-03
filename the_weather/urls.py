from django.urls import path
from .views import *

urlpatterns = [
    path('', weather, name = 'weath'),
    path('delete/<int:pk>/', DeleteWeatherView.as_view(), name = 'delete'),
    path('delete_all/', DeleteAllWeatherView.as_view(), name = 'delete-all')
]
