from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField()
    
    
    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}."


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    stock_actual = models.PositiveIntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        
    def __str__(self):
        return f'{self.nombre} ({self.stock_actual})'