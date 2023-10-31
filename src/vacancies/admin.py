from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Vacancy


@admin.register(Vacancy)
class VacancyAdmin(TranslationAdmin):
    pass
