
from django.urls import path
from accounts.views import sign_in, sign_out, sign_up, profile_details

urlpatterns = (
    path('sign-in/', sign_in, name='sign in user'),
    path('sign-out/', sign_out, name='sign out user'),
    path('sign-up/', sign_up, name='sign up user'),
    path('profile/', profile_details, name='profile details'),
)