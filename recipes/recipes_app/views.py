from django.shortcuts import render, redirect

# Create your views here.
from recipes_app.forms import RecipeForm
from recipes_app.models import Recipe


def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {"recipes": recipes})


def persist(request, recipe, template):
    if request.method == "GET":
        return render(request, template, {'form': RecipeForm(instance=recipe), 'recipe': recipe})
    else:
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return index(request)
        return render(request, template, {'form': form})


def create_recipes(request):
    recipe = Recipe()
    return persist(request, recipe, 'create.html')


def edit_recipes(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    return persist(request, recipe, 'edit.html')


def delete_recipes(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', {'form': RecipeForm(instance=recipe), 'recipe': recipe})
    recipe.delete()
    return redirect("home page")


def details_recipes(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients = recipe.ingredients.split(",")
    return render(request, 'details.html', {'recipe': recipe, 'ingredients': ingredients})

