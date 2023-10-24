from rest_framework import viewsets

from contact.api import serializers as ser
from contact import models as contact_models


class ContactViewSet(viewsets.ModelViewSet):
    queryset = contact_models.Contact.objects.all()
    serializer_class = ser.ContactSerializer
