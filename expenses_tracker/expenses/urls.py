from django.urls import path, include

from expenses.views import index, create_exp, edit_exp, delete_exp

urlpatterns = [
    path("", index, name='home'),
    path('create/', create_exp, name='create expenses page'),
    path('edit/<int:pk>/', edit_exp, name='edit expense page'),
    path('delete/<int:pk>/', delete_exp, name='delete expense page'),

]


