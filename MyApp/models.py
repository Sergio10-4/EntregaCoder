from os import name
from tabnanny import verbose
from django.db import models

# Create your models here.

class Productora(models.Model):

    nombre = models.CharField(max_length=100)
    fundacion = models.IntegerField()
    presupuesto = models.FloatField()

    def __str__(self):
        return f' {self.nombre} - {self.fundacion} - {self.presupuesto}'
    
    class Meta():

        verbose_name = 'Productora'
        verbose_name_plural = 'Productoras De Cine'
        ordering = ('nombre',)

class Pelicula(models.Model):

    nombre = models.CharField(max_length=100)
    duracion = models.DurationField()
    recaudacion = models.FloatField()
    productoraCinematografica = models.ForeignKey(Productora, on_delete=models.CASCADE)

    def __str__(self):
        return f' {self.nombre} - {self.duracion} - {self.recaudacion} - {self.productoraCinematografica}'
        
    class Meta():

        verbose_name = 'Pelicula'
        verbose_name_plural = 'Catalogo De Peliculas'
        ordering = ('nombre',)

class Serie(models.Model):

    nombre = models.CharField(max_length=100)
    cantidad_temporadas = models.IntegerField()
    fecha_estreno = models.DateField()
    productoraCinematografica = models.ForeignKey(Productora, on_delete=models.CASCADE)

    def __str__(self):
        return f' {self.nombre} - {self.cantidad_temporadas} - {self.fecha_estreno} - {self.productoraCinematografica}'
    
    class Meta():

        verbose_name = 'Serie'
        verbose_name_plural = 'Catalogo De Series'
        ordering = ('nombre',)
