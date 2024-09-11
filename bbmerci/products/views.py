from django.views import generic
from django.urls import reverse_lazy

from .forms import ProductForm
from .models import Product


class ProductsFormView(generic.FormView):
    template_name= "add_product.html"
    form_class = ProductForm
    success_url= reverse_lazy("add_product")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class ProductsListView(generic.ListView):
    model=Product
    template_name="list_product.html"
    context_object_name="products"
    
