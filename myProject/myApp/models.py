from django.db import models
from django.conf import settings

class Production(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    poster = models.ImageField(upload_to='images/')
    genre = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    cast = models.ImageField(upload_to='images/')
    release = models.DateField()
    trailer = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)

class VerProduction(models.Model):
    title = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='images/')
    genre = models.CharField(max_length=100)
    popularity = models.FloatField(default=0) 

    class Meta:
        ordering = ['-popularity']  
    
class PerfilAdministrador(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
