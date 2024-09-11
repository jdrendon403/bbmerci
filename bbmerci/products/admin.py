from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    model=Product
    list_display=["product", "price"]
    search_fields=["product", "price", "description"]

admin.site.register(Product, ProductAdmin)