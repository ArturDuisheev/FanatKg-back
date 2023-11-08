from django.core import validators as val
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from common.models import BaseModel
from contact import choices


class Address(BaseModel):
    address = models.TextField(
        _('Street'),
    )
    phones = models.ManyToManyField(
        'Phone',
        related_name='street_phone',
        verbose_name='Номер телефона'
    )

    def __str__(self):
        return f"Филиал: {self.address}"

    class Meta:
        verbose_name = _('Филиал')
        verbose_name_plural = _('Филиалы')


class Phone(BaseModel):
    phone = PhoneNumberField(
        _('Phone'),
        region='KG'
    )

    def __str__(self):
        return f'номер телефона: {self.phone}'

    class Meta:
        verbose_name = _('Телефон')
        verbose_name_plural = _('Телефоны')


class Link(models.Model):
    social_media = models.CharField(
        'Соц.Сети',
        max_length=17,
        choices=choices.SocialMedia.choices,
        default=choices.SocialMedia.TELEGRAM
    )
    link = models.URLField(verbose_name='Link')

    def __str__(self):
        return f'соц.сеть: {self.social_media}'

    class Meta:
        verbose_name = _('Ссылка')
        verbose_name_plural = _('Ссылки')


class Contact(models.Model):
    addresses = models.ManyToManyField(
        Address,
        verbose_name=_('Адрес'),
        related_name='contact_address'
    )
    email = models.EmailField(_('Email'))
    links = models.ManyToManyField(Link, verbose_name=_('Links'), related_name='contact_links')

    def __str__(self):
        return f'Контакты\nУлицы: {", ".join(str(street) for street in self.addresses.all())}'

    class Meta:
        verbose_name = _('Контакт')
        verbose_name_plural = _('Контакты')
