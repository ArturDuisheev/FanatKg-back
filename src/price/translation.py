from modeltranslation.translator import register, TranslationOptions
from .models import Location, Privilege


@register(Location)
class LocationTranslationOptions(TranslationOptions):
    fields = ('street', )
    required_languages = ('ky', 'ru', 'en')


@register(Privilege)
class PrivilegeTranslationOptions(TranslationOptions):
    fields = ('name', )
    required_languages = ('ky', 'ru', 'en')

