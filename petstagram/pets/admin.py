import modes as modes
from django.contrib import admin

# Register your models here.
from pets import models


class Pets(admin.ModelAdmin):
    list_display = ['type', 'name', 'age', ]
    list_filter = ['type', 'name', 'age']

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(models.Pet, Pets)
admin.site.register(models.Like)
