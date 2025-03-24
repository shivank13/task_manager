from django.urls import path
from .views import TaskCreateView

urlpatterns=[
    path('tasks/create/', TaskCreateView.as_view(), name='create_task')
]