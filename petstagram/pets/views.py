from django.shortcuts import render, redirect

# Create your views here.
from pets.models import Pet, Like


def pet_all(request):
    context = {
        'pets': Pet.objects.all()
    }
    return render(request, "pets/pet_list.html", context)


def pet_detail(request, pk):
    pet = Pet.objects.get(pk=pk)
    pet.likes_count = pet.like_set.count()
    context = {
        'pet': pet,
    }
    return render(request, 'pets/pet_detail.html', context)


def like_pet(request, pk):

    pet = Pet.objects.get(pk=pk)
    like = Like(pet=pet)
    like.pet = pet
    like.save()
    return redirect('pet details', pk)
