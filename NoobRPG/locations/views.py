__all__ = ()

from locations.models import Location
from locations.serializers import LocationSerializer
from rest_framework import permissions, viewsets


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]
