# core/routing.py

from django.urls import path
from . import consumers

websocket_patterns = [
    path('ws/title',consumers.MyConsumer.as_asgi())
]



