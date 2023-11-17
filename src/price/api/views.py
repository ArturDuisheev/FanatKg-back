from rest_framework import viewsets
from django.http import JsonResponse as json_resp

from price import models as price_models

from price.api import serializers as price_serializers

import seeder_beer as script


def start_seed(request):
    script.seed()
    return json_resp({'status': 'Seeder is successfully started'})


class LocationViewSet(viewsets.ModelViewSet):
    queryset = price_models.Location.objects.all()
    serializer_class = price_serializers.LocationSerializer


class PrivilegeViewSet(viewsets.ModelViewSet):
    queryset = price_models.Privilege.objects.all()
    serializer_class = price_serializers.PrivilegeSerializer
