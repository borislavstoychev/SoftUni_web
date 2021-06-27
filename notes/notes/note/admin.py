from django.contrib import admin

# Register your models here.
from notes.note import models

admin.site.register(models.Note)
