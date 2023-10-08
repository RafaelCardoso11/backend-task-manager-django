from rest_framework import serializers

from .models import Task

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        instance.is_active = True
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
class TaskSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Task
        fields = ('id', 'title', 'description',  'priority', 'completed', 'dueDate', 'createdAt')