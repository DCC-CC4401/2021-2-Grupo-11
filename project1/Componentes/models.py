from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class abstractComponent(models.Model):
    nombre = models.CharField(max_length=100, default='nombre')
    url = models.CharField(max_length=200, default='url')

    def __str__(self):
        return self.nombre  # name to be shown when called

# Create your models here.
class Procesador(abstractComponent):
    pass
    
class TarjetaDeVideo(abstractComponent):
    pass

    
class PlacaMadre(abstractComponent):
    pass
    
class DiscoDuro(abstractComponent):
    pass 
    
class RAM(abstractComponent):
    pass

class Gabinete(abstractComponent):
    pass
    
class FuenteDePoder(abstractComponent):
    pass  
    
class CoolerCPU(abstractComponent):
    pass   
    

class Build(models.Model):
    # usuario = models.ForeignKey(User,blank=True,null=True, on_delete=models.CASCADE)
    fecha_creación = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    procesador = models.ForeignKey(Procesador, on_delete=models.CASCADE)
