from django import forms
from .models import Productora, Pelicula, Serie

class ProductoraForm(forms.ModelForm):
    class Meta:
        model = Productora
        fields = ['nombre', 'fundacion', 'presupuesto']

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['nombre', 'duracion', 'recaudacion', 'productoraCinematografica']

class SerieForm(forms.ModelForm):
    class Meta:
        model = Serie
        fields = ['nombre', 'cantidad_temporadas', 'fecha_estreno', 'productoraCinematografica']