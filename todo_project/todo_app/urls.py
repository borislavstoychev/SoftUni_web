from django.urls import path

from todo_app import views
from todo_app.views import create_todo, dell_todo, change_todo_state

urlpatterns = [
    path('', views.index),
    path('todos-add/', create_todo),
    path('todos-dell/', dell_todo),
    path('todo-change-state/<int:pk>', change_todo_state)
]