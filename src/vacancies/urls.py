from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import views

router = DefaultRouter()

router.register(r'vacancy', views.VacancyViewSet, basename='vacancy')

urlpatterns = [
    path('', include(router.urls)),
]

