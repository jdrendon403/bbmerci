from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.views import generic
from django.urls import reverse_lazy

class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = "register.html"
    success_url = reverse_lazy("login")

class ProfileView(generic.CreateView):
    form_class = UserChangeForm
    template_name = "profile.html"
    success_url = reverse_lazy("list_product")