from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.
from accounts.forms import SignUpForm, SignInForm, ProfileForm
from accounts.models import Profile
from pets.models import Pet


def sign_up(request):
    if request.POST:
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('landing')

    else:
        form = SignUpForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/signup.html', context)


def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('landing')
    form = SignInForm()
    context = {
        'form': form,
    }
    return render(request, 'registration/sign_in.html', context)


def sign_out(request):
    logout(request)
    return redirect('landing')


@login_required(login_url='sign in user')
def profile_details(request):
    profile = Profile.objects.get(pk=request.user.id)
    user_pets = Pet.objects.filter(user_id=request.user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('landing')
    else:
        form = ProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
        'pets': user_pets,
    }

    return render(request, 'accounts/user_profile.html', context)