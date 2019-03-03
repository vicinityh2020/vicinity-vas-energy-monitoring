from django.contrib import admin
from django.urls import path, include

from application import views
from .views import LoginAPI, UserAPI

# from .api import RegistrationAPI, LoginAPI, UserAPI

urlpatterns = [
    path('water/usage/<period>/<int:timestamp>', views.water_usage),
    path('water/threshold', views.water_threshold),
    path('power/threshold', views.power_threshold),
    path('login', LoginAPI.as_view()),
    path('user', UserAPI.as_view())
]
