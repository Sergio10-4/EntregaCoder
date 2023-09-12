from django.contrib import admin
from matplotlib.pyplot import cla
from MyApp.models import Productora, Pelicula, Serie

class ProductoraAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'fundacion', 'presupuesto']
    search_fields = ['nombre', 'fundacion', 'presupuesto']
    list_filter = ['nombre', 'fundacion', 'presupuesto']

class PeliculaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'duracion', 'recaudacion', 'productoraCinematografica']
    search_fields = ['nombre', 'duracion', 'recaudacion', 'productoraCinematografica']
    list_filter = ['nombre', 'duracion', 'recaudacion', 'productoraCinematografica']

class SerieAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'cantidad_temporadas', 'fecha_estreno', 'productoraCinematografica']
    search_fields = ['nombre', 'cantidad_temporadas', 'fecha_estreno', 'productoraCinematografica']
    list_filter = ['nombre', 'cantidad_temporadas', 'fecha_estreno', 'productoraCinematografica']

# Register your models here.
admin.site.register(Productora, ProductoraAdmin)
admin.site.register(Pelicula, PeliculaAdmin)
admin.site.register(Serie, SerieAdmin)