from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator

from common.models import BaseModel


class Service(BaseModel):
    image = models.ImageField(
        _('Изображение для сервиса'), upload_to='services/%Y-%m-%d/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'svg', 'jpeg', 'png'])]
    )
    title = models.CharField(_('Название'), max_length=100)
    description = models.TextField(_('Описание'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Услуга')
        verbose_name_plural = _('Услуги')
