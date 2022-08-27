from . import views
from django.urls import path


urlpatterns = [
    path('', views.dashboard, name='dashboard'), #generate index on '' url (homepage)
    path('tasks/', views.tasks, name='tasks'),
    path('view-task/<str:task_id>', views.view_task, name="view-task"),
    path('edit-task/<str:task_id>', views.edit_task, name="edit-task"),
    path('delete-task/<str:task_id>', views.delete_task, name="delete-task"),
    path('login', views.login_user, name="login"),
    path('logout', views.logout_user, name="logout"),
    path('register', views.register_user, name="register"),
]