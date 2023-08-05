from django.urls import path
from .consumer import EventConsumer


ws_urlpatterns = [
    path('ws/tsp/', EventConsumer.as_asgi())
]