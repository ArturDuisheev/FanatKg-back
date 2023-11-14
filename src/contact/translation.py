from modeltranslation.translator import register, TranslationOptions
from .models import Address


@register(Address)
class AddressTranslationOptions(TranslationOptions):
    fields = ('address', )
    required_languages = ('ky', 'ru', 'en')
