__all__ = ()

from django.db import models
from items.models import Items


class SellerOfferManager(models.Manager):
    def all_fields(self) -> models.QuerySet:
        queryset = self.get_queryset().select_related(
            SellerOffer.item.field.name,
        )
        return queryset.order_by(
            SellerOffer.id.field.name,
        )


class SellerOffer(models.Model):
    objects = SellerOfferManager()
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
