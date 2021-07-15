from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('sign-out/', views.logout_view, name="sign out"),
    path('log-in/', views.login_view, name="sign in"),
]
