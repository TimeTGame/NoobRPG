__all__ = ()

from rarity.models import Rarity
from rest_framework import serializers


class RaritySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rarity
        fields = [
            'url',
            Rarity.id.field.name,
            Rarity.name.field.name,
            Rarity.slug.field.name,
        ]
