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

    def build_field(self, field_name, info, model_class, nested_depth):
        field_class, field_kwargs = super().build_field(
            field_name,
            info,
            model_class,
            nested_depth,
        )

        if field_name == 'url':
            field_kwargs['view_name'] = 'sellers-offers-detail'

        return field_class, field_kwargs
