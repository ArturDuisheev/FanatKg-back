from rest_framework import viewsets

from price import models as price_models
from price.api import serializers as price_serializers


class LocationViewSet(viewsets.ModelViewSet):
    queryset = price_models.Location.objects.all()
    serializer_class = price_serializers.LocationSerializer


class PrivilegeViewSet(viewsets.ModelViewSet):
    queryset = price_models.Privilege.objects.all()
    serializer_class = price_serializers.PrivilegeSerializer

