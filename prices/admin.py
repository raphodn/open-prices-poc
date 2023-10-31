from django.contrib import admin

from prices.models import Price


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product_code",
        "price",
        "currency",
        "location_osm_id",
        "source",
        "created",
    )

    readonly_fields = ["created"]

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
