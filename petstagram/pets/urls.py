from django.urls import path

from pets.views import pet_all, pet_detail, like_pet, create, edit, delete, comment_pet

urlpatterns = [
    path('', pet_all, name='list pets'),
    path('pet-details/<int:pk>/', pet_detail, name='pet details'),
    path('like/<int:pk>/', like_pet, name='like pet'),
    path('create/', create, name='create'),
    path('edit/<int:pk>', edit, name='edit'),
    path('delete/<int:pk>', delete, name='delete'),
    path('comment/<int:pk>', comment_pet, name='comment pet'),
]