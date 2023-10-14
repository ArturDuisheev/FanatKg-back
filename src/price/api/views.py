from rest_framework import viewsets

from price import models as price_models
from price.api import serializers as price_serializers


class PriceViewSet(viewsets.ModelViewSet):
    queryset = price_models.Price.objects.all()
    serializer_class = price_serializers.PriceSerializer


class HallListViewSet(viewsets.ModelViewSet):
    queryset = price_models.HallList.objects.all()
    serializer_class = price_serializers.HallListSerializer

