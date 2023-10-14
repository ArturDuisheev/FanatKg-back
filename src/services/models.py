from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel


class Vacancy(BaseModel):
    image = models.ImageField(
        _('Изображение вакансии'),
        upload_to='vacancies',
        blank=True,
        null=True
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
        return f'вакансия: {self.title}'

    class Meta:
        verbose_name = _('Вакансия')
        verbose_name_plural = _('Вакансии')


