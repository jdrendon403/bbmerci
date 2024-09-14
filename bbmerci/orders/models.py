from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class OrderModel(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    is_active=models.BooleanField(verbose_name="Activa", default=True)
    creation_date=models.DateTimeField(verbose_name="Creacion", auto_now_add=True)
    update_date=models.DateTimeField(verbose_name="Ultima Actualizacion", auto_now=True)

    def __str__(self) -> str:
        return f"order {self.id} by {self.user.username}"
    
class OrderProductModel(models.Model):
    order=models.ForeignKey(OrderModel, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity=models.IntegerField(verbose_name="Cantidad", default=1)
    
    def __str__(self) -> str:
        return f"{self.quantity} of {self.product} from order {self.order}"
    