from django.db import models
from django.utils import timezone
from Web.models import User

class Procesador(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    desc0 = models.CharField(max_length=50)
    desc1 = models.CharField(max_length=50)
    desc2 = models.CharField(max_length=50)
    desc3 = models.CharField(max_length=50)
    desc4 = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class GPU(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    desc0 = models.CharField(max_length=50)
    desc1 = models.CharField(max_length=50)
    desc2 = models.CharField(max_length=50)
    desc3 = models.CharField(max_length=50)
    desc4 = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class PlacaMadre(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    desc0 = models.CharField(max_length=50)
    desc1 = models.CharField(max_length=50)
    desc2 = models.CharField(max_length=50)
    desc3 = models.CharField(max_length=50)
    desc4 = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class DiscoDuro(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    desc0 = models.CharField(max_length=50)
    desc1 = models.CharField(max_length=50)
    desc2 = models.CharField(max_length=50)
    desc3 = models.CharField(max_length=50)
    desc4 = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class SSD(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    desc0 = models.CharField(max_length=50)
    desc1 = models.CharField(max_length=50)
    desc2 = models.CharField(max_length=50)
    desc3 = models.CharField(max_length=50)
    desc4 = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class RAM(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    desc0 = models.CharField(max_length=50)
    desc1 = models.CharField(max_length=50)
    desc2 = models.CharField(max_length=50)
    desc3 = models.CharField(max_length=50)
    desc4 = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Gabinete(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    desc0 = models.CharField(max_length=50)
    desc1 = models.CharField(max_length=50)
    desc2 = models.CharField(max_length=50)
    desc3 = models.CharField(max_length=50)
    desc4 = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class FuentePoder(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    desc0 = models.CharField(max_length=50)
    desc1 = models.CharField(max_length=50)
    desc2 = models.CharField(max_length=50)
    desc3 = models.CharField(max_length=50)
    desc4 = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class CoolerCPU(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    desc0 = models.CharField(max_length=50)
    desc1 = models.CharField(max_length=50)
    desc2 = models.CharField(max_length=50)
    desc3 = models.CharField(max_length=50)
    desc4 = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Build(models.Model):
    usuario = models.ForeignKey(User,blank=True,null=True, on_delete=models.CASCADE)
    fecha_creación = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    procesador = models.ForeignKey(Procesador, default="default", on_delete=models.CASCADE)
    tarjetavideo = models.ForeignKey(GPU, default="default", blank=True, null=True, on_delete=models.CASCADE)
    placamadre = models.ForeignKey(PlacaMadre, default="default", on_delete=models.CASCADE)
    discossd = models.ForeignKey(SSD, default="default", on_delete=models.CASCADE)
    discohdd = models.ForeignKey(DiscoDuro, default="default", on_delete=models.CASCADE)
    memoria = models.ForeignKey(RAM, default="default", on_delete=models.CASCADE)
    gabinete = models.ForeignKey(Gabinete, default="default", on_delete=models.CASCADE)
    fuente = models.ForeignKey(FuentePoder, default="default", on_delete=models.CASCADE)
    cooler = models.ForeignKey(CoolerCPU, default="default", blank=True, null=True, on_delete=models.CASCADE)

