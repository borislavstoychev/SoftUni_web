from django.shortcuts import render, redirect

# Create your views here.
from profiles.forms import ProfileForm
from profiles.models import Profile


def profile(request):
    prof = Profile.objects.first()
    return render(request, 'profile.html', {'profile': prof})


def persist(request, prof, template):
    if request.method == "GET":
        return render(request, template, {'form': ProfileForm(instance=prof)})
    else:
        form = ProfileForm(request.POST, instance=prof)
        if form.is_valid():
            form.save()
            return profile(request)
        return render(request, template, {'form': form})


def create(request):
    prof = Profile()
    return persist(request, prof, 'home-no-profile.html')


def edit(request, pk):
    prof = Profile.objects.get(pk=pk)
    return persist(request, prof, 'profile-edit.html')


def delete(request, pk):
    exp = Profile.objects.get(pk=pk)
    if request.method == "GET":
        prof = Profile.objects.get(pk=pk)
        return render(request, 'profile-delete.html', {'profile': prof})
    else:
        exp.delete()
        return redirect('home')
