from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

# Create your views here.
class TaskView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer