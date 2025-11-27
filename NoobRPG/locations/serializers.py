__all__ = ()

from locations.models import Location
from rest_framework import serializers


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = [
            'url',
            Location.id.field.name,
            Location.name.field.name,
            Location.slug.field.name,
        ]

    def build_field(self, field_name, info, model_class, nested_depth):
        field_class, field_kwargs = super().build_field(
            field_name,
            info,
            model_class,
            nested_depth,
        )

        if field_name == 'url':
            field_kwargs['view_name'] = 'location-detail'

        return field_class, field_kwargs
