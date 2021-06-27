from django.urls import path

from notes.note.views import index, add_note, edit_note, delete_note, details

urlpatterns = [
    path('', index, name='home page'),
    path('add/', add_note, name='add note page'),
    path('edit/<int:pk>', edit_note, name='edit note page'),
    path('delete/<int:pk>', delete_note, name='delete note page'),
    path('details/<int:pk>', details, name='note details page'),
]