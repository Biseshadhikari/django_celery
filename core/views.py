from django.shortcuts import render
from core.tasks import add  # Adjust import path as needed
from celery.result import AsyncResult

def home(request):
    # Start the Celery task asynchronously
    task = add.delay(5, 10)
    return render(request, 'index.html', {'task_id': task})

def result(request, task_id): 
    # Retrieve the result of the Celery task using the task_id
    result = AsyncResult(task_id)

    return render(request, 'result.html', {'result': result})
   