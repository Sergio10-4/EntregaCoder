import re
from django.template import Template, Context, loader
from django.shortcuts import render
from django.http import HttpResponse
from MyApp.models import Productora, Pelicula, Serie

def Inicio(req):

    return render(req, "inicio.html")

def productora(req):

    return render(req, "productoras.html")

def pelicula(req):

    return render(req, "peliculas.html")

def serie(req):

    return render(req, "series.html")

"""

def registro_productoras(req):

    lista_productoras = Productora.objects.all()

    return render(req, "Productoras.html", {"Productoras": lista_productoras})

#def registro_peliculas(req):

#    lista_peliculas = Pelicula.objects.all()

#    return render(req, "Peliculas.html", {"Peliculas": lista_peliculas})

def registro_Series(req):

    lista_series = Serie.objects.all()

    return render(req, "Series.html", {"Series": lista_series})
"""
def invocar_html(req):

    #dochtml = open('C:/Users/asus/Desktop/Proyecto/EntregaCoder/EntregaCoder/Templates/html.html')
    #plantilla = Template(dochtml.read())
    #dochtml.close()

    #contexto1 = Context()

    #doc2 = plantilla.render(contexto1)
    #return HttpResponse(doc2)

    plantilla = loader.get_template('html.html')
    return HttpResponse(plantilla)