from django.contrib import admin

# Register your models here.
from templates_advanced.pythons_auth.models import PythonsUser

admin.site.register(PythonsUser)

