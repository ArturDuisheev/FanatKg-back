from modeltranslation.translator import register, TranslationOptions
from .models import Service


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
    required_languages = ('ky', 'ru', 'en')
