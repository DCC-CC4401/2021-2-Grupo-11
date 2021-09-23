from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Procesador(models.Model):
    nombre = models.CharField(max_length=100)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre  # name to be shown when called
    
class TarjetaVideo(models.Model):
    nombre = models.CharField(max_length=100)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre  # name to be shown when called
    
class PlacaMadre(models.Model):
    nombre = models.CharField(max_length=100)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre  # name to be shown when called
    
class Disco(models.Model):
    nombre = models.CharField(max_length=100)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre  # name to be shown when called
    
class RAM(models.Model):
    nombre = models.CharField(max_length=100)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre  # name to be shown when called

class Gabinete(models.Model):
    nombre = models.CharField(max_length=100)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre  # name to be shown when called
    
class FuentePoder(models.Model):
    nombre = models.CharField(max_length=100)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre  # name to be shown when called
    
class CoolerCPU(models.Model):
    nombre = models.CharField(max_length=100)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre  # name to be shown when called

class Build(models.Model):
    # usuario = models.ForeignKey(User,blank=True,null=True, on_delete=models.CASCADE)
    fecha_creación = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    procesador = models.ForeignKey(Procesador, default="", on_delete=models.CASCADE)
    tarjetavideo = models.ForeignKey(TarjetaVideo, default="", blank=True, null=True, on_delete=models.CASCADE)
    placamadre = models.ForeignKey(PlacaMadre, default="", on_delete=models.CASCADE)
    disco = models.ForeignKey(Disco, default="", on_delete=models.CASCADE)
    memoria = models.ForeignKey(RAM, default="", on_delete=models.CASCADE)
    gabinete = models.ForeignKey(Gabinete, default="", on_delete=models.CASCADE)
    fuente = models.ForeignKey(FuentePoder, default="", on_delete=models.CASCADE)
    cooler = models.ForeignKey(CoolerCPU, default="", blank=True, null=True, on_delete=models.CASCADE)

