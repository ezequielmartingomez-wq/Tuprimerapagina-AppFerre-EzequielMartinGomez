from django.db import models

# Create your models here.


class Categoria(models.Model):
    categoria = models.CharField(max_length=50)
    subcategoria = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.categoria} ({self.subcategoria})"


class Producto(models.Model):
    producto = models.CharField(max_length=50)
    detalle = models.CharField(max_length=50)
    precio = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.detalle}, {self.producto}"


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.apellido}, {self.nombre}"


class Venta(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.nombre
