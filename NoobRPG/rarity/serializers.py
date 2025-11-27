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

    def build_field(self, field_name, info, model_class, nested_depth):
        field_class, field_kwargs = super().build_field(
            field_name,
            info,
            model_class,
            nested_depth,
        )

        if field_name == 'url':
            field_kwargs['view_name'] = 'rarity-detail'

        return field_class, field_kwargs
