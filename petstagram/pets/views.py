from django.shortcuts import render, redirect

# Create your views here.
from common.forms import CommentForm
from common.models import Comment
from pets.forms import PetCreateForm
from pets.models import Pet, Like


def pet_all(request):
    context = {
        'pets': Pet.objects.all(),
    }
    return render(request, "pet_list.html", context)


def pet_detail(request, pk):
    pet = Pet.objects.get(pk=pk)
    pet.likes_count = pet.like_set.count()
    if request.method == "GET":
        context = {
            'pet': pet,
            'comment_form': CommentForm(),
        }
        return render(request, 'pet_detail.html', context)
    else:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = Comment(comment=comment_form.cleaned_data['comment'])
            comment.pet = pet
            comment.save()
            return redirect("pet details", pk)

        context = {
            'pet': pet,
            'comment_form': CommentForm(),
        }
        return render(request, 'pet_detail.html', context)


def like_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    like = Like(pet=pet)
    like.pet = pet
    like.save()
    return redirect('pet details', pk)


def persist(request, pet, template):
    if request.method == "GET":
        form = PetCreateForm(instance=pet)
        return render(request, template, {'form': form})
    else:
        form = PetCreateForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet details', pet.pk)

        return render(request, template, {'form': form})


def create(request):
    pet = Pet()
    return persist(request, pet, 'pet_create.html')


def edit(request, pk):
    pet = Pet.objects.get(pk=pk)
    return persist(request, pet, 'pet_edit.html')


def delete(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == "GET":
        return render(request, 'pet_delete.html', {'pet': pet})
    else:
        pet.delete()
        return redirect('list pets')
