from modeltranslation.translator import register, TranslationOptions
from .models import Link, Phone, Contact


@register(Link)
class LinkTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ('affiliate',)
