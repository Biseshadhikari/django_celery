from celery import shared_task
from time import sleep

@shared_task(name="tasks_celery")
def add(x,y):
    sleep(5)
    return x+y