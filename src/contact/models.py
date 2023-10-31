from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from common.models import BaseModel
from price.models import Affiliate


class Phone(BaseModel):
    phone = PhoneNumberField(
        _('Номер'),
        region='KG'
    )

    def __str__(self):
        return str(self.phone)

    class Meta:
        verbose_name = _('Номер')
        verbose_name_plural = _('Номера')


class Link(models.Model):
    title = models.CharField(_('Title'), max_length=60)
    icon = models.ImageField(
        _('Icon'), upload_to="contact/icons/",
        validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'ico'])]
    )
    link = models.URLField(verbose_name='Link')

    def __str__(self):
        return f'{self.title}'


class Contact(BaseModel):
    phone = models.ManyToManyField(Phone, verbose_name=_('Phones'), related_name='contact_phones')
    affiliate = models.ForeignKey(
        Affiliate, verbose_name=_('Филиал'), on_delete=models.CASCADE, related_name='phone_affiliate'
    )

    @property
    def address_affiliate(self):
        return self.affiliate.address

    def __str__(self):
        return self.affiliate.address

    class Meta:
        verbose_name = _('Контакт')
        verbose_name_plural = _('Контакты')
