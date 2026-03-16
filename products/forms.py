# --- UNIDAD 11 - CODE ---
# Formularios en Django - Unidad 11: Playground Intermedio Parte II

from django import forms
from .models import Categoria, Producto, Cliente  # ← asegurate de tener Producto y Cliente

class CategoriaFormulario(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['categoria', 'subcategoria']
        labels = {
            'categoria': 'Nombre de la categoria',
            'subcategoria': 'Subcategoria'
        }

class BusquedaCategoriaFormulario(forms.Form):
    subcategoria = forms.CharField(max_length=50, label="Subcategoria", widget=forms.TextInput())

class ProductoFormulario(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['producto', 'detalle', 'precio']
        labels = {
            'producto': 'Nombre del producto',
            'detalle': 'Detalle',
            'precio': 'Precio'
        }

class ClienteFormulario(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'email', 'profesion']
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'email': 'Email',
            'profesion': 'Profesión'
        }
        