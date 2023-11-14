from rest_framework import serializers

from vacancies import models as vac_m


class VacancySerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)

    class Meta:
        model = vac_m.Vacancy
        exclude = ['title', 'description', 'address']

