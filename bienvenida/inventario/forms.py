from django import forms
from .models import Producto

class ProductoForm(forms.ModelsForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'descripcion', 'stock']
