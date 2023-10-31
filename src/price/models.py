from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel


class Affiliate(BaseModel):
    image = models.ImageField(_('Изображение филиала'), upload_to='affiliate/')
    address = models.CharField(_('Адрес'), max_length=100)

    def __str__(self):
        return f'Филиал {self.address}'

    class Meta:
        verbose_name = _('Филиал')
        verbose_name_plural = _('Филиалы')


class Hall(BaseModel):
    title = models.CharField(_('Название'), max_length=100)
    image = models.ImageField(_('Изображение зала'), upload_to='hall/')
    price = models.ImageField(_('Изображение цен'), upload_to='price/')
    affiliate = models.ForeignKey(
        Affiliate, on_delete=models.CASCADE, verbose_name=_('Филиал'), related_name='hall_affiliate'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Зал')
        verbose_name_plural = _('Залы')
