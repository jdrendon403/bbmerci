from django.views import generic
from django.urls import reverse_lazy

from rest_framework.views import APIView
from rest_framework.response import Response

from .forms import ProductForm
from .models import Product
from .serializers import ProductSerializer


class ProductsFormView(generic.FormView):
    template_name= "add_product.html"
    form_class = ProductForm
    success_url= reverse_lazy("list_product")

    def form_valid(self, form):
        print("validando")
        form.save()
        return super().form_valid(form)
    
class ProductsListView(generic.ListView):
    model=Product
    template_name="list_product.html"
    context_object_name="products"

class ProductListApiView(APIView):
    authentication_classes = [] #[SessionAuthentication, BasicAuthentication]
    permission_classes = [] #[IsAuthenticated]

    def get(self, request):
        products=Product.objects.all()
        serializer=ProductSerializer(products, many=True)
        return Response(serializer.data)
