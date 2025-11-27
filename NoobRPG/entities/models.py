__all__ = ()

import random

from core.models import EntityBaseModel
from django.contrib.auth.models import User
from django.db import models
from items.models import Items
from locations.models import Location
from sellers_offers.models import SellerOffer


class SellerManager(models.Manager):
    def all_fields(self) -> models.QuerySet:
        queryset = self.get_queryset().prefetch_related(
            Seller.offers.field.name,
        )
        return queryset.order_by(
            Seller.name.field.name,
        )


class Seller(models.Model):
    objects = SellerManager()
    name = models.CharField(
        'Entity name',
        max_length=100,
        help_text='Enter entity name',
    )
    offers = models.ManyToManyField(
        SellerOffer,
        blank=True,
        verbose_name='offer',
    )

    class Meta:
        verbose_name = 'seller'
        verbose_name_plural = 'sellers'

    def __str__(self):
        return f'{self.name}'


class NPCManager(models.Manager):
    def all_fields(self) -> models.QuerySet:
        queryset = (
            self.get_queryset()
            .select_related(
                NonPlayerCharacter.current_location.field.name,
            )
            .prefetch_related(
                NonPlayerCharacter.items_to_drop.field.name,
            )
        )
        return queryset.order_by(
            NonPlayerCharacter.name.field.name,
        )


class NonPlayerCharacter(EntityBaseModel):
    objects = NPCManager()
    items_to_drop = models.ManyToManyField(
        Items,
        blank=True,
        verbose_name='item',
    )

    class Meta:
        verbose_name = 'npc'
        verbose_name_plural = 'npcs'

    def __str__(self) -> str:
        return f'{self.name}'

    def drop_items(self) -> models.QuerySet:
        items = list(self.items_to_drop.all())
        if items:
            return random.choice(items)
        return None

    def taking_damage(self, damage: int) -> str | None:
        if self.hp > damage:
            self.hp -= damage
        else:
            self.hp = 0
        self.save()
        if self.hp == 0:
            return self.drop_items()
        return None

    def self_damage(self) -> int:
        return self.base_damage


class PlayerManager(models.Manager):
    def all_fields(self) -> models.QuerySet:
        queryset = (
            self.get_queryset()
            .select_related(
                Player.current_location.field.name,
                Player.start_location.field.name,
                Player.weapon.field.name,
            )
            .prefetch_related(
                Player.inventory.field.name,
            )
        )
        return queryset.order_by(
            Player.name.field.name,
        )


class Player(EntityBaseModel):
    objects = PlayerManager()
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='player_profile',
        help_text='The user account associated with this player',
    )
    inventory = models.ManyToManyField(
        Items,
        blank=True,
        verbose_name='item',
        related_name='player_inventory',
    )
    weapon = models.ForeignKey(
        Items,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name='equipped weapon',
        related_name='equipped_by_player',
    )
    start_location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        verbose_name='start location',
    )

    class Meta:
        verbose_name = 'player'
        verbose_name_plural = 'players'

    def __str__(self):
        return f'{self.name}'

    def to_start_location(self) -> str:
        self.current_location = self.start_location
        self.save()
        return f'You are now in start location: {self.current_location}'

    def equip_weapon(self, item: models.QuerySet) -> str:
        if item is None:
            self.weapon = None
            return 'Cannot equip weapon: Inventory is empty.'
        if item not in self.inventory.all():
            return 'Cannot equip weapon: Item not in inventory.'
        self.weapon = item
        self.save()
        return f'Equipped weapon: {self.weapon}.'

    def taking_damage(self, damage_hp: int, damage_mana: int) -> str:
        if self.hp >= damage_hp or self.mana >= damage_mana:
            self.hp -= damage_hp
            self.mana -= damage_mana
            message = (
                f'Your health is now {self.hp} and your mana is {self.mana}.'
            )
        else:
            self.hp = self.max_hp
            self.mana = self.max_mana
            self.to_start_location()
            message = (
                'You have lost. '
                f'You have been sent to the {self.start_location} location.'
            )
        self.save()
        return message

    def healing(self, hp_heal_amount: int, mana_heal_amount: int) -> str:
        healed_hp = self.hp + hp_heal_amount
        healed_mana = self.mana + mana_heal_amount
        if healed_hp > self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp += hp_heal_amount
        if healed_mana > self.max_mana:
            self.mana = self.max_mana
        else:
            self.mana += mana_heal_amount
        self.save(
            update_fields=[
                EntityBaseModel.hp.field.value,
                EntityBaseModel.mana.field.value,
            ],
        )
        return f'Your health is now {self.hp} and your mana is {self.mana}.'

    def self_damage(self) -> int:
        if self.weapon:
            return self.base_damage + self.weapon.damage
        return self.base_damage

    def attack(self, enemy: models.QuerySet) -> str:
        damage = self.self_damage()
        enemy.taking_damage(damage)
        return f'You dealt {damage} damage to an enemy.'
