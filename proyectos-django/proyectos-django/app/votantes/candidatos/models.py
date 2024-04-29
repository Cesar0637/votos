from django.utils import timezone
from django.db import models

class Partido(models.Model):
    nombre = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logos')
    descripcion = models.CharField(max_length=50,null=True)
    
    def __str__(self):
        return self.nombre
    
class Candidato(models.Model):
    nombre = models.CharField(max_length=50)
    apeido_Paterno = models.CharField(max_length=50, null=True)
    apeido_Materno = models.CharField(max_length=50, null=True)
    partidos = models.ForeignKey("candidatos.Partido", verbose_name='Partido',on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imagen',null=True)
    
    def __str__(self):
        return self.nombre
class Votacion (models.Model):
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    fecha = models.DateTimeField("Fecha", auto_now=True)