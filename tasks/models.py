from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name
    
class Task(models.Model):
    name=models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task_type = models.CharField(max_length=100)
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50)
    users = models.ManyToManyField(User, related_name='tasks')

    def __str__(self):
        return self.name
