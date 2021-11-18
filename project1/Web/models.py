from django.db import models
from django.utils import timezone
from Componentes.models import *
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=30, default='default')

    def __str__(self):
        return self.name

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    build_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    fecha = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    content = models.CharField(max_length=500)

    def __str__(self):
        return self.content