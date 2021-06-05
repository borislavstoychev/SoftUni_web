from django.shortcuts import render, redirect

# Create your views here.
from todo_app.models import Todo, Person


def index(request):
    todos = Todo.objects.all()
    context = {'todos': todos}
    return render(request, 'index.html', context=context)


def create_todo(request):
    text = request.POST['text']
    description = request.POST['description']
    owner_name = request.POST['owner']
    owner = Person.objects.filter(name=owner_name).first()
    if not owner:
        owner = Person(name=owner_name)
        owner.save()
    todo = Todo(
        title=text,
        description=description,
        owner=owner,
    )
    todo.save()
    return redirect('/')


def dell_todo(request):
    text = request.POST['text']
    description = request.POST['description']
    owner_name = request.POST['owner']
    owner = Person.objects.filter(name=owner_name).first()
    todo = Todo.objects.filter(title=text).first()
    if owner and todo:
        todo.delete()
    return redirect('/')


def change_todo_state(req, pk):
    todo = Todo.objects.get(pk=pk)
    todo.is_done = not todo.is_done
    todo.save()
    return redirect('/')
