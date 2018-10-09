from django.contrib import admin
from django.urls import path, include

from application import views

urlpatterns = [
    path('water/usage/<period>/<int:timestamp>', views.water_usage),
    path('water/threshold', views.water_threshold),
]
