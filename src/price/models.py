from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel


class Location(BaseModel):
    street = models.CharField(
        _('Улица'),
        max_length=80,
    )
    image = models.ImageField(
        _('Фото'),
        upload_to='images/price/',
        blank=True,
        null=True,
    )
    privilege = models.ManyToManyField(
        'Privilege',
        related_name='privilege_location',
        verbose_name='Описание прайса'
    )

    def __str__(self):
        return f'филиал: {self.street}'

    class Meta:
        verbose_name = _('Прайс')
        verbose_name_plural = _('Прайсы')


class Privilege(BaseModel):
    name = models.CharField(
        _('Название зала'),
        max_length=70
    )
    image = models.ImageField(
        _('Изображение'),
        upload_to='images/price/',
        blank=True,
        null=True
    )
    price_image = models.ImageField(
        _('Изображение прайсов'),
        upload_to='images/price_in_depth/',
        blank=True,
        null=True
    )

    def __str__(self):
        return f'Название зала: {self.name}'

    class Meta:
        verbose_name = _('Описание прайса')
        verbose_name_plural = _('Описание прайсов')
