from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import BaseModel


class Vacancy(BaseModel):
    title = models.CharField(_('Название'), max_length=100)
    position = models.CharField(_('Должность'), max_length=100)
    address = models.CharField(_('Филиал'), max_length=100)
    description = models.TextField(_('Описание'))
    url_for_vacancy = models.URLField(_('Google_form'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Вакансия')
        verbose_name_plural = _('Вакансии')
