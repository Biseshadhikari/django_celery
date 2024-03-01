from django.shortcuts import render
# from project.celery import add
from core.tasks import add
# Create your views here.


def home(request):
    x = add.delay(5,10)

    return render(request,'index.html',{'x':x})