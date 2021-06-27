from django.shortcuts import render, redirect

# Create your views here.
from notes.note.forms import NoteForm
from notes.note.models import Note
from notes.profiles.models import Profile
from notes.profiles.views import creat_profile


def index(request):
    if Profile.objects.exists():
        notes = Note.objects.all()
        return render(request, 'home-with-profile.html', {'notes': notes})
    return creat_profile(request)


def persist(request, note, template):
    if request.method == "GET":
        content = {
            'profile': Profile.objects.first(),
            'note': NoteForm(instance=note)
        }
        return render(request, template, content)
    new_note = NoteForm(request.POST, instance=note)
    if new_note.is_valid():
        new_note.save()
        return redirect('home page')
    return render(request, template, {'note': new_note})


def add_note(request):
    note = Note()
    return persist(request, note, 'note-create.html')


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    return persist(request, note, 'note-edit.html')


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == "GET":
        form = NoteForm(instance=note)
        for _, field in form.fields.items():
            field.widget.attrs['disabled'] = True
        return render(request, 'note-delete.html', {'form': form})
    note.delete()
    return redirect('home page')


def details(request, pk):
    note = Note.objects.get(pk=pk)
    return render(request, 'note-details.html', {'note': note})

