from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from contact import models as con_model

from .translation import AddressTranslationOptions

class AddressAdmin(TranslationAdmin):
    list_display = ('address', )

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(con_model.Address, AddressAdmin)
admin.site.register(con_model.Phone)
admin.site.register(con_model.Link)
admin.site.register(con_model.Contact)
