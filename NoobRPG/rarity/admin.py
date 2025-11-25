__all__ = ()

from django.contrib import admin
from rarity.models import Rarity


@admin.register(Rarity)
class RaritiesAdmin(admin.ModelAdmin):
    list_display = (
        Rarity.slug.field.name,
        Rarity.name.field.name,
    )
    list_display_links = (Rarity.name.field.name,)
    short_description = 'Rarity'
