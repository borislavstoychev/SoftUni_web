from django.urls import path

from todo_app import views
from todo_app.views import create_todo, dell_todo, change_todo_state, edit_task, index, log_in

urlpatterns = [
    path('', index, name='main'),
    path('creat-task', create_todo, name='creat task'),
    path('edit/<int:pk>', edit_task, name='edit task'),
    path('todos-dell/<int:pk>', dell_todo),
    path('todo-change-state/<int:pk>', change_todo_state),
    path('create/', create_todo, name='create_todo'),
    path('delete/<int:pk>', dell_todo, name='delete_todo'),
    path('update/<int:pk>', edit_task, name='update_todo'),
    path('login/', log_in, name='login')

]