from django import forms
from .models import Product

class ProductForm(forms.Form):
    product = forms.CharField(
        label="Nombre del Producto",
        max_length=50,
    )
    description = forms.CharField(
        label="Descripción del Producto",
        max_length=300,
    )
    price = forms.FloatField(
        label="Precio",
        min_value=100.0,
    )
    available = forms.BooleanField(
        label="Disponible",
        required=False,
        initial=True,
    )
    image = forms.ImageField(
        label="Foto",
        required=False,
    )

    def save(self):
        print("saving")
        Product.objects.create(
            product = self.cleaned_data["product"],
            description = self.cleaned_data["description"],
            price = self.cleaned_data["price"],
            available = self.cleaned_data["available"],
            image  = self.cleaned_data["image"],
        )
