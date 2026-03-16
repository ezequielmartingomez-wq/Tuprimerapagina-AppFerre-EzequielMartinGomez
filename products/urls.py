from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("probando/", views.probando_template, name="probando"),
    path("categorias/", views.categoria, name="categorias"),
    path("CategoriaFormulario/", views.categoriaFormulario, name="CategoriaFormulario"),
    path("buscarCategoria", views.buscarCategoria, name="buscarCategoria"),
    path("productoFormulario/", views.productoFormulario, name="productoFormulario"),
    path("clienteFormulario/", views.clienteFormulario, name="clienteFormulario"),
]
