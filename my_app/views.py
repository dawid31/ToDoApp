from datetime import date

from .forms import TaskForm
from .models import *

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def dashboard(request):
    return render(request, 'my_app/dashboard.html')

def tasks(request): 
    tasks = Task.objects.all()
    context = {'tasks': tasks,}
    return render(request, 'my_app/tasks.html', context)


def create_task(request):
    task_form = TaskForm()
    if request.method == "POST":
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return HttpResponseRedirect(reverse('tasks'))

    context = {'task_form': task_form}
    return render(request, 'my_app/create_task.html', context)


def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    context = {'task': task}
    if request.method == "POST":
        task.delete()
        return HttpResponseRedirect(reverse('tasks'))
    return render(request, 'my_app/delete_task.html', context)


def register_user(request):
    return render(request, 'my_app/register.html')



def login_user(request):
    return render(request, 'my_app/login.html')



    
    
 