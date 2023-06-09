from django.contrib import admin

from .models import (
    Project,
    Category,
    Creator,
    Donat,
)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = "id", "name", "price", "category", "url", "creator"
    list_display_links = "id", 'name',


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = "id", "name", "description",
    list_display_links = "id", 'name',


@admin.register(Creator)
class CategoryAdmin(admin.ModelAdmin):
    list_display = "id", "rating", "user",
    list_display_links = "id",


@admin.register(Donat)
class CategoryDonat(admin.ModelAdmin):
    list_display = "id", "money", "created_at",
    list_display_links = "id",
