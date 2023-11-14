from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Vacancy

from .translation import VacancyTranslationOptions


class VacancyAdmin(TranslationAdmin):
    list_display = ('title', 'description', 'address')
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(Vacancy, VacancyAdmin)
