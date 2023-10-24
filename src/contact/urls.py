from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import views

router = DefaultRouter()

router.register(r'contact', views.ContactViewSet, basename='contacts')


urlpatterns = [
    path('', include(router.urls)),
]
