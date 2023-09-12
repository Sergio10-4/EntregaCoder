import re
from django.template import Template, Context, loader
from django.shortcuts import render
from django.http import HttpResponse
from MyApp.models import Productora, Pelicula, Serie

def Inicio(req):

    return render(req, "inicio.html")

def productora(req):

    print('method', req.method)
    print('POST', req.POST)
    if req.method == 'POST':

        productora = Productora(Nombre=req.POST["Productora"], Fundacion=req.POST["Fundacion"], Presupuesto=req.POST["Presupuesto"])
        productora.save()

        return render(req, 'inicio.html')
    else:
        return render(req, "productoras.html")

def pelicula(req):

    print('method', req.method)
    print('POST', req.POST)
    if req.method == 'POST':

        pelicula = Pelicula(Nombre=req.POST["Pelicula"], Fundacion=req.POST["Duracion"], Presupuesto=req.POST["Recaudacion"])
        pelicula.save()

        return render(req, 'inicio.html')
    else:
        return render(req, "peliculas.html")

def serie(req):

    print('method', req.method)
    print('POST', req.POST)
    if req.method == 'POST':

        serie = Serie(Nombre=req.POST["Serie"], Fundacion=req.POST["Temporadas"], Presupuesto=req.POST["Estreno"])
        serie.save()

        return render(req, 'inicio.html')
    else:
        return render(req, "series.html")