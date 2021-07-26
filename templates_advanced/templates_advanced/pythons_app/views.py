from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import PythonCreateForm
from .models import Python

# Create your views here.
from ..core.decorators import any_group_required


# def index(req):
#     pythons = Python.objects.all()
#     return render(req, 'index.html', {'pythons': pythons})
from ..core.mixins import AnyGroupRequiredMixin, BootstrapFormMixin


class IndexView(ListView):
    template_name = 'index.html'
    model = Python
    context_object_name = 'pythons'
    paginate_by = 7


# @any_group_required(groups=['User'])
# def create(req):
#     if req.method == 'GET':
#         form = PythonCreateForm()
#         return render(req, 'create.html', {'form': form})
#     else:
#         form = PythonCreateForm(req.POST, req.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#         return render(req, 'create.html', {'form': form})

class PythonCreateView(AnyGroupRequiredMixin, CreateView):
    template_name = 'create.html'
    model = Python
    form_class = PythonCreateForm
    success_url = reverse_lazy('index')
