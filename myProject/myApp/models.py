from django.db import models
from django.conf import settings

class Production(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    poster = models.ImageField(upload_to='images/')
    genre = models.CharField(max_length=100)
    duration = models.IntegerField()
    director = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    cast = models.ImageField(upload_to='images/')
    release = models.DateField()
    trailer = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)

class VerProduction(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    poster = models.ImageField(upload_to='images/')
    genre = models.CharField(max_length=100)
    popularity = models.FloatField(default=0) 

    class Meta:
        ordering = ['-popularity']  

class Contenido(models.Model):
    TIPO_CHOICES = [
        ('P', 'Película'),
        ('S', 'Serie'),
    ]

    titulo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    descripcion = models.TextField()
    duracion = models.IntegerField()
    fecha_lanzamiento = models.DateField()
    imagen = models.ImageField(upload_to='contenido/')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} ({self.tipo})"
    
class PerfilAdministrador(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
