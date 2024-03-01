from django.shortcuts import render
from project.celery import add
# Create your views here.


def home(request):
    x = add.delay(5,10)
    # print(x)

    return render(request,'index.html',{'x':x})