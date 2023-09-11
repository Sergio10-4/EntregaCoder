from django.template import Template, Context, loader
from django.shortcuts import render
from django.http import HttpResponse
from MyApp.models import Productora, Pelicula, Serie

def Productora(req, nombre, fundacion, presupuesto):

    productora = Productora(Nombre=nombre, Fundacion=fundacion, Presupuesto=presupuesto)
    productora.save()

    return HttpResponse("Compañia Ingresada Correctamente!")

def Pelicula(req, nombre, duracion, recaudacion):

    pelicula = Pelicula(Nombre=nombre, Duracion=duracion, Recaudacion=recaudacion)
    pelicula.save()

    return HttpResponse("Pelicula Ingresada Correctamente!")

def Serie(req, nombre, cant_temporadas, año_estreno):

    serie = Serie(Nombre=nombre, Temporadas=cant_temporadas, Año=año_estreno)
    serie.save()

    return HttpResponse("Serie Ingresada Correctamente!")

def registro_productoras(req):

    lista_productoras = Productora.objects.all()

    return render(req, "Productoras.html", {"Productoras": lista_productoras})

def registro_peliculas(req):

    lista_peliculas = Pelicula.objects.all()

    return render(req, "Peliculas.html", {"Peliculas": lista_peliculas})

def registro_Series(req):

    lista_series = Serie.objects.all()

    return render(req, "Series.html", {"Series": lista_series})


def invocar_html(req):

    #dochtml = open('C:/Users/asus/Desktop/Proyecto/EntregaCoder/EntregaCoder/Templates/html.html')
    #plantilla = Template(dochtml.read())
    #dochtml.close()

    #contexto1 = Context()

    #doc2 = plantilla.render(contexto1)
    #return HttpResponse(doc2)

    plantilla = loader.get_template('html.html')
    return HttpResponse(plantilla)