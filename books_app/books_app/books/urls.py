from django.urls import path
from books_app.books.views import index, edit, create

urlpatterns = [
    path('', index, name='main'),
    path('edit/<int:pk>', edit, name='edit_book'),
    path('creat/', create, name='creat_book')
]
