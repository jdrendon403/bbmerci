from django.views.generic import DetailView
from .models import OrderModel

class MyOrderView(DetailView):
    model = OrderModel
    template_name = "my_order.html"
    context_object_name = "my_order"

    def get_object(self, queryset=None):
        return OrderModel.objects.filter(is_active=True).first()