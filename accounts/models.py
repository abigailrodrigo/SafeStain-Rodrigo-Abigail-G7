from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        USER = "USER", "User"
        ADMIN = "ADMIN", "Admin"

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.USER
    )
    email = models.EmailField(unique=True) 
    skin_type = models.CharField(max_length=20, blank=True, null=True)
    skin_triggers = models.TextField(blank=True)

    def __str__(self):
        return self.username