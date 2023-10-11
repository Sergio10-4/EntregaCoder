from dataclasses import fields
import email
from os import name
from tabnanny import verbose
from django.db import models
from django.forms import Widget
from django import forms
from matplotlib import widgets
from django.core.validators import MaxLengthValidator
from sqlalchemy import Null
from django.conf import settings
from django.contrib.auth.models import User, AbstractUser, Permission, Group
# Create your models here.


class Tag(models.Model):

    GENEROS = (
        ('Accion', 'Acción'),
        ('Comedia', 'Comedia'),
        ('Drama', 'Drama'),
        ('Fantasia', 'Fantasía'),
        ('Animacion', 'Animacion'),
        ('Terror', 'Terror'),
        ('Thriller', 'Thriller'),
        ('Suspenso', 'Suspenso'),
        ('Sci-Fi', 'Sci-Fi'),
        # Agrega más géneros según tus necesidades
    )

    nombre = models.CharField(max_length=100, choices=GENEROS)

    def __str__(self):
        return f' {self.nombre}'
    
    class Meta():

        verbose_name = 'Generos'
        verbose_name_plural = 'Generos De Cine'
        ordering = ('nombre',)

class Actor(models.Model):
    nombre = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='actores/')

    def __str__(self):
        return f' {self.nombre} - {self.avatar}'
    
    class Meta():

        verbose_name = 'Actor'
        verbose_name_plural = 'Actores De Cine'
        ordering = ('nombre',)

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
    rating = models.IntegerField(null=True)
    tags = models.ManyToManyField(Tag)
    descripcion = models.TextField(null=True, validators=[MaxLengthValidator(250)])
    reparto = models.ManyToManyField(Actor)
    portada = models.ImageField(null=True)
    productoraCinematografica = models.ForeignKey(Productora, on_delete=models.CASCADE)

    def __str__(self):
        return f' {self.nombre} - {self.duracion} - {self.recaudacion} - {self.rating} - {self.tags} - {self.descripcion} - {self.reparto} - {self.portada} - {self.productoraCinematografica}'
        
    class Meta():

        verbose_name = 'Pelicula'
        verbose_name_plural = 'Catalogo De Peliculas'
        ordering = ('nombre',)

class ListaPeliculas(models.Model):

    nombre_pelicula = models.CharField(max_length=255)
    peliculas = models.ManyToManyField(Pelicula)

    def __str__(self):

        return f' {self.nombre_pelicula}'
    
    class Meta():

        verbose_name = 'Lista'
        verbose_name_plural = 'Lista De Peliculas'
        ordering = ('nombre_pelicula',)

class Serie(models.Model):

    nombre = models.CharField(max_length=100)
    cantidad_temporadas = models.IntegerField()
    fecha_estreno = models.DateField()
    rating = models.IntegerField(null=True)
    tags = models.ManyToManyField(Tag)
    descripcion = models.TextField(null=True, validators=[MaxLengthValidator(250)])
    reparto = models.ManyToManyField(Actor)
    portada = models.ImageField(null=True)
    productoraCinematografica = models.ForeignKey(Productora, on_delete=models.CASCADE)

    def __str__(self):
        return f' {self.nombre} - {self.cantidad_temporadas} - {self.fecha_estreno} - {self.rating} - {self.tags} - {self.descripcion} - {self.reparto} - {self.portada} - {self.productoraCinematografica}'
    
    class Meta():

        verbose_name = 'Serie'
        verbose_name_plural = 'Catalogo De Series'
        ordering = ('nombre',)

class CustomUser(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    fotoPerfil = models.ImageField(null=True, upload_to='perfilImages/')
    descripcionUsuario = models.TextField(null=True, validators=[MaxLengthValidator(250)])
    listadepeliculas = models.ManyToManyField(Pelicula, related_name='usuarios_que_guardaron')

    groups = models.ManyToManyField(Group, related_name='customuser_set')
    user_permissions = models.ManyToManyField(
        Permission, related_name='customuser_set'
    )

    def __str__(self):
        return f' {self.username} - {self.email} - {self.password}'
    
    class Meta():

        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ('username',)

class UserRegistration(models.Model):
    user = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    agree_terms = models.BooleanField()
    foto_perfil = models.ImageField(null=True, upload_to='perfil/')
    descripcion_usuario = models.TextField(null=True, validators=[MaxLengthValidator(250)])

    def __str__(self):
        return f' {self.username} - {self.email} - {self.password} - {self.agree_terms} - {self.foto_perfil} - {self.descripcion_usuario}'
    class Meta():

        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ('user',)

class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    peliculas_guardadas = models.ManyToManyField(Pelicula)

    def __str__(self):
        return f' {self.usuario.username} - {self.peliculas_guardadas}'

