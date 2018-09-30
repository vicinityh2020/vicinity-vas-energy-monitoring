from django.urls import path
from adapter import views

urlpatterns = [
    path('objects', views.thing_description),
    # path('objects/<subscriber_id>/events/<eid>', views.receive_event),
]
