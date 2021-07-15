from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import PythonCreateForm
from .models import Python

# Create your views here.
from ..core.decorators import any_group_required


def index(req):
    pythons = Python.objects.all()
    return render(req, 'index.html', {'pythons': pythons})


def login_view(request):
    user = authenticate(request, username='Bobby', password='bobby900729')
    if user:
        login(request, user)
        return redirect('index')


def logout_view(request):
    logout(request)
    return redirect('index')


@any_group_required(groups=['User'])
def create(req):
    if req.method == 'GET':
        form = PythonCreateForm()
        return render(req, 'create.html', {'form': form})
    else:
        form = PythonCreateForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(req, 'create.html', {'form': form})
