from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, FormView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.mixins import AccessMixin
from premarket.forms import RegisterForm
from model_market.models import PreModel

#--- Homepage
class HomeView(TemplateView):
    model = PreModel

# Create your views here.
class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'

class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    permission_denied_message = "Owner only can update/delete the object"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user != self.object.owner:
            self.handle_no_permission()
        return super().get(request, *args, **kwargs)