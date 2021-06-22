from django.shortcuts import render, redirect

# Create your views here.
from expenses.forms import ExpensesForm
from expenses.models import Expense
from profiles.models import Profile
from profiles.views import create


# def index(request):
#     if request.method == 'GET':
#         return create(request)
#     else:
#         expenses = Expense.objects.all()
#         return render(request, 'home-with-profile.html', {'expenses': expenses})

def calculate_budget(profile, expenses):
    expenses_cost = sum(expense.price for expense in expenses)
    return profile.budget - expenses_cost


def index(request):
    if Profile.objects.exists():
        profile = Profile.objects.first()
        expenses = Expense.objects.all()

        profile.budget_left = calculate_budget(profile, expenses)

        context = {
            'profile': profile,
            'expenses': expenses,
        }
        return render(request, 'home-with-profile.html', context)
    else:
        return create(request)


def persist(request, expense, template):
    if request.method == "GET":
        return render(request, template, {'form': ExpensesForm(instance=expense)})
    else:
        form = ExpensesForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return index(request)
        return render(request, template, {'form': expense})


def create_exp(request):
    exp = Expense()
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
