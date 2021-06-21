from django.shortcuts import render, redirect

# Create your views here.
from expenses.forms import ExpensesForm
from expenses.models import Expense
from profiles.forms import ProfileForm
from profiles.models import Profile
from profiles.views import create


def index(request):
    if request.method == 'GET':
        return create(request)
    else:
        expenses = Expense.objects.all()
        return render(request, 'home-with-profile.html', {'expenses': expenses})


def persist(request, expense, template):
    if request.method == "GET":
        return render(request, template, {'form': expense})
    else:
        form = ExpensesForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
        return render(request, template, {'form': expense})


def create_exp(request):
    exp = ExpensesForm()
    return persist(request, exp, 'expense-create.html')


def edit_exp(request, pk):
    exp = Expense.objects.get(pk=pk)
    return persist(request, exp, 'expense-edit.html')


def delete_exp(request, pk):
    exp = Expense.objects.get(pk=pk)
    if request.method == "GET":
        return render(request, 'expense-delete.html', {'form': exp})
    else:
        exp.delete()
        return index(request)
