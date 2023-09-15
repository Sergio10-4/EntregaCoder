from math import prod
import re
from django.template import Template, Context, loader
from django.shortcuts import render
from django.http import HttpResponse
from MyApp.forms import ProductoraForm, PeliculaForm, SerieForm
from MyApp.models import Productora, Pelicula, Serie
from django.db.models import *

def Inicio(req):

    return render(req, "inicio.html")

def productora(req):
    if req.method == 'POST':
        formulario = ProductoraForm(req.POST)
        if formulario.is_valid():
            formulario.save()
            return render(req, 'inicio.html')
    else:
        formulario = ProductoraForm()
    return render(req, "productoras.html", {'form': formulario})

def pelicula(req):
    if req.method == 'POST':
        formulario = PeliculaForm(req.POST)
        if formulario.is_valid():
            formulario.save()
            return render(req, 'inicio.html')
    else:
        formulario = PeliculaForm()
    return render(req, "peliculas.html", {'form': formulario})

def serie(req):
    if req.method == 'POST':
        formulario = SerieForm(req.POST)
        if formulario.is_valid():
            formulario.save()
            return render(req, 'inicio.html')
    else:
        formulario = SerieForm()
    return render(req, "series.html", {'form': formulario})

def buscar_peliculas(req):
    query = req.GET.get('query', '')  # Obtener el valor ingresado en el campo de búsqueda
    peliculas = Pelicula.objects.filter(nombre__icontains=query)  # Realizar la búsqueda en la base de datos
    return render(req, 'resultadobusqueda.html', {'peliculas': peliculas, 'query': query})

def buscar_series(req):
    query = req.GET.get('query', '')  # Obtener el valor ingresado en el campo de búsqueda
    series = Serie.objects.filter(nombre__icontains=query)  # Realizar la búsqueda en la base de datos
    return render(req, 'resultadobusquedaserie.html', {'series': series, 'query': query})

def buscar_productoras(req):
    query = req.GET.get('query', '')  # Obtener el valor ingresado en el campo de búsqueda
    productoras = Productora.objects.filter(nombre__icontains=query)  # Realizar la búsqueda en la base de datos
    return render(req, 'resultadobusquedaproductora.html', {'productoras': productoras, 'query': query})
def peliculaTitulo(request):
    context = {
        'titulo': 'Esta Es La Ventana De Películas'
    }
    return render(request, 'herencia.html', context)

def serieTitulo(request):
    context = {
        'titulo': 'Esta Es La Ventana De Series'
    }
    return render(request, 'herencia.html', context)

def productoraTitulo(request):
    context = {
        'titulo': 'Esta Es La Ventana De Productoras'
    }
    return render(request, 'herencia.html', context)