from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    bio = models.TextField()

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    editorial = models.CharField(max_length=50)
    genero = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()