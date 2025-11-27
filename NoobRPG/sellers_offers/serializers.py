__all__ = ()

from rest_framework import serializers
from sellers_offers.models import SellerOffer


class SellerOfferSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SellerOffer
        fields = [
            'url',
            SellerOffer.id.field.name,
            SellerOffer.item.field.name,
            SellerOffer.cost.field.name,
        ]
