from django.db import models

# Create your models here.
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


    def __str__(self):
        return self.title
    
