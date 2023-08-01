# models.py

from django.db import models
from django.contrib.auth.models import AbstractUser, User


class UserProfile(models.Model):
    # Add any additional fields you want for your custom user model here
    # For example, you can add fields for user profile information
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the value to the current date and time when the object is created
    updated_at = models.DateTimeField(auto_now=True)  # Automatically update the value to the current date and time whenever the object is saved

    def __str__(self):
        return f"{self.id} - {self.user.username}"
