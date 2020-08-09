from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from model_market.models import PreModel, Task, Framework
from premarket.views import OwnerOnlyMixin


# # Create your views here.
# class TaskListView(ListView):
#     model = Task

# class FrameWorkListView(ListView):
#     model = Framework

# class TaskFrameWorkView(ListView):
#     model = Task

# class TaskTemplateView(TemplateView):
#     template_name = "model_market/task_list.html"

# class FrameworkTemplateView(TemplateView):
#     template_name = "model_market/framework_list.html"

class IndexListView(ListView):
    model = PreModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = PreModel.objects.all()
        return context

class TaskDetailView(DetailView):
    model = Task

class FrameWorkDetailView(DetailView):
    model = Framework

class ModelDetailView(DetailView):
    model = PreModel

class ModelCreateView(LoginRequiredMixin, CreateView):
    model = PreModel
    fields = ['task', 'title', 'description', 'price', 'framework', 'model_file']
    success_url = reverse_lazy('mm:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['objects'] = PreModel.objects.all()
        return context
    
    def form_valid(self, form): 
        form.instance.owner = self.request.user 
        return super().form_valid(form) 

class ModelChangeView(LoginRequiredMixin, ListView):
    template_name = 'model_market/premodel_change_list.html'

    def get_queryset(self):
        return PreModel.objects.filter(owner=self.request.user)

class ModelUpdateView(OwnerOnlyMixin, UpdateView):
    model = PreModel
    fields = ['task', 'title', 'description', 'price', 'framework', 'model_file']
    success_url = reverse_lazy('mm:index')

class ModelDeleteView(OwnerOnlyMixin, DeleteView):
    model = PreModel
    success_url = reverse_lazy('mm:index')