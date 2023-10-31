from rest_framework.generics import ListAPIView, RetrieveAPIView

from . import serializers
from price import models


class AffiliateListAPIView(ListAPIView):
    queryset = models.Affiliate.objects.all()
    serializer_class = serializers.AffiliateListSerializer


class AffiliateDetailAPIView(RetrieveAPIView):
    queryset = models.Affiliate.objects.all()
    serializer_class = serializers.AffiliateDetailSerializer
    lookup_field = 'id'
