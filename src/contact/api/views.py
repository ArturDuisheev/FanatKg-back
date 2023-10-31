from rest_framework.generics import ListAPIView

from .serializers import ContactSerializer, LinkSerializer
from contact.models import Contact, Link


class ContactListAPIView(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class LinkListAPIView(ListAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer