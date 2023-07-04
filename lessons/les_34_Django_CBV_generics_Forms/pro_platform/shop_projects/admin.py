from django.contrib import admin

from .models import (
    Project,
    Category,
    Order,
    OrderPaymentDetails,
)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = "id", "name", "price", "updated_at"
    list_display_links = "id", 'name'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = "id", "name", "description", "archived",
    list_display_links = "id", 'name'


# form for filling details in creating orders page
class PaymentDetailsInline(admin.TabularInline):
    model = OrderPaymentDetails


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # implement OrderPaymentDetails in Orders
    inlines = [
        PaymentDetailsInline,
    ]
    list_display = "id", "address", "user", "promocode", "created_at"
    list_display_links = "id", "promocode"


@admin.register(OrderPaymentDetails)
class OrderPaymentDetailsAdmin(admin.ModelAdmin):
    list_display = "id", "payed_at", "card_ends_with", "status", "order"
    list_display_links = "id", "status"
