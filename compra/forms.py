from django.forms import ModelForm
from .models import Producto, Proveedor

class AgregarProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre','precio', 'stock_actual', 'proveedor']





class AgregarProveedorForm(ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'apellido', 'dni']
    
    