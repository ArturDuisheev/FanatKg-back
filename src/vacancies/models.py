from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel


class Vacancy(BaseModel):
    title = models.CharField(
        _('Title'),
        max_length=80
    )
    description = models.TextField(
        _('Description')
    )
    address = models.CharField(
        _('Address'),
        max_length=100,
    )
    google_form = models.URLField(
        _('Google Form'),
    )

    def __str__(self):
        return f"вакансия: {self.title}"

    class Meta:
        verbose_name = _('Вакансия')
        verbose_name_plural = _('Вакансии')
