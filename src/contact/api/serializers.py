from rest_framework import serializers

from contact import models


class PhonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Phone
        fields = 'id phone'.split()


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Link
        fields = 'id title icon link'.split()


class ContactSerializer(serializers.ModelSerializer):
    phone = PhonSerializer(many=True)

    class Meta:
       model = models.Contact
       fields = 'id address_affiliate phone '.split()


