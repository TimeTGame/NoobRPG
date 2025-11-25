__all__ = ()

from django.contrib import admin
from locations.models import Location


@admin.register(Location)
class LocationsAdmin(admin.ModelAdmin):
    list_display = (
        Location.slug.field.name,
        Location.name.field.name,
    )
    list_display_links = (Location.name.field.name,)
    short_description = 'location'
