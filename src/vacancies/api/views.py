from rest_framework.generics import ListAPIView
from vacancies.models import Vacancy
from .serializers import VacancySerializer


class VacancyListAPIView(ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
