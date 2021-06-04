from django.shortcuts import render

# Create your views here.
from todo_app.models import Todo


def index(request):
    todos = Todo.objects.all()
    context = {'todos': todos}
    return render(request, 'index.html', context=context)
