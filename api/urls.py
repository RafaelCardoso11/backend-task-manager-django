
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)

from rest_framework.response import Response

from django.urls import path
from .views import TaskListCreateView, TaskRetrieveUpdateDestroyView, CompleteMultipleTasksView, UserRegistrationView, CustomTokenObtainPairView



    
urlpatterns = [
    path('auth/token', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh-token', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/verify-token', TokenVerifyView.as_view(), name='token_verify'),
    path('auth/register', UserRegistrationView.as_view(), name='user-registration'),
    path('task', TaskListCreateView.as_view(), name='task-list-create'),
    path('task/<int:pk>', TaskRetrieveUpdateDestroyView.as_view(), name='task-retrieve-update-destroy'),
    path('task/complete', CompleteMultipleTasksView.as_view(), name='task-complete'),
]
