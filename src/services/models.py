from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator

from common.models import BaseModel


class Service(BaseModel):
    image = models.ImageField(
        _('Image services'),
        upload_to='services/images/%Y-%m-%d/',
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'svg', 'jpeg', 'png'])
        ]
    )
    title = models.CharField(
        _('Title'),
        max_length=100
    )
    description = models.TextField(
        _('Description'),
        blank=True,
        null=True
    )

    def __str__(self):
        return f'услуга: {self.title}'

    class Meta:
        verbose_name = _('Услуга')
        verbose_name_plural = _('Услуги')
