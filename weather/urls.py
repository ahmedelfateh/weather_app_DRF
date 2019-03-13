from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.WeatherList),  # the path for our index view
]
