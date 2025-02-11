from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class User(AbstractUser):
    clerk_id = models.CharField(max_length=255, unique=True, null=True, blank=True)
    username = models.CharField(max_length=1000, null=True, blank=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    image_url = models.URLField(max_length=500, blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True)  # Make email unique!
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_signed_in_at = models.DateTimeField(blank=True, null=True)

    # Set email as the unique identifier for authentication
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # You can add other required fields if needed

    def __str__(self):
        return self.email
