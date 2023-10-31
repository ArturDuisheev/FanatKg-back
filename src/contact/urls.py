from django.urls import path

from .api.views import ContactListAPIView, LinkListAPIView

urlpatterns = [
    path('contact/', ContactListAPIView.as_view()),
    path('link/', LinkListAPIView.as_view())
]
