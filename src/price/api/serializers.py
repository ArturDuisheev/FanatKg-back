from rest_framework import serializers
from price import models as price_models


class HoursDeltaSerializer(serializers.ModelSerializer):
    class Meta:
        model = price_models.HourDelta
        fields = ('id', 'price', 'price_currency', 'to', 'from_hour')


class PriceSerializer(serializers.ModelSerializer):
    hours_delta_list = HoursDeltaSerializer(many=True, required=False)

    class Meta:
        model = price_models.Price
        fields = ('id', 'hour', 'hours_delta_list')


class HallListSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)
    price_list = PriceSerializer(many=True, required=False)

    class Meta:
        model = price_models.HallList
        fields = ('id', 'title', 'street', 'price_list', 'created_at')
