from django.forms import BaseModelForm
from django.http import HttpResponse
from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import OrderModel, OrderProductModel
from .forms import AddProductForm

class MyOrderView(LoginRequiredMixin, DetailView):
    model = OrderModel
    template_name = "my_order.html"
    context_object_name = "my_order"

    def get_object(self, queryset=None):
        return OrderModel.objects.filter(is_active=True, user=self.request.user).first()
    
class AddToOrderView(LoginRequiredMixin, CreateView):
    template_name = "add_to_order.html"
    form_class = AddProductForm
    success_url = reverse_lazy("my_order")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        order, _ = OrderModel.objects.get_or_create(is_active=True, user=self.request.user)
        form.instance.order = order
        form.instance.quantity = 1
        form.save()
        return super().form_valid(form)