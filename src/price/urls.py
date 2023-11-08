from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import views

router = DefaultRouter()

router.register(r'location', views.LocationViewSet, basename='location')
router.register(r'privilege', views.PrivilegeViewSet, basename='privilege')


urlpatterns = [
    path('', include(router.urls)),
]
