from django.contrib import admin
from matplotlib.pyplot import cla
from django.utils.html import format_html
from MyApp.models import Productora, Pelicula, Serie, UserRegistration, Actor, Tag, CustomUser

class ProductoraAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'fundacion', 'presupuesto']
    search_fields = ['nombre', 'fundacion', 'presupuesto']
    list_filter = ['nombre', 'fundacion', 'presupuesto']

class PeliculaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'duracion', 'recaudacion', 'rating', 'display_reparto', 'display_tags', 'portada', 'descripcion', 'productoraCinematografica']

    def display_tags(self, obj):
        return ', '.join(tag.nombre for tag in obj.tags.all())
    display_tags.short_description = 'Generos'

    def display_reparto(self, obj):
        return ', '.join(actor.nombre for actor in obj.reparto.all())
    display_reparto.short_description = 'Reparto'

    search_fields = ['nombre', 'duracion', 'recaudacion', 'rating', 'display_reparto', 'display_tags', 'portada', 'descripcion', 'productoraCinematografica']
    list_filter = ['nombre', 'duracion', 'recaudacion', 'rating', 'reparto', 'productoraCinematografica']

class SerieAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'cantidad_temporadas', 'fecha_estreno', 'rating', 'display_reparto', 'display_tags', 'descripcion', 'portada', 'productoraCinematografica']

    def display_tags(self, obj):
        return ', '.join(tag.nombre for tag in obj.tags.all())
    display_tags.short_description = 'Generos'

    def display_reparto(self, obj):
        return ', '.join(actor.nombre for actor in obj.reparto.all())
    display_reparto.short_description = 'Reparto'

    search_fields = ['nombre', 'cantidad_temporadas', 'fecha_estreno', 'rating', 'display_reparto', 'display_tags', 'descripcion', 'portada', 'productoraCinematografica']
    list_filter = ['nombre', 'cantidad_temporadas', 'fecha_estreno', 'rating', 'reparto', 'productoraCinematografica']

class UserAdmin(admin.ModelAdmin):
    list_display = ['user', 'email', 'password', 'agree_terms', 'foto_perfil', 'descripcion_usuario']
    search_fields = ['user', 'email', 'password', 'agree_terms', 'foto_perfil', 'descripcion_usuario']
    list_filter = ['user', 'email', 'password', 'agree_terms', 'foto_perfil', 'descripcion_usuario']

class ActorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'avatar']
    search_fields = ['nombre', 'avatar']
    list_filter = ['nombre', 'avatar']

class TagAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']
    list_filter = ['nombre']

class abstractUser(admin.ModelAdmin):
    list_display = ['username', 'email', 'password', 'fotoPerfil', 'descripcionUsuario']
    search_fields = ['username', 'email', 'password']
    list_filter = ['username', 'email', 'password']

# Register your models here.
admin.site.register(Productora, ProductoraAdmin)
admin.site.register(Pelicula, PeliculaAdmin)
admin.site.register(Serie, SerieAdmin)
admin.site.register(UserRegistration, UserAdmin)
admin.site.register(Actor ,ActorAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(CustomUser, abstractUser)