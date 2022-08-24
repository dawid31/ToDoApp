from . import views
from django.urls import path


urlpatterns = [
    path('', views.dashboard, name='dashboard'), #generate index on '' url (homepage)
    path('tasks', views.tasks, name='tasks'),
    path('create-task', views.create_task, name='create-task'),
    path('delete-task/<str:task_id>', views.delete_task, name="delete-task"),
    path('login', views.login_user, name="login"),
    path('register', views.register_user, name="register"),
]