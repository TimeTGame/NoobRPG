__all__ = ()

from django.contrib import admin
from items.models import Items


@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    list_display = (
        Items.name.field.name,
        Items.rarity.field.name,
        Items.damage.field.name,
    )
    list_display_links = (Items.name.field.name,)
    short_description = 'Items'
