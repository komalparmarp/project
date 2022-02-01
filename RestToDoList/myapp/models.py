from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    birth_date = models.DateTimeField(null=True, blank=True)


class Todolist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_related')
    title = models.CharField(max_length=10, null=False, blank=False, help_text="Enter your ToDoList Title")
    description = models.CharField(max_length=100, null=False, blank=False, help_text="Write here your work")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
