__all__ = ()

from django.core.validators import MinValueValidator
from django.db import models
from locations.models import Location


class EntityBaseModel(models.Model):
    name = models.CharField(
        'entity name',
        max_length=100,
        help_text='Enter entity name',
    )
    max_hp = models.IntegerField(
        'entity max health',
        default=100,
        help_text='Enter entity max health',
    )
    hp = models.IntegerField(
        'entity current health',
        default=100,
        validators=[MinValueValidator(0)],
        help_text='Enter entity current health',
    )
    max_mana = models.IntegerField(
        'entity max mana',
        default=20,
        help_text='Enter entity max mana',
    )
    mana = models.IntegerField(
        'entity current mana',
        default=20,
        validators=[MinValueValidator(0)],
        help_text='Enter entity current mana',
    )
    base_damage = models.IntegerField(
        'entity damage',
        default=10,
        help_text='Enter the damage the entity causes',
    )
    current_location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        verbose_name='entity location',
        related_name='%(class)s_entities',
    )
    is_in_battle = models.BooleanField(
        'is entity in battle',
        default=False,
        help_text='Specify whether the entity is in combat',
    )

    class Meta:
        abstract = True
        verbose_name = 'base entity'
        verbose_name_plural = 'base entitites'

    def __str__(self):
        return f'{self.name}'
