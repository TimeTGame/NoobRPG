__all__ = ()

from core.functions import get_filterable_fields
from django.core.exceptions import FieldError
from items.models import Items
from items.serializers import ItemSerializer
from rest_framework import permissions, viewsets


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.all_fields()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Items.objects.all_fields()
        allowed_params = get_filterable_fields(Items, depth=1)

        for param, value in self.request.query_params.items():
            if param in allowed_params:
                try:
                    queryset = queryset.filter(**{param: value})
                except (TypeError, ValueError, FieldError):
                    continue

        return queryset
