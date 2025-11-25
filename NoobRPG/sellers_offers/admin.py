__all__ = ()

from django.contrib import admin
from sellers_offers.models import SellerOffer


@admin.register(SellerOffer)
class SellerOffersAdmin(admin.ModelAdmin):
    list_display = (
        SellerOffer.item.field.name,
        SellerOffer.cost.field.name,
    )
    short_description = 'SellerOffer'
