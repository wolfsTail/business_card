from django.urls import path
from chat import views

ulrpatterns = [
    path("", views.check_incidents, name="incidents"),
    path("<uuid:uuid>/", views.group_chat, name="incident_chat"),
]