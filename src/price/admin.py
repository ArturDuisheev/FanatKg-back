from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Hall, Affiliate


class HallInline(admin.StackedInline,):
    model = Hall
    extra = 1


@admin.register(Affiliate)
class AffiliateAdmin(TranslationAdmin):
    inlines = (HallInline,)
