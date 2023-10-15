from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import views

router = DefaultRouter()

router.register(r'service', views.ServiceViewSet, basename='service')

urlpatterns = [
    path('', include(router.urls)),
]
