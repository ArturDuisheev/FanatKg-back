from rest_framework import serializers

from contact import models as con_models


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = con_models.Phone
        fields = ['id', 'phone']


class AddressSerializer(serializers.ModelSerializer):
    phones = PhoneSerializer(many=True)

    class Meta:
        model = con_models.Address
        fields = ('id', 'address', 'phones')


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = con_models.Link
        fields = ('id', 'social_media', 'link')


class ContactSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True)
    links = LinkSerializer(many=True)

    class Meta:
        model = con_models.Contact
        fields = ('id', 'addresses', 'email', 'links')

    def create(self, validated_data):
        addresses_data = validated_data.pop('addresses', [])
        links_data = validated_data.pop('links', [])

        contact = con_models.Contact.objects.create(**validated_data)
        for address_data in addresses_data:
            phones_data = address_data.pop('phones', [])
            address, created = con_models.Address.objects.get_or_create(**address_data)
            contact.addresses.add(address)
            for phone_data in phones_data:
                con_models.Phone.objects.create(**phone_data)
        for link_data in links_data:
            print(link_data)
            link, created = con_models.Link.objects.get_or_create(**link_data)
            contact.links.add(link)
        return contact

