from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Production(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)
    genre = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    cast = models.CharField(max_length=100)
    release = models.DateField()
    trailer = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    


class PerfilAdministrador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
