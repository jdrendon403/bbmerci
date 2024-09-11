from django.db import models


class Product(models.Model):
    product = models.TextField(
        verbose_name="Product",
        max_length=50,
    )
    description = models.TextField(
        verbose_name="Descripción del Producto",
        max_length=300,
    )
    price = models.FloatField(
        verbose_name="Precio",
    )
    available = models.BooleanField(
        verbose_name="Disponible",
        default=True,
    )
    image = models.ImageField(
        verbose_name="Foto",
        upload_to="imgs",
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.product
    
