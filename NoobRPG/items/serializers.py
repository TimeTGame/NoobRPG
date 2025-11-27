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

    def build_field(self, field_name, info, model_class, nested_depth):
        field_class, field_kwargs = super().build_field(
            field_name,
            info,
            model_class,
            nested_depth,
        )

        if field_name == 'url':
            field_kwargs['view_name'] = 'items-detail'

        return field_class, field_kwargs
