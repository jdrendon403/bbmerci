from django.forms import ModelForm
from .models import OrderProductModel

class AddProductForm(ModelForm):
    class Meta:
        model = OrderProductModel
        fields = ["product"]