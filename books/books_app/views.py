from django.shortcuts import render, redirect

from books_app.forms import FormBook
from books_app.models import Book


def index(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'index.html', context)


def persist(request, book, template_name):
    if request.method == "GET":
        form = FormBook(instance=book)
        return render(request, f'{template_name}.html', {'form': form})
    else:
        form = FormBook(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('main')
        return render(request, f'{template_name}.html', {'form': form})


def create(request):
    return persist(request, Book(), 'create')


def edit(request, pk):
    return persist(request, Book.objects.get(pk=pk), 'edit')

