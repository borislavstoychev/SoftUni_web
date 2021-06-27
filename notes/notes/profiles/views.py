from django.shortcuts import render, redirect

# Create your views here.
from notes.note.models import Note
from notes.profiles.forms import ProfileForm
from notes.profiles.models import Profile


def profile_index(request):
    profile = Profile.objects.first()
    count = len(Note.objects.all())
    return render(request, 'profile.html', {'profile': profile, 'count': count})


def creat_profile(request):
    if request.method == "GET":
        profile = Profile()
        return render(request, 'home-no-profile.html', {'form': ProfileForm(instance=profile), 'profile': profile})
    new_profile = ProfileForm(request.POST)
    if new_profile.is_valid():
        new_profile.save()
        return redirect('profile page')
    return render(request, 'home-no-profile.html', {'form': new_profile})


def delete_profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    profile.delete()
    Note.objects.all().delete()
    return redirect('home page')
