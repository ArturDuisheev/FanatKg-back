from django.urls import path

from .api import views

urlpatterns = [
    path('affiliate/', views.AffiliateListAPIView.as_view()),
    path('affiliate/price/<str:id>/', views.AffiliateDetailAPIView.as_view()),
]
