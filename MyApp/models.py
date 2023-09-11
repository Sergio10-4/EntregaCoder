from django.db import models

# Create your models here.

class Productora(models.Model):

    nombre = models.CharField(max_length=20)
    fundacion = models.IntegerField()
    presupuesto = models.FloatField()

class Pelicula(models.Model):

    nombre = models.CharField(max_length=20)
    duracion = models.DurationField()
    recaudacion = models.FloatField()

class Serie(models.Model):

    nombre = models.CharField(max_length=20)
    cantidad_temporadas = models.IntegerField()
    fecha_estreno = models.DateField()
