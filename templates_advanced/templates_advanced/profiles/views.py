from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from templates_advanced.profiles.forms import ProfileForm
from templates_advanced.profiles.models import Profile


@login_required
def profile_details(request):
    profile = Profile.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile
    }

    return render(request, 'profiles/details.html', context)