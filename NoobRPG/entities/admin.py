__all__ = ()

from django.contrib import admin
from entities.models import NonPlayerCharacter, Player, Seller


@admin.register(Seller)
class SellersAdmin(admin.ModelAdmin):
    list_display = (
        Seller.name.field.name,
    )
    filter_horizontal = (Seller.offers.field.name,)
    list_display_links = (Seller.name.field.name,)
    short_description = 'Seller'


@admin.register(NonPlayerCharacter)
class NPCsAdmin(admin.ModelAdmin):
    list_display = (
        Player.name.field.name,
        Player.current_location.field.name,
        Player.is_in_battle.field.name,
    )
    filter_horizontal = (NonPlayerCharacter.items_to_drop.field.name,)
    list_display_links = (NonPlayerCharacter.name.field.name,)
    short_description = 'NPC'


@admin.register(Player)
class PlayersAdmin(admin.ModelAdmin):
    list_display = (
        Player.name.field.name,
        Player.current_location.field.name,
        Player.is_in_battle.field.name,
    )
    filter_horizontal = (Player.inventory.field.name,)
    list_display_links = (Player.name.field.name,)
    short_description = 'Player'
