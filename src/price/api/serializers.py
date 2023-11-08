from rest_framework import serializers
from price import models as price_models


class PrivilegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = price_models.Privilege
        fields = (
            'id',
            'name',
            'image',
            'price_image')


class LocationSerializer(serializers.ModelSerializer):
    privilege = PrivilegeSerializer(many=True)

    class Meta:
        model = price_models.Location
        fields = (
            'id',
            'name',
            'image',
            'privilege')

    def create(self, validated_data):
        privileges_data = validated_data.pop('privilege', [])
        location = price_models.Location.objects.create(**validated_data)
        # всех приветсвует программа утренний итератор )))))
        for privilege_data in privileges_data:
            privilege, created = price_models.Privilege.objects.get_or_create(**privilege_data)
            location.privilege.add(privilege)

        return location
