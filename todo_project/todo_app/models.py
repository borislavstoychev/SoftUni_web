from django.db import models


# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'Person: {self.name}'

    class Meta:
        verbose_name_plural = 'people'


class Category(models.Model):
    HOME_CHOICE = 'Home'
    WORK_CHOICE = 'Work stuff'
    NAME_CHOICES = (
        (HOME_CHOICE, 'Home stuff'),
        (WORK_CHOICE, 'Work stuff')
    )

    name = models.CharField(max_length=20, choices=NAME_CHOICES)

    class Meta:
        verbose_name_plural = 'categories'


class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    is_done = models.BooleanField(default=False)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, )
    categories = models.ManyToManyField(Category)
    stat_date = models.DateField(auto_now=True)
