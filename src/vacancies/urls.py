from django.urls import path
from .api.views import VacancyListAPIView

urlpatterns = [
    path('vacancy/', VacancyListAPIView.as_view())
]
