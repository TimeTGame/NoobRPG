__all__ = []

from core.functions import get_filterable_fields
from django.core.exceptions import FieldError
from entities.models import NonPlayerCharacter as NPCModel
from entities.models import Player, Seller
from entities.serializers import (
    NPCSerializer,
    PlayerSerializer,
    SellerSerializer,
)
from rest_framework import permissions, viewsets


class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all_fields()
    serializer_class = SellerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Seller.objects.all_fields()
        allowed_params = get_filterable_fields(Seller, depth=1)

        for param, value in self.request.query_params.items():
            if param in allowed_params:
                try:
                    queryset = queryset.filter(**{param: value})
                except (TypeError, ValueError, FieldError):
                    continue

        return queryset


class NPCsViewSet(viewsets.ModelViewSet):
    queryset = NPCModel.objects.all_fields()
    serializer_class = NPCSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = NPCModel.objects.all_fields()
        allowed_params = get_filterable_fields(NPCModel, depth=1)

        for param, value in self.request.query_params.items():
            if param in allowed_params:
                try:
                    queryset = queryset.filter(**{param: value})
                except (TypeError, ValueError, FieldError):
                    continue

        return queryset


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all_fields()
    serializer_class = PlayerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Player.objects.all_fields()
        allowed_params = get_filterable_fields(Player, depth=1)

        for param, value in self.request.query_params.items():
            if param in allowed_params:
                try:
                    queryset = queryset.filter(**{param: value})
                except (TypeError, ValueError, FieldError):
                    continue

        return queryset
