from django.core import validators as val
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from common.models import BaseModel


class Street(BaseModel):
    street = models.TextField(
        _('Street'),
    )

    def __str__(self):
        return f"улица: {self.street}"

    class Meta:
        verbose_name = _('Street')
        verbose_name_plural = _('Streets')


class Phone(BaseModel):
    phone = PhoneNumberField(
        _('Phone'),
        region='KG'
    )

    def __str__(self):
        return f'номер телефона: {self.phone}'


class Link(models.Model):
    title = models.CharField(
        _('Title'),
        max_length=60
    )
    icon = models.ImageField(
        _('Icon'),
        upload_to="contact/icons/",
        validators=[
            val.FileExtensionValidator(allowed_extensions=[
                'png', 'jpg', 'jpeg', 'ico'
            ])
        ]
    )
    link = models.URLField(verbose_name='Link')

    def __str__(self):
        return f'соц.сеть: {self.title}'


class Contact(models.Model):
    streets = models.ManyToManyField(Street, verbose_name=_('Streets'), related_name='contact_streets')
    phones = models.ManyToManyField(Phone, verbose_name=_('Phones'), related_name='contact_phones')
    email = models.EmailField(_('Email'))
    links = models.ManyToManyField(Link, verbose_name=_('Links'), related_name='contact_links')

    def __str__(self):
        return f'Контакты\nУлицы: {", ".join(str(street) for street in self.streets.all())}'

    class Meta:
        verbose_name = _('Контакт')
        verbose_name_plural = _('Контакты')
