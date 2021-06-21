from django.urls import path, include

from profiles.views import profile, create, edit, delete

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('create/', create, name='create'),
    path('edit/<int:pk>/', edit, name='edit'),
    path("delete/<int:pk>", delete, name='delete')
]