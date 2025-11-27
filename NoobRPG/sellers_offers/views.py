__all__ = ()

from core.functions import get_filterable_fields
from django.core.exceptions import FieldError
from rest_framework import permissions, viewsets
from sellers_offers.models import SellerOffer
from sellers_offers.serializers import SellerOfferSerializer


class SellerOfferViewSet(viewsets.ModelViewSet):
    queryset = SellerOffer.objects.all_fields()
    serializer_class = SellerOfferSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = SellerOffer.objects.all_fields()
        allowed_params = get_filterable_fields(SellerOffer, depth=1)

        for param, value in self.request.query_params.items():
            if param in allowed_params:
                try:
                    queryset = queryset.filter(**{param: value})
                except (TypeError, ValueError, FieldError):
                    continue

        return queryset
