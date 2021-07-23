
from django.urls import path

from templates_advanced.pythons_auth import views

urlpatterns = (
    path('sign-up/', views.SignUpView.as_view(), name='sign up'),
    path('sign-in/', views.SignInView.as_view(), name='sign in'),
    path('sign-out/', views.SignOutView.as_view(), name='sign out'),
)