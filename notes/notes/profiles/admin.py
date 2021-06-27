from django.contrib import admin

# Register your models here.
from notes.profiles import models

admin.site.register(models.Profile)
