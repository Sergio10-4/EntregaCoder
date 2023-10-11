from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Actor, Productora, Pelicula, Serie, Tag, UserRegistration, CustomUser
from django.contrib.auth.forms import AuthenticationForm

class UsuarioForm(forms.Form):
    
    class Meta:
        model = CustomUser
        fields = ['fotoPerfil', 'descripcionUsuario']

class ProductoraForm(forms.ModelForm):
    class Meta:
        model = Productora
        fields = ['nombre', 'fundacion', 'presupuesto']

class PeliculaForm(forms.ModelForm):

    class Meta:
        model = Pelicula
        fields = ['nombre', 'duracion', 'recaudacion', 'rating', 'descripcion', 'portada', 'productoraCinematografica']

class SerieForm(forms.ModelForm):
    class Meta:
        model = Serie
        fields = ['nombre', 'cantidad_temporadas', 'fecha_estreno', 'rating', 'descripcion', 'portada', 'productoraCinematografica']

class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ['nombre', 'avatar']

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['nombre']

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = ['user', 'email', 'password', 'agree_terms']
        widgets = {
            'password': forms.PasswordInput(),
        }

class LoginForm(AuthenticationForm):
    pass

class ModificarEmailForm(forms.Form):
    nuevo_email = forms.EmailField(label='Nuevo correo electrónico')


class AgregarPeliculaForm(forms.Form):
    pelicula_nombre = forms.ModelChoiceField(queryset=Pelicula.objects.all(), empty_label=None)