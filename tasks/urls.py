from django.urls import path
from .views import TaskCreateView, UserTaskView, TaskAssignView

urlpatterns=[
    path('tasks/create/', TaskCreateView.as_view(), name='create-task'),
    path('tasks/<int:pk>/assign/', TaskAssignView.as_view(), name='assign-task'),
    path('tasks/user/<int:user_id>/', UserTaskView.as_view(), name='get-user-tasks')
]