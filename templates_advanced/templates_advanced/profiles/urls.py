from django.urls import path

from templates_advanced.profiles.views import profile_details, ProfileUpdateView

urlpatterns = (
    path('<int:pk>/', ProfileUpdateView.as_view(), name='profile details'),
)

import templates_advanced.profiles.signals