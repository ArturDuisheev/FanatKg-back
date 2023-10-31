from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Phone, Contact, Link


@admin.register(Contact)
class ContactAdmin(TranslationAdmin):
    pass


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    pass


@admin.register(Link)
class LinkAdmin(TranslationAdmin):
    pass
