from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Model3D)
class Model3DAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "image",
        "views",
        "uploads",
    )

@admin.register(models.Badge)
class BadgeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "critaire",
    )

@admin.register(models.UserBadge)
class UserBadgeAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "badge",
        "date_awarded",
    )
