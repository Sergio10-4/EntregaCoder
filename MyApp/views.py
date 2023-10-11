from math import prod
import re
from django.template import Template, Context, loader
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from flask import request
from matplotlib.style import context
from MyApp.forms import AgregarPeliculaForm, ProductoraForm, PeliculaForm, SerieForm, UserRegistrationForm, ModificarEmailForm, LoginForm, UsuarioForm
from MyApp.models import Productora, Pelicula, ListaPeliculas, Serie, Tag, UserRegistration, PerfilUsuario, CustomUser
from django.db.models import *
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def Inicio(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, passowrd=password)
            if user is not None:
                login(request, user)
                return redirect('Perfil')
            else:
                print("Inicio De Sesion Fallido")
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()

    login_form = AuthenticationForm()
    return render(request, "inicio.html", {'form': form, 'login_form': login_form})

def home(request):
    return render(request, 'home.html')

def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request.POST)
            if form.is_valid():
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request, username=username, passowrd=password)
                if user is not None:
                    login(request, user)
                    return redirect('Perfil')
                else:
                    print("Inicio De Sesion Fallido")
            else:
                print(form.errors)
        else:
            form = UserRegistrationForm()

        login_form = AuthenticationForm()
        return render(request, "inicio.html", {'form': form, 'login_form': login_form})
    else:
        return redirect('Inicio')

@csrf_protect
def loginView(req):
    return render(req, 'profile.html')

def productora(req):
    if req.method == 'POST':
        formulario = ProductoraForm(req.POST)
        if formulario.is_valid():
            formulario.save()
            return render(req, 'home.html')
    else:
        formulario = ProductoraForm()
    return render(req, "productoras.html", {'form': formulario})

def pelicula(request):
    if request.method == 'POST':
        formulario = PeliculaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return render(request, 'home.html')
    else:
        formulario = PeliculaForm()

    context = {
        'form': formulario
    }
    return render(request, "peliculas.html", context)

def agregar_peliculas_a_lista(request, lista_nombre):
    lista = get_object_or_404(ListaPeliculas, id=lista_nombre)
    
    if request.method == 'POST':
        form = AgregarPeliculaForm(request.POST)
        if form.is_valid():
            pelicula = form.cleaned_data['pelicula_nombre']
            lista.peliculas.add(pelicula)
            lista.save()
            return redirect('catalogopeliculas', lista_nombre=lista_nombre)
    else:
        form = AgregarPeliculaForm()

    peliculas_guardadas = lista.peliculas.all()

    return render(request,'parallax.html', {'lista': lista, 'peliculas_guardadas': peliculas_guardadas, 'form': form})

def serie(request):
    if request.method == 'POST':
        formulario = SerieForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return render(request, 'home.html')
    else:
        formulario = SerieForm()

    context = {
        'form': formulario
    }
    return render(request, "series.html", context)

def usuario(request):
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return render(request, 'home.html')
    else:
        formulario = UsuarioForm()

    context = {
        'form': formulario
    }
    return render(request, "usuarios.html", context)

def buscar_peliculas(request):
    query = request.GET.get('query', '')
    peliculas = Pelicula.objects.filter(nombre__icontains=query)
    generos = Tag.objects.filter(pelicula__in=peliculas).values('nombre')
    return render(request, 'resultadobusqueda.html', {'peliculas': peliculas, 'generos': generos})

def buscar_series(req):
    query = req.GET.get('query', '')
    series = Serie.objects.filter(nombre__icontains=query)
    generos = Tag.objects.filter(serie__in=series).values('nombre')
    return render(req, 'resultadobusquedaserie.html', {'series': series, 'query': query, 'generos': generos})

def buscar_productoras(req):
    query = req.GET.get('query', '')
    productoras = Productora.objects.filter(nombre__icontains=query)
    return render(req, 'resultadobusquedaproductora.html', {'productoras': productoras, 'query': query})

def buscar_usuarios(request):
    query = request.GET.get('query', '')
    usuarios = UserRegistration.objects.filter(user__icontains=query)
    return render(request, 'resultadobusqueda.html', {'query': query, 'usuarios': usuarios, })


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

def paginaInicio(request):
    context = {
        'titulo': 'Esta Es La Ventana De Inicio'
    }
    return render(request, 'herencia.html', context)

def aboutMe(request):
    return render(request, 'aboutme.html')
def peliCatalogo(request):
    return render(request, 'CatalogoPeliculas.html')

def serieCatalogo(request):
    return render(request, 'CatalogoSeries.html')

def productCatalogo(request):
    return render(request, 'CatalogoProductoras.html')

def Error(request):
    return render(request, 'Error404.html')

def listaActores(request):
    return render(request, 'Error404.html')

def listaGeneros(request):
    return render(request, 'Error404.html')

def aboutPage(request):
    return render(request, 'aboutPage.html')

def aboutDev(request):
    return render(request, 'aboutmedos.html')

def cambiarContraseña(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('Perfil')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'parallax.html', {'form': form})

@login_required
def perfilUsuario(request):
    if request.user.is_authenticated:
        try:
            perfil_usuario = PerfilUsuario.objects.get(usuario=request.username)
            peliculas_guardadas = perfil_usuario.peliculas_guardadas.all()
        except PerfilUsuario.DoesNotExist:
            perfil_usuario = None
            peliculas_guardadas = []

        context = {
            'username': request.user.username,
            'peliculas_guardadas': peliculas_guardadas
        }

        return render(request, 'profile.html', context)
    else:
        return render(request, 'inicio.html')

def cerrarSesion(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('Inicio')

def modificarEmail(request):
    if request.method == 'POST':
        form = ModificarEmailForm(request.POST)
        if form.is_valid():
            nuevo_email = form.cleaned_data['nuevo_email']
            user = request.user
            user.email = nuevo_email
            user.save()
            return redirect('home')
    else:
        form = ModificarEmailForm()
    
    return render(request, 'parallax.html', {'form': form})