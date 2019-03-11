""" statusModelAPIs URL Configuration """

from django.conf.urls import url


from .views import (
    WeatherListAPIView,
    CityDetailAPIView,
    CityWeatherAPIView,
)

urlpatterns = [

    url(r'^$', WeatherListAPIView.as_view()),
    url(r'^(?P<pk>\d+)/$', CityDetailAPIView.as_view()),
    url(r'^city/', CityWeatherAPIView.as_view()),

]
