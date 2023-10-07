from django.urls import path
from .views import TaskListCreateView, TaskRetrieveUpdateDestroyView, CompleteMultipleTasksView

urlpatterns = [
    path('task', TaskListCreateView.as_view(), name='task-list-create'),
    path('task/<int:pk>', TaskRetrieveUpdateDestroyView.as_view(), name='task-retrieve-update-destroy'),
    path('task/complete', CompleteMultipleTasksView.as_view(), name='task-complete'),
]
