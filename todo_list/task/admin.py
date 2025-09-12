from django.contrib import admin
from . import models


@admin.register(models.Task)
class UserAdmin(admin.ModelAdmin):
    pass
