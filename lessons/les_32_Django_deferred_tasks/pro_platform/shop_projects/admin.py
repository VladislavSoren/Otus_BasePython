from django.contrib import admin

from .models import Project, Category, Order


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = "id", "name", "price", "updated_at"
    list_display_links = "id", 'name'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = "id", "name", "description"
    list_display_links = "id", 'name'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # inlines = [
    #     PaymentDetailsInline,
    # ]
    list_display = "id", "address", "user", "promocode", "created_at"
    list_display_links = "id", "promocode"