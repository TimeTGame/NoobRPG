__all__ = ()

from django.db import models
from items.models import Items


class SellerOffer(models.Model):
    item = models.ForeignKey(
        Items,
        on_delete=models.CASCADE,
        help_text='Enter item',
        verbose_name='item',
    )
    cost = models.IntegerField(
        'Item cost',
        default=100,
        help_text='Enter item cost',
    )

    class Meta:
        verbose_name = 'seller offer'
        verbose_name_plural = 'sellers offers'

    def __str__(self):
        return f'{self.item} - {self.cost}P'
