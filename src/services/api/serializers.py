from rest_framework import serializers

from services import models as service_models


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = service_models.Service
        fields = ['id', 'image', 'title', 'description']
