from django.contrib import admin
from .models import OrderModel, OrderProductModel

class OrderProductInLineAdmin(admin.TabularInline):
    model=OrderProductModel
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    model=OrderModel
    list_display=["id", "user", "creation_date", "update_date", "is_active"]
    search_fields=["user", "is_active"]
    inlines=[OrderProductInLineAdmin]

admin.site.register(OrderModel, OrderAdmin)
