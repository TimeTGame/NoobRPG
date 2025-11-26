__all__ = ()

from django.db import models


class Location(models.Model):
    name = models.CharField(
        'Location name',
        max_length=150,
        help_text='Enter location name',
    )
    slug = models.SlugField(
        'Location slug',
        max_length=150,
        help_text='Enter location slug',
    )

    def __str__(self):
        return f'{self.name}'
