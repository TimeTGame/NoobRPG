__all__ = ()

from locations.models import Location
from rest_framework import serializers


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = [
            Location.id.field.name,
            Location.name.field.name,
            Location.slug.field.name,
        ]
