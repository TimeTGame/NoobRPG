__all__ = ()

from items.models import Items
from rest_framework import serializers


class ItemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Items
        fields = [
            'url',
            Items.id.field.name,
            Items.name.field.name,
            Items.rarity.field.name,
            Items.damage.field.name,
        ]
