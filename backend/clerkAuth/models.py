from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# Optionally, create a custom user manager if you need extra functionality
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    clerk_id = models.CharField(max_length=255, unique=True, null=True, blank=True)
    # Optional username for display purposes only
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

    objects = CustomUserManager()  # Use your custom manager

    def __str__(self):
        return self.email
