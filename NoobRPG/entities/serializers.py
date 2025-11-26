__all__ = ()

from entities.models import NonPlayerCharacter as NPCModel
from entities.models import Player, Seller
from rest_framework import serializers


class SellerSerializer(serializers.HyperlinkedModelSerializer):
    offers = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Seller
        fields = [
            'url',
            Seller.id.field.name,
            Seller.name.field.name,
            Seller.offers.field.name,
        ]

    def build_field(self, field_name, info, model_class, nested_depth):
        field_class, field_kwargs = super().build_field(
            field_name,
            info,
            model_class,
            nested_depth,
        )

        if field_name == 'url':
            field_kwargs['view_name'] = 'sellers-detail'

        return field_class, field_kwargs


class NPCSerializer(serializers.HyperlinkedModelSerializer):
    items_to_drop = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = NPCModel
        fields = [
            'url',
            NPCModel.id.field.name,
            NPCModel.name.field.name,
            NPCModel.max_hp.field.name,
            NPCModel.hp.field.name,
            NPCModel.max_mana.field.name,
            NPCModel.mana.field.name,
            NPCModel.base_damage.field.name,
            NPCModel.is_in_battle.field.name,
            NPCModel.current_location.field.name,
            NPCModel.items_to_drop.field.name,
        ]

    def build_field(self, field_name, info, model_class, nested_depth):
        field_class, field_kwargs = super().build_field(
            field_name,
            info,
            model_class,
            nested_depth,
        )

        if field_name == 'url':
            field_kwargs['view_name'] = 'npcs-detail'

        return field_class, field_kwargs


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    inventory = serializers.StringRelatedField(many=True, read_only=True)
    weapon = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Player
        fields = [
            'url',
            Player.id.field.name,
            Player.name.field.name,
            Player.max_hp.field.name,
            Player.hp.field.name,
            Player.max_mana.field.name,
            Player.mana.field.name,
            Player.base_damage.field.name,
            Player.is_in_battle.field.name,
            Player.current_location.field.name,
            Player.inventory.field.name,
            Player.weapon.field.name,
            Player.start_location.field.name,
        ]

    def build_field(self, field_name, info, model_class, nested_depth):
        field_class, field_kwargs = super().build_field(
            field_name,
            info,
            model_class,
            nested_depth,
        )

        if field_name == 'url':
            field_kwargs['view_name'] = 'players-detail'

        return field_class, field_kwargs
