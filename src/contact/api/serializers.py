from rest_framework import serializers as ser

from contact import models as con_models


class StreetSerializer(ser.ModelSerializer):
    created_at = ser.DateTimeField(read_only=True, format='%Y-%m-%d')

    class Meta:
        model = con_models.Street
        fields = (
            'id',
            'street',
            'created_at',
        )


class PhoneSerializer(ser.ModelSerializer):
    created_at = ser.DateTimeField(read_only=True, format='%Y-%m-%d')

    class Meta:
        model = con_models.Phone
        fields = (
            'id',
            'phone',
            'created_at',
        )


class LinkSerializer(ser.ModelSerializer):
    created_at = ser.DateTimeField(read_only=True, format='%Y-%m-%d')

    class Meta:
        model = con_models.Link
        fields = (
            'id',
            'title',
            'icon',
            'link',
            'created_at',
        )


class ContactSerializer(ser.ModelSerializer):
    streets = StreetSerializer(many=True)
    phones = PhoneSerializer(many=True)
    links = LinkSerializer(many=True)
    created_at = ser.DateTimeField(read_only=True, format='%Y-%m-%d')

    class Meta:
        model = con_models.Contact
        fields = (
            'id',
            'streets',
            'phones',
            'email',
            'links',
            'created_at',
        )
