from rest_framework import viewsets

from vacancies.api import serializers as ser
from vacancies import models as vac_m


class VacancyViewSet(viewsets.ModelViewSet):
    queryset = vac_m.Vacancy.objects.all()
    serializer_class = ser.VacancySerializer
