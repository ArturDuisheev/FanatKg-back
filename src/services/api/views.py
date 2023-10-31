from rest_framework.generics import ListCreateAPIView

from . import utils
from .serializers import ServiceSerializer
from services.models import Service


class ServiceListAPIView(ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def perform_create(self, serializer):
        image = self.request.data.get('image')
        compressed_image_buffer = (utils.compress_image(image))
        service = serializer.save()
        service.image.save(f"{service.id}.jpg", compressed_image_buffer)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)