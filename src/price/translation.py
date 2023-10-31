from modeltranslation.translator import register, TranslationOptions
from .models import Affiliate, Hall


@register(Hall)
class HallTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Affiliate)
class AffiliateTranslationOptions(TranslationOptions):
    fields = ('address',)
