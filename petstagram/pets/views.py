from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from common.forms import CommentForm
from pets.forms import PetCreateForm, EditPetForm
from pets.models import Pet, Like



def pet_all(request):
    context = {
        'pets': Pet.objects.all(),
    }
    return render(request, "pet_list.html", context)


def pet_detail(request, pk):
    pet = Pet.objects.get(pk=pk)
    pet.likes_count = pet.like_set.count()
    is_owner = pet.user == request.user
    is_liked_by_user = pet.like_set.filter(user_id=request.user.id).exists()
    context = {
        'pet': pet,
        'comment_form': CommentForm(
            initial={
                'pet_pk': pk,
            }),
        'comments': pet.comment_set.all(),
        'is_owner': is_owner,
        'is_liked': is_liked_by_user,
    }

    return render(request, 'pet_detail.html', context)


@login_required
def comment_pet(request, pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.save()

    return redirect('pet details', pk)


def like_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    like_object_by_user = pet.like_set.filter(user_id=request.user.id) \
        .first()
    if like_object_by_user:
        like_object_by_user.delete()
    else:
        like = Like(pet=pet, user=request.user)
        like.pet = pet
        like.save()
    return redirect('pet details', pk)


def persist(request, pet, template, form=None):
    if request.method == "GET":
        form = PetCreateForm(instance=pet)
        return render(request, template, {'form': form})
    else:
        if not form:
            form = PetCreateForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()
            return redirect('pet details', pet.pk)

        return render(request, template, {'form': form})


@login_required
def create(request):
    pet = Pet()
    return persist(request, pet, 'pet_create.html')


def edit(request, pk):
    pet = Pet.objects.get(pk=pk)
    form = EditPetForm(request.POST, request.FILES, instance=pet)
    return persist(request, pet, 'pet_edit.html')


def delete(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == "GET":
        return render(request, 'pet_delete.html', {'pet': pet})
    else:
        pet.delete()
        return redirect('list pets')
