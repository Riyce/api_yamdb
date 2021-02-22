from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email обязателен')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, **extra_fields)
        user.role = 'admin'
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    class Role(models.TextChoices):
        USER = 'user'
        MODERATOR = 'moderator'
        ADMIN = 'admin'
        DJANGO_ADMIN = 'django_admin'

    username = models.CharField(max_length=30, unique=True,
                                verbose_name='Username',
                                error_messages={
                                    'unique':
                                        _("username already exists.")})
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(unique=True)
    role = models.TextField(choices=Role.choices, default='user')
    bio = models.TextField(verbose_name='О себе', null=True)
    objects = UserManager()
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def is_admin(self):
        return self.role == self.Role.ADMIN

    def is_moderator(self):
        return self.role == self.Role.MODERATOR

    def is_staff(self):
        return self.is_admin() or self.is_moderator()

    class Meta:
        ordering = ['-id']
