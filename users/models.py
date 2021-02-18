from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    class Role(models.TextChoices):
        USER = 'User'
        MODERATOR = 'Moderator'
        ADMIN = 'Admin'
        DJANGO_ADMIN = 'Django_admin'

    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name="profile")
    description = models.TextField(blank=True, null=True)
    role = models.TextField(choices=Role.choices, default='User')

    def __str__(self):
        return self.user.username
