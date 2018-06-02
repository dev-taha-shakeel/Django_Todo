from django.contrib import admin

from .models import todo, users

# Register your models here.

admin.site.register(todo)
admin.site.register(users)
