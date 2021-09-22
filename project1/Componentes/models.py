from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Procesador(models.Model):
    nombre = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    frecuencia = models.CharField(max_length=20)
    frecuencia_turbo = models.CharField(max_length=20)
    nucleo = models.CharField(max_length=50)
    cache = models.CharField(max_length=50)
    socket = models.CharField(max_length=20)
    nucleo = models.CharField(max_length=100)
    proceso = models.CharField(max_length=20)
    tdp = models.CharField(max_length=20)
    cooler = models.CharField(max_length=50)
    graficos = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre  # name to be shown when called

class Build(models.Model):
    # usuario = models.ForeignKey(User,blank=True,null=True, on_delete=models.CASCADE)
    fecha_creación = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    procesador = models.ForeignKey(Procesador, on_delete=models.CASCADE)