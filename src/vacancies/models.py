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
    requirement = models.TextField(
        _('Requirements')
    )
    condition = models.TextField(
        _('Conditions')
    )
    contact = models.CharField(
        _('Contacts'),
        max_length=160
    )
    url_for_vacancy = models.URLField(
        _('Google form'),
    )

    def __str__(self):
        return f"вакансия: {self.title}"

    class Meta:
        verbose_name = _('Вакансия')
        verbose_name_plural = _('Вакансии')
