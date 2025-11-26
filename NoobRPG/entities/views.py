__all__ = []

from entities.models import NonPlayerCharacter as NPCModel
from entities.models import Player, Seller
from entities.serializers import (
    NPCSerializer,
    PlayerSerializer,
    SellerSerializer,
)
from rest_framework import permissions, viewsets


class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = [permissions.IsAuthenticated]


class NPCsViewSet(viewsets.ModelViewSet):
    queryset = NPCModel.objects.all()
    serializer_class = NPCSerializer
    permission_classes = [permissions.IsAuthenticated]


class NPCsInLocationViewSet(viewsets.ModelViewSet):
    serializer_class = NPCSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        location_slug = self.kwargs.get('location_slug')
        if location_slug:
            return NPCModel.objects.in_location(location_slug)
        return NPCModel.objects.none()


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [permissions.IsAuthenticated]
