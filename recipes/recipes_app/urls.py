from django.urls import path

from recipes_app.views import index, edit_recipes, delete_recipes, details_recipes, create_recipes

urlpatterns = [
    path('', index, name='home page'),
    path('create/', create_recipes, name='create recipe page'),
    path('edit/<int:pk>', edit_recipes, name='edit recipe page'),
    path('delete/<int:pk>', delete_recipes, name='delete recipe page'),
    path('details/<int:pk>', details_recipes, name='recipe details page'),
]