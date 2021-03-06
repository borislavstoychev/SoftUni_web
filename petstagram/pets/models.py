from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
UserModel = get_user_model()


class Pet(models.Model):
    DOG = 'dog'
    CAT = 'cat'
    PARROT = 'parrot'
    UNKNOWN = 'unknown'
    PET_TYPE = (
        (DOG, "Dog"),
        (CAT, 'Cat'),
        (PARROT, 'Parrot'),
        (UNKNOWN, 'Unknown'),
    )
    type = models.CharField(max_length=7, choices=PET_TYPE, default=UNKNOWN)
    name = models.CharField(max_length=7)
    age = models.PositiveIntegerField(blank=False)
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to='images/pets')
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.type} {self.name}, Age: {self.age}"


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

from .signals import *


