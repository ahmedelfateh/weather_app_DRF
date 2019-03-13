from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


def WeatherList(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=4d1639b5e5a75cee2b3dc0246ad1517a'
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()
    api_data = []

    for city in cities:
        weather = requests.get(url.format(city)).json()

        city_weather = {
            'city': city,
            'temperature': weather['main']['temp'],
            'description': weather['weather'][0]['description'],
            'icon': weather['weather'][0]['icon'],
        }

        api_data.append(city_weather)

    print(api_data)

    context = {'api_data': api_data, 'form': form}
    return render(request, 'index.html', context)
