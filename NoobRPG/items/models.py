__all__ = ()

from django.db import models
from rarity.models import Rarity


class ItemManager(models.Manager):
    def all_fields(self) -> models.QuerySet:
        queryset = self.get_queryset().select_related(
            Items.rarity.field.name,
        )
        return queryset.order_by(
            Items.id.field.name,
        )


class Items(models.Model):
    objects = ItemManager()
    name = models.CharField(
        'item name',
        max_length=100,
        help_text='Enter item name',
    )
    rarity = models.ForeignKey(
        Rarity,
        on_delete=models.CASCADE,
        help_text='Enter item rarity',
        verbose_name='rarity',
    )
    damage = models.IntegerField(
        'damage when used as a weapon',
        default=1,
        help_text='Enter damage when used as a weapon',
    )

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'items'

    def __str__(self):
        return f'{self.name}'
