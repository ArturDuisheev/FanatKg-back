from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import views

router = DefaultRouter()

router.register(r'price', views.PriceViewSet, basename='price')
router.register(r'HallList', views.HallListViewSet, basename='Halllist')


urlpatterns = [
    path('', include(router.urls)),
]
