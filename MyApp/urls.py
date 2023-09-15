"""
URL configuration for EntregaCoder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MyApp.views import *

urlpatterns = [
    #path('Productoras/<nombre>/<fundacion>/<presupuesto>', Productora),
    path('indice-productoras/', productora, name="Productoras"),
    #path('Pelicula/<nombre>/<duracion>/<recaudacion>', Pelicula),
    path('indice-peliculas/', pelicula, name="Peliculas"),
    path('indice-series/', serie, name="Series"),
    path('', Inicio, name="Inicio"),
    path('buscar-peliculas/', buscar_peliculas, name='buscarpelicula'),
    path('buscar-serie/', buscar_series, name="buscarserie"),
    path('buscar-productora/', buscar_productoras, name="buscarproductora"),
    path('pelicula/', peliculaTitulo, name='pelicula'),
    path('serie/', serieTitulo, name='serie'),
    path('productora/', productoraTitulo, name='productora'),
]


