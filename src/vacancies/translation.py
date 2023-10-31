from modeltranslation.translator import register, TranslationOptions
from .models import Vacancy


@register(Vacancy)
class VacancyTranslationOptions(TranslationOptions):
    fields = ('title', 'position', 'address', 'description')
