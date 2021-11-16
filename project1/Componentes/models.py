from django.db import models
from django.utils import timezone
from Web.models import User


class GPU(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    precio = models.CharField(max_length=20)
    cat0 = models.CharField(max_length=50)
    cat1 = models.CharField(max_length=50)
    cat2 = models.CharField(max_length=50)
    cat3 = models.CharField(max_length=50)
    cat4 = models.CharField(max_length=50)
    des0 = models.CharField(max_length=50)
    des1 = models.CharField(max_length=50)
    des2 = models.CharField(max_length=50)
    des3 = models.CharField(max_length=50)
    des4 = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Procesador(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    precio = models.CharField(max_length=20)
    cat0 = models.CharField(max_length=50)
    cat1 = models.CharField(max_length=50)
    cat2 = models.CharField(max_length=50)
    cat3 = models.CharField(max_length=50)
    cat4 = models.CharField(max_length=50)
    des0 = models.CharField(max_length=50)
    des1 = models.CharField(max_length=50)
    des2 = models.CharField(max_length=50)
    des3 = models.CharField(max_length=50)
    des4 = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class PlacaMadre(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    precio = models.CharField(max_length=20)
    cat0 = models.CharField(max_length=50)
    cat1 = models.CharField(max_length=50)
    cat2 = models.CharField(max_length=50)
    cat3 = models.CharField(max_length=50)
    cat4 = models.CharField(max_length=50)
    des0 = models.CharField(max_length=50)
    des1 = models.CharField(max_length=50)
    des2 = models.CharField(max_length=50)
    des3 = models.CharField(max_length=50)
    des4 = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class RAM(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    precio = models.CharField(max_length=20)
    cat0 = models.CharField(max_length=50)
    cat1 = models.CharField(max_length=50)
    cat2 = models.CharField(max_length=50)
    cat3 = models.CharField(max_length=50)
    cat4 = models.CharField(max_length=50)
    des0 = models.CharField(max_length=50)
    des1 = models.CharField(max_length=50)
    des2 = models.CharField(max_length=50)
    des3 = models.CharField(max_length=50)
    des4 = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class DiscoDuro(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    precio = models.CharField(max_length=20)
    cat0 = models.CharField(max_length=50)
    cat1 = models.CharField(max_length=50)
    cat2 = models.CharField(max_length=50)
    cat3 = models.CharField(max_length=50)
    cat4 = models.CharField(max_length=50)
    des0 = models.CharField(max_length=50)
    des1 = models.CharField(max_length=50)
    des2 = models.CharField(max_length=50)
    des3 = models.CharField(max_length=50)
    des4 = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class SSD(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    precio = models.CharField(max_length=20)
    cat0 = models.CharField(max_length=50)
    cat1 = models.CharField(max_length=50)
    cat2 = models.CharField(max_length=50)
    cat3 = models.CharField(max_length=50)
    cat4 = models.CharField(max_length=50)
    des0 = models.CharField(max_length=50)
    des1 = models.CharField(max_length=50)
    des2 = models.CharField(max_length=50)
    des3 = models.CharField(max_length=50)
    des4 = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Gabinete(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    precio = models.CharField(max_length=20)
    cat0 = models.CharField(max_length=50)
    cat1 = models.CharField(max_length=50)
    cat2 = models.CharField(max_length=50)
    cat3 = models.CharField(max_length=50)
    cat4 = models.CharField(max_length=50)
    des0 = models.CharField(max_length=50)
    des1 = models.CharField(max_length=50)
    des2 = models.CharField(max_length=50)
    des3 = models.CharField(max_length=50)
    des4 = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class FuentePoder(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    precio = models.CharField(max_length=20)
    cat0 = models.CharField(max_length=50)
    cat1 = models.CharField(max_length=50)
    cat2 = models.CharField(max_length=50)
    cat3 = models.CharField(max_length=50)
    cat4 = models.CharField(max_length=50)
    des0 = models.CharField(max_length=50)
    des1 = models.CharField(max_length=50)
    des2 = models.CharField(max_length=50)
    des3 = models.CharField(max_length=50)
    des4 = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class CoolerCPU(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    precio = models.CharField(max_length=20)
    cat0 = models.CharField(max_length=50)
    cat1 = models.CharField(max_length=50)
    cat2 = models.CharField(max_length=50)
    cat3 = models.CharField(max_length=50)
    cat4 = models.CharField(max_length=50)
    des0 = models.CharField(max_length=50)
    des1 = models.CharField(max_length=50)
    des2 = models.CharField(max_length=50)
    des3 = models.CharField(max_length=50)
    des4 = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Mouse(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    precio = models.CharField(max_length=20)
    cat0 = models.CharField(max_length=50)
    cat1 = models.CharField(max_length=50)
    cat2 = models.CharField(max_length=50)
    cat3 = models.CharField(max_length=50)
    cat4 = models.CharField(max_length=50)
    des0 = models.CharField(max_length=50)
    des1 = models.CharField(max_length=50)
    des2 = models.CharField(max_length=50)
    des3 = models.CharField(max_length=50)
    des4 = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Teclado(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    precio = models.CharField(max_length=20)
    cat0 = models.CharField(max_length=50)
    cat1 = models.CharField(max_length=50)
    cat2 = models.CharField(max_length=50)
    cat3 = models.CharField(max_length=50)
    cat4 = models.CharField(max_length=50)
    des0 = models.CharField(max_length=50)
    des1 = models.CharField(max_length=50)
    des2 = models.CharField(max_length=50)
    des3 = models.CharField(max_length=50)
    des4 = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Monitor(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    precio = models.CharField(max_length=20)
    cat0 = models.CharField(max_length=50)
    cat1 = models.CharField(max_length=50)
    cat2 = models.CharField(max_length=50)
    cat3 = models.CharField(max_length=50)
    cat4 = models.CharField(max_length=50)
    des0 = models.CharField(max_length=50)
    des1 = models.CharField(max_length=50)
    des2 = models.CharField(max_length=50)
    des3 = models.CharField(max_length=50)
    des4 = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Audifonos(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    precio = models.CharField(max_length=20)
    cat0 = models.CharField(max_length=50)
    cat1 = models.CharField(max_length=50)
    cat2 = models.CharField(max_length=50)
    cat3 = models.CharField(max_length=50)
    cat4 = models.CharField(max_length=50)
    des0 = models.CharField(max_length=50)
    des1 = models.CharField(max_length=50)
    des2 = models.CharField(max_length=50)
    des3 = models.CharField(max_length=50)
    des4 = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class SillaGamer(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    precio = models.CharField(max_length=20)
    cat0 = models.CharField(max_length=50)
    cat1 = models.CharField(max_length=50)
    cat2 = models.CharField(max_length=50)
    cat3 = models.CharField(max_length=50)
    cat4 = models.CharField(max_length=50)
    des0 = models.CharField(max_length=50)
    des1 = models.CharField(max_length=50)
    des2 = models.CharField(max_length=50)
    des3 = models.CharField(max_length=50)
    des4 = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Build(models.Model):
    name = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    creacion = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    tarjetavideo = models.ForeignKey(GPU, blank=True, null=True, on_delete=models.CASCADE)
    procesador = models.ForeignKey(Procesador, on_delete=models.CASCADE)
    placamadre = models.ForeignKey(PlacaMadre, on_delete=models.CASCADE)
    memoria = models.ForeignKey(RAM, on_delete=models.CASCADE)
    discohdd = models.ForeignKey(DiscoDuro, blank=True, null=True, on_delete=models.CASCADE)
    discossd = models.ForeignKey(SSD, blank=True, null=True, on_delete=models.CASCADE)
    gabinete = models.ForeignKey(Gabinete, on_delete=models.CASCADE)
    fuente = models.ForeignKey(FuentePoder, on_delete=models.CASCADE)
    cooler = models.ForeignKey(CoolerCPU, blank=True, null=True, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)



    def __str__(self):
        return self.name


class Setup(models.Model):
    name = models.CharField(max_length=100)
    usuario = models.ForeignKey(User,blank=True,null=True, on_delete=models.CASCADE)
    creacion = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    mouse = models.ForeignKey(Mouse, on_delete=models.CASCADE)
    teclado = models.ForeignKey(Teclado, on_delete=models.CASCADE)
    monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE)
    audifono = models.ForeignKey(Audifonos, on_delete=models.CASCADE)
    sillagamer = models.ForeignKey(SillaGamer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
