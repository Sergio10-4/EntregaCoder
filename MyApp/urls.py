from django.contrib import admin
from django.urls import path
from .views import perfilUsuario, profile, usuario
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('indice-productoras/', views.productora, name="Productoras"),
    path('indice-peliculas/', views.pelicula, name="Peliculas"),
    path('indice-series/', views.serie, name="Series"),
    path('inicio/', views.Inicio, name="Inicio"),
    path('home/', views.home, name="home"),
    path('registrar-usuario/', views.usuario, name="añadirusuario"),
    path('buscar-peliculas/', views.buscar_peliculas, name='buscarpelicula'),
    path('buscar-serie/', views.buscar_series, name="buscarserie"),
    path('buscar-productora/', views.buscar_productoras, name="buscarproductora"),
    path('buscar-usuarios/', views.buscar_usuarios, name="buscarusuarios"),
    path('pelicula/', views.peliculaTitulo, name='pelicula'),
    path('serie/', views.serieTitulo, name='serie'),
    path('productora/', views.productoraTitulo, name='productora'),
    path('acerca-de-mi/', views.aboutMe, name='aboutme'),
    path('catalogo-de-peliculas/', views.peliCatalogo, name='catalogopeliculas'),
    path('catalogo-de-series/', views.serieCatalogo, name='catalogoseries'),
    path('catalogo-de-productoras/', views.productCatalogo, name='catalogoproductoras'),
    path('Error-404/', views.Error, name='Error'),
    path('lista-de-Actores/', views.listaActores, name='Cast'),
    path('lista-de-categorias/', views.listaGeneros, name='Categorias'),
    path('acerca-de-pagina/', views.aboutPage, name='aboutpage'),
    path('acerca-del-dev/', views.aboutDev, name='sobremi'),
    path('perfil-de-usuario/', views.loginView, name='Perfil'),
    path('perfil-de/', views.profile, name='PerfilUsuario'),
    path('cerrar-sesion/', views.cerrarSesion, name='cerrarSesion'),
    path('cambiar-contraseña/', views.cambiarContraseña, name='parallax'),
    path('lista/<int:lista_nombre>/', views.agregar_peliculas_a_lista, name='peliculasUsuario'),
]