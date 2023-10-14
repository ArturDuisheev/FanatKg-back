from django.db import models
from django.utils.translation import gettext_lazy as _
from djmoney.models.fields import MoneyField

from common.models import BaseModel


class HourDelta(BaseModel):
    price = MoneyField(
        _('price'),
        max_digits=10,
        decimal_places=0,
    )
    price_model = models.ForeignKey(
        'Price',
        verbose_name=_('price'),
        related_name='hours_delta_list',
        on_delete=models.CASCADE
    )
    to = models.CharField(
        _('to'),
        max_length=255,
        null=True,
        blank=True
    )
    from_hour = models.CharField(
        _('from'),
        max_length=255,
        null=True,
        blank=True

    )


class Price(BaseModel):
    hour = models.CharField(
        _('hour'),
        max_length=255,
    )
    hall = models.ForeignKey(
        'HallList',
        verbose_name=_('hall'),
        related_name='price_list',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.hour}'

    class Meta:
        verbose_name = _('Прайс')
        verbose_name_plural = _('Прайсы')


class HallList(BaseModel):
    title = models.CharField(
        _('title'),
        max_length=255,
    )
    street = models.CharField(
        _('street'),
        max_length=255,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'зал: {self.title} | филиал: {self.street}'

    class Meta:
        verbose_name = _('Список залов')
        verbose_name_plural = _('Списки залов')
