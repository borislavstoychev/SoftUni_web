from django.urls import path

from todo_app import views
from todo_app.views import create_todo, dell_todo, change_todo_state, edit_task, index

urlpatterns = [
    path('', index, name='main'),
    path('creat-task', create_todo, name='creat task'),
    path('edit/<int:pk>', edit_task, name='edit task'),
    path('todos-dell/<int:pk>', dell_todo),
    path('todo-change-state/<int:pk>', change_todo_state),

]