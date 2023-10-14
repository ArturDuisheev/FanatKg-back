from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import views
# Создаем роутер
router = DefaultRouter()

# Регистрируем представления с роутером
router.register(r'price', views.PriceViewSet, basename='price')
router.register(r'HallList', views.HallListViewSet, basename='Halllist')

# Включаем URL-маршруты из роутера
urlpatterns = [
    path('', include(router.urls)),
]
