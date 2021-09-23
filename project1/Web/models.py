from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=30, default='uwu')

    def __str__(self):
        return self.nombre  # name to be shown when called
