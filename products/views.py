from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Categoria
from .forms import CategoriaFormulario, BusquedaCategoriaFormulario, ProductoFormulario, ClienteFormulario


# * Ejemplo de CARGA DE TEMPLATE MANUAL
def inicio(request):
    template = loader.get_template("products/inicio.html")
    return HttpResponse(template.render())


def probando_template(request):
    contexto = {
        "nom": "Juan",
        "ap": "Perez",
        "notas": [10, 7, 3, 9],
    }
    return render(request, "products/probando.html", contexto)


def categoria(request):
    categoria = Categoria.objects.all()
    contexto = {"categorias": categoria}
    return render(request, "products/categorias.html", contexto)


def categoriaFormulario(request):
    form = CategoriaFormulario(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return render(request, "products/categorias_exito.html")
    else:
        form = CategoriaFormulario(initial={})
    return render(request, "products/categorias_formulario.html", {"form": form})


def buscarCategoria(request):
    if request.method == "GET":
        form = BusquedaCategoriaFormulario(request.GET)
        if form.is_valid():
            subcategoria= form.cleaned_data["subcategoria"]
            resultados = Categoria.objects.filter(subcategoria=subcategoria)
            return render(
                request,
                "products/resultados_busqueda.html",
                {"resultados": resultados, "form": form},
            )
    else:
        form = BusquedaCategoriaFormulario()
    return render(request, "products/buscar_categoria.html", {"form": form})

def productoFormulario(request):
    form = ProductoFormulario(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return render(request, "products/producto_exito.html")
    return render(request, "products/producto_formulario.html", {"form": form})

def clienteFormulario(request):
    form = ClienteFormulario(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return render(request, "products/cliente_exito.html")
    return render(request, "products/cliente_formulario.html", {"form": form})
