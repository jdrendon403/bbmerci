from django.urls import path
from .views import MyOrderView, AddToOrderView

urlpatterns = [
    path('my_order', MyOrderView.as_view(), name="my_order"),
    path('add_to_order', AddToOrderView.as_view(), name="add_to_order"),
]