from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils import timezone
import random
import string

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_set",  # Custom related_name to avoid conflict
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_user_permissions",  # Custom related_name to avoid conflict
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )
    phone_number = models.CharField(max_length=15, blank=False, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    level =  models. IntegerField(default=1)
    def __str__(self):
        return self.username

class VerificationCode(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        return (timezone.now() - self.created_at).seconds < 300  # 5分钟有效