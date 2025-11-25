__all__ = ()

from django.db import models


class Rarity(models.Model):
    name = models.CharField(
        'Rarity name',
        max_length=100,
        help_text='Enter rarity name',
    )
    slug = models.SlugField(
        'Rarity slug',
        max_length=100,
        help_text='Enter slug for rarity',
    )

    class Meta:
        verbose_name = 'rarity'
        verbose_name_plural = 'list of rarities'

    def __str__(self):
        return f'{self.name}'
