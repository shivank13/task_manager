from rest_framework import serializers
from .models import Task, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'mobile']

class TaskSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only= True)   

    class Meta:
        model = Task
        fields = '__all__'     