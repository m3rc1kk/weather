from django.http import HttpResponse
from django.urls import reverse_lazy
import requests
from django.shortcuts import redirect, render
from .forms import *
from Weather.settings import APIkey
from .models import *
from django.views import View, generic

def weather(request):
    temp = False
    weath_obj = False
    weather_data = []
    weathmodel = WeatherModel.objects.all()
    if request.method == 'POST':
        form = WeatherForm(request.POST)
        if form.is_valid():
            
            form.save()    
    else:
        form = WeatherForm()
        
    for el in weathmodel:
        
        try:
            r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={el}&appid={APIkey}&units=metric'
            )
            data = r.json()
            
            city_weather = {
                'city': el,
                'temp': data['main']['temp'],
                'desc': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
            }

            
            weather_data.append(city_weather)
            
            

        except:
            WeatherModel.objects.filter(city = el).delete()
            form = WeatherForm()
            

    return render(request, 'the_weather/weather.html', {'weather_data': weather_data, 'form': form, 'weathmodel': weathmodel})



class DeleteWeatherView(generic.DeleteView):
    model = WeatherModel
    template_name = 'the_weather/delete.html'
    success_url = reverse_lazy('weath')


class DeleteAllWeatherView(View):
    def get(self, request):
        weathermodel = WeatherModel.objects.all()
        weathermodel.delete()
        return redirect('weath')