import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    id = models.UUIDField(
        _('уникальный идентификатор'),
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    created_at = models.DateTimeField(
        _('создано в: '),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        _('обновленно в: '),
        auto_now=True
    )

    class Meta:
        abstract = True

