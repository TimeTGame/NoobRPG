__all__ = ()

from core.functions import get_filterable_fields
from django.core.exceptions import FieldError
from rarity.models import Rarity
from rarity.serializers import RaritySerializer
from rest_framework import permissions, viewsets


class RarityViewSet(viewsets.ModelViewSet):
    queryset = Rarity.objects.all()
    serializer_class = RaritySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Rarity.objects.all()
        allowed_params = get_filterable_fields(Rarity, depth=1)

        for param, value in self.request.query_params.items():
            if param in allowed_params:
                try:
                    queryset = queryset.filter(**{param: value})
                except (TypeError, ValueError, FieldError):
                    continue

        return queryset
