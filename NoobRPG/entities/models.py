__all__ = ()

import random

from core.models import EntityBaseModel
from django.db import models
from items.models import Items
from locations.models import Location
from sellers_offers.models import SellerOffer


class Seller(models.Model):
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


class NonPlayerCharacter(EntityBaseModel):
    items_to_drop = models.ManyToManyField(
        Items,
        blank=True,
        verbose_name='item',
    )

    class Meta:
        verbose_name = 'npc'
        verbose_name_plural = 'npc'

    def __str__(self):
        return f'{self.name}'

    def drop_items(self):
        return random.choice(self.items_to_drop)

    def taking_damage(self, damage):
        if self.hp > damage:
            self.hp -= damage
        else:
            self.hp = 0
            return self.drop_items()
        return None

    def dealing_damage(self):
        return self.damage


class Player(EntityBaseModel):
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

    def to_start_location(self):
        self.location = self.start_location
        self.save()

    def equip_weapon(self, item):
        if item is None:
            self.weapon = None
            return
        if item not in self.inventory.all():
            raise ValueError('Cannot equip weapon: item not in inventory.')
        self.weapon = item
        self.save()

    def taking_damage(self, damage_hp, damage_mana):
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

    def healing(self, hp_heal_amount, mana_heal_amount):
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
        return (
            f'Your health is now {self.hp} and your mana is {self.mana}.'
        )

    def dealing_damage(self):
        if self.weapon:
            return self.base_damage + self.weapon.damage
        return self.base_damage
