from django.urls import path

from .api.views import ServiceListAPIView

urlpatterns = [
    path('service/', ServiceListAPIView.as_view())
]
