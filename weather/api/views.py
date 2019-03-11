# https://home.openweathermap.org/api_keys

import json
from rest_framework import (
    views,
    mixins,
    generics,
)
from .serializers import CitySerializer
from weather.models import City

from rest_framework.response import Response
import requests


class CityWeatherAPIView(
    generics.ListAPIView,
):
    serializer_class = CitySerializer
    queryset = City.objects.all()

    def get(request, qs):
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}%20vegas&units=imperial&appid=4d1639b5e5a75cee2b3dc0246ad1517a'
        city = qs
        city_weather = requests.get(url.format(city)).json()
        return Response(city_weather)

    def get_queryset(self):
        qs = City.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(id__icontains=query)
        qs = 'las'
        return qs


class WeatherListAPIView(
        mixins.CreateModelMixin,
        generics.ListAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()

    def get_queryset(self):
        qs = City.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(id__icontains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CityDetailAPIView(
        generics.RetrieveAPIView,
):

    serializer_class = CitySerializer
    queryset = City.objects.all()
