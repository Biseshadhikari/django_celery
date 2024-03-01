
from django.urls import path
from .views import *
urlpatterns = [
    path('', home,name = "home"),
    path('result/<str:task_id>/', result,name = "result"),
]
