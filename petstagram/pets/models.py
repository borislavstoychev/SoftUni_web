from django.db import models


# Create your models here.

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
    image_url = models.URLField(blank=False)

    def __str__(self):
        return f"{self.type} {self.name}, Age: {self.age}"


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

