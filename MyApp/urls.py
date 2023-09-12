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
from MyApp.views import Inicio
from MyApp.views import *

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('Productoras/<nombre>/<fundacion>/<presupuesto>', Productora),
    path('indice-productoras/', productora),
    #path('Pelicula/<nombre>/<duracion>/<recaudacion>', Pelicula),
    path('indice-peliculas/', pelicula),
    #path('Series/<nombre>/<cant_temporadas>/<año_estreno>', Serie),
    path('indice-series/', serie),
    #path('template/', invocar_html),
    path('', Inicio),
]


