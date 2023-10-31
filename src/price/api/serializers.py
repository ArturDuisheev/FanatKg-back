from rest_framework import serializers

from price.models import Hall, Affiliate


class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = 'id title image price'.split()


class AffiliateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Affiliate
        fields = 'id image address'.split()


class AffiliateDetailSerializer(serializers.ModelSerializer):
    hall_affiliate = HallSerializer(many=True)

    class Meta:
        model = Affiliate
        fields = 'id hall_affiliate'.split()
