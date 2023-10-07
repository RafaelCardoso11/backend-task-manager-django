from rest_framework import serializers

from .models import Task
class TaskSerializer(serializers.Serializer):
    class  Meta:
        model = Task
        fields = ('id', 'title', 'description', 'due_date')