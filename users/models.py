from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('delivery_agent', 'Delivery Agent'),
        ('customer', 'Customer'),
    )
    name = models.CharField(max_length=255, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    is_blocked = models.BooleanField(default=False)  # Can be blocked/unblocked
    is_deleted = models.BooleanField(default=False)  # Soft delete

    def __str__(self):
        return f"{self.username} ({self.role})"
