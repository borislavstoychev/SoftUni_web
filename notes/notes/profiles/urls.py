from django.urls import path

from notes.profiles.views import profile_index, delete_profile

urlpatterns = [
    path('profile/', profile_index, name='profile page'),
    path('prfile/delete/<int:pk>', delete_profile, name='delete profile')
]