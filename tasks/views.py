from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task,User
from . serializers import TaskSerializer, UserSerializer
from django.shortcuts import get_object_or_404

class TaskCreateView(APIView):
    def post(self, request):
        serializer = TaskSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
