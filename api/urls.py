from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from django.urls import path
from .views import TaskListCreateView, TaskRetrieveUpdateDestroyView, CompleteMultipleTasksView, UserRegistrationView

urlpatterns = [
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('register', UserRegistrationView.as_view(), name='user-registration'),
    path('task', TaskListCreateView.as_view(), name='task-list-create'),
    path('task/<int:pk>', TaskRetrieveUpdateDestroyView.as_view(), name='task-retrieve-update-destroy'),
    path('task/complete', CompleteMultipleTasksView.as_view(), name='task-complete'),
]
