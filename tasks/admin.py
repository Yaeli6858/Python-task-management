from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Task, CustomUser, Team

admin.site.register(Task)
admin.site.register(CustomUser)
admin.site.register(Team)