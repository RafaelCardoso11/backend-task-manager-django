from django.contrib import admin
from django.urls import path, include
from api import urls
from rest_framework import urls as rest_framework
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tasks', include(urls)),
    path('api/', include(rest_framework))
]
