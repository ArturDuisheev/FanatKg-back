from rest_framework import viewsets
from services.api import utils as u

from services import models as service_models
from services.api import serializers as service_serializers


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = service_models.Service.objects.all()
    serializer_class = service_serializers.ServiceSerializer

    def perform_create(self, serializer):
        image = self.request.data.get('image')
        compressed_image_buffer = u.compress_image(image)
        service = serializer.save()
        service.image.save(f"{service.id}.jpg", compressed_image_buffer)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

