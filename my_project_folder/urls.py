
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_app.urls')) #urls.py z folderu my_app zajmie sie tymi url
]
