from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .models import TestModel
from .forms import TestModelForm

class TestModelListView(ListView):
    model = TestModel
    template_name = 'test_model_list.html'  # Update with your template name
    context_object_name = 'test_models'

class TestModelCreateView(CreateView):
    model = TestModel
    form_class = TestModelForm
    template_name = 'test_model_form.html'  # Update with your template name

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class TestModelUpdateView(UpdateView):
    model = TestModel
    form_class = TestModelForm
    template_name = 'test_model_form.html'  # Update with your template name

class TestModelDetailView(DetailView):
    model = TestModel
    template_name = 'test_model_detail.html'  # Update with your template name
    context_object_name = 'test_model'
