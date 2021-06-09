from django.forms import CharField, Textarea
from django.shortcuts import render, redirect

# Create your views here.
from todo_app.forms import TodoForm, FormName
from todo_app.models import Todo, Person


def index(request, form=None, form_action='create task', pk=None):
    if not form:
        form = TodoForm()
    context = {
        'todos': Todo.objects.all().order_by('is_done'),
        'todo_form': form,
        'form_action': form_action,
        'pk': pk,
    }

    return render(request, 'todo_app/index.html', context)


def edit_task(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == 'GET':
        form = TodoForm(initial=todo.__dict__)
        return render(request, "todo_app/edit.html", {'form': form})
    else:
        form = TodoForm(request.POST)
        if not form.is_valid():
            render(request, "todo_app/edit.html", {'form': form})
        todo.text = form.cleaned_data['title']
        todo.description = form.cleaned_data['description']
        owner_name = form.cleaned_data['owner']
        owner = Person.objects.filter(name=owner_name).first()
        if not owner:
            owner = Person(name=owner_name)
            owner.save()
        todo.owner = owner
        todo.save()
        return render(request, 'todo_app/create.html', {"form": form})


def create_todo(request):
    form = TodoForm(request.POST)
    if not form.is_valid():
        form = TodoForm(field_order=[CharField(), CharField(widget=Textarea), CharField(max_length=100)])
        return render(request, 'todo_app/create.html', {'form': form})
    text = form.cleaned_data['title']
    description = form.cleaned_data['description']
    owner_name = form.cleaned_data['owner']
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
    return redirect("/")


def log_in(request):
    form = FormName(request.POST)
    if not form.is_valid():
        return render(request, 'todo_app/create.html', {"form": form})
    name = form.cleaned_data['name']
    age = form.cleaned_data['age']
    email = form.cleaned_data['email']
    password = form.cleaned_data['password']
    tex = form.cleaned_data['text']
    bot_catcher = form.cleaned_data['bot_catcher']

    return render(request, 'todo_app/login.html', {'form': form})


def dell_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('/')


def change_todo_state(req, pk):
    todo = Todo.objects.get(pk=pk)
    todo.is_done = not todo.is_done
    todo.save()
    return redirect('/')