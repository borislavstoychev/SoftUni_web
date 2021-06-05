from django.contrib import admin

# Register your models here.
from todo_app import models


class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner']
    list_filter = ['owner']

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(models.Todo, TodoAdmin)
admin.site.register(models.Category)
admin.site.register(models.Person)
