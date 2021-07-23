from django.contrib.auth import logout, login, get_user_model
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView

from templates_advanced import settings
from templates_advanced.pythons_auth.forms import SignUpForm, SignInForm


UserModel = get_user_model()


# def sign_up(request):
#     if request.POST:
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('index')
#
#     else:
#         form = SignUpForm()
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'auth/sign-up.html', context)


class SignUpView(CreateView):
    template_name = 'auth/sign-up.html'
    model = UserModel
    form_class = SignUpForm
    success_url = reverse_lazy('index')


# def sign_in(request):
#     if request.method == 'POST':
#         form = SignInForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('index')
#     form = SignInForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'auth/sign-in.html', context)

# user = authenticate(request, username='Bobby', password='bobby900729')
    # if user:
    #     login(request, user)
    #     return redirect('index')

class SignInView(LoginView):
    template_name = 'auth/sign-in.html'
    form_class = SignInForm

    def get_success_url(self):
        return reverse('index')


# def logout_view(request):
#     logout(request)
#     return redirect('index')

class SignOutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)



