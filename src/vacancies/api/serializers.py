from rest_framework import serializers
from vacancies.models import Vacancy


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = 'id title address description url_for_vacancy '.split()
