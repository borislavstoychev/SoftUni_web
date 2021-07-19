from django.contrib.auth import logout, login
from django.shortcuts import render, redirect


# Create your views here.
from templates_advanced.pythons_auth.forms import SignUpForm, SignInForm


def sign_up(request):
    if request.POST:
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign in')

    else:
        form = SignUpForm()

    context = {
        'form': form,
    }

    return render(request, 'auth/sign-up.html', context)


def login_view(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    form = SignInForm()
    context = {
        'form': form,
    }
    return render(request, 'auth/sign-in.html', context)

# user = authenticate(request, username='Bobby', password='bobby900729')
    # if user:
    #     login(request, user)
    #     return redirect('index')


def logout_view(request):
    logout(request)
    return redirect('index')

