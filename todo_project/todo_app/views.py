from django.forms import CharField, Textarea
from django.shortcuts import render, redirect

# Create your views here.
from todo_app.forms import TodoForm, FormName, StateFilterForm
from todo_app.models import Todo, Person
from todo_app.services import TodosService


def index(request):
    filter_form = StateFilterForm(request.GET)
    filter_form.is_valid()
    state = filter_form.cleaned_data['state']
    service = TodosService(state)

    context = {
        'filter_form': filter_form,
        'todos': service.get_by_state(),
    }

    return render(request, 'index.html', context)


def edit_task(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == 'GET':
        form = TodoForm(initial={"title": todo.title, "description": todo.description, "owner": todo.owner.name})
        return render(request, "todo_app/edit.html", {'form': form})
    else:
        form = TodoForm(request.POST)
        if form.is_valid():
            todo.title = form.cleaned_data['title']
            todo.description = form.cleaned_data['description']
            owner_name = form.cleaned_data['owner']
            owner = Person.objects.filter(name=owner_name).first()
            if not owner:
                owner = Person(name=owner_name)
                owner.save()
            todo.owner = owner
            todo.save()
            return redirect('/')
        return render(request, "todo_app/edit.html", {'form': form})


def create_todo(request):
    if request.method == "GET":
        return render(request, 'todo_app/create.html', {'form': TodoForm()})
    else:
        form = TodoForm(request.POST)
        if form.is_valid():
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
        return render(request, 'todo_app/create.html', {'form': form})


# def persist(req, todo, template_name):
#     if req.method == "GET":
#         form = TodoForm(initial={"title": todo.title, "description": todo.description, "owner": todo.owner.name})
#         return render(req, f'todo_app/{template_name}.html', {'form': form})
#     form = TodoForm(req.POST)
#     if form.is_valid():
#         todo.text = form.cleaned_data['title']
#         todo.description = form.cleaned_data['description']
#         owner_name = form.cleaned_data['owner']
#         owner = Person.objects.filter(name=owner_name).first()
#         if not owner:
#             owner = Person(name=owner_name)
#             owner.save()
#         todo.owner = owner
#         todo.save()
#         return redirect('/')
#     return render(req, f'todo_app/{template_name}.html', {'form': form})
#
#
# def create_todo(request):
#     return persist(request, TodoForm(), 'create')
#
#
# def edit_task(request, pk):
#     return persist(request, Todo.objects.get(pk=pk), 'edit')


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
