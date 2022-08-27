from datetime import date

from .forms import TaskForm, UserRegisterForm
from .models import *


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from django.contrib import messages

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def dashboard(request):
    user = request.user
    context = {'user': user}
    return render(request, 'my_app/dashboard.html', context)


def register_user(request):
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST) #variable stores content from form fields
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            messages.success(request, 'Account created succesfully')
            # return HttpResponseRedirect(reverse('dashboard'))
        else:
            messages.error(request, 'Unknown error appeared during registartion')
    return render(request, 'my_app/register.html', {'form': form})



def login_user(request):
    # if request.user.is_authenticated:
    #     return redirect('dashboard')
    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist.')
        try:
            password = User.objects.get(password=password)
        except:
            messages.error(request, 'Invalid pasword')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')

    return render(request, 'my_app/login.html')


def logout_user(request):
    logout(request)
    return render(request, 'my_app/logout.html')


@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user)
    context = {'tasks': tasks}
    if request.method == "POST":
        task_form = request.POST.get('content')
        Task.objects.create(name=task_form, user=request.user)
    return render(request, 'my_app/tasks.html', context)


def view_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    context = {'task': task}
    return render(request, 'my_app/view_task.html', context)


def edit_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    context = {'task': task}

    if request.method == "POST":
        task.name = request.POST.get('content')
        task.save()
        context = {'task': task}
        return HttpResponseRedirect(reverse('tasks'))

    return render(request, 'my_app/edit_task.html', context)


def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    context = {'task': task}
    if request.method == "POST":
        task.delete()
        return HttpResponseRedirect(reverse('tasks'))
    return render(request, 'my_app/delete_task.html', context)






    
    
 